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
Designers should not only use AI, but design it, and through it redesign the systems we live in.

## Headline
Researcher, Entrepreneur in Design AI.

## Short bio
Ling Fan is Professor in Design AI at Tongji University, founding director of its Design Artificial Intelligence Lab, and founder and chairman of Tezign. Trained as an architect at Princeton and the Harvard Graduate School of Design, he studies the computability of creativity: how designers can shape AI itself and, through it, redesign systems and organizations. His research is carried into AI systems used by more than 200 enterprises and over one million professionals.

## Biography (from Ling's CV, October 2026)
Ling Fan is an internationally recognized researcher and entrepreneur whose work has helped shape the emerging field of Design AI.

Fan is a Professor in Design AI at Tongji University and the Founding Director of the Tongji University Design AI Lab. At the center of his research is the computability of creativity: how creativity can be computationally represented, understood, reasoned through, and enacted while preserving the subjectivity and plurality on which it depends. He approaches this question through three interconnected areas. Creative Reasoning investigates how to train reasoning models to generate, evaluate, and develop divergent possibilities. Subjective World Models explore how to train foundation models that can represent differences in human perception, preference, values, and judgment. Agentic Creativity examines how to design and develop autonomous AI systems that can initiate, participate in, and extend creative work. Fan has authored or co-authored more than 100 publications on design and artificial intelligence. The research and technology teams he has led have developed an intellectual property portfolio comprising more than 200 invention patent applications across AI foundation models, systems, and applications.

Fan founded Tezign to translate this research into technologies deployed at scale. The company has raised more than US$150 million from investors including Temasek, Sequoia Capital, and Hearst Ventures, and reached a valuation exceeding US$1 billion. Serving over one million professional users, Tezign builds and deploys agentic AI systems to address real-world problems and help organizations transform how they understand people, make decisions, and create. For Fan, this practice is an extension of research: a way to examine how AI operates within real social and organizational contexts, understand its consequences for people and institutions, and explore how it can be designed and deployed responsibly.

Trained as an architect, Fan approaches AI as an extension of architecture’s broader capacity to synthesize knowledge across design, technology, business, and the humanities. His work asks how designers can shape AI itself and, through it, reshape systems, organizations, and the possibilities of human creativity. Fan holds a Doctor of Design from Harvard University and a Master of Architecture from Princeton University. He is a World Economic Forum Young Global Leader, an Aspen Institute China Fellow, and a member of the Aspen Global Leadership Network.

## Contact email
lfan@tongji.edu.cn

## Profiles (name: link)
- LinkedIn: https://www.linkedin.com/in/ling-fan/
<!-- Substack hidden until Ling has updated it (2026-10-04); remove these comment marks to restore:
- Substack: https://fanling.substack.com/
-->

## Newsletter (link | description)
- https://fanling.substack.com/ | Occasional writing on design, AI and creativity, by email.

<!-- Blog hidden until Ling has updated Substack (2026-10-04); remove these comment marks to restore:
## Blog (name | description)
- Fatflatfloat | Ling's blog on Substack, on design, AI and education, in English and Chinese.
-->

# Research

## Title
The Computability of Creativity

## Text
Past and present, the research asks one question: how creativity can be computationally represented, reasoned through and enacted, while preserving the subjectivity and plurality on which it depends.

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
- Validation: against in-depth interviews with real people, and behavioral-economics games played by personas and humans
- Research line: Subjective World Models, Design AI Lab, Tongji University

## Links
- atypica.ai: https://atypica.ai/about

## Training
The model is trained on data from real users, person by person. Each persona is assembled from four layers of evidence that come from different sources and carry different weight: expression (reviews, posts and survey answers, cheap to collect and self-reported), story (how the person narrates their own life and identity), cognition (decision weights for price, brand, health, convenience, social approval and novelty, inferred from behavior rather than asked) and behavior (orders, clicks, repeat purchases and lapses, costly to collect but already fact).

The layers are checked against each other. When they disagree, as when someone ticks "cutting down on sugar" in a survey and orders sweet tea four times that month, the contradiction is not averaged away but kept as a feature of that person.

Given the person's history and a new event, the model rolls the person forward many times, independently, and returns a distribution of reactions rather than one answer. That distribution is the form in which it is tested: against AI-led in-depth interviews with the same real people, run without the model seeing the interviews, and against behavioral-economics games played by personas and humans alike, following Park et al. (2024). Once a design reaches the market, the gap between predicted and actual response is used to recalibrate the decision weights of the personas concerned, and the next rollout starts from the calibrated state.

## atypica
atypica.AI is a subjective-world simulation agent built on the model. Given a research question, it assembles the relevant personas, interviews them one by one, runs discussions and user tests among them, and writes up what it finds, with every claim traced back to the persona evidence behind it.

It turns the model into a research instrument that designers, researchers and businesses can use before anything exists: to see how different people would respond to a product, a message or a policy, and why.

