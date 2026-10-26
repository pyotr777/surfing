import { parsePost, postLink, selectComments, validateReply } from './bluesky-core.js';
import styles from './bluesky-comments.css';
import { auth, publishReply } from './bluesky-auth.js';
const API = 'https://public.api.bsky.app/xrpc/';


const copy = {
  ja: {
    title: 'Blueskyでのコメント', reply: 'Blueskyで返信', all: 'すべてのコメント',
    loading: 'コメントを読み込み中…', empty: '指定した期間のコメントはありません。',
    error: 'コメントを読み込めませんでした。Blueskyでご覧いただけます。',
    parent: '返信先のコメント',
    period: hours => hours ? `過去${hours}時間の返信を表示しています。` : 'すべての期間の返信を表示しています。',
    note: '返信にはBlueskyアカウントが必要です。コメントは各言語版で共通です。ここでは本文のみを表示します。画像などの添付はBlueskyでご覧ください。',
  },
  ru: {
    title: 'Обсуждение в Bluesky', reply: 'Ответить в Bluesky', all: 'Всё обсуждение',
    loading: 'Загрузка комментариев…', empty: 'За выбранный период комментариев нет.',
    error: 'Не удалось загрузить комментарии. Обсуждение можно открыть в Bluesky.',
    parent: 'Ответ на комментарий',
    period: hours => hours ? `Показаны ответы за последние ${hours} ч.` : 'Показаны ответы за всё время.',
    note: 'Для ответа нужен аккаунт Bluesky. Обсуждение общее для всех языковых версий. Здесь показаны текстовые версии ответов; изображения и другие вложения доступны в Bluesky.',
  },
  en: {
    title: 'Discussion on Bluesky', reply: 'Reply on Bluesky', all: 'Full discussion',
    loading: 'Loading comments…', empty: 'No comments in this time window.',
    error: 'Comments could not be loaded. You can open the discussion on Bluesky.',
    parent: 'Reply to a comment',
    period: hours => hours ? `Showing replies from the last ${hours} hours.` : 'Showing replies from all time.',
    note: 'A Bluesky account is required to reply. All language versions share this discussion. Text versions are shown here; images and other attachments are available on Bluesky.',
  },
};

Object.assign(copy.ru, {
  localHttp: 'Для входа откройте локальный сайт через HTTP-сервер, а не как файл. Например: http://127.0.0.1:8765/surfing/.', localIp: 'Для локального входа используйте адрес 127.0.0.1 вместо localhost.', openLocal: 'Открыть локальную страницу',
  signIn: 'Войти через Bluesky', handle: 'Ваш адрес в Bluesky', handleHint: 'например, name.bsky.social',
  comment: 'Ваш комментарий', send: 'Отправить', sending: 'Отправка…', signOut: 'Выйти',
  signedIn: 'Вы вошли как', loginError: 'Не удалось войти. Попробуйте ещё раз или ответьте в Bluesky.',
  sendError: 'Не удалось подтвердить отправку. Текст сохранён. Проверьте обсуждение перед повторной отправкой.',
  sent: 'Ответ опубликован.', openReply: 'Открыть ответ',
  limit: 'До 300 символов.',
});
Object.assign(copy.en, {
  localHttp: 'To sign in, open the local site through an HTTP server, not as a file. For example: http://127.0.0.1:8765/surfing/.', localIp: 'For local sign-in, use 127.0.0.1 instead of localhost.', openLocal: 'Open local page',
  signIn: 'Sign in with Bluesky', handle: 'Your Bluesky handle', handleHint: 'for example, name.bsky.social',
  comment: 'Your comment', send: 'Send', sending: 'Sending…', signOut: 'Sign out',
  signedIn: 'Signed in as', loginError: 'Sign-in failed. Try again or reply on Bluesky.',
  sendError: 'Could not confirm submission. Your text is saved. Check the discussion before trying again.',
  sent: 'Reply published.', openReply: 'Open reply',
  limit: 'Up to 300 characters.',
});
Object.assign(copy.ja, {
  localHttp: 'ログインするには、ファイルではなくローカルHTTPサーバー経由で開いてください。例: http://127.0.0.1:8765/surfing/', localIp: 'ローカルログインにはlocalhostではなく127.0.0.1を使用してください。', openLocal: 'ローカルページを開く',
  signIn: 'Blueskyでログイン', handle: 'Blueskyのハンドル', handleHint: '例: name.bsky.social',
  comment: 'コメント', send: '送信', sending: '送信中…', signOut: 'ログアウト',
  signedIn: 'ログイン中:', loginError: 'ログインできませんでした。再試行するか、Blueskyで返信してください。',
  sendError: '送信を確認できませんでした。本文は保存されています。再送信する前にBlueskyをご確認ください。',
  sent: '返信を投稿しました。', openReply: '返信を開く',
  limit: '300文字まで。',
});

