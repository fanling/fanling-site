# fanling.ai 与 GSD 作品集：源文件说明

- 所有文字在 `content.md`（英文，一份内容同时生成网站和 PDF，文件开头有修改说明）。`src/content.py` 只负责读取它，另外记着每件作品用哪张结构图；结构图在 `src/diagrams.py`。
- Ling 在 Claude Doc（https://claude.ai/code/artifact/7adfea2c-50dc-4f6c-a5e6-5f88d7b33231）里改文字；把文档导出为 markdown 后用 `python3 src/sync_from_doc.py <导出文件>` 写回 `content.md`。
- 改完 `content.md` 后运行 `sh build.sh`，会同时重新生成 PDF 和网站。
- 重新生成 PDF：`cd src && python3 portfolio.py portfolio.html && node render.js portfolio.html ../../gsd-application/portfolio/LingFan_GSD_Portfolio_draft.pdf`
- 重新生成网站：`cd src && python3 site.py ../site`（静态 HTML，可直接放到任何静态托管上，再把 fanling.ai 指过去；目前没有上线，也没有改域名）。
- `content.md` 里的 `[To add: ...]` 在 PDF 和网站上显示为蓝色 “To add”，提交前要全部替换。

## GitHub 与 Vercel 部署
- 整个 `fanling-site/` 文件夹就是 GitHub 仓库的内容。网站生成好的静态文件 `site/` 也一起提交；Vercel 不运行任何构建，直接发布 `site/`（见 `vercel.json`，已开启无 `.html` 后缀的网址）。
- 更新网站：改 `content.md` → `sh build.sh` → `sh publish.sh <owner>/<repo> "说明"`。推送后 Vercel 自动重新部署。
- 视频都在 11 MB 以下，无需另外压缩；`__pycache__` 和中间文件 `src/portfolio.html` 不进仓库。