## Cases (kind | title | text | figures)
- Enterprise | Global food brand: concept testing in days | For a Lunar New Year chocolate launch, the team used AI consumers to co-create and filter concepts, then cross-checked the signal against real interviews. Three routes were scored (Gift Box Edition 84, Lunar Mini Bar 71, Festival Tin 63) and the gift box was chosen for markets including China, Singapore and Malaysia. Concept testing went from months to days, weak ideas were filtered early, and the AI-selected concept outperformed the control by 23 per cent in market validation. | 6× R&D throughput; 80% cost saving; 5 markets
- Enterprise | Power tools brand: an always-on panel of professionals | Professional users are expensive and hard to recruit. Personas built from real interview data now serve as an always-on panel for concept, interface and CAD review, giving feedback on prototypes such as grip angle, weight balance and trigger reach in gloves. Product teams test industrial-design decisions immediately instead of waiting on recruiting cycles. | $0 recruiting cost; real-time feedback
- Academic | University research team: household-scale policy simulation | Researchers interviewed core family members one by one, built AI personas from the interviews and assembled them into 17,647 household-scale virtual family panels to simulate responses to policy. Testing that would have taken years of qualitative fieldwork ran in days, while keeping household-level nuance. | 17,647 family panels; 200+ archetypes; days, not years

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

# Past work 01 | Datafying Creativity

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
- c | Chinese folk craft dataset | Traditional crafts including Jinshan farmer painting, used to study how AI can support the inheritance of craft (Decoration, 2022). In an installation built on it, visitors sketch a person, a house or a tree, and the system paints the scene in the Jinshan style.
- d | Prometheus | A knowledge graph that constructs design knowledge in a form machines can reason over. Ask it a question about design and it unfolds the concepts and sources linked to the answer. [To add: what the graph contains and its scale]

## Facts
- Talks: The Computability of Design, Brown University (2024); keynote, Hong Kong Polytechnic University (2023)
- Research line: The Computability of Creativity, Design AI Lab

## Links

## Project a
Colour carries meaning differently in different cultures, and Chinese youth subcultures have developed colour languages of their own. The project collected and annotated colour palettes from these subcultures and built them into a dataset; each band of stripes shows the palettes of one subculture, read side by side.

On the dataset the Lab trained models for culture-inspired, multimodal palette generation and colorization. A designer chooses a subculture, such as electronic music, enters the feeling they want in a few words ("sunny, joyful, passionate") and uploads an image; the tool proposes a palette in that subculture's idiom, lets the designer adjust each colour by hue, lightness and saturation, and colours the design with the result.

It asks whether a culture's taste in colour can be represented explicitly enough for a machine to learn it without flattening it. Published as "Culture-Inspired Multi-Modal Color Palette Generation and Colorization: A Chinese Youth Subculture Case" (IEEE MIPR 2021), with a related study of music visualization through multimodal colour generation (NIME 2021); the dataset is the subject of Li Yufan's doctoral dissertation, "Subcultural Color: The Study and Construction of a Color Dataset" (2020).

## Project b
Blind-box designer toys are a consumer form in which taste, rarity and collecting meet, and new series succeed or fail quickly. The project assembled a dataset of 211 figures from leading blind-box series and analysed each one along four dimensions: shape, theme, price and colour.

Shape: animals make up 39.3 per cent of the figures, humanoids 35.2, fantastical creatures 15.6, licensed collaborations 6.5 and figures from legend 3.3; the proportion of eye to face was measured on every figure and abstracted into face templates. Theme: figures were coded by scene, daily life, tradition, story, companionship, desire and function, with animals and monsters (47) and food (28) the largest groups. Price: every series was placed on radial charts by price. Colour: a palette was extracted from every figure and grouped by series.

The dataset was then used to generate new figures, outfits, props and scenes in 3D, so that designers can explore a series before it is modelled by hand. It tests how far a fast-moving, trend-driven design language can be captured as data, and where the designer's judgment of what will be loved remains decisive.

## Project c
Folk crafts are passed on by apprenticeship and are at risk when that chain breaks. The project built a dataset of Chinese folk craft, beginning with Jinshan farmer painting from the outskirts of Shanghai, and studied how AI can support the inheritance of a craft rather than replace its makers.

On the dataset the Lab built AI Zanhui, an installation in which anyone can paint in the Jinshan style. A visitor chooses one of three themes drawn from the paintings themselves (Living and Working in Peace, Land of Fish and Rice, A New Era), sketches a house, a tree or a person, and signs the drawing; the system then paints the scene in the Jinshan palette and composition, with the signature set as a seal. The sketch decides what is in the picture, and the craft decides how it is painted.

It lets people take part in a craft they could not otherwise practise, and it asks which parts of a folk style can be learned from examples and which still belong to its makers. Published as "AI Empowering the Inheritance of Traditional Craft Art: A Case Study of Jinshan Farmer Paintings" (Decoration, 2022).

## Project d
Datasets record examples of design; Prometheus records design knowledge itself. Named after the figure who brought fire and knowledge to humankind, it is a knowledge graph that links the concepts, methods, works and sources of design through typed relations (is a, belongs to, visual element, relational element, principle, period, modern category), so that models can reason over design knowledge rather than only imitate examples.

