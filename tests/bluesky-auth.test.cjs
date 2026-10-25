const { test } = require('node:test');
const assert = require('node:assert/strict');
const { build } = require('esbuild');
const mockSdk = `export function buildAtprotoLoopbackClientMetadata({scope,redirect_uris}) {
 return { client_id:'http://localhost?' + new URLSearchParams({scope,redirect_uri:redirect_uris[0]}), scope, redirect_uris, application_type:'native' };
}
export class BrowserOAuthClient {
  constructor(options) { globalThis.clientOptions = options; }
  async initRestore() { return globalThis.mockSession ? {session: globalThis.mockSession} : undefined; }
  async authorize(handle, options) { globalThis.authorization = {handle, options}; return new URL('https://bsky.social/oauth/authorize'); }
  async revoke(did) { globalThis.revokedDid = did; globalThis.mockSession = undefined; }
  async initCallback() { return globalThis.callbackResult; }
}`;
const authModule = build({ entryPoints: ['src/bluesky-auth.js'], bundle: true, write: false, format: 'esm',
  define: { 'import.meta.url': JSON.stringify('https://pyotr777.github.io/surfing/js/bluesky-comments.js') },
  plugins: [{ name: 'test-oauth', setup(b) {
    b.onResolve({filter: /^@atproto\/oauth-client-browser$/}, () => ({path:'sdk',namespace:'mock'}));
    b.onLoad({filter: /.*/, namespace:'mock'}, () => ({contents: mockSdk}));
  }}],
}).then(r => import('data:text/javascript;base64,' + Buffer.from(r.outputFiles[0].text).toString('base64')));

test('posting uses the authenticated DID and exact root and parent references', async () => {
  const { publishReply } = await authModule;
  const root = {uri:'at://did:plc:author/app.bsky.feed.post/root',cid:'root-cid'};
  const parent = {uri:'at://did:plc:reader/app.bsky.feed.post/parent',cid:'parent-cid'};
  let submitted;
  const session = {did:'did:plc:visitor', async fetchHandler(path, init) {
    assert.equal(path, '/xrpc/com.atproto.repo.createRecord');
    assert.equal(init.method, 'POST');
    submitted = JSON.parse(init.body);
    return Response.json({uri:'at://did:plc:visitor/app.bsky.feed.post/new',cid:'new-cid'});
  }};
  await publishReply(session,root,parent,'  🌊 Hello  ');
  assert.equal(submitted.repo,session.did);
  assert.deepEqual(submitted.record.reply,{root,parent});
  assert.equal(submitted.record.text,'🌊 Hello');
  assert.equal(submitted.collection,'app.bsky.feed.post');
  await assert.rejects(publishReply(undefined, root, parent, 'hello'));
  await assert.rejects(publishReply({...session,fetchHandler:async()=>new Response('',{status:403})},root,parent,'hello'));
});

test('OAuth restore, redirect and callback never post; logout revokes the session', async () => {
  const { auth } = await authModule;
  let assigned, returned;
  global.location={href:'https://pyotr777.github.io/surfing/spots/asahi/mansionsita/index.html',origin:'https://pyotr777.github.io',assign:url=>assigned=url,replace:url=>returned=url};
  global.mockSession={did:'did:plc:visitor'};
  assert.equal((await auth.restore()).did, 'did:plc:visitor');
  await auth.signIn('@visitor.bsky.social','/surfing/spots/asahi/mansionsita/index_ja.html#bluesky-comments');
  assert.equal(authorization.handle,'visitor.bsky.social');
  assert.equal(authorization.options.scope,'atproto repo:app.bsky.feed.post?action=create');
  assert.equal(assigned,'https://bsky.social/oauth/authorize');
  global.callbackResult={state:'https://evil.test/'};
  await auth.callback();
  assert.equal(returned,'https://pyotr777.github.io/surfing/');
  await auth.signOut();
  assert.equal(global.revokedDid,'did:plc:visitor');
  assert.equal(await auth.restore(),undefined);
});

test('OAuth documents are bounded before dependency validation', async () => {
  const { boundedFetch, checkDocument } = await authModule;
  assert.throws(()=>checkDocument(new Array(257).fill('x')));
  assert.throws(()=>checkDocument({a:[1,2]}, {nodes:2}));
  const original=global.fetch;
  try {
    global.fetch=async()=>new Response('x'.repeat(262145));
    await assert.rejects(boundedFetch('https://example.test'), /too large/);
    global.fetch=async()=>Response.json({keys:new Array(257).fill('x')});
    await assert.rejects(boundedFetch('https://example.test'), /too large/);
    global.fetch=async()=>Response.json({issuer:'https://bsky.social'});
    assert.deepEqual(await (await boundedFetch('https://example.test')).json(),{issuer:'https://bsky.social'});
  } finally {global.fetch=original;}
});


test('local OAuth uses loopback metadata and the current port/site prefix', async () => {
  const { clientMetadataFor } = await authModule;
  for (const prefix of ['/surfing/', '/']) {
    const local = clientMetadataFor('http://127.0.0.1:8765' + prefix + 'spots/asahi/mansionsita/index.html',
      'http://127.0.0.1:8765' + prefix + 'js/bluesky-comments.js?v=abc');
    const id = new URL(local.client_id);
    assert.equal(id.origin, 'http://localhost');
    assert.equal(id.pathname, '/');
    assert.equal(id.searchParams.get('redirect_uri'), 'http://127.0.0.1:8765' + prefix + 'bluesky-callback.html');
    assert.equal(id.searchParams.get('scope'), 'atproto repo:app.bsky.feed.post?action=create');
    assert.equal(local.application_type, 'native');
  }
  assert.throws(() => clientMetadataFor('file:///tmp/surfing/index.html','file:///tmp/surfing/js/bluesky-comments.js'),
    error => error.code === 'LOCAL_HTTP_REQUIRED');
  assert.throws(() => clientMetadataFor('http://localhost:8765/surfing/index.html','http://localhost:8765/surfing/js/bluesky-comments.js'),
    error => error.code === 'LOOPBACK_IP_REQUIRED' && error.url === 'http://127.0.0.1:8765/surfing/index.html');
});
