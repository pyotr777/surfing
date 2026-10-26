const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');

const source = readFileSync('src/bluesky-core.js', 'utf8');
global.HTMLElement = class {};
global.customElements = { define() {} };
const modulePromise = import('data:text/javascript;base64,' + Buffer.from(source).toString('base64'));
const now = Date.parse('2026-10-25T12:00:00Z');
function reply(id, hours, replies = [], did = 'did:plc:reader') {
  return { post: { uri: `at://did:plc:reader/app.bsky.feed.post/${id}`,
    author: { did }, record: { text: id, createdAt: new Date(now - hours * 3600000).toISOString() } }, replies };
}

test('72-hour window includes boundary, excludes old, future and invalid dates; visits old parents', async () => {
  const { selectComments } = await modulePromise;
  const invalid = reply('invalid', 1);
  invalid.post.record.createdAt = 'invalid';
  const tree = { replies: [reply('old', 100, [reply('nested', 2)]), reply('boundary', 72),
    reply('future', -1), invalid, reply('new', 1)] };
  assert.deepEqual(selectComments(tree, { now }).map(p => p.record.text), ['new', 'nested', 'boundary']);
  assert.equal(selectComments(tree, { now, hours: 0 }).length, 4);
  assert.equal(selectComments(tree, { now, hours: 48 }).length, 2);
});

test('hidden/excluded branches and unavailable replies stay out of results', async () => {
  const { selectComments } = await modulePromise;
  const hidden = reply('hidden', 1, [reply('hiddenChild', 1)]);
  const excluded = reply('excluded', 1, [reply('excludedChild', 1)], 'did:plc:excluded');
  const visible = reply('visible', 1);
  const tree = { replies: [hidden, excluded, { blocked: true }, { notFound: true }, visible, visible] };
  assert.deepEqual(selectComments(tree, { now, hidden: [hidden.post.uri], excluded: ['did:plc:excluded'] })
    .map(p => p.record.text), ['visible']);
});

test('invalid time windows fail instead of exposing all comments', async () => {
  const { selectComments } = await modulePromise;
  for (const hours of [-1, NaN, Infinity]) assert.throws(() => selectComments({}, { hours }));
});

test('post references accept Bluesky URLs and AT URIs, reject unrelated origins', async () => {
  const { parsePost } = await modulePromise;
  assert.deepEqual(parsePost('https://bsky.app/profile/example.bsky.social/post/abc?foo=bar'),
    { actor: 'example.bsky.social', key: 'abc' });
  assert.deepEqual(parsePost('at://did:plc:example/app.bsky.feed.post/abc'), { actor: 'did:plc:example', key: 'abc' });
  for (const url of ['javascript:alert(1)', 'https://evil.test/profile/test/post/abc', 'https://bsky.app/profile/test']) {
    assert.throws(() => parsePost(url));
  }
});


test('reply length counts graphemes; empty, oversized and excessive UTF-8 are rejected', async () => {
  const { validateReply } = await modulePromise;
  assert.equal(validateReply('  Привет 🌊  '), 'Привет 🌊');
  assert.equal(validateReply('🌊'.repeat(300)).length, 600);
  for (const text of ['  ', 'a'.repeat(301), '👨‍👩‍👧‍👦'.repeat(121)]) assert.throws(() => validateReply(text));
});

test('OAuth return paths stay on the same site', async () => {
  const { safeReturn } = await modulePromise;
  const origin = 'https://pyotr777.github.io';
  assert.equal(safeReturn('/surfing/spots/asahi/mansionsita/index_ru.html#bluesky-comments', origin),
    origin + '/surfing/spots/asahi/mansionsita/index_ru.html#bluesky-comments');
  for (const value of ['https://evil.test/', '//evil.test/', 'javascript:alert(1)', '/another-project/', '/surfing/bluesky-callback.html']) {
    assert.equal(safeReturn(value, origin), origin + '/surfing/');
  }
});


test('local callback returns work when serving the output directly at the root', async () => {
 const {safeReturn} = await modulePromise;
 assert.equal(safeReturn('/spots/asahi/mansionsita/index_ru.html#bluesky-comments','http://127.0.0.1:8765','/'),
  'http://127.0.0.1:8765/spots/asahi/mansionsita/index_ru.html#bluesky-comments');
 assert.equal(safeReturn('https://evil.test/','http://127.0.0.1:8765','/'), 'http://127.0.0.1:8765/');
});