A visitor asks a question in plain language. Asked "What is design?", it unfolds design into its visual elements (texture, colour, shape, size), its principles (usability), its periods (prehistoric, ancient, modern) and its fields (product, environmental, visual communication, new media). Asked how green relates to warm colours, it traces the path between them. Asked what a serif is, it returns the sentences in its sources behind the answer and links each one to the concept it supports.

It is the step from datafying creative work to making design knowledge computable, at the meeting point of design and AI that the project calls creativity.

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
- b | Qualitative study: A History of Creative Tools | From perspective and photography to computers, software and AI, each change in tools has altered the threshold, the process and the possibilities of creative work. The study follows three threads from 1400 to 2026: technology brings new capabilities, tools turn them into practice, and ideas keep asking what creating means. The first edition was completed in 2023; the second, in 2026, adds generation, reasoning, agents and world models. Its nine-panel timeline was shown at the WDCC 2026 Theme Exhibition in Shanghai, where Ling served as Co-Chief Curator. Funded by the National Social Science Fund of China (2024–2027).

## Facts
- First set out in: From Universality of Computation to the Universality of Imagination (2019)
- Paper: The Brain-Machine-Ratio model for designer and AI collaboration (IEEE MIPR 2021)
- Used by: Design teams at Alibaba and Tencent
- Timeline: nine panels, 1400 to 2026; first edition 2023, second edition 2026
- Exhibited: WDCC 2026 Theme Exhibition, "Designing Generation: From AI-Driven Design to Designing AI", World Design Cities Conference, Shanghai; Ling was Co-Chief Curator of WDCC 2026
- Funding: National Social Science Fund of China, Research on the Evolution of Design Tools in the Era of Artificial Intelligence (2024–2027); Ministry of Education (2020); Shanghai art and technology program (2019)
- Timeline team: Ling Fan with Li Dan, He Ziming, Wu Pengfei and Zhong Siyuan (2023); Ling Fan with Xia Lei and Zhou Zhiyuan (2026)
- Research line: Human–AI collaboration, Design AI Lab

## Links
- Paper (IEEE MIPR 2021): https://doi.org/10.1109/MIPR51284.2021.00058

# Tezign

## Subtitle
Founder and Chairman, 2015–present

## Page title
From Research to Practice

## Text
Entrepreneurship extends the research into practice: models and agents developed through research are carried into products that organizations use, responsibly and at scale, to understand people, make decisions and create.

## Company
Founded in 2015 to translate research into technologies deployed at scale, Tezign builds agentic AI systems for organizations. It serves more than 200 enterprises and over one million professional users, and has raised more than US$150 million from investors including Temasek, Sequoia Capital and Hearst Ventures.

## Products (name | link | description | image)
- Tezign | https://www.tezign.com/en | The Generative Enterprise Agent (GEA) platform: post-trained models, context systems, agent harnesses and long-running, proactive agents for consumer insight, product innovation and marketing growth. | tezign-home.jpg
- atypica.AI | https://atypica.ai | A social-simulation agent built on subjective world models. | atypica-home.jpg
- MuseDAM | https://www.musedam.cc/en-US | An AI-native context system that makes the right content reliably available to the right people and AI. | musedam-home.jpg

## Product pages (name | kind | text)
- Tezign | Generative Enterprise Agent | GEA is the platform on which Tezign's agents run. It is built in layers: models, including the Subjective World Model, the Creative Reasoning Model and a hub of third-party models; a context layer that organizes a company's content, knowledge and past decisions into a context graph; an agent operating system that builds, connects and supervises agents; and proactive agents for consumer insight, product innovation and marketing growth. Agents start from one verifiable business loop, work continuously within governed boundaries, and expand to more teams as they prove themselves. In a 2025 blind test, client brand managers and creative directors preferred the full system built on the two models to a base model in 970 of 1,260 votes.
- atypica.AI | Social simulation agent | atypica.AI simulates the human response to a business or social decision. Grounded in real-world attitudinal and behavioral data, it creates simulated people that teams can interview, test and learn from, and then evaluates its predictions against responses from real people. It is where the Subjective World Model meets its users.
- MuseDAM | AI-native context system | MuseDAM is an AI-native system for an organization's creative assets and the context around them. It organizes, tags and parses images, video, 3D and documents automatically, lets teams find assets by conversation rather than folders, and keeps versions, comments, permissions and usage in one place, so that the right content is reliably available to the right people and to the organization's AI agents.

# Lab

## Title
Design AI Lab

## Text
Ling founded the Design Artificial Intelligence Lab at Tongji University in 2017 as the research home of this work. Its master's, doctoral and postdoctoral researchers study the computability of creativity, through creative reasoning, subjective world models and agentic creativity, with applications in design, innovation, education and human–AI collaboration. The Lab has produced more than 100 publications and secured more than US$5 million in research funding from the National Social Science Fund of China, the National Natural Science Foundation of China, the Ministry of Education, Shanghai municipal programs and industry partners including Alibaba, ByteDance and Aptar. Ling currently advises 8 doctoral students and about 15 master's students, and 15 master's students have graduated under his supervision; graduates lead AI product design and development at technology companies, or go on to research at universities and research institutions.

