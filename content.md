<!--
范凌个人网站与 GSD 作品集的文字源文件（英文）。可直接编辑的版本在 Claude Doc：https://claude.ai/code/artifact/7adfea2c-50dc-4f6c-a5e6-5f88d7b33231 ，Ling 在那里改，Claude 把改动同步到本文件后重新生成网站和 PDF。

怎么改：
- 以 "# " 开头的是栏目，以 "## " 开头的是栏目里的一项。标题行请不要改名，只改下面的文字。
- 段落之间空一行。
- "- 标签: 内容" 是一行事实（冒号后面要有一个空格）。
- "- 年份 | 标题 | 出处" 这样的行用竖线分隔各栏，栏的顺序不要变；没有内容的栏留空即可。
- [To add: ...] 是待补的地方，网站和 PDF 上会显示成蓝色的 “To add”。
- *文字* 表示斜体。
改完后在对话里说一声，Claude 会重新生成网站和 PDF。
-->

# Basics

## Name
Ling Fan

## Chinese name
范凌

## Thesis
Designing AI, and through it, redesigning systems.

## Short bio
Ling Fan is a globally recognized entrepreneur and scholar of design AI. He is a Professor in Design AI at Tongji University, where he founded the Design Artificial Intelligence Lab, and the founder and chairman of Tezign, a unicorn that builds agentic AI for more than 200 Fortune 500 companies around the world. Trained as an architect at Princeton (MArch) and Harvard (Doctor of Design), he works on how designers can shape AI itself and, through it, redesign systems and organizations. Ling is a World Economic Forum Young Global Leader, an Aspen Institute China Fellow and a member of the Aspen Global Leadership Network.

## Contact email
lfan@tongji.edu.cn

## Profiles (name: link)
- LinkedIn: https://www.linkedin.com/in/ling-fan/
- Substack: https://fanling.substack.com/

## Substack (name | description)
- Fatflatfloat | Ling's newsletter on design, AI and education, in English and Chinese.

# Statement

## Text
For most of its history, architecture was a synthesizing discipline. Vitruvius asked the architect to know geometry, history, music, medicine and law, and the Renaissance gave that figure a name: the *uomo universale*, at once builder, engineer and humanist. The modern division of labor narrowed the architect into a specialist of form and space.

I believe artificial intelligence gives design a chance to recover that breadth. The designer can now design the intelligence itself: what it learns from, how it reasons, how it acts. Through it, the designer can redesign the systems in which people create, decide and live together. That is a far larger canvas than form, and it is close to what Buckminster Fuller meant by comprehensive anticipatory design science.

Before I became an entrepreneur I wrote an essay, *The Future in the Past: Fuller, Alexander, and Negroponte*, trying to read my own path as a trajectory of Fuller's. The decade since has been an attempt to test it on two fronts. At the Design AI Lab at Tongji University I study the computability of creativity: whether the subjective and divergent qualities of design can be represented, evaluated and generated. At Tezign I have built these ideas into agentic AI systems used by more than 200 enterprises and over one million professional users, so that claims about design and AI can rest on evidence.

The works that follow are not buildings. They are models, datasets, agents and the institutions that carry them. I present each the way an architect presents a project: the question it answers, its structure, how it performs in use, and what it taught me.

# Work 01 | Subjective World Model

## Subtitle
atypica.AI: a foundation model that simulates human behavior, decisions and feelings

## Question
Can a model represent people as they actually differ, in taste, judgment and story, rather than as an average?

## Text
Most AI models are trained to converge on the most probable answer, and in doing so they erase the differences between people. They also learn from public text, which records what people say, not what they do. A subjective world model takes the opposite aim: its state is a single person.

Each person is built from four layers of evidence: expression (what they say in reviews, posts and surveys), story (how they narrate their own lives), cognition (the weights they actually give to price, taste, health or novelty, inferred from their choices rather than asked) and behavior (what they did). When the layers disagree, as when someone who says they avoid sugar keeps ordering sweet tea, the contradiction is kept as evidence rather than averaged away. Given a new event, the model rolls the person forward many times and returns a distribution of reactions, not a single guess.

The model is checked against people. Its predictions are compared with in-depth interviews of the same people, and AI personas play the same behavioral-economics games as humans, following Park et al. (2024). When a design reaches the market, the gap between predicted and actual response is used to recalibrate the personas.

