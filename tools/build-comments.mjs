import { build } from 'esbuild';
await build({
  entryPoints: ['src/bluesky-comments.js'],
  outfile: 'rawsite/js/bluesky-comments.js', bundle: true, format: 'esm',
  platform: 'browser', target: ['es2022'], minify: true,
  legalComments: 'eof', loader: { '.css': 'text' },
});