## Facts
- Publications: 100 articles and papers
- Intellectual property: led the filing of 200 invention patent applications
- Research funding: more than US$5 million

## Funded projects (years | project | funder)
- 2024–2027 | Research on the Evolution of Design Tools in the Era of Artificial Intelligence | National Social Science Fund of China
- 2024–2025 | Multimodal Digital Asset Management Based on High-Quality Industrial Corpora | Shanghai Industrial High-Quality Development Special Fund
- 2024 | New Design Capabilities: an AIGC Competence Development Platform for the Design Industry | Shanghai Cultural and Creative Industry Development Fund
- 2023 | Tezign's Multimodal Content Generation Algorithm | Xuhui District Large-Scale Model and Generative AI Initiative
- 2020–2023 | Trends in Art and Design Practices in the Context of Artificial Intelligence | Ministry of Education

# Student advising

## Text
Ling currently advises 8 doctoral students and about 15 master's students, and 15 master's students have graduated under his supervision.

Graduates lead AI product design and development at technology companies, or go on to research at universities and research institutions.

## Doctoral students (year of entry | name | dissertation title; from Ling's CV, October 2026)
- 2024 | Mudasir Ahmed | Generative Ethnography: AI-Based Simulation of Social Dynamics for Small and Medium-Sized Enterprises in Pakistan
- 2023 | Li Dan | A Quantitative Study of Tool Effects on Creativity in Design Practice
- 2022 | Xia Lei | Digital Embodiment in Human–AI Collaborative Design Processes
- 2022 | Chen Danyang | Multi-Agent Design Teams in Brand Marketing: Theory, Architecture, and Implementation
- 2021 | He Ziming | Layout and Style: Generative Systems for Spatial Design
- 2020 | Li Yufan | Subcultural Color: The Study and Construction of a Color Dataset
- 2019 | Yan Sida | Design as Data: Translating Design to Machine
- 2019 | Zhuo Jinggang | Intelligent Layout Systems: Development and Application
- 2018 | Gao Yifang | Crossing Creator Identities under the Diffusion of Generative AI: Mechanisms and Pathways
- 2017 | Gong Shuyu | DesignNet: The Construction and Study of a Graphic Design Dataset

# Writing

## Books (year | title | publisher)
- 2019 | From Universality of Computation to the Universality of Imagination: A Catalog on Design and Artificial Intelligence | Tongji University Press
- 2014 | Ten Dialogues: Hui Wang × Ling Fan | Tongji University Press

# News

## News (date | item | link; newest first)
- 2026 | Co-Chief Curator of the 2026 World Design Cities Conference (WDCC), Shanghai | https://designcities.net/conference/2026-world-design-cities-conference-in-shanghai/
- 2026 | Spoke at the launch of the NYU Shanghai Global Institute for Longevity and Resilience | https://shanghai.nyu.edu/news/nyu-shanghai-launches-global-institute-longevity-and-resilience
- 2026 | Joined the Steering Committee of Business of Design Week (BODW), Hong Kong | —
- 2026 | Quoted by Xinmin Evening News on the Subjective World Model, an AI architecture for modelling people's preferences and decisions | https://finance.sina.com.cn/jjxw/2026-08-12/doc-inimzumt4069600.shtml
- 2026 | Interviewed in CCTV's live broadcast from the World Artificial Intelligence Conference, Shanghai, on AI moving from conversation to action | https://www.tezign.com/en/updates/ai-challenges-opportunities-human-relationship
- 2026 | Gave the talk "The Subjective World Model" at Super AI, Singapore | https://www.youtube.com/watch?v=tCl8s9B2WqU&t=3s
- 2026 | Paper at DRS2026, Edinburgh: "Design for Dignified Longevity: Olfactory-Enhanced VR Meditation for Sustained Mindfulness Practice" | https://dl.designresearchsociety.org/drs-conference-papers/drs2026/researchpapers/91
- 2026 | Paper at CHI 2026: "The Wetland Quest", on VR and empathy for urban wildlife | https://doi.org/10.1145/3772318.3790443
- 2026 | Keynote on agentic business at the AI business forum co-hosted by Tezign and CEIBS, Shanghai | https://www.tezign.com/en/updates/tezhan-ai-business-evolution-forum
- 2025 | Gave the L. C. Dillenback Lecture at Syracuse University School of Architecture | https://www.youtube.com/watch?v=owxND_hP4nE
- 2025 | "Design AI" exhibition on the computability of creativity at the 2025 World Design Cities Conference, Shanghai | https://www.icloudnews.net/a/105824.html
- 2025 | Featured by People's Daily on combining technology and creativity | https://www.tezign.com/en/updates/mp-peoples-daily-agent
- 2025 | Interviewed by The Paper: "AI has mostly been talking; next it has to work" | https://m.thepaper.cn/newsDetail_forward_30804203
- 2025 | Profiled by China News Service on bringing technology into the creative field | https://www.sh.chinanews.com.cn/kjjy/2025-04-30/135412.shtml
- 2025 | Named a New Tech Pioneer by VOGUE Business | —
- 2025 | Launched atypica.AI | https://atypica.ai/about
- 2024 | Named to Forbes China's 2024 New Era Disruptive Founders list | https://www.cnpp.cn/focus/3513627.html