atypica.AI puts this research into use. It builds AI personas and lets them take part in interviews, user tests and discussions, so that designers, researchers and businesses can simulate how different people would respond to a product, a message or a policy before it exists. Its premise is a design premise: people do not choose between things; they choose between descriptions of things.

## Facts
- Used by: more than one million people in 50 countries
- Validation: against in-depth interviews with real people, and behavioral-economics games played by personas and humans
- Research line: Subjective World Models, Design AI Lab, Tongji University

## Links
- atypica.ai: https://atypica.ai/about

# Work 02 | Creative Reasoning

## Subtitle
A reasoning model that puts divergent thinking before convergent thinking

## Question
What would a reasoning model look like if its goal were to discover new possibilities rather than converge on one correct answer?

## Text
Reasoning models are usually trained toward convergence: a single, verifiable answer. Design works differently. A designer opens a space of options, sets them against each other, discards most, and combines what remains into something no single option contained.

The Creative Reasoning Model is trained to reason the same way. It breaks a brief into sub-problems, unfolds several possibilities for each, often borrowed from other fields, compares and prunes them, and fuses what survives. It treats exploratory value and the discovery of new possibilities as explicit objectives. To our knowledge it is the first divergent, creativity-centered reasoning model.

Divergence does not come from prompting; it has to be in the training data. The model learns from the decision records of real design projects: 10,000 trajectories from more than 180 companies, each annotated by hand from brief to delivery. Each one keeps the ideas that were dropped, who dropped them and why, because judgment is learned from what was rejected as much as from what was chosen. A small model trained to force divergence expanded these seeds to one million trajectories, sampled and checked by practitioners who had run similar projects.

## Facts
- Evaluation: 77% preference in a 2025 blind test: 970 of 1,260 votes by client brand managers and creative directors, comparing Tezign's full system built on Works 01 and 02 with a base model (p < 0.001)
- Developed at: Tezign, with the Design AI Lab, Tongji University
- Research line: Creative Reasoning, Design AI Lab

## Links
- Creative Reasoning: https://creative-reasoning.com/

# Work 03 | Agentic Creativity

## Subtitle
A long-horizon creative agent

## Question
Can an agent take part in the whole arc of creative work, and extend what a team can imagine rather than automate it?

## Text
Most AI tools answer one prompt at a time. Product innovation is a long process: sensing what people want, framing an opportunity, generating and testing concepts, and carrying the result to market. Agentic creativity asks how autonomous agents can participate in, and extend, that creative act rather than merely automate parts of it.

The product-innovation agent, which runs inside atypica.AI, is designed for the whole horizon. Given a brief such as a new spring gift box, it asks the questions that set the bounds, studies what the company already learned and what people are saying, diverges with the Creative Reasoning Model, and tests each direction in parallel with Subjective World Model personas and interviews. It returns a recommendation in which every claim traces back to its evidence.

People stay in the loop: they set the bounds, approve the plan before costly work starts and make the final call. Every decision, including what was rejected and why, is written back to a graph of the organization's decisions, so the next project starts from it.

The design builds on the Lab's research on human-centered creativity with vision–language models and on multi-agent collaboration in design workflows, and it runs on Tezign's infrastructure of post-trained models, context systems and agent harnesses.

## Facts
- Used for: consumer insight, product innovation and marketing growth at Tezign
- Runs in: atypica.AI, on Tezign's agent platform
- Research: Aug-Creativity (HCII 2025); multi-agent collaborative design (HCII 2024)
- Research line: Agentic Creativity, Design AI Lab

## Links

# Past work 01 | The Computability of Creativity

## Subtitle
Datasets and a knowledge graph

## Question
Which parts of creative work can be computed, and what must data and knowledge contain for creativity to be identified, evaluated and generated?

## Text
This series is the ground beneath the three models. Each project gathers a body of design knowledge into a form a machine can learn from, and in doing so tests where creative work can be computed and where it resists.

The datasets come from places design research rarely looks: the colour cultures of Chinese youth subcultures, the fast-moving world of blind-box designer toys, and traditional crafts such as Jinshan farmer painting. Prometheus goes a step further and constructs design knowledge itself as a knowledge graph that models can reason over.

Together they make three things possible: identifying creativity, evaluating it, and generating creative work.

