# fanling.ai 网站交接说明

写于 2026-10-06，从 Claude 项目 “Harvard GSD Professorship” 交接到新的 fanling.ai 网站项目。新项目只需要这份文件加上 GitHub 仓库 `fanling/fanling-site`，不需要旧项目里的任何其他东西。

## 一、现在的状态

- 网站已上线：https://www.fanling.ai （`fanling.ai` 会 308 跳转到 `www`）。Vercel 备用地址 https://fanling-site.vercel.app/
- 仓库：https://github.com/fanling/fanling-site 。`main` 分支就是线上版本，最后一次上线是 2026-10-04 11:36（移动端修复、隐藏 Substack、SEO/GEO）。
- **还没上线的改动**在分支 `claude/project-thread-drmsah`（2026-10-06 推送，含这份文件）。它是 2026-10-04 下午之后的最新源文件，包括下面“待上线修改”里的两处事实更正。Vercel 只会给这个分支生成预览，不影响线上。已开 PR：https://github.com/fanling/fanling-site/pull/1 。范老师确认后，合并这个 PR 到 `main` 就会自动上线。

## 二、待上线修改（已改好，在上面的分支里）

1. **atypica 不再写“100 万用户”。** 范老师 2026-10-04 确认：“over one million professional users” 这个数字属于 Tezign，不属于 atypica。atypica 作品页去掉了 “Used by: more than one million people in 50 countries”，Entrepreneurship 页 atypica 的一句话介绍也去掉了用户数。Tezign 的 “over one million professional users” 保留。
2. **博士生 Mudasir Ahmed。** 名字顺序是 “Mudasir Ahmed”（不是 Ahmed Mudasir），2024 年入学，论文题目：“Generative Ethnography: AI-Based Simulation of Social Dynamics for Small and Medium-Sized Enterprises in **Pakistan**”（不是 ASEAN）。在 Lab 页的博士生名单里。
3. 同一批还有一些作品集（PDF）带出来的网站小改动：Datafying Creativity 里 “Chinese traditional craft” 改为 “Chinese folk craft”；Creative Reasoning 结构图的标注更新；MuseDAM 介绍里 “content system” 改为 “context system”。

上线前建议在 Vercel 预览里过一遍 Research、Lab、Entrepreneurship 三页。

## 三、读者和网站结构（范老师 2026-10-04 定的）

- **读者**：海外学术和研究界的读者（院校、评审、合作者）。网站是个人简介和作品集，不是纯设计作品集。改动保持克制。
- **首页**：标题 “Researcher, Entrepreneur in Design AI.”；简介用 CV 里的短版 Profile。首页只放 Current research、Entrepreneurship 和带 YouTube 链接的演讲。
- **导航**：Research | Entrepreneurship | Talks | Writing | About | News
- **Research**：页面标题 “The Computability of Creativity”，三栏：
  - Current Research：01 Subjective World Model（atypica.AI）、02 Creative Reasoning、03 Agentic Creativity
  - Past Research：“Datafying Creativity”（原名 Computability of Design/Creativity，含四个子项目：青年亚文化色彩数据集、盲盒数据集、中国民间工艺数据集〔金山农民画〕、Prometheus 设计知识图谱）；“Brain–Machine Ratio (BMR)” 是**一个**课题（定量研究 + 定性研究 “A History of Creative Tools”），不要拆成两个。
  - Design AI Lab：链接到 lab.html（实验室介绍、经费、博士生名单）。
- **Entrepreneurship**：标题 “From Research to Practice”，结构和 Research 页一致：The Company（Tezign）+ Products（Tezign、atypica.AI、MuseDAM 三个，配首页截图）。这一页的文字不写 “Ling's”，也不提 “the Lab / Design AI Lab”。
- **Talks**：开头一段 + 三个主题（Design AI: The Computability of Creativity；Agentic Transformation for Business；Subjective World Model: Simulating People's Preferences and Decisions）+ 邀请联系邮箱 lfan@tongji.edu.cn。列表照搬 CV（34 场），另有 6 场中文视频演讲。
- **Writing**：Books（只有两本：2019 年 “From Universality of Computation to the Universality of Imagination”；2014 年 “Ten Dialogues: Hui Wang × Ling Fan”），然后 Publications（照 2026 年 10 月版 CV 的分类列表）。Substack 博客目前用注释隐藏，等范老师开始维护再打开。
- **About**：照 2026 年 10 月版 CV：任职、教育、荣誉、服务。不设展览栏目。
- **News**：17 条，都带链接。

## 四、已确认的事实（写网站时以此为准）