# Talks

## Text
Ling Fan is a frequent speaker at universities, forums and platforms on design, AI and agentic transformation. Recurring topics:

## Topics (one per line)
- Design AI: The Computability of Creativity
- Agentic Transformation for Business
- Subjective World Model: Simulating People's Preferences and Decisions

## Contact
If you are interested in inviting Ling to speak, please contact lfan@tongji.edu.cn.

## Talks (year | venue | title | video link; from Ling's CV, October 2026)
- 2026 | Invited speaker, Schwarzman College, Tsinghua University, Beijing | Token Economy | 
- 2026 | Invited speaker, Shanghai New York University, Shanghai | The Subjective World Model | 
- 2026 | Invited speaker, SuperAI, Singapore | The Subjective World Model | https://www.youtube.com/watch?v=tCl8s9B2WqU&t=3s
- 2025 | L. C. Dillenback Lecture, Syracuse University, Syracuse, NY | Design AI 2.0 | https://www.youtube.com/watch?v=owxND_hP4nE
- 2025 | Livestream course, Hundun Academy (in Chinese) | How to Make AI Work Quietly, Like a Team of Minions | https://www.sohu.com/a/887713113_99922069
- 2024 | Panelist, Business of Design Week (BODW), Hong Kong | Design Intelligence in Tech Ecosystems | 
- 2024 | Keynote, D20 Global Design Deans Summit, Hangzhou | Research and Practice in Design AI | 
- 2024 | Brown University, Providence, RI | The Computability of Design | 
- 2024 | China Europe International Business School (CEIBS), Shanghai | Best Practices in AI and Business Innovation | 
- 2023 | Opening keynote, AIGC Industry Forum, World Artificial Intelligence Conference (WAIC), Shanghai | AI and Industrial Imagination | 
- 2023 | Keynote, Hong Kong Polytechnic University | The Computability of Design and Possibilities of Generative Design | https://www.youtube.com/watch?v=4EzYikrUDUg&list=PL16ugZF7jMZWVtZk6_q1OERR8p4aFNer7
- 2023 | Course, Hundun Academy (in Chinese) | Creativity Has Its Own Moore's Law | https://www.sohu.com/a/719086457_99922069
- 2023 | Video interview, bilibili (in Chinese) | Dialogue with Founder | https://www.bilibili.com/video/BV19c411J7dy/
- 2020 | Video interview, Jiemian (in Chinese) | Never Let a Single Boundary Define You | https://m.jiemian.com/article/866007.html
- 2019 | Panel, Carnegie Mellon University, Pittsburgh, PA | AI and Innovation | 
- 2019 | Keynote, X Design Conference, Harvard Business School and Harvard Graduate School of Design, Boston, MA | Design and AI | 
- 2018 | Speaker, World Economic Forum Annual Meeting, Davos, Switzerland | Digitalization and Consumer Technology | 
- 2018 | Panelist, Gaidar Forum, Moscow, Russia | Enterprise Digitalization and Intelligence | 
- 2017 | Keynote, The Economist Innovation Summit | The Era of Digital and Content Business | 
- 2017 | Panelist, Boao Forum for Asia, Boao, China | Design: More Than Aesthetics | 
- 2017 | Conference of the Institute of Network Society, China Academy of Art, Hangzhou (in Chinese) | Design Creativity and Machine Intelligence | https://caa-ins.org/archives/2367
- 2016 | Keynote, Ant International Forum | The Politics of Human-Machine Interaction | 
- 2015 | TEDx Ningbo, China | Can the Internet Rebuild Trust? | 
- 2015 | Lecture, University of California, Los Angeles, CA | The Formal Logic of Chinese Cities | 
- 2014 | Keynote, Design Matters Conference, San Francisco, CA | Designing Trust | 
- 2014 | Lecture, China GSD Lecture Series, Harvard Graduate School of Design, Cambridge, MA | Future in the Past | 
- 2013 | Lecture, Harvard Graduate School of Design, Cambridge, MA | Possibilities of Contemporary Architectural Practice | 
- 2013 | Lecture, Harvard Graduate School of Design, Cambridge, MA | The Political Formation of Contemporary Chinese Urban Form | 
- 2013 | Lecture, Princeton University School of Architecture, Princeton, NJ | The Political Economy of Design Technology | 
- 2013 | Panel chair, Princeton-Fung Global Forum | The Future of the City | 
- 2012 | Lecture, China GSD Lecture Series, Harvard Graduate School of Design, Cambridge, MA | Architecture for the Multitude | 
- 2012 | Watershed: 21st-Century Water Territories symposium, University of California, Los Angeles, CA | A Case to Provide Clean Water in West China | 
- 2012 | Panel co-chair, Asia Business Conference, Harvard Business School, Boston, MA | Emerging Megacities and Urbanization | 
- 2010 | Soft Energy workshop, Princeton Center for Architecture, Urbanism, and Infrastructure, Shanghai | Soft Design Strategy to Increase Soft Power | 
- 2010 | Emerging Architectural Practices and the City in Asia symposium, Columbia University GSAPP Studio-X | Design for Impact | 
- 2010 | Hard, Soft, Fast, Slow: Mobility in 21st-Century Cities symposium, Princeton University School of Architecture, Princeton, NJ | Design for Impact | 
- 2010 | Research in Flux symposium, CAFA Art Museum and Columbia University, Beijing | Fat Flat Float: Three Social Tactics | 
- 2010 | Winter School Lecture Series, Architectural Association School of Architecture, Beijing | Being Beijing | 
- 2008 | Keynote, Business of Design Week (BODW), Hong Kong | Opportunities in Mixed Reality | 