## Series (letter | name | description)
- a | Youth-subculture colour dataset | Colour palettes drawn from Chinese youth subcultures, used for culture-inspired multimodal palette generation and colorization (IEEE MIPR 2021).
- b | Blind-box dataset | A dataset of blind-box designer toys, a consumer form where taste, rarity and collecting meet, used to generate new figures, outfits, props and scenes in 3D. [To add: scale of the dataset]
- c | Chinese traditional craft dataset | Traditional crafts including Jinshan farmer painting, used to study how AI can support the inheritance of craft (Decoration, 2022). In an installation built on it, visitors sketch a person, a house or a tree, and the system paints the scene in the Jinshan style.
- d | Prometheus | A knowledge graph that constructs design knowledge in a form machines can reason over. Ask it a question about design and it unfolds the concepts and sources linked to the answer. [To add: what the graph contains and its scale]

## Facts
- Talks: The Computability of Design, Brown University (2024); keynote, Hong Kong Polytechnic University (2023)
- Research line: The Computability of Creativity, Design AI Lab

## Links

# Past work 02 | Brain–Machine Ratio (BMR)

## Subtitle
A quantitative study and a qualitative study

## Question
In a creative process shared by people and machines, which part should each take, and how can that division be measured?

## Text
The Brain–Machine Ratio (BMR) asks how creative work should be divided between the designer's judgment and the machine's capacity.

It is studied in two ways, side by side. The quantitative study measures how the work divides today, task by task. The qualitative study traces how that division came to be, through six centuries of creative tools.

## Series (letter | name | description)
- a | Quantitative study | The BMR quadrant sorts creative tasks by two questions: do people want to do the task or only have to, and can machines do it? The upper half is what people should lead; the lower half is what they can hand to machines. BMR 1.0 measures capability, the ratio of human to machine input in each task. BMR 2.0 multiplies that ratio by subjectivity, the will people bring to a task. BMR 3.0 is about trust: AI that automates what is easy and safe to delegate, and augments what is hard and cannot be delegated. Design teams at Alibaba and Tencent have used it to build teams and organize creative workflows (IEEE MIPR 2021).
- b | Qualitative study: A History of Creative Tools | From perspective and photography to computers, software and AI, each change in tools has altered the threshold, the process and the possibilities of creative work. The study follows three threads from 1400 to 2026: technology brings new capabilities, tools turn them into practice, and ideas keep asking what creating means. The first edition was completed in 2023; the second, in 2026, adds generation, reasoning, agents and world models. Its nine-panel timeline was shown at the WDCC 2026 Theme Exhibition in Shanghai. Funded by the National Social Science Fund of China (2024–2027).

## Facts
- First set out in: From Universality of Computation to the Universality of Imagination (2019)
- Paper: The Brain-Machine-Ratio model for designer and AI collaboration (IEEE MIPR 2021)
- Used by: Design teams at Alibaba and Tencent
- Timeline: nine panels, 1400 to 2026; first edition 2023, second edition 2026
- Exhibited: WDCC 2026 Theme Exhibition, "Designing Generation: From AI-Driven Design to Designing AI", World Design Cities Conference, Shanghai
- Funding: National Social Science Fund of China, Research on the Evolution of Design Tools in the Era of Artificial Intelligence (2024–2027); Ministry of Education (2020); Shanghai art and technology program (2019)
- Timeline team: Ling Fan with Li Dan, He Ziming, Wu Pengfei and Zhong Siyuan (2023); Ling Fan with Xia Lei and Zhou Zhiyuan (2026)
- Research line: Human–AI collaboration, Design AI Lab

## Links
- Paper (IEEE MIPR 2021): https://doi.org/10.1109/MIPR51284.2021.00058

# Tezign

## Subtitle
Design science at production scale · Founder and Chairman, 2015–present

## Text
I founded Tezign to find out whether design science can hold up, and scale, in the world. The company builds an agentic AI platform for business: post-trained models, context systems, agent harnesses, and long-running, proactive agents for consumer insight, product innovation and marketing growth.

Tezign is where these works are tested at production scale. Use returns evidence, and evidence returns new research questions to the Lab.

## Facts
- Clients: 200+ global enterprises
- Users: more than one million professional users
- Funding: more than US$150 million raised; valuation above US$1 billion
- Investors: Temasek, Sequoia Capital, Hearst Ventures, among others
- Agent activity: monthly uses of each thousand assets in its content library rose from 12 in 2023 to 3,240, 99% of them started by AI agents
- Recognition: first on The Information's Top 50 Innovators list

# Lab

## Title
Design Artificial Intelligence Lab, Tongji University

## Text
Founded in 2017, the Lab is the research home of this work: about twenty master's, doctoral and postdoctoral researchers working on the computational foundations of creativity, subjective world models and creative reasoning, with applications in design, innovation, education and human–AI collaboration.