function readDraft(key) {
  try { return sessionStorage.getItem(key) || ''; } catch { return ''; }
}
function saveDraft(key, value) {
  try { value ? sessionStorage.setItem(key, value) : sessionStorage.removeItem(key); } catch {}
}

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text) node.textContent = text;
  if (className) node.className = className;
  if (tag === 'button') node.classList.add('action-button');
  return node;
}

function link(text, url) {
  const node = element('a', text);
  node.href = url;
  node.target = '_blank';
  node.rel = 'noopener noreferrer';
  return node;
}

class SurfingBlueskyComments extends HTMLElement {
  connectedCallback() {
    if (this.started) return;
    this.started = true;
    this.id ||= 'bluesky-comments';
    this.auth = auth;
    this.words = copy[(this.getAttribute('lang') || document.documentElement.lang).split('-')[0]] || copy.en;
    this.status = element('p');
    this.status.setAttribute('role', 'status');
    this.list = element('div', '', 'bluesky-comment-list');
    this.append(element('h2', this.words.title), this.status, this.list);
    this.buildForm();
    this.load();
  }

  buildForm() {
    this.draftKey = 'surfing-bluesky-draft:' + this.getAttribute('post');
    this.authStatus = element('p');
    this.authStatus.setAttribute('role', 'status');
    this.loginForm = element('form', '', 'bluesky-login');
    const handleLabel = element('label', this.words.handle);
    this.handle = element('input');
    this.handle.name = 'handle';
    this.handle.type = 'text';
    this.handle.autocomplete = 'username';
    this.handle.placeholder = this.words.handleHint;
    this.handle.required = true;
    handleLabel.append(this.handle);
    this.login = element('button', this.words.signIn);
    this.login.type = 'submit';
    this.loginForm.append(handleLabel, this.login);
    this.loginForm.addEventListener('submit', async event => {
      event.preventDefault();
      this.login.disabled = true;
      this.authStatus.textContent = '';
      this.persistDraft();
      try {
        await this.auth.signIn(this.handle.value, location.pathname + location.search + '#bluesky-comments');
      } catch (error) { this.showAuthError(error); }
      finally { this.login.disabled = false; }
    });
    this.account = element('div', '', 'bluesky-account');
    this.accountName = element('span');
    this.logout = element('button', this.words.signOut);
    this.logout.type = 'button';
    this.logout.addEventListener('click', async () => {
      this.logout.disabled = true;
      try { await this.auth.signOut(); }
      catch (error) { this.showAuthError(error); }
      finally { this.session = undefined; this.logout.disabled = false; this.updateForm(); }
    });
    this.account.append(this.accountName, this.logout);
    this.composer = element('form', '', 'bluesky-composer');
    const label = element('label', this.words.comment);
    this.text = element('textarea');
    this.text.name = 'comment';
    this.text.rows = 4;
    this.text.maxLength = 3000;
    this.text.required = true;
    this.text.value = readDraft(this.draftKey);
    saveDraft(this.draftKey + ':parent', '');
    this.text.addEventListener('input', () => { this.persistDraft(); this.updateForm(); });
    label.append(this.text);
    this.send = element('button', this.words.send);
    this.send.type = 'submit';
    this.sendStatus = element('p');
    this.sendStatus.setAttribute('role', 'status');
    this.composer.append(label, element('p', this.words.limit, 'bluesky-comment-note'), this.send, this.sendStatus);
    this.composer.addEventListener('submit', event => { event.preventDefault(); this.submitReply(); });
    this.append(this.loginForm, this.account, this.authStatus, this.composer);
    this.updateForm();
    this.auth.restore().then(async session => {
      this.session = session;
      this.updateForm();
      if (session) {
        try {
          const profile = await this.request('app.bsky.actor.getProfile', { actor: session.did });
          this.sessionLabel = '@' + profile.handle;
          this.updateForm();
        } catch {}
      }
    })
      .catch(error => this.showAuthError(error));
  }

  showAuthError(error) {
    if (error?.code === 'LOCAL_HTTP_REQUIRED') {
      this.authStatus.textContent = this.words.localHttp;
    } else if (error?.code === 'LOOPBACK_IP_REQUIRED') {
      this.authStatus.replaceChildren(this.words.localIp + ' ', link(this.words.openLocal, error.url));
    } else {
      this.authStatus.textContent = this.words.loginError;
      console.warn('Bluesky authentication failed:', error);
    }
  }

  persistDraft() {
    saveDraft(this.draftKey, this.text.value);
  }

  updateForm() {
    this.loginForm.hidden = Boolean(this.session);
    this.account.hidden = !this.session;
    this.accountName.textContent = this.session ? this.words.signedIn + (this.sessionLabel ? ' ' + this.sessionLabel : ' Bluesky') : '';
    let valid = false;
    try { validateReply(this.text.value); valid = true; } catch {}
    this.send.disabled = !this.session || !this.rootRef || !valid || this.sending;
    this.text.disabled = Boolean(this.sending);
    this.logout.disabled = Boolean(this.sending);
    this.send.textContent = this.sending ? this.words.sending : this.words.send;
  }

