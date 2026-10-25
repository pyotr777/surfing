export function parsePost(value) {
  const match = /^at:\/\/([^/]+)\/app\.bsky\.feed\.post\/([a-zA-Z0-9]+)$/.exec(value);
  if (match) return { actor: match[1], key: match[2] };
  const url = new URL(value);
  const path = /^\/profile\/([^/]+)\/post\/([a-zA-Z0-9]+)\/?$/.exec(url.pathname);
  if (url.origin !== 'https://bsky.app' || !path) throw new Error('Invalid Bluesky post');
  return { actor: decodeURIComponent(path[1]), key: path[2] };
}

export function postLink(uri) {
  const { actor, key } = parsePost(uri);
  return `https://bsky.app/profile/${encodeURIComponent(actor)}/post/${key}`;
}

// Walk old parents too: they may contain recent replies. Hidden branches stay hidden.
export function selectComments(thread, { hours = 72, now = Date.now(), hidden = [], excluded = [] } = {}) {
  if (!Number.isFinite(hours) || hours < 0) throw new Error('Invalid time window');
  const result = [];
  const seen = new Set();
  const hiddenSet = new Set(hidden);
  const excludedSet = new Set(excluded);
  const cutoff = hours === 0 ? -Infinity : now - hours * 3600000;
  function visit(node) {
    const post = node?.post;
    if (!post || seen.has(post.uri) || hiddenSet.has(post.uri) || excludedSet.has(post.author?.did)) return;
    seen.add(post.uri);
    const created = Date.parse(post.record?.createdAt);
    if (Number.isFinite(created) && created >= cutoff && created <= now) result.push(post);
    for (const reply of node.replies || []) visit(reply);
  }
  for (const reply of thread.replies || []) visit(reply);
  return result.sort((a, b) => Date.parse(b.record.createdAt) - Date.parse(a.record.createdAt));
}

export function safeReturn(value, origin = location.origin, basePath = '/surfing/') {
  const fallback = new URL(basePath, origin);
  try {
    const target = new URL(value, origin);
    return target.origin === origin && target.pathname.startsWith(fallback.pathname) &&
      target.pathname !== fallback.pathname + 'bluesky-callback.html' ? target.href : fallback.href;
  } catch { return fallback.href; }
}


export function validateReply(text) {
  const value = text.trim();
  const length = [...new Intl.Segmenter(undefined, { granularity: 'grapheme' }).segment(value)].length;
  if (!length || length > 300 || new TextEncoder().encode(value).length > 3000) {
    throw new Error('Invalid reply length');
  }
  return value;
}