## Facts
- Publications: 100 articles and papers
- Intellectual property: led the filing of 200 invention patent applications
- Research funding: US$5 million, from NGOs, national funding agencies and global companies

## Funded projects (years | project | funder)
- 2024–2027 | Research on the Evolution of Design Tools in the Era of Artificial Intelligence | National Social Science Fund of China
- 2024–2025 | Multimodal Digital Asset Management Based on High-Quality Industrial Corpora | Shanghai Industrial High-Quality Development Special Fund
- 2024 | New Design Capabilities: an AIGC Competence Development Platform for the Design Industry | Shanghai Cultural and Creative Industry Development Fund
- 2020–2023 | Trends in Art and Design Practices in the Context of Artificial Intelligence | Ministry of Education

# Teaching

## Text
I have taught design AI for nearly two decades, on three continents: at the Central Academy of Fine Arts, the Oslo School of Architecture and Design, the University of California, Berkeley, and, since 2016, Tongji University.

My teaching asks students from different disciplines to experiment in two directions at once: how AI changes their own creative practice, and how they might design new relationships with intelligent systems. I pair a foundation course with hackathons that bring learning by doing to a public showcase, and with invited voices from design, technology and business.

## Supervision and programs
I currently supervise 10 doctoral students, and 30 of my master's students have graduated. Former students lead product and design at AI companies; two of my doctoral graduates now teach at universities.

At Tongji I co-founded two of the first degree programs among the world's design schools to combine AI and design: the graduate program in AI and Data Design and the undergraduate program in AI and Visual Communication.

# Writing

## Books (year | title | publisher)
- 2019 | From Universality of Computation to the Universality of Imagination: A Catalog on Design and Artificial Intelligence | Tongji University Press
- 2014 | Ten Dialogues: Hui Wang × Ling Fan | Tongji University Press

# News

## News (date | item | link; newest first)
- 2026 | Joined the Steering Committee of Business of Design Week (BODW), Hong Kong | —
- 2026 | Spoke on agentic transformation in business and society at the World Artificial Intelligence Conference, Shanghai | —
- 2026 | Gave the talk "The Subjective World Model" at Super AI, Singapore | https://www.youtube.com/watch?v=tCl8s9B2WqU&t=3s
- 2026 | Paper at CHI 2026: "The Wetland Quest", on VR and empathy for urban wildlife | https://doi.org/10.1145/3772318.3790443
- 2025 | Gave the L. C. Dillenback Lecture at Syracuse University School of Architecture | https://www.youtube.com/watch?v=owxND_hP4nE
- 2025 | Named a Business Innovation Leader by Vogue Business | —
- 2025 | Launched atypica.AI | https://atypica.ai/about

# Talks

## Talks (year | venue | title | video link)
- 2026 | World Artificial Intelligence Conference, Shanghai | Agentic Transformation in Business and Society | 
- 2026 | Super AI, Singapore | The Subjective World Model | https://www.youtube.com/watch?v=tCl8s9B2WqU&t=3s
- 2025 | Syracuse University School of Architecture | L. C. Dillenback Lecture: Design+AI: Research and Entrepreneurship | https://www.youtube.com/watch?v=owxND_hP4nE
- 2024 | Brown University | The Computability of Design | 
- 2024 | China Europe International Business School | Best Practices in AI and Business Innovation | 
- 2023 | Hong Kong Polytechnic University | The Computability of Design and Possibilities of Generative Design (keynote) | https://www.youtube.com/watch?v=4EzYikrUDUg&list=PL16ugZF7jMZWVtZk6_q1OERR8p4aFNer7
- 2019 | X Design Conference, Harvard Business School and Harvard GSD | Design and AI (keynote) | 

# Publications