# Publications

Copied from Ling's CV (October 2026), in the CV's categories and order. Books are under Writing.

## Journal Articles (year | authors | title | where published | DOI or link)
- 2026 | Xia, L., Li, X., Wang, Z., Chen, H., Zhu, X., & Fan, L. | DMSAA-SLAM: RGB-D SLAM for dynamic scenes via diffusion self-attention. | Pattern Recognition, 179(Part A), 113576. | https://doi.org/10.1016/j.patcog.2026.113576
- 2022 | Fan, L., Li, D., Zhuo, J., Yan, S., & Gong, S. | AI empowering the inheritance of traditional craft art: A case study of Jinshan farmer paintings. | Decoration, (7), 94–98. [In Chinese] | https://doi.org/10.3969/j.issn.0412-3662.2022.07.014
- 2019 | Yu, T., Guo, J., Li, W., Wang, H. J., & Fan, L. | Recommendation with diversity: An adaptive trust-aware model. | Decision Support Systems, 123, 113073. | https://doi.org/10.1016/j.dss.2019.113073
- 2010 | Fan, L., Brazier, C., & Lam, T. | Becoming Beijing: Developer-architect dynamics in socio-political context. | Architecture and Urbanism (A+U), (7), 94–99. | —
- 2007 | Fan, L., & O’Donnell, C. | Interview with Peter Eisenman. | Time + Architecture, 2007(6), 112–117. | —
- 2007 | Eisenman, P. | Aspects of modernism: Maison Dom-ino and the self-referential sign (L. | Fan, Trans.). Time + Architecture, 2007(6), 106–111. | —