- 同济大学 Professor in Design AI；Tongji University Design AI Lab 创始主任。**实验室成立年份一律写 2017**（范老师确认过三次，即使 CV 或长江学者材料写 2016）。
- 研究总问题：the computability of creativity，“while preserving the subjectivity and plurality on which it depends”。三个方向：Creative Reasoning、Subjective World Models、Agentic Creativity。
- 100+ 篇论文；“more than 200 invention patent applications”。研究经费写 “more than US$5 million”。
- 教学：在读博士 8 人，在读硕士约 15 人，已毕业硕士 15 人（替代旧的 10/30）。毕业生去向：科技公司的 AI 产品设计与开发，或高校和研究机构做研究。参与创办同济两个学位项目：硕士 “AI and Data Design”、本科 “AI and Visual Communication”。
- Tezign：2015 年创立，服务 200+ 企业、超过 100 万专业用户，融资超过 1.5 亿美元（Temasek、Sequoia Capital、Hearst Ventures），估值超过 10 亿美元。**100 万用户只属于 Tezign。**
- WDCC 英文全称 “World Design Cities Conference”（不是 Capital）；范老师是 Co-Chief Curator。
- Vogue 称号：New Tech Pioneer。Syracuse 2025 演讲题目：“Design AI 2.0”。
- 其他荣誉：Fast Company Innovator of the Year、Fortune 40 Under 40、WEF Young Global Leader、Aspen Institute China Fellow。
- 学历：Harvard GSD Doctor of Design；Princeton Master of Architecture。
- 链接：LinkedIn https://www.linkedin.com/in/ling-fan/ ；Substack https://fanling.substack.com/（Fatflatfloat，暂时隐藏）。

## 五、写作偏好

- 英文材料避免读起来“太中国式”的表述；可持续等议题按美国院校关心的方式写，不用中国政策框架。
- 写创业时不要先讲钱，先讲社会和商业影响。
- Entrepreneurship 页不写 “Ling's”，不提 Lab。
- 只用有出处的真实数字；不确定的数字宁可不写。

## 六、内容放在哪里

- **`content.md`（仓库根目录）是唯一的文字来源**，英文。网站和 GSD 作品集 PDF 都从它生成。文件开头有格式说明；`<!-- -->` 注释里的内容不会出现在网站上；一个单元格只有 “—” 表示空。
- 每个作品用哪些图、哪张结构图，写在 `src/content.py` 的 `_WORK_SETTINGS`；结构图（SVG 线稿）在 `src/diagrams.py`；页面模板在 `src/site.py`；图片和视频在 `src/media/`（构建时复制到 `site/media/`）。
- 范老师习惯在 Claude Doc “范凌网站与作品集文字” 里改文字：https://claude.ai/code/artifact/7adfea2c-50dc-4f6c-a5e6-5f88d7b33231 。这个文档**没有完全同步**（LinkedIn/Substack、10-04 之后的修改都没进去），以 `content.md` 为准。若继续用文档改：把文档导出为 markdown，用 `python3 src/sync_from_doc.py <导出文件>` 写回 `content.md`，或者手动对照改。
- `notes/talks-news-proposal.md`：Talks 和 News 的提案记录，其中范老师确认的部分已上网站。

## 七、构建和发布流程

1. 改 `content.md`（或 `src/` 里的模板、结构图）。
2. 生成网站：`cd src && python3 site.py ../site`。会生成 `site/` 下所有静态页面，以及 sitemap.xml、robots.txt、llms.txt。
   - `sh build.sh` 会同时生成作品集 PDF，但它把 PDF 写到旧项目的 `../gsd-application/portfolio/`，新项目里没有这个目录。只做网站时用上面这条命令就够了。
3. 提交并推送到 `fanling/fanling-site`。`site/` 也要提交：Vercel 不跑构建，直接发布 `site/`（见 `vercel.json`，开启了 cleanUrls，网址不带 .html）。
4. 推到 `main` 即自动上线；推到其他分支只生成 Vercel 预览。**上线前要有范老师明确同意。**
5. 上线后到 www.fanling.ai 对应页面核对。
- 云端会话第一次推送前，可能需要先把 `fanling/fanling-site` 加为可推送仓库。
- `__pycache__` 和 `src/portfolio.html`（PDF 中间文件）不进仓库，见 `.gitignore`。
- 移动端：2026-10-04 在 390px 宽度下检查过，所有页面没有横向溢出。

## 八、域名和托管

- 托管在 Vercel，连着这个 GitHub 仓库（范老师自己导入的）。
- 域名 DNS 在 Cloudflare，记录是灰云（DNS only，不走 Cloudflare 代理）。`www.fanling.ai` 是主域名。
- Claude 不碰域名和 DNS；需要改时由范老师在 Cloudflare / Vercel 里操作。
- 旧网站 fan0.ai 已经无法访问。另有一个旧页面 fanling.tezign.net。

## 九、还没做的事

- 合并 PR #1（分支 `claude/project-thread-drmsah`）上线（第二节的两处更正），等范老师确认。
- BMR 页面里团队成员的英文名是 Claude 按拼音转写的，范老师还没确认。
- 可选：Substack 开始维护后，在 `content.md` 里去掉注释，重新打开博客栏目。
- 可选：把 Claude Doc 和 `content.md` 重新同步一次，避免以后改文字时用到旧版本。