## Publications (year | authors | title | where published | DOI or link; papers and essays together, newest first)
- 2026 | Fan, L. | [To add: title of the 2026 essay on AI] | [To add: where published] | —
- 2026 | Xia, L., Li, X., Fan, J., Li, D., & Fan, L. | The Wetland Quest: Fostering empathy and literacy for urban herpetofauna through VR wetland exploration. | Proceedings of CHI 2026, Article 1559, 1–15. | https://doi.org/10.1145/3772318.3790443
- 2025 | Fan, L. | [To add: title of the 2025 essay on AI] | [To add: where published] | —
- 2025 | Li, D., Xia, L., & Fan, L. | Aug-Creativity: Framework for human-centered creativity with vision language models. | HCII 2025, LNCS 15770, 86–101. | https://doi.org/10.1007/978-3-031-93864-1_7
- 2025 | Li, X., He, Z., Xi, L., Zeng, S., Zhang, D., & Fan, L. | Generative AI meets creative design: Shaping a dynamic learning ecosystem. | IASDR 2025: Design Next. | https://doi.org/10.21606/iasdr.2025.520
- 2025 | Li, X., Wu, P., He, Z., Li, J., & Fan, L. | Multi-agent AI: Collaborative design with multiple AI tools in interior design workflow. | HCI International 2024 Late Breaking Posters, CCIS 2320, 202–211. | https://doi.org/10.1007/978-3-031-78531-3_23
- 2024 | Fan, L. | [To add: title of the 2024 essay on AI] | [To add: where published] | —
- 2022 | Fan, L., Li, D., Zhuo, J., et al. | AI empowering the inheritance of traditional craft art: A case study of Jinshan farmer paintings. | Decoration, (7), 94–98. | https://doi.org/10.3969/j.issn.0412-3662.2022.07.014
- 2021 | Fan, L., Bao, Y., Gong, S., Yan, S., & Wang, H. J. | The Brain-Machine-Ratio model for designer and AI collaboration. | IEEE MIPR 2021, 308–313. | https://doi.org/10.1109/MIPR51284.2021.00058
- 2021 | Li, Y., Zhuo, J., Fan, L., & Wang, H. J. | Culture-inspired multi-modal color palette generation and colorization: A Chinese youth subculture case. | IEEE MIPR 2021, 382–385. | https://doi.org/10.1109/MIPR51284.2021.00071
- before 2015 | Fan, L. | The Future in the Past: Fuller, Alexander, and Negroponte. | [To add: where and when published] | —
- 2010 | Fan, L., Brazier, C., & Lam, T. | Becoming Beijing: Developer-architect dynamics in socio-political context. | Architecture & Urbanism, (7), 94–99. | 

# Patents

## Patents (title | number)
- Sub-Task Invocation System | ZL 202210689841.2
- Aesthetic Feature-Based Poster CTR Prediction | ZL 202110100658.X
- Adaptive Creative Generation Based on Structured Theory | ZL 201911304845.9
- Method and System for Generating Creative Assets | ZL 201910344677.X

# Appointments

## Appointments (years | institution | role)
- 2016–present | Tongji University, College of Design and Innovation | Professor in Design AI
- 2017–present | Tongji University, Design Artificial Intelligence Lab | Founding Director
- — | Shanghai Research Institute for Intelligent Autonomous Systems | Professor
- 2016 | M+ Museum of Visual Culture, Hong Kong | Inaugural Design Trust / M+ Design Fellow
- 2013–2015 | University of California, Berkeley | Lecturer
- 2012–2013 | Harvard Graduate School of Design | Teaching Fellow
- 2007–2011 | Central Academy of Fine Arts, Beijing | Lecturer
- 2007–2010 | Princeton Center for Architecture, Urbanism, and Infrastructure | Fellow
- 2008 | Oslo School of Architecture and Design | Visiting Lecturer

# Education

## Degrees (year | school | degree)
- 2014 | Harvard University | Doctor of Design
- 2007 | Princeton University | Master of Architecture
- 2005 | Tongji University | Bachelor of Architecture

# Honors

## Honors (year | honor)
- 2025 | Business Innovation Leader, Vogue Business
- 2023 | New Growth Pioneer, Harvard Business Review
- 2019 | 40 Under 40, Fortune
- — | Innovator of the Year, Fast Company
- 2018 | National Award for Design Talent, China
- 2017 | Young Global Leader, World Economic Forum
- 2016 | Cultural Leader, World Economic Forum
- 2016– | Aspen Institute China Fellow; Aspen Global Leadership Network

# Service

## Service (years | role)
- 2026– | Steering Committee Member, Business of Design Week (BODW), Hong Kong
- 2024– | Chairman, AI and Business Initiative, China Europe International Business School
- 2024– | Trustee, China Social Entrepreneur Foundation
- 2022– | Chief Expert, National Industrial Design Center, China
- 2019– | Member, IEEE Council for Extended Intelligence
- 2018– | Trustee, Yunqi Academy of Engineering

# Media

## Media
- Harvard Business Review (2026)
- People's Daily (2025)
- Tatler (2024)
- Bloomberg (2021): “Harvard-Trained Designer Creates China Business Software Unicorn”
- Forbes (2020)
