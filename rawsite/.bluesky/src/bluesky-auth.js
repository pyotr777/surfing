import { safeReturn, validateReply } from './bluesky-core.js';
import { BrowserOAuthClient, buildAtprotoLoopbackClientMetadata } from '@atproto/oauth-client-browser';
import metadata from '../../bluesky-client-metadata.json';

// Keep untrusted discovery documents small before the SDK validates them.
export function checkDocument(value, budget = { nodes: 5000 }) {
  if (--budget.nodes < 0) throw new Error('OAuth document too complex');
  if (value && typeof value === 'object') {
    const values = Object.values(value);
    if (values.length > 256) throw new Error('OAuth collection too large');
    for (const child of values) checkDocument(child, budget);
  }
}
export async function boundedFetch(input, init) {
  const response = await fetch(input, init);
  if (!response.body) return response;
  const reader = response.body.getReader();
  const chunks = [];
  let length = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      length += value.byteLength;
      if (length > 262144) throw new Error('OAuth response too large');
      chunks.push(value);
    }
  } catch (error) {
    await reader.cancel().catch(() => {});
    throw error;
  } finally { reader.releaseLock(); }
  const body = await new Blob(chunks).text();
  if ((response.headers.get('content-type') || '').includes('json') && body) checkDocument(JSON.parse(body));
  const copy = new Response(body, { status: response.status, statusText: response.statusText, headers: response.headers });
  Object.defineProperty(copy, 'url', { value: response.url });
  return copy;
}


export function clientMetadataFor(pageHref, assetHref) {
  const page = new URL(pageHref);
  const base = new URL('../', assetHref);
  if (page.protocol === 'file:') {
    throw Object.assign(new Error('Open the local website over HTTP, not file://'), { code: 'LOCAL_HTTP_REQUIRED' });
  }
  if (page.hostname === 'localhost') {
    const target = new URL(page);
    target.hostname = '127.0.0.1';
    throw Object.assign(new Error('Use 127.0.0.1 for local Bluesky sign-in'), { code: 'LOOPBACK_IP_REQUIRED', url: target.href });
  }
  if (['127.0.0.1', '[::1]'].includes(page.hostname)) {
    if (page.protocol !== 'http:') {
      throw Object.assign(new Error('Use http://127.0.0.1 for local sign-in'), { code: 'LOCAL_HTTP_REQUIRED' });
    }
    return buildAtprotoLoopbackClientMetadata({
      scope: metadata.scope,
      redirect_uris: [new URL('bluesky-callback.html', base).href],
    });
  }
  return metadata;
}
function returnToSite(value) {
  const base = new URL('../', import.meta.url);
  return safeReturn(value, location.origin, base.pathname);
}

let client;
let initialized;
let session;
function getClient() {
  return client ||= new BrowserOAuthClient({ clientMetadata: clientMetadataFor(location.href, import.meta.url),
    handleResolver: 'https://bsky.social/', fetch: boundedFetch });
}
export const auth = {
  async restore() {
    // Read-only pages do not need to contact an authorization server until a session exists.
    initialized ||= getClient().initRestore().then(result => session = result?.session).catch(error => {
      initialized = undefined;
      throw error;
    });
    return initialized;
  },
  async signIn(handle, returnTo) {
    const url = await getClient().authorize(handle.trim().replace(/^@/, ''), {
      scope: metadata.scope, state: returnToSite(returnTo),
    });
    location.assign(url.href);
  },
  async signOut() {
    try { if (session) await getClient().revoke(session.did); }
    finally { session = undefined; initialized = undefined; }
  },
  async callback() {
    const result = await getClient().initCallback();
    location.replace(returnToSite(result.state));
  },
};


export async function publishReply(session, root, parent, text) {
  if (!session?.did || !root?.uri || !root?.cid || !parent?.uri || !parent?.cid) throw new Error('Missing reply context');
  const record = { $type: 'app.bsky.feed.post', text: validateReply(text),
    createdAt: new Date().toISOString(), reply: { root, parent } };
  const response = await session.fetchHandler('/xrpc/com.atproto.repo.createRecord', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ repo: session.did, collection: 'app.bsky.feed.post', record }),
  });
  if (!response.ok) throw new Error('Reply was not accepted');
  const result = await response.json();
  if (!result.uri || !result.cid) throw new Error('Invalid publish response');
  return { ...result, record };
}