## Refereed Conference Papers (year | authors | title | where published | DOI or link)
- 2026 | Xia, L., Li, X., Fan, J., Li, D., & Fan, L. | The Wetland Quest: Fostering empathy and literacy for urban herpetofauna through VR wetland exploration. | In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI ’26), Article 1559, 1–15. ACM. | https://doi.org/10.1145/3772318.3790443
- 2026 | Pei, Y., & Fan, L. | Evaluating creative efficacy in human-AI design convergence: An experimental study of support modes. | In DRS2026: Edinburgh. Design Research Society. | https://doi.org/10.21606/drs.2026.1125
- 2026 | Xia, L., Li, X., Li, D., & Fan, L. | Design for dignified longevity: Olfactory-enhanced VR meditation for sustained mindfulness practice. | In DRS2026: Edinburgh. Design Research Society. | https://doi.org/10.21606/drs.2026.672
- 2026 | Xia, L., Li, X., Li, D., Zhang, S., Fan, J., & Fan, L. | VLA-Ethos: Designing ethical vision-language-action models for inclusive education. | In Learning and Collaboration Technologies: HCII 2026 (LNCS 16731, pp. 514–529). Springer. | https://doi.org/10.1007/978-3-032-30542-8_32
- 2025 | Xia, L., Li, X., Fan, J., & Fan, L. | Designing AR-based warehouse management systems using the PECI framework: A comparative user study of interface performance and experience. | In IASDR 2025: Design Next. Design Research Society. | https://doi.org/10.21606/iasdr.2025.818
- 2025 | Li, X., He, Z., Xi, L., Zeng, S., Zhang, D., & Fan, L. | Generative AI meets creative design: Shaping a dynamic learning ecosystem. | In IASDR 2025: Design Next. Design Research Society. | https://doi.org/10.21606/iasdr.2025.520
- 2025 | Li, D., Xia, L., & Fan, L. | Aug-Creativity: Framework for human-centered creativity with vision language models. | In Human-Computer Interaction: HCII 2025 (LNCS 15770, pp. 86–101). Springer. | https://doi.org/10.1007/978-3-031-93864-1_7
- 2025 | Xia, L., Hu, Y., Li, X., Li, D., Zeng, S., & Fan, L. | Enhancing altruistic behavior through virtual reality: The impact of immersive environments and digital embodiment on prosocial tendencies. | In Virtual, Augmented and Mixed Reality: HCII 2025 (LNCS 15789, pp. 245–259). Springer. | https://doi.org/10.1007/978-3-031-93712-5_15
- 2024 | Xia, L., Li, X., Qin, Y., Li, D., & Fan, L. | Enhancing design education through spatial computing: A comparative study of traditional and immersive technologies in chair design projects. | In 2024 IEEE Frontiers in Education Conference (FIE), 1–8. IEEE. | https://doi.org/10.1109/FIE61694.2024.10893086
- 2024 | Li, X., Xia, L., He, Z., Wu, P., Chen, D., & Fan, L. | Enhancing interior design education through the integration of AIGC tools: A novel “Creator-Thon” approach. | In 2024 IEEE Frontiers in Education Conference (FIE), 1–8. IEEE. | https://doi.org/10.1109/FIE61694.2024.10893341
- 2024 | He, Z., Zou, X., Wu, P., Fan, L., & Li, X. | Creating and experiencing 3D immersion using generative 2D diffusion: An integrated framework. | In 2024 IEEE International Conference on Multimedia and Expo Workshops (ICMEW), 1–6. IEEE. | https://doi.org/10.1109/ICMEW63481.2024.10645466
- 2021 | Zheng, C., Zhang, K., Wang, H. J., Fan, L., & Wang, Z. | Enhanced Seq2Seq autoencoder via contrastive learning for abstractive text summarization. | In 2021 IEEE International Conference on Big Data (Big Data), 1764–1771. IEEE. | https://doi.org/10.1109/BigData52589.2021.9671819
- 2021 | Li, Y., Zhuo, J., Fan, L., Wang, Z., & Wang, H. J. | Semantically enriched music visualization via multimodal color generation. | In Proceedings of the International Conference on New Interfaces for Musical Expression (NIME 2021). | https://doi.org/10.21428/92fbeb44.2fb614f7
- 2021 | Fan, L., Bao, Y., Gong, S., Yan, S., & Wang, H. J. | The brain-machine-ratio model for designer and AI collaboration. | In 2021 IEEE 4th International Conference on Multimedia Information Processing and Retrieval (MIPR), 308–313. IEEE. | https://doi.org/10.1109/MIPR51284.2021.00058
- 2021 | Li, Y., Zhuo, J., Fan, L., & Wang, H. J. | Culture-inspired multi-modal color palette generation and colorization: A Chinese youth subculture case. | In 2021 IEEE 4th International Conference on Multimedia Information Processing and Retrieval (MIPR), 382–385. IEEE. | https://doi.org/10.1109/MIPR51284.2021.00071

## Extended Abstracts and Posters (year | authors | title | where published | DOI or link)
- 2025 | Xia, L., Li, X., Zeng, S., Chen, D., & Fan, L. | Navigating stakeholder tensions in spatial computing: A participatory design approach for inclusive mixed reality environments. | In Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA ’25), Article 415, 1–6. ACM. | https://doi.org/10.1145/3706599.3720268
- 2025 | Li, X., Wu, P., He, Z., Li, J., & Fan, L. | Multi-agent AI: Collaborative design with multiple AI tools in interior design workflow. | In HCI International 2024 – Late Breaking Posters (CCIS 2320, pp. 202–211). Springer. | https://doi.org/10.1007/978-3-031-78531-3_23
- 2025 | Li, X., He, Z., Wu, P., Li, J., & Fan, L. | A computational aesthetic measurement framework for AI design: A case study of office space design. | In HCI International 2024 – Late Breaking Posters (CCIS 2320, pp. 212–220). Springer. | https://doi.org/10.1007/978-3-031-78531-3_24
- 2025 | Wu, P., Li, X., He, Z., & Fan, L. | AdvisorAI: Transforming graphic advertising with generative AI-enhanced design strategies. | In HCI International 2024 – Late Breaking Posters (CCIS 2320, pp. 295–304). Springer. | https://doi.org/10.1007/978-3-031-78531-3_32
- 2024 | He, Z., Li, X., Wu, P., Fan, L., Wang, H. J., Wang, N., Li, M., & Chen, Y. | Generating architectural floor plans through conditional large diffusion model. | In HCI International 2024 Posters (CCIS 2120, pp. 53–63). Springer. | https://doi.org/10.1007/978-3-031-62110-9_6
- 2023 | Fan, L., Wang, H. J., Zhang, K., Pei, Z., & Li, A. | Towards an automatic prompt optimization framework for AI image generation. | In HCI International 2023 Posters (CCIS 1836, pp. 405–410). Springer. | https://doi.org/10.1007/978-3-031-36004-6_55
- 2023 | He, Z., Li, X., Fan, L., & Wang, H. J. | Revamping interior design workflow through generative artificial intelligence. | In HCI International 2023 Posters (CCIS 1835, pp. 607–613). Springer. | https://doi.org/10.1007/978-3-031-36001-5_78

