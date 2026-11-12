# The Survival Guide — website

A static website: plain HTML, CSS and a little JavaScript. It needs no database or server-side code, and runs offline once saved.

## What's in this folder

| Folder | What it is |
|---|---|
| `site/` | **The finished website. Deploy this folder.** |
| `source/` | Everything used to build it, so new chapters can be added later. |

Inside `source/`:

- `plan.md`: the master plan. The site's menu and every planned chapter come from Section 4 of this file.
- `content/`: the written chapters, one HTML fragment each.
- `content/_status.json`: which chapters are fact-checked.
- `assets/`: the stylesheet and script.
- `build.py`: rebuilds `site/` from the plan and content. Run it with `python3 build.py`; it uses only Python's standard library.
- `CONTENT_SPEC.md`: the writing, sourcing and illustration rules every chapter follows.
- `VERIFY_BRIEF.md`: the independent fact-check procedure.
- `reports/`: each chapter's research notes and fact-check report.

## Deploy

Any static web server works. Point it at the `site/` folder.

**Cloudflare (Workers Static Assets):** `wrangler.jsonc` in the repo root serves `./site` as a static Worker named `survivalguide`. In the Cloudflare dashboard, go to Workers & Pages → Create → Import a repository, pick this repo, and leave the build command empty with `npx wrangler deploy` as the deploy command. Every push to `main` then redeploys. Add the custom domain under the Worker's Settings → Domains & Routes.

To update the site: run `python3 build.py`, commit the rebuilt `site/` folder, and push.

**Docker (e.g., on a NAS):**

```bash
docker run -d --name survival-guide --restart unless-stopped \
  -p 8088:80 \
  -v /path/to/survival-guide/site:/usr/share/nginx/html:ro \
  nginx:alpine
```

Then open `http://<your-server-ip>:8088`.

**No server at all:** open `site/index.html` in a browser. Navigation and search both work from local files.

## Notes

- Fonts load from Google Fonts when online. Offline, the site falls back to system fonts.
- Every illustration is an original inline SVG drawing. There are no external images.
- Pages marked **Planned** are outlines from the plan. Pages marked **Researched & fact-checked** list their sources at the bottom.
- To add a chapter:
  1. Write the fragment to `source/content/<slug>.html` following `CONTENT_SPEC.md`.
  2. Map it in `CONTENT_MAP` or `EXTRA_PAGES` in `build.py`.
  3. Mark it in `_status.json`.
  4. Run `python3 build.py`.