  async submitReply() {
    if (this.send.disabled || this.sending) return;
    this.sending = true;
    this.sendStatus.textContent = '';
    this.updateForm();
    try {
      const result = await publishReply(this.session, this.rootRef, this.postRef, this.text.value);
      this.text.value = '';
      this.persistDraft();
      this.sendStatus.replaceChildren(this.words.sent + ' ', link(this.words.openReply, postLink(result.uri)));
      await this.load();
    } catch { this.sendStatus.textContent = this.words.sendError; }
    finally { this.sending = false; this.updateForm(); }
  }

  async request(method, params) {
    const response = await fetch(API + method + '?' + new URLSearchParams(params), {
      credentials: 'omit', signal: AbortSignal.timeout(15000),
    });
    if (!response.ok) throw new Error('Bluesky request failed');
    return response.json();
  }

  async load() {
    this.status.textContent = this.words.loading;
    this.list.replaceChildren();
    try {
      const rawHours = this.getAttribute('max-age-hours') ?? '72';
      const hours = rawHours.trim() ? Number(rawHours) : NaN;
      if (!Number.isFinite(hours) || hours < 0) throw new Error('Invalid time window');
      const { actor, key } = parsePost(this.getAttribute('post') || '');
      const original = `at://${actor}/app.bsky.feed.post/${key}`;
      if (!this.actions) {
        this.actions = element('p', '', 'bluesky-comment-actions');
        this.actions.append(link(this.words.reply, postLink(original)), document.createTextNode(' · '), link(this.words.all, postLink(original)));
        this.insertBefore(this.actions, this.loginForm);
        this.insertBefore(element('p', this.words.note, 'bluesky-comment-note'), this.loginForm);
      }
      const did = actor.startsWith('did:') ? actor :
        (await this.request('com.atproto.identity.resolveHandle', { handle: actor })).did;
      if (!did?.startsWith('did:')) throw new Error('Invalid identity');
      const uri = `at://${did}/app.bsky.feed.post/${key}`;
      const data = await this.request('app.bsky.feed.getPostThread', { uri, depth: 100, parentHeight: 0 });
      if (!data.thread?.post) throw new Error('Thread unavailable');
      this.postRef = { uri: data.thread.post.uri, cid: data.thread.post.cid };
      this.rootRef = data.thread.post.record.reply?.root || this.postRef;
      this.updateForm();
      const comments = selectComments(data.thread, {
        hours, hidden: data.threadgate?.record?.hiddenReplies || [],
        excluded: (this.getAttribute('exclude-dids') || '').split(/[\s,]+/).filter(Boolean),
      });
      for (const post of comments) {
        const article = element('article', '', 'bluesky-comment');
        const header = element('p', '', 'bluesky-comment-meta');
        const date = element('time', new Date(post.record.createdAt).toLocaleString(this.getAttribute('lang') || document.documentElement.lang || 'en'));
        date.dateTime = post.record.createdAt;
        const permalink = link('', postLink(post.uri));
        permalink.append(date);
        header.append(link(post.author.displayName || post.author.handle,
          `https://bsky.app/profile/${encodeURIComponent(post.author.did)}`), document.createTextNode(' · '), permalink);
        article.append(header);
        const parent = post.record.reply?.parent?.uri;
        if (parent && parent !== uri) article.append(link(this.words.parent, postLink(parent)));
        // Treat remote content as text, never as HTML.
        article.append(element('p', post.record.text, 'bluesky-comment-text'));
        this.list.append(article);
      }
      this.status.textContent = comments.length ? this.words.period(hours) : this.words.empty;
    } catch {
      this.rootRef = undefined;
      this.updateForm();
      this.list.replaceChildren();
      this.status.textContent = this.words.error;
    }
  }
}

if (!customElements.get('surfing-bluesky-comments')) {
  customElements.define('surfing-bluesky-comments', SurfingBlueskyComments);
}

if (!document.getElementById('bluesky-comments-styles')) {
  const style = element('style');
  style.id = 'bluesky-comments-styles';
  style.textContent = styles;
  document.head.append(style);
}
for (const script of document.querySelectorAll('script[data-bluesky-post]')) {
  if (script.dataset.blueskyMounted) continue;
  script.dataset.blueskyMounted = 'true';
  const comments = document.createElement('surfing-bluesky-comments');
  comments.setAttribute('post', script.dataset.blueskyPost);
  comments.setAttribute('max-age-hours', script.dataset.blueskyHours || '72');
  comments.setAttribute('exclude-dids', script.dataset.blueskyExclude || '');
  if (script.lang) comments.setAttribute('lang', script.lang);
  script.before(comments);
}
if (document.getElementById('bluesky-callback-status')) {
  auth.callback().catch(() => {
    document.getElementById('bluesky-callback-status').textContent =
      'Sign-in failed or cancelled. Return to the page and try again. / Вход не выполнен. Вернитесь на страницу и попробуйте снова. / ログインできませんでした。元のページで再試行してください。';
  });
}