## Preprints (year | authors | title | where published | DOI or link)
- 2020 | Zheng, C., Zhang, K., Wang, H. J., & Fan, L. | A two-phase approach for abstractive podcast summarization. | — | https://arxiv.org/abs/2011.08291
- 2020 | Zhuo, J., Fan, L., & Wang, H. J. | A framework and dataset for abstract art generation via CalligraphyGAN. | — | https://arxiv.org/abs/2012.00744
- 2020 | Zheng, C., Wang, H. J., Zhang, K., & Fan, L. | A baseline analysis for podcast abstractive summarization. | — | https://arxiv.org/abs/2008.10648

## Book Chapters, Professional Articles, and Reports (year | authors | title | where published | DOI or link)
- 2019 | Fan, L. | Cross-disciplinary integration of art and design with artificial intelligence. | People’s Daily. | —
- 2017–2019 | Tongji Design AI Lab & Tezign. | Design and A.I. Report, annual editions 2017, 2018, 2019. | — | —
- 2015 | Fan, L. | The “contemporary” as a case. | In J. Shi (Ed.), New observations: Essays in architectural criticism. Tongji University Press. | —
- 2013 | Fan, L. | Spatialization of the collective: The logic and dialectics of urban forms in China. | In C. C. M. Lee (Ed.), Xiamen: The megaplot (Common Frameworks: Rethinking the Developmental City in China, Pt. 1, pp. 45–60). Harvard University Graduate School of Design. | —

# Patents

## Patents (title | number)
- Sub-Task Invocation System | ZL 202210689841.2
- Aesthetic Feature-Based Poster CTR Prediction | ZL 202110100658.X
- Adaptive Creative Generation Based on Structured Theory | ZL 201911304845.9
- Method and System for Generating Creative Assets | ZL 201910344677.X

# Appointments

## Appointments (years | institution | role; from Ling's CV, October 2026)
- 2016–present | Tongji University, College of Design and Innovation, Shanghai | Professor in Design AI
- 2017–present | Tongji University, Design Artificial Intelligence Lab | Founding Director
- 2025–present | Shanghai Research Institute for Intelligent Autonomous Systems | Professor
- 2013–2015 | University of California, Berkeley | Lecturer
- 2008 | Oslo School of Architecture and Design | Visiting Lecturer
- 2007–2011 | Central Academy of Fine Arts, Beijing | Lecturer
- 2007–2010 | Princeton Center for Architecture, Urbanism, and Infrastructure | Research Fellow

# Education

## Degrees (year | school | degree)
- 2014 | Harvard University, Graduate School of Design | Doctor of Design (DDes)
- 2007 | Princeton University | Master of Architecture (MArch)
- 2005 | Tongji University | Bachelor of Architecture (BArch)

# Honors

## Honors (year | organization | honor; from Ling's CV, October 2026)
- 2025 | VOGUE Business | New Tech Pioneer
- 2024 | Forbes | Disruptive Founders
- 2023 | Harvard Business Review | New Growth Pioneer
- 2020 | IDEAT | Future Award
- 2019 | Fortune | 40 Under 40
- 2018 | Fast Company | China's 100 Most Creative People in Business
- 2018 | Guanghua Longteng Award | Top 10 Outstanding Young Designers of China
- 2017 | World Economic Forum | Young Global Leader
- 2016 | Aspen Institute | China Fellowship
- 2016 | World Economic Forum | Cultural Leader
- 2015 | Design Trust / M+, Hong Kong | Design Fellowship (inaugural)
- 2015 | Shanghai | Pujiang Talent Program
- 2013 | Ministry of Foreign Affairs and Economic Affairs, Netherlands | Future Leaders Program
- 2011–2014 | China Scholarship Council | National Scholarship
- 2011 | Martell Art Foundation | Focus on Future Art Talents Program (inaugural cohort)

# Service

## Service (years | organization | role; from Ling's CV, October 2026)
- 2026– | Business of Design Week (BODW), Hong Kong Design Centre | Member, Steering Committee
- 2026 | World Design Cities Conference (WDCC) | Co-Chief Curator
- 2024– | China Europe International Business School (CEIBS) | Chairman, AI and Business Initiative
- 2024– | China Social Entrepreneur Foundation | Trustee
- 2024 | Design Intelligence Award (DIA), Hangzhou | Nominating Juror
- 2024 | Global Design Award, Shenzhen | Juror
- 2022– | National Industrial Design Center, China | Chief Expert
- 2020– | Future Science Forum | Trustee of Youth Council
- 2019– | IEEE Council for Extended Intelligence | Member
- 2018– | Yunqi Academy of Engineering | Trustee
- 2016– | Aspen Global Leadership Network | Member

# Media

## Media
- Harvard Business Review (2026)
- People's Daily (2025)
- Tatler (2024)
- Bloomberg (2021): “Harvard-Trained Designer Creates China Business Software Unicorn”
- Forbes (2020)
