# arXiv corpus — LLM-based code-quality assessment (2024–2026)

165 papers. Generated 2026-06-27.

### Same Scrutiny, More Time: Eye Tracking Insights into Reviewing LLM-Labelled Code
- **2606.26505** · 2026-06-25 · cs.SE
- Ranim Khojah, Francisco Gomes de Oliveira Neto, Mazen Mohamad et al.
- [`pdfs/2606.26505_same-scrutiny-more-time-eye-tracking-insights-into-reviewing-llm-label.pdf`](pdfs/2606.26505_same-scrutiny-more-time-eye-tracking-insights-into-reviewing-llm-label.pdf) · [abs](https://arxiv.org/abs/2606.26505)

Modern software development increasingly involves the use of large language models (LLMs) to generate code. Despite their rapid advancement, LLMs remain prone to errors and hallucinations, emphasizing the importance of careful code inspection. However, in practice, developers' trust in LLM-generated code and their willingness to review it thoroughly may differ from these recommendations. How developers actually behave when reviewing LLM-generated code remains largely unexplored. In this study, w…

### OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning
- **2606.25757** · 2026-06-24 · cs.CL
- Wenxuan Jiang, Zining Fan, Zijian Zhang et al.
- [`pdfs/2606.25757_opera-aligning-open-ended-reasoning-via-objective-perplexity-based-rei.pdf`](pdfs/2606.25757_opera-aligning-open-ended-reasoning-via-objective-perplexity-based-rei.pdf) · [abs](https://arxiv.org/abs/2606.25757)

Reinforcement Learning (RL) has enabled LLMs to excel in objective reasoning tasks such as mathematics and code generation. However, applying RL to open-ended tasks, such as creative writing, remains challenging because LLM-as-a-judge reward models often exhibit stylistic biases and positional inconsistencies, leading to unstable supervision. To address this, we propose OPERA (Objective Perplexity-based Reflective Alignment), which replaces unreliable external judges with intrinsic rewards deriv…

### Helpful or Harmful? Evaluating LLM-Assisted Vulnerability Patching via a Human Study
- **2606.25973** · 2026-06-24 · cs.SE
- Giulian Biolo, Michael Tezza, Yuanjun Gong et al.
- [`pdfs/2606.25973_helpful-or-harmful-evaluating-llm-assisted-vulnerability-patching-via.pdf`](pdfs/2606.25973_helpful-or-harmful-evaluating-llm-assisted-vulnerability-patching-via.pdf) · [abs](https://arxiv.org/abs/2606.25973)

Software vulnerability remediation is a cognitively demanding task that requires specialized security expertise often lacking in general developers. In the meantime, Large Language Models (LLMs) assisted tools show potential in vulnerability detection, location, and repair tasks. [Hypothesis:] While LLM-assistance is hypothesized to accelerate patching, it also risks introducing hallucinations or insecure code, leading to a higher likelihood of generating superficial repairs that bypass the stan…

### Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning
- **2606.25356** · 2026-06-24 · cs.CR
- Andrew Stoltman, Johnathan Tang, Haipeng Cai
- [`pdfs/2606.25356_representation-matters-an-empirical-study-of-program-representations-f.pdf`](pdfs/2606.25356_representation-matters-an-empirical-study-of-program-representations-f.pdf) · [abs](https://arxiv.org/abs/2606.25356)

Large Language Models (LLMs) are increasingly used for automated vulnerability detection, but it remains unclear how program structure and semantics should be represented for LLM-based reasoning. Most prompting-based approaches provide raw source code, implicitly assuming that more source-level context gives the model better evidence. This paper challenges that assumption through RepBench, an empirical benchmark comparing raw source code with static-analysis-based program representations. RepBen…

### Detecting and Controlling Sycophancy with Cascading Linear Features
- **2606.26155** · 2026-06-23 · cs.AI
- Maty Bohacek, Rishub Jain, Nicholas Dufour et al.
- [`pdfs/2606.26155_detecting-and-controlling-sycophancy-with-cascading-linear-features.pdf`](pdfs/2606.26155_detecting-and-controlling-sycophancy-with-cascading-linear-features.pdf) · [abs](https://arxiv.org/abs/2606.26155)

Interpreting and controlling model behaviors through activation steering methods requires many pairs of contrastive samples that clearly exhibit desired or undesired behavior. These data pairs determine the degree to which interpretability frameworks can reliably detect model features responsible for a behavior, and therefore the ability to steer models toward or away from such behavior. In this work, we present an iterative data generation pipeline that isolates cascading linear features respon…

### Understanding the (In)Security of Vibe-Coded Applications
- **2606.23130** · 2026-06-22 · cs.CR
- Junquan Deng, Zhiyu Fan, Ruijie Meng
- [`pdfs/2606.23130_understanding-the-in-security-of-vibe-coded-applications.pdf`](pdfs/2606.23130_understanding-the-in-security-of-vibe-coded-applications.pdf) · [abs](https://arxiv.org/abs/2606.23130)

Recent advances in large language models (LLMs) have enabled vibe coding, an emerging software development paradigm in which users create applications primarily through natural-language interactions with AI agents. Due to its low barrier to entry, vibe coding is rapidly gaining adoption in practice. Unlike conventional AI-assisted programming, where developers remain responsible for implementation and code review, vibe coding delegates a substantial portion of development to AI systems. This shi…

### CFPO: Counterfactual Policy Optimization for Multimodal Reasoning
- **2606.23206** · 2026-06-22 · cs.CV
- Zhangyuan Yu, Wanran Sun, Guangjing Yang et al.
- [`pdfs/2606.23206_cfpo-counterfactual-policy-optimization-for-multimodal-reasoning.pdf`](pdfs/2606.23206_cfpo-counterfactual-policy-optimization-for-multimodal-reasoning.pdf) · [abs](https://arxiv.org/abs/2606.23206)

Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities in multimodal reasoning. However, prevailing reinforcement learning (RL) paradigms lack explicit counterfactual enhancement and causal learning mechanisms. This fundamental deficiency results in severe grounding failures, manifesting as a tendency to ignore visual evidence in favor of language priors or exhibiting hallucination drift during long chain-of-thought reasoning. To address this root cause, we propose Counte…

### BabelJudge: Measuring LLM-as-a-Judge Reliability Across Languages and Agent Trajectories
- **2606.22329** · 2026-06-21 · cs.CL
- Shreyas KC
- [`pdfs/2606.22329_babeljudge-measuring-llm-as-a-judge-reliability-across-languages-and-a.pdf`](pdfs/2606.22329_babeljudge-measuring-llm-as-a-judge-reliability-across-languages-and-a.pdf) · [abs](https://arxiv.org/abs/2606.22329)

LLM-as-a-judge has become the dominant approach to scalable evaluation in NLP pipelines, yet judges themselves carry systematic biases that raw accuracy hides: they favor responses placed in slot A (position bias), they prefer longer responses regardless of quality (verbosity bias), and their reliability degrades sharply in lower-resource languages. We introduce BabelJudge, an open-source benchmark and reliability audit framework that measures all four failure modes -- position bias, verbosity b…

### BLUEX v2: Benchmarking LLMs on Open-Ended Questions from Brazilian University Entrance Exams
- **2606.22723** · 2026-06-21 · cs.CL
- João Guilherme Alves Santos, Giovana Kerche Bonás, Thiago Laitz et al.
- [`pdfs/2606.22723_bluex-v2-benchmarking-llms-on-open-ended-questions-from-brazilian-univ.pdf`](pdfs/2606.22723_bluex-v2-benchmarking-llms-on-open-ended-questions-from-brazilian-univ.pdf) · [abs](https://arxiv.org/abs/2606.22723)

Although Large Language Models (LLMs) excel in many tasks, their assessment in Portuguese has received less attention, particularly for open-ended, discursive tasks that demand deeper reasoning and generation capabilities. While the original BLUEX benchmark addressed the scarcity of Portuguese evaluation datasets through multiple-choice questions from Brazilian university entrance exams, it did not cover the more challenging second-phase examinations, which require free-form written responses. I…

### Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases
- **2606.22263** · 2026-06-20 · cs.CR
- Yiwei Hou, Hao Wang, Muxi Lyu et al.
- [`pdfs/2606.22263_revelio-cost-efficient-agentic-memory-safety-vulnerability-detection-f.pdf`](pdfs/2606.22263_revelio-cost-efficient-agentic-memory-safety-vulnerability-detection-f.pdf) · [abs](https://arxiv.org/abs/2606.22263)

Memory safety vulnerabilities remain a significant threat even for projects with extensive fuzzing and manual auditing. Recent results suggest that large language models hold great promise for detecting such vulnerabilities, but they are unreliable, at risk of hallucination, and challenging to scale to repository-size codebases. This paper presents Revelio, a cost-efficient end-to-end agentic framework for memory-safety vulnerability discovery. Revelio addresses the problem of hallucination by g…

### GitReq: A Gold Standard Dataset for Software Quality Requirements
- **2606.21810** · 2026-06-20 · cs.SE
- Farha Kamal, Md Humaun Kabir, Md Rakibul Islam
- [`pdfs/2606.21810_gitreq-a-gold-standard-dataset-for-software-quality-requirements.pdf`](pdfs/2606.21810_gitreq-a-gold-standard-dataset-for-software-quality-requirements.pdf) · [abs](https://arxiv.org/abs/2606.21810)

GitHub issue trackers contain millions of developer-written quality concerns, including performance bottlenecks and security vulnerabilities, yet no publicly available GitHub dataset classifies these into fine-grained software quality categories. We construct and release GitReq GitHub Requirement Issue, comprising 6,302 expert-validated requirements mined from 55,588 raw GitHub candidates across 4,080 repositories, labeled across eight ISO/IEC 25010:2011-aligned categories: Performance, Security…

### Evaluating LLMs for Real-World Web Vulnerability Detection
- **2606.21397** · 2026-06-19 · cs.CR
- Sebastian Neef, Luca Jungnickel, Antonio Benjamin Buchholz et al.
- [`pdfs/2606.21397_evaluating-llms-for-real-world-web-vulnerability-detection.pdf`](pdfs/2606.21397_evaluating-llms-for-real-world-web-vulnerability-detection.pdf) · [abs](https://arxiv.org/abs/2606.21397)

Large Language Models (LLMs) have emerged as a promising tool for automated vulnerability detection, yet their effectiveness on web-specific vulnerabilities remains to be explored. This work benchmarks six frontier (Claude Opus 4.6, Codex GPT-5.4, Gemini 3.1-pro-preview) and open-weight models (Qwen 3.5, Qwen 3 Coder Next, MiniMax M2.5) on their ability to detect real-world web vulnerabilities using static analysis in WordPress plugins, including SQL injection, stored cross-site scripting, path …

### Assessing Language Models for Salient Class Identification
- **2606.21629** · 2026-06-19 · cs.SE
- Bo Xiong, Chaoran Cai, Kaipeng Xiong et al.
- [`pdfs/2606.21629_assessing-language-models-for-salient-class-identification.pdf`](pdfs/2606.21629_assessing-language-models-for-salient-class-identification.pdf) · [abs](https://arxiv.org/abs/2606.21629)

Code review requires reviewers to understand the core intent of code changes, which becomes difficult when a commit modifies multiple classes. In such commits, one or more primarily modified classes, referred to as salient classes, may induce modifications in other classes. Accurate identification of salient classes offers reviewers an effective entry point to navigate code changes and facilitates program comprehension. Existing state-of-the-art approaches rely on complex program-analysis proced…

### Counsel: A Meta-Evaluation Dataset for Agentic Tasks
- **2606.21627** · 2026-06-19 · cs.AI
- Sashank Pisupati, Henry Broomfield, Eujeong Choi et al.
- [`pdfs/2606.21627_counsel-a-meta-evaluation-dataset-for-agentic-tasks.pdf`](pdfs/2606.21627_counsel-a-meta-evaluation-dataset-for-agentic-tasks.pdf) · [abs](https://arxiv.org/abs/2606.21627)

As agentic systems tackle increasingly complex multi-step tasks, evaluating their trajectories presents a major bottleneck - human annotation of a single trajectory on popular agentic benchmarks can take hours, making it difficult to scale evaluations for measuring performance or curating training data. This has driven widespread reliance on automated approaches such as LLM-as-a-judge (LLMJ) to critique agents at the process and outcome-levels at scale, however, the soundness of LLMJ critiques o…

### Towards LLM-Powered Automation of a Dark Matter Constraint Repository
- **2606.21658** · 2026-06-19 · hep-ex
- Lanqing Yuan, Karthik Ramanathan
- [`pdfs/2606.21658_towards-llm-powered-automation-of-a-dark-matter-constraint-repository.pdf`](pdfs/2606.21658_towards-llm-powered-automation-of-a-dark-matter-constraint-repository.pdf) · [abs](https://arxiv.org/abs/2606.21658)

Dark matter constraint repositories are critical community infrastructure, giving experimentalists and theorists a shared landscape of existing bounds. Yet the most widely-used repositories are maintained by individual volunteers, creating a sustainability risk as the pace of new results accelerates. We present a large language model (LLM) pipeline that monitors arXiv, extracts limit curves from papers, integrates them as code, and opens pull requests (PRs) for human review. On a 346-paper bench…

### CoRaCommit: A VS Code Extension for Commit Message Generation with Exemplar Retrieval
- **2606.19814** · 2026-06-18 · cs.SE
- Chaoran Cai, Bo Xiong, Chong Wang et al.
- [`pdfs/2606.19814_coracommit-a-vs-code-extension-for-commit-message-generation-with-exem.pdf`](pdfs/2606.19814_coracommit-a-vs-code-extension-for-commit-message-generation-with-exem.pdf) · [abs](https://arxiv.org/abs/2606.19814)

Commit messages are essential textual artifacts that describe the intent behind code changes, and play a critical role in version control, code review, and historical tracking. However, in practice, commit messages are primarily authored manually, which is time-consuming and often results in inconsistent quality and non-uniform expression. Existing VS Code extensions for commit message generation typically directly invoke large language models based on the code diff, without leveraging similar c…

### PromptMark: A Prompt-Guided Iterative-Feedback Framework for Source Code Watermarking
- **2606.20835** · 2026-06-18 · cs.CR
- Istiaq Ahmed Fahad, Mridha Md. Nafis Fuad, Kazi Sakib
- [`pdfs/2606.20835_promptmark-a-prompt-guided-iterative-feedback-framework-for-source-cod.pdf`](pdfs/2606.20835_promptmark-a-prompt-guided-iterative-feedback-framework-for-source-cod.pdf) · [abs](https://arxiv.org/abs/2606.20835)

Watermarking has become a crucial technique for ensuring provenance and accountability in AI-generated source code. As large language models (LLMs) are increasingly integrated into development workflows, reliable attribution remains challenging. In practice, most developers rely on commercial LLM APIs operating under black-box constraints, making existing approaches that require access to the decoding process less feasible for real-world integration. To address this limitation, we propose Prompt…

### Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages
- **2606.20517** · 2026-06-18 · cs.AI
- Maria Ivanova, Pavel Zadorozhny, Rodion Levichev et al.
- [`pdfs/2606.20517_multi-lcb-extending-livecodebench-to-multiple-programming-languages.pdf`](pdfs/2606.20517_multi-lcb-extending-livecodebench-to-multiple-programming-languages.pdf) · [abs](https://arxiv.org/abs/2606.20517)

LiveCodeBench (LCB) has recently become a widely adopted benchmark for evaluating large language models (LLMs) on code-generation tasks. By curating competitive programming problems, constantly adding fresh problems to the set, and filtering them by release dates, LCB provides contamination-aware evaluation and offers a holistic view of coding capability. However, LCB remains restricted to Python, leaving open the question of whether LLMs can generalize across the diverse programming languages r…

### Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
- **2606.20482** · 2026-06-18 · cs.CL
- Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari et al.
- [`pdfs/2606.20482_your-mouse-and-eyes-secretly-leak-your-preference-llm-alignment-using.pdf`](pdfs/2606.20482_your-mouse-and-eyes-secretly-leak-your-preference-llm-alignment-using.pdf) · [abs](https://arxiv.org/abs/2606.20482)

To align a Large Language Model (LLM), most existing methods collect explicit human feedback and train a reward model to predict the human preference based on the response text. These existing methods have two key limitations. First, the users rarely provide explicit feedback for LLM responses, which makes the high-quality preference annotation expensive to collect. Second, the methods do not leverage implicit human feedback, which has proven vital to the economic moats of Internet giants. To qu…

### Steerable Cultural Preference Optimization of Reward Models
- **2606.18606** · 2026-06-17 · cs.CL
- Minsik Oh, Advit Deepak, Sophie Wu et al.
- [`pdfs/2606.18606_steerable-cultural-preference-optimization-of-reward-models.pdf`](pdfs/2606.18606_steerable-cultural-preference-optimization-of-reward-models.pdf) · [abs](https://arxiv.org/abs/2606.18606)

It is essential for large language model (LLM) technology to serve many different cultural sub-communities in a manner that is acceptable to each community. However, research on LLM alignment has so far predominantly focused on predicting a unified response preference of annotators from certain regions. This paper aims to advance the development of alignment models with a more global outlook, that are able to accurately represent the preferences of subcommunities and do not exhibit excessive bia…

### PracRepair: LLM-Empowered Automated Program Repair Inspired by Human-Like Debugging Practices
- **2606.17612** · 2026-06-16 · cs.SE
- Yu Cheng, Zhongxin Liu, Zhenchang Xing et al.
- [`pdfs/2606.17612_pracrepair-llm-empowered-automated-program-repair-inspired-by-human-li.pdf`](pdfs/2606.17612_pracrepair-llm-empowered-automated-program-repair-inspired-by-human-li.pdf) · [abs](https://arxiv.org/abs/2606.17612)

As software systems grow in scale and complexity, debugging and repair remain costly and time-consuming. Large language models (LLMs) have advanced automated program repair (APR), but existing LLM-based APR approaches still largely rely on static or retrieved context, error messages, and coarse-grained validation outcomes. As a result, they underutilize dynamic information for failure understanding and repair, including failure-execution dynamics and patch-validation dynamics. Effectively levera…

### Unlocking LLM Code Correction with Iterative Feedback Loops
- **2606.17514** · 2026-06-16 · cs.SE
- Le Zhang, Suresh Kothari
- [`pdfs/2606.17514_unlocking-llm-code-correction-with-iterative-feedback-loops.pdf`](pdfs/2606.17514_unlocking-llm-code-correction-with-iterative-feedback-loops.pdf) · [abs](https://arxiv.org/abs/2606.17514)

Large Language Models have shown remarkable capabilities in code generation. However, most existing evaluations focus only on single-attempt accuracy and overlook the iterative refinement process that is central to real-world programming. This study presents a systematic investigation of LLMs' ability to rectify their own code through execution feedback. Using real-world programming problems across four models and two major programming languages, this study evaluates performance using iterative …

### The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning
- **2606.16152** · 2026-06-15 · cs.AI
- Haolong Qian, Xianliang Yang, Yinuo ma et al.
- [`pdfs/2606.16152_the-quality-utility-paradox-why-high-reward-data-impairs-small-model-m.pdf`](pdfs/2606.16152_the-quality-utility-paradox-why-high-reward-data-impairs-small-model-m.pdf) · [abs](https://arxiv.org/abs/2606.16152)

Knowledge distillation from powerful reasoning models is widely used to improve Small Language Models (SLMs) on mathematical reasoning, often assuming that traces with higher reward model scores provide more useful supervision. We identify a counterintuitive \textbf{Quality-Utility Paradox} in mathematical reasoning distillation. Data refined or synthesized by a stronger Oracle obtains higher perceived quality according to reward models, yet consistently underperforms traces generated by the SLM…

### Mask-Proof: An LLM-based Automated Data Curation Pipeline on Mathematical Proofs
- **2606.15258** · 2026-06-13 · cs.AI
- Jierui Zhang, Siyuan Tan, Xinhang Li et al.
- [`pdfs/2606.15258_mask-proof-an-llm-based-automated-data-curation-pipeline-on-mathematic.pdf`](pdfs/2606.15258_mask-proof-an-llm-based-automated-data-curation-pipeline-on-mathematic.pdf) · [abs](https://arxiv.org/abs/2606.15258)

Large language models (LLMs) are increasingly capable of mathematical problem solving and can even assist with research-level proofs, yet we still lack a scalable and reproducible way to measure step-level reasoning in long proofs across diverse sources. This evaluation gap limits trustworthy AI assistance in proof-certified scientific progress. Existing evaluations often emphasize final answers or rely on costly expert grading, while end-to-end proof generation remains open-ended and hard to ve…

### Code Correctness Signals in LLM Hidden States: Pre-Generation Probing and Repair Geometry
- **2606.14530** · 2026-06-12 · cs.LG
- Carlo Di Cicco
- [`pdfs/2606.14530_code-correctness-signals-in-llm-hidden-states-pre-generation-probing-a.pdf`](pdfs/2606.14530_code-correctness-signals-in-llm-hidden-states-pre-generation-probing-a.pdf) · [abs](https://arxiv.org/abs/2606.14530)

Large language models encode rich information in their hidden states. This work asks whether code correctness is legible in the hidden states of Qwen3-4B-Instruct-2507, before it generates and as it repairs a failed attempt, studied on 444 LiveCodeBench tasks. It reports two findings connected by a single confound-control tool: residualization. First, the correctness of the model's first-attempt code is linearly decodable from the prompt-final hidden state, with a leakage-free held-out AUC of 0.…

### tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration
- **2606.14445** · 2026-06-12 · cs.SE
- Minseo Kim
- [`pdfs/2606.14445_tap-a-file-based-protocol-for-heterogeneous-llm-agent-collaboration.pdf`](pdfs/2606.14445_tap-a-file-based-protocol-for-heterogeneous-llm-agent-collaboration.pdf) · [abs](https://arxiv.org/abs/2606.14445)

Existing multi-agent software development systems have proposed many forms of agent collaboration, including role-based collaboration and automated code review. However, many systems assume a common runtime, a central conversation server, or the same API family. Under these assumptions, LLM agents from different vendors cannot easily exchange messages directly from their own execution environments while dividing development and review work on a shared codebase. This paper presents tap, a file-ba…

### GitHub Template Repositories: Served Domains, Maintenance, and Practitioner Guidelines
- **2606.14616** · 2026-06-12 · cs.SE
- Leuson Da Silva, Altaf Allah Abbassi, Imen Trabelsi et al.
- [`pdfs/2606.14616_github-template-repositories-served-domains-maintenance-and-practition.pdf`](pdfs/2606.14616_github-template-repositories-served-domains-maintenance-and-practition.pdf) · [abs](https://arxiv.org/abs/2606.14616)

Over time, GitHub has introduced different strategies for sharing reusable code artifacts. In addition to fork-based reuse, template repositories provide a distinct feature for generating new projects from scaffolding. Although this feature has been available since 2019, little is known about the domains it supports, its maintenance characteristics, or the practices that guide practitioners for effective template design. To address this gap, we conduct a large-scale empirical study of GitHub tem…

### Evaluating LLMs for Obfuscation Detection and Classification in Android Apps
- **2606.14233** · 2026-06-12 · cs.SE
- Luca Ferrari, Marco Alecci, Jordan Samhi et al.
- [`pdfs/2606.14233_evaluating-llms-for-obfuscation-detection-and-classification-in-androi.pdf`](pdfs/2606.14233_evaluating-llms-for-obfuscation-detection-and-classification-in-androi.pdf) · [abs](https://arxiv.org/abs/2606.14233)

Android applications (apps) developers increasingly rely on code obfuscation techniques to hinder reverse engineering and protect intellectual property. However, obfuscation also reduces the effectiveness of static analysis and vulnerability detection tools, creating challenges for Android security analysis. Existing approaches for detecting obfuscation in Android apps predominantly rely on handcrafted heuristics, engineered features, or task-specific learning pipelines, which may struggle to ge…

### FactoryLLM: A Safe and Open-Source AI Playground for Evaluating LLMs in Smart Factories
- **2606.14119** · 2026-06-12 · cs.AI
- Yash Pulse, Yong-Bin Kang, Abhik Banerjee et al.
- [`pdfs/2606.14119_factoryllm-a-safe-and-open-source-ai-playground-for-evaluating-llms-in.pdf`](pdfs/2606.14119_factoryllm-a-safe-and-open-source-ai-playground-for-evaluating-llms-in.pdf) · [abs](https://arxiv.org/abs/2606.14119)

Fault diagnostics and recovery in smart factories is challenging because critical information is dispersed across manuals of multiple machines which are interconnected through the manufacturing process. Large Language Models (LLMs) can provide a promising approach. In this paper, we propose FactoryLLM, a safe and open-source AI playground designed for evaluating different LLM-based retrieval-augmented generation (RAG) models by analysing documents from multiple machines across the manufacturing …

### Persona-Pruner: Sculpting Lightweight Models for Role-Playing
- **2606.14695** · 2026-06-12 · cs.LG
- Jinsu Kim, Jihoon Tack, Noah Lee et al.
- [`pdfs/2606.14695_persona-pruner-sculpting-lightweight-models-for-role-playing.pdf`](pdfs/2606.14695_persona-pruner-sculpting-lightweight-models-for-role-playing.pdf) · [abs](https://arxiv.org/abs/2606.14695)

Language Models (LMs) have shown remarkable potential as role-playing chatbots, delivering consistent, stylized interactions when given a specification of a character or user persona. However, applying these capabilities to real-world applications (e.g., ecosystems with numerous NPCs interacting simultaneously) exposes a critical inefficiency due to the excessive computational cost. In this paper, we question the necessity of dedicating a full, generalist model to a single persona, hypothesizing…

### The End of Code Review: Coding Agents Supersede Human Inspection
- **2606.13175** · 2026-06-11 · cs.SE
- Martin Monperrus
- [`pdfs/2606.13175_the-end-of-code-review-coding-agents-supersede-human-inspection.pdf`](pdfs/2606.13175_the-end-of-code-review-coding-agents-supersede-human-inspection.pdf) · [abs](https://arxiv.org/abs/2606.13175)

Code review has been the primary quality gate in software development since Fagan formalised code inspection in 1976. For five decades, having a human examine and comment on a colleague's changes before merge has been a cornerstone practice at organisations of every size. Coding agents are large language model (LLM)-based autonomous systems capable of reading, writing, testing, and repairing software. We argue that coding agents have crossed a threshold of capability at which traditional human c…

### SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents
- **2606.13757** · 2026-06-11 · cs.CR
- Rui Melo, Riccardo Fogliato, Sean Zhou et al.
- [`pdfs/2606.13757_sevra-bench-social-engineering-of-vulnerabilities-in-review-agents.pdf`](pdfs/2606.13757_sevra-bench-social-engineering-of-vulnerabilities-in-review-agents.pdf) · [abs](https://arxiv.org/abs/2606.13757)

Large language model (LLM) reviewers are increasingly used in pull-request (PR) workflows, where their approvals help decide which code is merged into a repository. This raises a question that benchmarks for static vulnerability detection or code generation do not address: can an automated reviewer reject a malicious contribution when the attacker controls both the code change and the accompanying PR text? We introduce SEVRA-BENCH (Social Engineering of Vulnerabilities in Review Agents), a bench…

### Detecting Functional Memorization in Code Language Models
- **2606.12764** · 2026-06-11 · cs.LG
- Matthieu Meeus, Anil Ramakrishna, Matthew Grange et al.
- [`pdfs/2606.12764_detecting-functional-memorization-in-code-language-models.pdf`](pdfs/2606.12764_detecting-functional-memorization-in-code-language-models.pdf) · [abs](https://arxiv.org/abs/2606.12764)

Large language models (LLMs) are increasingly used to generate code at scale. Meanwhile, prior work has investigated whether training data may be recoverable from model outputs, by auditing the textual overlap between training examples and model generations. Code, however, can be functionally equivalent while textually dissimilar. In this work, we study functional memorization: extraction of functional logic beyond what verbatim metrics detect. We construct a counterfactual setup for Olmo-3-32B,…

### Reward Modeling for Multi-Agent Orchestration
- **2606.13598** · 2026-06-11 · cs.AI
- King Yeung Tsang, Zihao Zhao, Vishal Venkataramani et al.
- [`pdfs/2606.13598_reward-modeling-for-multi-agent-orchestration.pdf`](pdfs/2606.13598_reward-modeling-for-multi-agent-orchestration.pdf) · [abs](https://arxiv.org/abs/2606.13598)

Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model trai…

### From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation
- **2606.13221** · 2026-06-11 · cs.LG
- Bora Kargi, David Salinas
- [`pdfs/2606.13221_from-uncertain-judgments-to-calibrated-rankings-conformal-elo-estimati.pdf`](pdfs/2606.13221_from-uncertain-judgments-to-calibrated-rankings-conformal-elo-estimati.pdf) · [abs](https://arxiv.org/abs/2606.13221)

Evaluating new large language models typically requires costly human annotation campaigns at scale. LLM-as-a-judge offers a cheaper alternative, but judge scores carry systematic errors - such as position bias, self-preference, or intransitivity - that can strongly miscalibrate the resulting rankings. We quantify the resulting judge-human disagreement at two complementary levels. At the local level, we estimate per-battle uncertainty from the judge's own score differences by propagating calibrat…

### HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection
- **2606.12620** · 2026-06-10 · cs.SE
- Luke Patterson, Li Wang, Adam Faulkner
- [`pdfs/2606.12620_hybridcodeauthorship-a-benchmark-dataset-for-line-level-code-authorshi.pdf`](pdfs/2606.12620_hybridcodeauthorship-a-benchmark-dataset-for-line-level-code-authorshi.pdf) · [abs](https://arxiv.org/abs/2606.12620)

Thanks to the rapid adoption of AI code assistants powered by large language models (LLMs), industry codebases are, increasingly, a hybrid of AI- and human-authored code. For risk management and productivity analysis purposes, it is crucial to enable fine-grained location detection of AI-generated code. To develop algorithms for this task, quality benchmarks are needed to assess performance. However, existing benchmarks tend to comprise academic, LeetCode-style problems and presume a code snippe…

### Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis
- **2606.11755** · 2026-06-10 · cs.SE
- Hongzhou Rao, Zikan Dong, Yanjie Zhao et al.
- [`pdfs/2606.11755_acoda-adversarial-code-obfuscation-for-defending-against-llm-based-ana.pdf`](pdfs/2606.11755_acoda-adversarial-code-obfuscation-for-defending-against-llm-based-ana.pdf) · [abs](https://arxiv.org/abs/2606.11755)

With the widespread adoption of Large Language Models (LLMs) in software engineering (SE) tasks such as code understanding, debugging, and vulnerability detection, their powerful semantic reasoning ability has also introduced new security and privacy risks. LLMs can analyze, reconstruct, or even reverse-engineer source code logic, potentially leading to the leakage of intellectual property. To address this issue, we propose Acoda, a genetic algorithm-based adversarial code obfuscation framework …

### Foresight: Iterative Reasoning About Clues that Matter for Navigation
- **2606.12550** · 2026-06-10 · cs.RO
- Arthur Zhang, Carl Qi, Donne Su et al.
- [`pdfs/2606.12550_foresight-iterative-reasoning-about-clues-that-matter-for-navigation.pdf`](pdfs/2606.12550_foresight-iterative-reasoning-about-clues-that-matter-for-navigation.pdf) · [abs](https://arxiv.org/abs/2606.12550)

Open-world mapless navigation from sparse language instructions requires resolving underspecified goals and inferring which environmental cues are relevant for reaching the goal. For instance, reaching an out-of-view destination may require interpreting ramps, signs, or detours that reveal where to go or which route to take. Prior works are limited by their reliance on known navigation factors and closed-set factor categories, or identify cues before motion planning and miss plan-dependent cues.…

### The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes
- **2606.11470** · 2026-06-09 · cs.CL
- Avinash Anand, Mahisha Ramesh, Avni Mittal et al.
- [`pdfs/2606.11470_the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-p.pdf`](pdfs/2606.11470_the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-p.pdf) · [abs](https://arxiv.org/abs/2606.11470)

Large Language Models (LLMs) have achieved strong performance across natural language processing tasks, yet reliable reasoning remains an open challenge. Although modern LLMs show progress in structured inference, multi-step problem solving, and contextual understanding, their reasoning behavior is often inconsistent and sensitive to prompting strategies, task design, and model scale. This survey provides a systematic analysis of more than 300 recent papers from arXiv, Semantic Scholar, Google S…

### $τ$-Rec: A Verifiable Benchmark for Agentic Recommender Systems
- **2606.10156** · 2026-06-08 · cs.IR
- Bharath Sivaram Narasimhan, Karthik R Narasimhan
- [`pdfs/2606.10156_rec-a-verifiable-benchmark-for-agentic-recommender-systems.pdf`](pdfs/2606.10156_rec-a-verifiable-benchmark-for-agentic-recommender-systems.pdf) · [abs](https://arxiv.org/abs/2606.10156)

As recommender systems transition toward agentic, multi-turn conversational interfaces, evaluation paradigms have struggled to keep pace. Current benchmarks often rely on "LLM-as-a-judge" evaluations, which introduce subjectivity, high costs and inconsistency. We present $τ$-Rec, a benchmark for agentic recommender systems that replaces subjective evaluation with verifiable rewards and a reveal-tagged elicitation (RTE) mechanism that controls how task constraints surface during dialogue. By test…

### TRIAGE: Dialectical Reasoning for Explainable Risk Prediction on Irregularly Sampled Medical Time Series with LLMs
- **2606.09030** · 2026-06-08 · cs.LG
- Hyeongwon Jang, Gyouk Chu, Changhun Kim et al.
- [`pdfs/2606.09030_triage-dialectical-reasoning-for-explainable-risk-prediction-on-irregu.pdf`](pdfs/2606.09030_triage-dialectical-reasoning-for-explainable-risk-prediction-on-irregu.pdf) · [abs](https://arxiv.org/abs/2606.09030)

Clinical early warning systems built on electronic health records, in which clinical observations are recorded as irregularly sampled medical time series (ISMTS), must deliver both calibrated risk scores for patient triage and interpretable rationales that clinicians can verify. Large Language Models (LLMs) have been explored for this task, yet they collapse graded clinical risk into overconfident binary predictions. This risk polarization undermines both calibration and cross-patient comparabil…

### Gradient-Guided Reward Optimization for Inference-time Alignment
- **2606.09635** · 2026-06-08 · cs.CL
- Hankun Lin, Ruqi Zhang
- [`pdfs/2606.09635_gradient-guided-reward-optimization-for-inference-time-alignment.pdf`](pdfs/2606.09635_gradient-guided-reward-optimization-for-inference-time-alignment.pdf) · [abs](https://arxiv.org/abs/2606.09635)

Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges,…

### Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems
- **2606.10078** · 2026-06-08 · cs.IR
- Yaochen Zhu, Harald Steck, James McInerney et al.
- [`pdfs/2606.10078_mult-dpo-multinomial-direct-preference-optimization-for-recommender-sy.pdf`](pdfs/2606.10078_mult-dpo-multinomial-direct-preference-optimization-for-recommender-sy.pdf) · [abs](https://arxiv.org/abs/2606.10078)

Direct preference optimization (DPO) is a simple and effective alignment strategy for large language models (LLMs) based on pairwise preferences. In recommender systems, however, user feedback is rarely pairwise. For a given context, e.g., a user, a session, or a conversation, we typically observe set-wise preferences with multiple positive items, where every positive item should outrank every unobserved or explicitly negative item, with no prescribed order among the positives or the negatives t…

### When LLMs Invent Rust Crates: An Empirical Study of Hallucination Patterns and Mitigation
- **2606.08444** · 2026-06-07 · cs.SE
- Jieming Zheng, Hao Guan, Yepang Liu
- [`pdfs/2606.08444_when-llms-invent-rust-crates-an-empirical-study-of-hallucination-patte.pdf`](pdfs/2606.08444_when-llms-invent-rust-crates-an-empirical-study-of-hallucination-patte.pdf) · [abs](https://arxiv.org/abs/2606.08444)

Large Language Models (LLMs) have become powerful tools for code generation, yet they remain prone to hallucinations-producing plausible but incorrect or fabricated outputs. Among these, package hallucination, where an LLM suggests non-existent dependencies, poses an emerging security risk to the software supply chain. While previous studies focus on popular languages like Python or JavaScript, in this work we present the first large-scale empirical study on crate hallucination in LLM-generated …

### Biological Reasoning-Informed Regression for Interpretable Regulatory DNA Activity Prediction
- **2606.08147** · 2026-06-06 · q-bio.GN
- Yi Duan, Zhao Yang, Jiwei Zhu et al.
- [`pdfs/2606.08147_biological-reasoning-informed-regression-for-interpretable-regulatory.pdf`](pdfs/2606.08147_biological-reasoning-informed-regression-for-interpretable-regulatory.pdf) · [abs](https://arxiv.org/abs/2606.08147)

DNA cis-regulatory elements (CREs) such as enhancers control gene expression levels. Accurately predicting regulatory activity from DNA sequences is valuable but challenging, as it requires understanding complex biological regulatory processes. Existing methods typically regress activity scores from sequences in a black-box manner, limiting both interpretability and regression performance. Meanwhile, large language models (LLMs) benefit from explicit reasoning processes, yet directly applying LL…

### On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus
- **2606.07363** · 2026-06-05 · cs.CR
- Xiaoting Zhang, Zhipeng Gao, Yiran Lv et al.
- [`pdfs/2606.07363_on-the-shoulders-of-giants-empowering-automated-smart-contract-auditin.pdf`](pdfs/2606.07363_on-the-shoulders-of-giants-empowering-automated-smart-contract-auditin.pdf) · [abs](https://arxiv.org/abs/2606.07363)

High-quality smart contract auditing datasets are crucial for evaluating security tools and advancing smart contract security research. Two major limitations of existing datasets are the manual-induced scalability bottleneck and the deficiency in data granularity and diversity. To address these limitations, we propose GiANT, an automated framework designed to curate smart contract auditing datasets by distilling vulnerability insights from real-world auditing reports. GiANT employs a divide-and-…

### Towards the Readability of LLM-Generated Codes through Multitask Representation Engineering
- **2606.06214** · 2026-06-04 · cs.SE
- Huifan Gao, Liuhua He, Yinghui Pan et al.
- [`pdfs/2606.06214_towards-the-readability-of-llm-generated-codes-through-multitask-repre.pdf`](pdfs/2606.06214_towards-the-readability-of-llm-generated-codes-through-multitask-repre.pdf) · [abs](https://arxiv.org/abs/2606.06214)

Correctness and readability are key measures of code quality, respectively ensuring functional fidelity and ease of comprehension. While most existing research focuses on improving the correctness of large language models~(LLMs) generated codes, readability remains under-addressed. Enhancing readability through targeted control is challenging due to its subjective nature. In this article, we employ representation engineering~(RepE) as the targeted control method given its characteristics of low …

### Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Code-Generation Skill
- **2606.06454** · 2026-06-04 · cs.SE
- Mehmet Iscan
- [`pdfs/2606.06454_scaffold-not-vocabulary-a-controlled-two-tier-pre-registered-study-of.pdf`](pdfs/2606.06454_scaffold-not-vocabulary-a-controlled-two-tier-pre-registered-study-of.pdf) · [abs](https://arxiv.org/abs/2606.06454)

Large language models increasingly write, review, and judge code, and a fast-growing practice equips them with prompt 'skills' that ask the model to reason like a scientist. A prominent example tells the model to act as a Popperian falsificationist, and such skills are reported to improve generated code. But these gains are almost always read off an LLM-as-a-judge, an instrument with documented positional, self-preference, and stylistic biases. We ask: if it appears to help, is the gain from the…

### Benchmark Everything Everywhere All at Once
- **2606.06462** · 2026-06-04 · cs.AI
- Shiyun Xiong, Dongming Wu, Peiwen Sun et al.
- [`pdfs/2606.06462_benchmark-everything-everywhere-all-at-once.pdf`](pdfs/2606.06462_benchmark-everything-everywhere-all-at-once.pdf) · [abs](https://arxiv.org/abs/2606.06462)

Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse, raising concerns about sustainability and scalability. Moreover, existing benchmarks often quickly reach performance saturation after their release, resulting in insufficient discrimination among state-of-the-art models. To address these challenges, we introduce Benchmark Agent, a fully autonomous …

### Video-Rate Streaming Stylization on a Vision-Aware MLLM-Conditioned Edit Diffusion: Asymmetric Batched Inference on a Distilled UNet + MLLM Text Encoder
- **2606.05981** · 2026-06-04 · cs.CV
- Yoshiyuki Ootani
- [`pdfs/2606.05981_video-rate-streaming-stylization-on-a-vision-aware-mllm-conditioned-ed.pdf`](pdfs/2606.05981_video-rate-streaming-stylization-on-a-vision-aware-mllm-conditioned-ed.pdf) · [abs](https://arxiv.org/abs/2606.05981)

Aggressive distillation of the diffusion U-Net inverts the per-frame bottleneck of real-time text-to-image pipelines: once the denoiser is a 4-step or 1-step distilled student, the text encoder becomes the critical path. This inversion is most acute in vision-aware edit diffusion, where the encoder is a multimodal large language model (MLLM). We study the case of a 0.39B distilled edit U-Net paired with a 2.13B MLLM text encoder (Qwen3-VL) and present a streaming pipeline targeted at this regime…

### Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models
- **2606.04739** · 2026-06-03 · cs.SE
- Sabrina Kaniewski, Fabian Schmidt, Tobias Heer
- [`pdfs/2606.04739_revisiting-vul-rag-reproducibility-and-replicability-of-rag-based-vuln.pdf`](pdfs/2606.04739_revisiting-vul-rag-reproducibility-and-replicability-of-rag-based-vuln.pdf) · [abs](https://arxiv.org/abs/2606.04739)

Large language models (LLMs) have shown strong potential for automated software vulnerability detection, particularly in retrieval-augmented generation (RAG) settings. However, for approaches relying on proprietary models and APIs, reproducibility and replicability remain largely unexplored, raising the question of whether reported results generalize or depend primarily on specific model choices. In this work, we present a reproducibility study of Vul-RAG, a RAG-based framework for source code v…

### TeleSWEBench: A Commit-Driven Benchmark for Evaluating LLM-Powered Software Engineering in Telecommunications
- **2606.05001** · 2026-06-03 · cs.SE
- Pranshav Gajjar, Ali Mamaghani, Dinesh Bharadia et al.
- [`pdfs/2606.05001_teleswebench-a-commit-driven-benchmark-for-evaluating-llm-powered-soft.pdf`](pdfs/2606.05001_teleswebench-a-commit-driven-benchmark-for-evaluating-llm-powered-soft.pdf) · [abs](https://arxiv.org/abs/2606.05001)

With the telecommunications field embracing zero touch management alongside novel O-RAN and AI-RAN frameworks, contemporary telecom networks now function as immensely intricate and heavily softwareized codebases. While automated software engineering (ASE) tools and Software Engineering (SWE) Agents hold the potential to alleviate the critical code generation bottleneck in this domain, their ability to navigate and modify specialized, mathematically rigorous wireless stacks like srsRAN 5G remains…

### Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning
- **2606.04923** · 2026-06-03 · cs.LG
- Xuekang Wang, Zhuoyuan Hao, Shuo Hou et al.
- [`pdfs/2606.04923_reproducing-analyzing-and-detecting-reward-hacking-in-rubric-based-rei.pdf`](pdfs/2606.04923_reproducing-analyzing-and-detecting-reward-hacking-in-rubric-based-rei.pdf) · [abs](https://arxiv.org/abs/2606.04923)

Rubric-based reinforcement learning (RL) uses an LLM-as-a-Judge (LaaJ) to score model outputs according to rubrics as rewards. However, policy models may exploit latent biases in the judge, leading to reward hacking and ineffective or unsafe training outcomes. In real-world rubric-based RL, such hacking behaviors are often subtle and entangled with multiple judge biases, making them difficult to analyze, detect, and mitigate. In this paper, we introduce CHERRL, a controllable hacking environment…

### Follow-Your-Preference++: Rethinking Preference Alignment for Image Inpainting
- **2606.03216** · 2026-06-02 · cs.CV
- Junkun Yuan, Yutao Shen, Toru Aonishi et al.
- [`pdfs/2606.03216_follow-your-preference-rethinking-preference-alignment-for-image-inpai.pdf`](pdfs/2606.03216_follow-your-preference-rethinking-preference-alignment-for-image-inpai.pdf) · [abs](https://arxiv.org/abs/2606.03216)

We study preference alignment for image inpainting. Rather than proposing yet another method, we revisit the problem from first principles and reassess its core challenges. We adopt the widely used direct preference optimization framework and construct preference training data with publicly available reward models. Our empirical study spans nine reward models, two benchmarks, and two baseline inpainting models that differ in architecture and generative mechanism. Our main findings are: (1) Most …

### Comparing ML-Specific and General Python Code Smells Across Project Characteristics
- **2606.01882** · 2026-06-01 · cs.SE
- Halimeh Agh, Betül Cimendag, Stefan Wagner
- [`pdfs/2606.01882_comparing-ml-specific-and-general-python-code-smells-across-project-ch.pdf`](pdfs/2606.01882_comparing-ml-specific-and-general-python-code-smells-across-project-ch.pdf) · [abs](https://arxiv.org/abs/2606.01882)

Machine learning systems consist of general-purpose code as well as machine-learning-specific code. While ML-specific code smells have been identified, their connection to project characteristics and their interaction with overall code quality are not well understood. Without this knowledge, quality assurance strategies remain one-size-fits-all, failing to account for the contextual factors that drive technical debt in ML systems. We present empirical evidence by examining how six project featur…

### Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation
- **2606.01629** · 2026-06-01 · cs.CL
- Junjie Chen, Yuxi Dong, Haitao Li et al.
- [`pdfs/2606.01629_benchmarking-llm-as-a-judge-for-long-form-output-evaluation.pdf`](pdfs/2606.01629_benchmarking-llm-as-a-judge-for-long-form-output-evaluation.pdf) · [abs](https://arxiv.org/abs/2606.01629)

As large language models (LLMs) are increasingly used for long-form generation, reliably evaluating long-form outputs has become a critical challenge. LLM-as-a-judge offers a scalable alternative to human evaluation, yet its reliability in long-form output evaluation remains underexamined: existing meta-evaluation benchmarks focus mainly on short-form outputs. Compared with short-form evaluation, long-form evaluation is not merely a matter of output length; it often requires judges to make more …

### Trust-Calibrated Code Review: A Participatory Design Study of Review Workflows for LLM-Generated Multi-File Changes
- **2606.01969** · 2026-06-01 · cs.SE
- Lo Gullstrand Heander, Agnia Sergeyuk, Ilya Zakharov et al.
- [`pdfs/2606.01969_trust-calibrated-code-review-a-participatory-design-study-of-review-wo.pdf`](pdfs/2606.01969_trust-calibrated-code-review-a-participatory-design-study-of-review-wo.pdf) · [abs](https://arxiv.org/abs/2606.01969)

Background: Developers increasingly review multi-file code changes generated by LLM-based agents, yet no validated end-to-end workflow or IDE tooling design exists for this scenario. Aims: We investigate (RQ1) the challenges developers face when reviewing LLM-generated multi-file changes and (RQ2) how developers envision effective workflows for this task. Method: In collaboration with JetBrains, we conducted a participatory design study structured using the double-diamond design process with Dis…

### Improving LLM-Based Go Code Review through Issue-List Generation and Context Augmentation
- **2606.01859** · 2026-06-01 · cs.SE
- Kexin Sun, Yucong Guan, Jiaqi Sun et al.
- [`pdfs/2606.01859_improving-llm-based-go-code-review-through-issue-list-generation-and-c.pdf`](pdfs/2606.01859_improving-llm-based-go-code-review-through-issue-list-generation-and-c.pdf) · [abs](https://arxiv.org/abs/2606.01859)

LLMs have shown strong potential for automating code review, yet their practical utility depends heavily on the design of generation and context strategies. In this paper, we investigate how to improve LLM-based code review through generation strategy and contextual augmentation. We first propose an issue-list review paradigm, in which LLMs enumerate all potential issues rather than reporting only the single most important one (i.e., primary-issue review). We then systematically compare three ty…

### CodegenBench: Can LLMs Write Efficient Code Across Architectures?
- **2606.04023** · 2026-06-01 · cs.SE
- Jie Li, Wenzhao Wu, Junqi Hu et al.
- [`pdfs/2606.04023_codegenbench-can-llms-write-efficient-code-across-architectures.pdf`](pdfs/2606.04023_codegenbench-can-llms-write-efficient-code-across-architectures.pdf) · [abs](https://arxiv.org/abs/2606.04023)

While large language models (LLMs) have been extensively evaluated on code generation tasks for general-purpose programming and GPU-accelerated environments (e.g., PyTorch, CUDA), their capabilities in CPU-oriented high-performance computing (HPC) across diverse architectures remain underexplored. To bridge this gap, we introduce CodegenBench, a comprehensive benchmark suite designed to evaluate the generation of efficient parallel code across three distinct hardware platforms: x86_64, Sunway, a…

### EstRTL: Functional Estimation Guided RTL Code Generation
- **2606.09867** · 2026-06-01 · cs.AR
- Qi Xiong, Renzhi Chen, Bowei Wang et al.
- [`pdfs/2606.09867_estrtl-functional-estimation-guided-rtl-code-generation.pdf`](pdfs/2606.09867_estrtl-functional-estimation-guided-rtl-code-generation.pdf) · [abs](https://arxiv.org/abs/2606.09867)

Optimizing register transfer level (RTL) code is of vital importance in hardware design. Large language models (LLMs) provide new methods for the automatic generation and optimization of RTL code, offering the potential to significantly accelerate the design process and reduce human effort. However, existing methods for generating RTL code often focus on model fine-tuning and the use of various expansion techniques to enhance the RTL code generation capabilities, lacking attention to the functio…

### From Rocq to Metal: A Pipeline for Formally Verified Microcontroller Firmware
- **2606.02651** · 2026-05-31 · cs.PL
- Valentin Bergeron, Karolina Gorna
- [`pdfs/2606.02651_from-rocq-to-metal-a-pipeline-for-formally-verified-microcontroller-fi.pdf`](pdfs/2606.02651_from-rocq-to-metal-a-pipeline-for-formally-verified-microcontroller-fi.pdf) · [abs](https://arxiv.org/abs/2606.02651)

Enforcing invariants in safety-critical systems is increasingly urgent as AI-generated code becomes widespread. Unfortunately, the runtimes required to support high-level specification languages are too large for most embedded targets. In this article, we show how formally verified firmware is achievable today. We built Encore!, a bare-metal Continuation Passing Style (CPS) virtual machine (VM) that runs Rocq-extracted Scheme on microcontrollers. We also show how to structure firmware as a pure …

### TukaBench: A Culturally Grounded Jailbreak Benchmark for African Languages
- **2606.01322** · 2026-05-31 · cs.CL
- Victor Akinode, Senyu Li, Wassim Hamidouche et al.
- [`pdfs/2606.01322_tukabench-a-culturally-grounded-jailbreak-benchmark-for-african-langua.pdf`](pdfs/2606.01322_tukabench-a-culturally-grounded-jailbreak-benchmark-for-african-langua.pdf) · [abs](https://arxiv.org/abs/2606.01322)

Safety evaluation of Large Language Models (LLMs) remains heavily English-centric, leaving Low-Resource Languages (LRLs), particularly African ones, critically underexplored. We introduce TUKABENCH, a jailbreak benchmark for seven African languages that extends JailbreakBench (JBB) beyond direct translation through four settings: human translation of JBB prompts, English adaptation to African contexts followed by human translation, human-curated prompts validated through interactions with GPT-5.…

### Med-HEAL: Analyzing and Mitigating Hallucinations in Medical LLMs with Hallucination-Aware In-Context Learning
- **2606.01301** · 2026-05-31 · cs.CL
- Yiming Liao, Zeno Franco, Jose Eduardo Lizarraga Mazaba et al.
- [`pdfs/2606.01301_med-heal-analyzing-and-mitigating-hallucinations-in-medical-llms-with.pdf`](pdfs/2606.01301_med-heal-analyzing-and-mitigating-hallucinations-in-medical-llms-with.pdf) · [abs](https://arxiv.org/abs/2606.01301)

Hallucinations in medical large language models (LLMs) pose serious risks for clinical decision support, particularly when models must reason over complex electronic health records (EHRs). However, existing benchmarks often lack a realistic clinical context and provide limited insight into how hallucinations can be mitigated in practice. We introduce Med-HEAL, a framework for systematically identifying, analyzing, and mitigating hallucinations in medical LLMs using clinically grounded data. Buil…

### Preference-Aware Rubric Learning for Personalized Evaluation
- **2605.31545** · 2026-05-29 · cs.CL
- Yilun Qiu, Xiaoyan Zhao, Yang Zhang et al.
- [`pdfs/2605.31545_preference-aware-rubric-learning-for-personalized-evaluation.pdf`](pdfs/2605.31545_preference-aware-rubric-learning-for-personalized-evaluation.pdf) · [abs](https://arxiv.org/abs/2605.31545)

As Large Language Models (LLMs) evolve from general-purpose assistants to user-centric agents, personalization has become central to aligning model behavior with individual preferences, making the evaluation of personalized alignment a critical bottleneck. Existing evaluation methods-ranging from automatic metrics to LLM-as-a-judge approaches-fail to capture subjective, user-specific preferences embedded in long-term interaction histories. We identify three essential principles for reliable and …

### Differentially Private Preference Data Synthesis for Large Language Model Alignment
- **2605.30808** · 2026-05-29 · cs.CR
- Fengyu Gao, Jing Yang
- [`pdfs/2605.30808_differentially-private-preference-data-synthesis-for-large-language-mo.pdf`](pdfs/2605.30808_differentially-private-preference-data-synthesis-for-large-language-mo.pdf) · [abs](https://arxiv.org/abs/2605.30808)

Preference alignment is a crucial post-training step for large language models (LLMs) to ensure their outputs align with human values. However, post-training on real human preference data raises privacy concerns, as these datasets often contain sensitive user prompts and human judgments. To address this, we propose DPPrefSyn, a novel algorithm for generating differentially private (DP) synthetic preference data to enable privacy-preserving preference alignment. DPPrefSyn is a principled framewor…

### Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency
- **2605.30208** · 2026-05-28 · cs.SE
- Chris Adams, Arjun Singh Banga, Parveen Bansal et al.
- [`pdfs/2605.30208_automating-low-risk-code-review-at-meta-radar-risk-calibration-and-rev.pdf`](pdfs/2605.30208_automating-low-risk-code-review-at-meta-radar-risk-calibration-and-rev.pdf) · [abs](https://arxiv.org/abs/2605.30208)

AI-assisted coding tools have altered software production. At Meta, significant lines of code per human-landed diff grew by 105.9% year over year and per-developer diff volume rose 51%, with agentic AI responsible for over 80% of that growth. Meanwhile, the share of diffs receiving timely review has declined, exposing a widening gap between code supply and reviewer bandwidth. We ask three questions that progress from feasibility through calibration to impact: (1) can risk-stratified automation o…

### Inferring Code Correctness from Specification
- **2605.29822** · 2026-05-28 · cs.SE
- Tambon Florian, Papadakis Mike
- [`pdfs/2605.29822_inferring-code-correctness-from-specification.pdf`](pdfs/2605.29822_inferring-code-correctness-from-specification.pdf) · [abs](https://arxiv.org/abs/2605.29822)

Large language models (LLMs) have become integral to modern software development, enabling automated code generation at scale. However, validating the correctness of LLM-generated code remains a critical and largely unsolved challenge. Existing approaches either rely on dynamic consensus across multiple code candidates - making them costly and difficult to scale - or on static reasoning that is susceptible to dynamic bugs and order bias. In this paper, we propose TRAILS~ (Targeted Reasoning Agre…

### Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection
- **2605.29901** · 2026-05-28 · cs.CR
- Syafiq Al Atiiq, Chun Zhou, Christian Gehrmann
- [`pdfs/2605.29901_dissecting-the-black-box-circuit-level-analysis-of-llm-vulnerability-d.pdf`](pdfs/2605.29901_dissecting-the-black-box-circuit-level-analysis-of-llm-vulnerability-d.pdf) · [abs](https://arxiv.org/abs/2605.29901)

Large language models (LLMs) can detect software vulnerabilities, but how do they actually identify vulnerable code? We address this question using mechanistic interpretability; analyzing the internal computations of a neural network to understand its reasoning process.Using Circuit Tracer on Gemma-2-2b, we trace the computational pathways activated when the model classifies 472 C/C++ code samples as vulnerable or safe. Our analysis reveals a surprising finding: the model primarily relies on saf…

### Multi-Agent LLM-based Metamorphic Testing for REST APIs
- **2605.28321** · 2026-05-27 · cs.SE
- Shehroz Khan, Abdullah Mughees, Gaadha Sudheerbabu et al.
- [`pdfs/2605.28321_multi-agent-llm-based-metamorphic-testing-for-rest-apis.pdf`](pdfs/2605.28321_multi-agent-llm-based-metamorphic-testing-for-rest-apis.pdf) · [abs](https://arxiv.org/abs/2605.28321)

As REST APIs become an increasingly significant part of software systems, their validation is becoming more critical. Hence, testing and uncovering underlying issues are of utmost importance for improving software quality. However, testing REST APIs is challenging mainly due to the difficulty of assessing whether the output of an API call is correct, i.e., the test oracle problem. Metamorphic testing is a specification-based testing approach for situations where correct outputs are unknown or no…

### Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study
- **2605.28710** · 2026-05-27 · cs.CL
- Irune Zubiaga, Aitor Soroa, Rodrigo Agerri
- [`pdfs/2605.28710_towards-reliable-multilingual-llms-as-a-judge-an-empirical-study.pdf`](pdfs/2605.28710_towards-reliable-multilingual-llms-as-a-judge-an-empirical-study.pdf) · [abs](https://arxiv.org/abs/2605.28710)

Large language models (LLMs) are increasingly used for the automatic evaluation of generated text, yet most prior work focuses on English. Despite the growing demand for multilingual evaluation, extending LLM-based evaluators to multilingual settings remains challenging, particularly for low-resource languages and scenarios where in-domain data is scarce. This work explores several strategies for developing multilingual LLMs-as-a-judge, considering whether in-domain data is available for fine-tu…

### Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization
- **2605.26457** · 2026-05-26 · cs.SE
- Anmol Agarwal, Natalie Neamtu, Pranjal Aggarwal et al.
- [`pdfs/2605.26457_verus-specgym-an-agentic-environment-for-evaluating-specification-auto.pdf`](pdfs/2605.26457_verus-specgym-an-agentic-environment-for-evaluating-specification-auto.pdf) · [abs](https://arxiv.org/abs/2605.26457)

AI coding agents are increasingly used to write real-world software, but ensuring that their outputs are correct remains a fundamental challenge. Formal verification offers a promising path: an agent generates code together with a machine-checked proof, guaranteeing that the code satisfies a formal specification. However, there is no guarantee that the formal spec itself matches the user's intent. In this work, we study specification autoformalization: whether LLM agents can translate informal p…

### Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models
- **2605.26100** · 2026-05-25 · cs.SE
- Bar Weiss, Antonio Abu-Nassar, Adi Sosnovich et al.
- [`pdfs/2605.26100_beyond-summaries-structure-aware-labeling-of-code-changes-with-large-l.pdf`](pdfs/2605.26100_beyond-summaries-structure-aware-labeling-of-code-changes-with-large-l.pdf) · [abs](https://arxiv.org/abs/2605.26100)

Code review is a critical practice in software engineering, yet the growing scale and frequency of code patches in modern projects, together with the widespread adoption of AI code assistants, make manual review increasingly challenging. Identifying the types of changes within a patch, such as renames, moves, or logic modifications, can substantially improve review efficiency by enabling prioritization, filtering, and automation. However, existing LLM-based approaches to code review have largely…

### PennySynth: RAG-Driven Data Synthesis for Automated Quantum Code Generation
- **2605.25572** · 2026-05-25 · cs.CL
- Minghao Shao, Nouhaila Innan, Hariharan Janardhanan et al.
- [`pdfs/2605.25572_pennysynth-rag-driven-data-synthesis-for-automated-quantum-code-genera.pdf`](pdfs/2605.25572_pennysynth-rag-driven-data-synthesis-for-automated-quantum-code-genera.pdf) · [abs](https://arxiv.org/abs/2605.25572)

The growing complexity of quantum programming frameworks has exposed a critical limitation in existing large language model (LLM)-based code assistants: general-purpose models hallucinate PennyLane-specific gate names, misplace device configurations, and produce structurally invalid circuits when faced with specialized quantum coding challenges. We present PennySynth, a retrieval-augmented generation framework that addresses this gap by conditioning LLM inference on a curated knowledge base of 1…

### AutoSG: LLM-Driven Solver Generation Solely from Task Prompts for Expensive Optimization
- **2605.25658** · 2026-05-25 · cs.CL
- Haoran Gu, Handing Wang, Yi Mei et al.
- [`pdfs/2605.25658_autosg-llm-driven-solver-generation-solely-from-task-prompts-for-expen.pdf`](pdfs/2605.25658_autosg-llm-driven-solver-generation-solely-from-task-prompts-for-expen.pdf) · [abs](https://arxiv.org/abs/2605.25658)

Expensive optimization tasks are ubiquitous in real-world applications, demanding highly specialized solvers. While LLM-driven automated solver generation shows promise, current paradigms face three critical issues when tackling expensive optimization: factual hallucinations due to deficient domain knowledge, the frequent dismantling of previously established locally optimal structures during refinement, and the prohibitive evaluation costs alongside restricted generalization caused by executing…

### CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures
- **2605.25338** · 2026-05-25 · cs.LG
- Akash Bonagiri, Devang Borkar, Gerard Janno Anderias et al.
- [`pdfs/2605.25338_causalflow-causal-attribution-and-counterfactual-repair-for-llm-agent.pdf`](pdfs/2605.25338_causalflow-causal-attribution-and-counterfactual-repair-for-llm-agent.pdf) · [abs](https://arxiv.org/abs/2605.25338)

Large language model (LLM) agents frequently fail on multi-step tasks involving reasoning, tool use, and environment interaction. While such failures are typically logged or retried heuristically, they contain structured signals about where execution broke down. We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision. CausalFlow models execution traces as sequential chains of dependent steps and computes …

### LLM-as-a-Judge in Healthcare: A Scoping Analysis of Applications, Methods, and Human Alignment
- **2605.25273** · 2026-05-24 · cs.CY
- Lingyao Li, Deyi Li, Chen Chen et al.
- [`pdfs/2605.25273_llm-as-a-judge-in-healthcare-a-scoping-analysis-of-applications-method.pdf`](pdfs/2605.25273_llm-as-a-judge-in-healthcare-a-scoping-analysis-of-applications-method.pdf) · [abs](https://arxiv.org/abs/2605.25273)

Large language models (LLMs) are increasingly deployed across healthcare applications, including clinical documentation, diagnostic reasoning, medicine recommendation, and medical education. Their outputs are largely unstructured clinical text, which is difficult to reliably evaluate at scale. LLM-as-a-Judge, in which an LLM evaluates another system's output against task-specific criteria, offers a scalable alternative and is increasingly used in clinical evaluation, yet its validity in healthca…

### Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges
- **2605.26156** · 2026-05-24 · cs.CR
- Xianglin Yang, Bryan Hooi, Gelei Deng et al.
- [`pdfs/2605.26156_turning-bias-into-bugs-bandit-guided-style-manipulation-attacks-on-llm.pdf`](pdfs/2605.26156_turning-bias-into-bugs-bandit-guided-style-manipulation-attacks-on-llm.pdf) · [abs](https://arxiv.org/abs/2605.26156)

The known stylistic biases in LLM judges, such as a preference for verbosity or specific sentence structures, present an underexplored security vulnerability. In this work, we introduce BITE (BIas exploraTion and Exploitation), a black-box adversarial framework that learns semantics-preserving edits to mislead an LLM judge and artificially inflate the scores it assigns. We cast the selection of stylistic edits as a contextual bandit problem and use a LinUCB policy to adaptively choose edits that…

### Subjective Code Preferences in Experts and Large Language Models
- **2605.25296** · 2026-05-24 · cs.HC
- Anna Mokhova, Subhabrata Dutta, Iryna Gurevych et al.
- [`pdfs/2605.25296_subjective-code-preferences-in-experts-and-large-language-models.pdf`](pdfs/2605.25296_subjective-code-preferences-in-experts-and-large-language-models.pdf) · [abs](https://arxiv.org/abs/2605.25296)

Large Language Models (LLMs) have become increasingly popular for coding tasks, with subjective coding preferences being an essential element to adapt to programmers' personal needs. Existing work overlooks such characteristics and mainly focuses on code correctness. In this study, we propose a typification of four subjective coding preference axes - complexity, commenting, modularity, and readability - motivated by common engineering habits and validated by 25 software engineers. We collect a d…

### PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection
- **2605.24171** · 2026-05-22 · cs.LG
- Steffen J. Camarato, Yahya Hmaiti, Mandana Ghadamian et al.
- [`pdfs/2605.24171_promptaudit-auditing-prompt-sensitivity-in-llm-based-vulnerability-det.pdf`](pdfs/2605.24171_promptaudit-auditing-prompt-sensitivity-in-llm-based-vulnerability-det.pdf) · [abs](https://arxiv.org/abs/2605.24171)

Large language models are increasingly used for vulnerability detection, yet their reliability under different prompt formulations remains uncharacterized. We present PromptAudit, a controlled evaluation framework that isolates prompt effects by fixing the dataset, decoding, and parsing while varying only the prompting strategy. Using five prompting strategies across five open-weight models on 1,000 CVEs (6,074 code samples spanning 16 programming languages), we evaluate accuracy, recall, absten…

### LLM Code Smells: A Taxonomy and Detection Approach
- **2605.22976** · 2026-05-21 · cs.SE
- Zacharie Chenail-Larcher, Brahim Mahmoudi, Naouel Moha et al.
- [`pdfs/2605.22976_llm-code-smells-a-taxonomy-and-detection-approach.pdf`](pdfs/2605.22976_llm-code-smells-a-taxonomy-and-detection-approach.pdf) · [abs](https://arxiv.org/abs/2605.22976)

Large Language Models (LLMs) are increasingly integrated into software systems for diverse purposes, due to their versatility, flexibility, and ability to simulate human reasoning to some extent. However, poor integration of LLM inference in source code can undermine software system quality. Therefore, inadequate LLM integration coding practices must be documented to help developers mitigate such issues. Following our earlier work on LLM code smells, this paper consolidates and refines the conce…

### Self-Evolving Multi-Agent Systems via Decentralized Memory
- **2605.22721** · 2026-05-21 · cs.MA
- Guangya Hao, Yunbo Long, Zhuokai Zhao
- [`pdfs/2605.22721_self-evolving-multi-agent-systems-via-decentralized-memory.pdf`](pdfs/2605.22721_self-evolving-multi-agent-systems-via-decentralized-memory.pdf) · [abs](https://arxiv.org/abs/2605.22721)

Self-evolving multi-agent systems (MAS) have emerged as a promising route to LLM agents that continually improve from experience, with persistent memory at their foundation. However, existing designs almost exclusively adopt a centralized repository shared across agents, incurring communication and coordination overhead, raising privacy concerns, and collapsing agent diversity. We propose DecentMem, a decentralized memory framework in which each agent maintains its own dual-pool memory -- an exp…

### Vector Policy Optimization: Training for Diversity Improves Test-Time Search
- **2605.22817** · 2026-05-21 · cs.LG
- Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld et al.
- [`pdfs/2605.22817_vector-policy-optimization-training-for-diversity-improves-test-time-s.pdf`](pdfs/2605.22817_vector-policy-optimization-training-for-diversity-improves-test-time-s.pdf) · [abs](https://arxiv.org/abs/2605.22817)

Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po…

### Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning
- **2605.22511** · 2026-05-21 · cs.AI
- Zihan Liang, Yufei Ma, Ben Chen et al.
- [`pdfs/2605.22511_search-e1-self-distillation-drives-self-evolution-in-search-augmented.pdf`](pdfs/2605.22511_search-e1-self-distillation-drives-self-evolution-in-search-augmented.pdf) · [abs](https://arxiv.org/abs/2605.22511)

Post-training has become the dominant recipe for turning a language model into a competent search-augmented reasoning agent. A line of recent work pushes its performance further by adding elaborate machinery on top of this standard pipeline. These augmentations import external supervision from stronger external systems, attach auxiliary modules such as process reward models or retrospective critics, restructure the rollout itself with tree search or multi-stage curricula, or shape the reward wit…

### Combating Harms of Generative AI in CS1 with Code Review Interviews and a Flipped Classroom
- **2605.21374** · 2026-05-20 · cs.HC
- Peter Fowles, Erik Falor, Sulove Bhattarai et al.
- [`pdfs/2605.21374_combating-harms-of-generative-ai-in-cs1-with-code-review-interviews-an.pdf`](pdfs/2605.21374_combating-harms-of-generative-ai-in-cs1-with-code-review-interviews-an.pdf) · [abs](https://arxiv.org/abs/2605.21374)

Background and Context: Large Language Models (LLMs) are more accessible and accurate than ever before, raising significant concerns for computing educators. One major concern is students using LLMs to bypass the effort needed to understand concepts and metacognitive strategies essential for success in computer science. Objectives: We contribute a unique approach to assessing and building up student understanding through weekly oral code review assessments. These formative assessments incentiviz…

### Can LLMs Produce Better Object-Oriented Designs than Human-Involved Development?
- **2605.19901** · 2026-05-19 · cs.SE
- Zushuai Zhang, Elliott Wen, Ewan Tempero
- [`pdfs/2605.19901_can-llms-produce-better-object-oriented-designs-than-human-involved-de.pdf`](pdfs/2605.19901_can-llms-produce-better-object-oriented-designs-than-human-involved-de.pdf) · [abs](https://arxiv.org/abs/2605.19901)

Background: Large Language Models (LLMs) are increasingly used for code generation. However, their ability to generate multi-class projects that require object-oriented design (OOD) remains unclear, especially relative to projects developed with human involvement. Aims: The primary objective of this study is to compare OOD quality in projects from three authorship conditions: PreAI (human-involved projects produced before widespread LLM use), PostAI (human-involved projects produced after widesp…

### OpenCompass: A Universal Evaluation Platform for Large Language Models
- **2605.19276** · 2026-05-19 · cs.CL
- Maosong Cao, Kai Chen, Haodong Duan et al.
- [`pdfs/2605.19276_opencompass-a-universal-evaluation-platform-for-large-language-models.pdf`](pdfs/2605.19276_opencompass-a-universal-evaluation-platform-for-large-language-models.pdf) · [abs](https://arxiv.org/abs/2605.19276)

In recent years, the field of artificial intelligence has undergone a paradigm shift from task-specific small-scale models to general-purpose large language models (LLMs). With the rapid iteration of LLMs, objective, quantitative, and comprehensive evaluation of their capabilities has become a critical link in advancing technological development. Currently, the mainstream static benchmark dataset-based evaluation methods face challenges such as the diversity of task types, inconsistent evaluatio…

### Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review of Thirteen Malicious-Code Prompt Corpora (2023-2025)
- **2605.20351** · 2026-05-19 · cs.CR
- Richard J. Young, Gregory D. Moody
- [`pdfs/2605.20351_refusal-evaluation-in-coding-llms-and-code-agents-a-systematic-review.pdf`](pdfs/2605.20351_refusal-evaluation-in-coding-llms-and-code-agents-a-systematic-review.pdf) · [abs](https://arxiv.org/abs/2605.20351)

The evaluation of large language model refusal on malicious-coding tasks now spans at least thirteen publicly released prompt corpora (AdvBench, the CyberSecEval family, RMCBench, RedCode, MCGMark, JailbreakBench, CySecBench, MalwareBench, CIRCLE, MOCHA, ASTRA, Scam2Prompt / Innoc2Scam-bench, and JAWS-Bench), each constructed under a different protocol, released under different licensing terms, and validated (or not) against different inter-rater reliability standards. Existing surveys treat cod…

### Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection
- **2605.18153** · 2026-05-18 · cs.SE
- Xin Peng, Bo Lin, Jing Wang et al.
- [`pdfs/2605.18153_three-heads-are-better-than-one-a-multi-perspective-reasoning-framewor.pdf`](pdfs/2605.18153_three-heads-are-better-than-one-a-multi-perspective-reasoning-framewor.pdf) · [abs](https://arxiv.org/abs/2605.18153)

Automated vulnerability detection is crucial for enhancing software security by identifying potential flaws that attackers could exploit, thereby reducing the reliance on labor-intensive manual code audits. Recent advancements have shifted towards leveraging large language models (LLMs) for vulnerability detection, with techniques like Vul-RAG and VulnSage demonstrating progress through structured prompting and external knowledge integration. However, these approaches typically rely on a single …

### BLAgent: Agentic RAG for File-Level Bug Localization
- **2605.17965** · 2026-05-18 · cs.SE
- Md Afif Al Mamun, Gias Uddin
- [`pdfs/2605.17965_blagent-agentic-rag-for-file-level-bug-localization.pdf`](pdfs/2605.17965_blagent-agentic-rag-for-file-level-bug-localization.pdf) · [abs](https://arxiv.org/abs/2605.17965)

Bug localization remains a key bottleneck in downstream software maintenance tasks, including root cause analysis, triage, and automated program repair (APR), despite recent advances in large language model (LLM)-based repair systems. File-level bug localization is especially critical in hierarchical pipelines, where errors can propagate to downstream stages such as statement-level localization or patch generation. While Retrieval-Augmented Generation (RAG) offers a promising direction for groun…

### General Preference Reinforcement Learning
- **2605.18721** · 2026-05-18 · cs.LG
- Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal et al.
- [`pdfs/2605.18721_general-preference-reinforcement-learning.pdf`](pdfs/2605.18721_general-preference-reinforcement-learning.pdf) · [abs](https://arxiv.org/abs/2605.18721)

Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code but depends on a programmatic verifier that cannot reach open-ended tasks, while preference optimization handles open-ended generation yet forgoes the continuous exploration that powers online RL. Closing this gap requires a verifier for open-ended quality, but a scalar reward model is the wrong sh…

### Rethinking Code Review in the Age of AI: A Vision for Agentic Code Review
- **2605.17548** · 2026-05-17 · cs.SE
- Hüseyin Özgür Kamalı, Erdem Tuna, Vahid Haratian et al.
- [`pdfs/2605.17548_rethinking-code-review-in-the-age-of-ai-a-vision-for-agentic-code-revi.pdf`](pdfs/2605.17548_rethinking-code-review-in-the-age-of-ai-a-vision-for-agentic-code-revi.pdf) · [abs](https://arxiv.org/abs/2605.17548)

Code review has evolved for decades, from informal peer checking to today's pull request (PR) workflows, yet it remains a largely manual and cognitively demanding process. The rise of Artificial Intelligence (AI) coding assistants has intensified this challenge: while these tools increase code production velocity, they also expand the volume of code requiring review, turning code review into a growing bottleneck. Current AI support in code review remains fragmented, with tools focusing on isolat…

### Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification
- **2605.17609** · 2026-05-17 · cs.LG
- Shaddin Dughmi, Mahdi Haghifam, Yusuf Hakan Kalayci
- [`pdfs/2605.17609_adaptive-generate-rank-verify-inference-time-search-with-costly-verifi.pdf`](pdfs/2605.17609_adaptive-generate-rank-verify-inference-time-search-with-costly-verifi.pdf) · [abs](https://arxiv.org/abs/2605.17609)

Many inference-time language-model pipelines combine a cheap reward signal with an expensive verifier, such as exact answer checking in mathematical reasoning or hidden-test execution in code generation. We formalize this setting using a learning-theoretic lens as generative active search: a cost-sensitive first-positive search problem in which a policy adaptively samples candidates from an unknown distribution, observes cheap scores, and pays for verifier labels until it finds a positive exampl…

### ClaHF: A Human Feedback-inspired Reinforcement Learning Framework for Improving Classification Tasks
- **2605.17458** · 2026-05-17 · cs.LG
- Tianxiang Xu, Xiaoyan Zhu, Xin Lai et al.
- [`pdfs/2605.17458_clahf-a-human-feedback-inspired-reinforcement-learning-framework-for-i.pdf`](pdfs/2605.17458_clahf-a-human-feedback-inspired-reinforcement-learning-framework-for-i.pdf) · [abs](https://arxiv.org/abs/2605.17458)

Text classification models are typically trained via supervised fine-tuning (SFT). However, SFT essentially performs behavior cloning from instance-wise labels and thus fails to adequately capture relative preference relations among samples, which limits the model's ability to shape decision boundaries and calibrate predictive confidence. In this paper, we propose ClaHF, a human feedback-inspired reinforcement learning (RL) framework for text classification that integrates preference modeling an…

### Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
- **2605.16215** · 2026-05-15 · cs.AI
- Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan et al.
- [`pdfs/2605.16215_fully-open-meditron-an-auditable-pipeline-for-clinical-llms.pdf`](pdfs/2605.16215_fully-open-meditron-an-auditable-pipeline-for-clinical-llms.pdf) · [abs](https://arxiv.org/abs/2605.16215)

Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron…

### Runtime-Structured Task Decomposition for Agentic Coding Systems
- **2605.15425** · 2026-05-14 · cs.SE
- Shubhi Asthana, Bing Zhang, Chad DeLuca et al.
- [`pdfs/2605.15425_runtime-structured-task-decomposition-for-agentic-coding-systems.pdf`](pdfs/2605.15425_runtime-structured-task-decomposition-for-agentic-coding-systems.pdf) · [abs](https://arxiv.org/abs/2605.15425)

Agentic coding systems increasingly use large language models (LLMs) for software engineering tasks such as debugging, root cause analysis, and code review. However, many existing systems encode task logic, execution flow, and output generation inside monolithic prompts. This design creates brittle behavior, limited debuggability, and high retry costs because failures often require rerunning the full workflow. We present runtime-structured task decomposition, an architectural approach in which t…

### SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle
- **2605.13139** · 2026-05-13 · cs.SE
- Hao Guan, Lingyue Fu, Shao Zhang et al.
- [`pdfs/2605.13139_swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolutio.pdf`](pdfs/2605.13139_swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolutio.pdf) · [abs](https://arxiv.org/abs/2605.13139)

As autonomous code agents move toward end-to-end software development, evaluating their practical autonomy becomes critical. Current benchmarks hide friction by testing agents in pre-configured environments, and their static evaluation pipelines frequently fail when parsing fully autonomous trajectories. We address these limitations with SWE-Cycle, a benchmark of 489 rigorously filtered instances. SWE-Cycle evaluates agents across three isolated tasks, including environment reconstruction, code …

### RTLC -- Research, Teach-to-Learn, Critique: A three-stage prompting paradigm inspired by the Feynman Learning Technique that lifts LLM-as-judge accuracy on JudgeBench with no fine-tuning
- **2605.13695** · 2026-05-13 · cs.CL
- Andrea Morandi
- [`pdfs/2605.13695_rtlc-research-teach-to-learn-critique-a-three-stage-prompting-paradigm.pdf`](pdfs/2605.13695_rtlc-research-teach-to-learn-critique-a-three-stage-prompting-paradigm.pdf) · [abs](https://arxiv.org/abs/2605.13695)

LLM-as-a-judge is now the default measurement instrument for open-ended generation, but on the public JudgeBench benchmark even strong instruction-tuned judges barely scrape past random on objective-correctness pairwise items. We introduce RTLC, a three-stage prompting recipe -- Research, Teach-to-Learn, Critique -- that promotes a single black-box LLM into an ensemble-of-thought judge with no fine-tuning, retrieval, or external tools. Stage 1 wraps the input in a fixed pedagogical scaffold port…

### AcquisitionSynthesis: Targeted Data Generation using Acquisition Functions
- **2605.13149** · 2026-05-13 · cs.CL
- Ishika Agarwal, Sofia Stoica, Emre Can Acikgoz et al.
- [`pdfs/2605.13149_acquisitionsynthesis-targeted-data-generation-using-acquisition-functi.pdf`](pdfs/2605.13149_acquisitionsynthesis-targeted-data-generation-using-acquisition-functi.pdf) · [abs](https://arxiv.org/abs/2605.13149)

Data quality remains a critical bottleneck in developing capable, competitive models. Researchers have explored many ways to generate top quality samples. Some works rely on rejection sampling: generating lots of synthetic samples and filtering out low-quality samples. Other works rely on larger or closed-source models to extract model weaknesses, necessary skills, or a curriculum off of which to base data generation. These works have one common limitation: there is no quantitative approach to m…

### Fine-Tuning Models for Automated Code Review Feedback
- **2605.12610** · 2026-05-12 · cs.SE
- Smitha S Kumar, Michael A Lones, Manuel Maarek et al.
- [`pdfs/2605.12610_fine-tuning-models-for-automated-code-review-feedback.pdf`](pdfs/2605.12610_fine-tuning-models-for-automated-code-review-feedback.pdf) · [abs](https://arxiv.org/abs/2605.12610)

Large Language Models have introduced new possibilities for programming education through personalized support, content creation, and automated feedback. While recent studies have demonstrated the potential for feedback generation, many techniques rely on proprietary models, raising concerns about cost, computational demands, and the ethical implications of sharing student code. Open LLMs provide an alternative approach, but they do not currently have the capabilities of proprietary models. To a…

### Bidirectional Empowerment of Metamorphic Testing and Large Language Models: A Systematic Survey
- **2605.13898** · 2026-05-12 · cs.SE
- Zheng Zheng, Zenghui Zhou, Yinwang Xu et al.
- [`pdfs/2605.13898_bidirectional-empowerment-of-metamorphic-testing-and-large-language-mo.pdf`](pdfs/2605.13898_bidirectional-empowerment-of-metamorphic-testing-and-large-language-mo.pdf) · [abs](https://arxiv.org/abs/2605.13898)

Large language models (LLMs) have introduced substantial challenges to software quality assurance due to their generative, probabilistic, and open-ended nature, which intensifies the oracle problem and limits the applicability of traditional testing methods. Metamorphic testing (MT), which checks necessary relations among multiple related executions rather than relying on exact expected outputs, has emerged as a promising approach for testing LLMs and other oracle-deficient systems. At the same …

### Characterizing the Failure Modes of LLMs in Resolving Real-World GitHub Issues
- **2605.12270** · 2026-05-12 · cs.SE
- Yanjie Jiang, Yian Huang, Guancheng Wang et al.
- [`pdfs/2605.12270_characterizing-the-failure-modes-of-llms-in-resolving-real-world-githu.pdf`](pdfs/2605.12270_characterizing-the-failure-modes-of-llms-in-resolving-real-world-githu.pdf) · [abs](https://arxiv.org/abs/2605.12270)

Large Language Models (LLMs) are increasingly deployed to resolve real-world GitHub issues. However, despite their potential, the specific failure modes of these models in complex repair tasks remain poorly understood. To characterize how LLM behavior diverges from human developer practices, this paper evaluates three state-of-the-art models, i.e., Claude 4.5 Sonnet, Gemini 3 Pro, and GPT-5, on the SWE-bench Verified dataset. We conduct a rigorous manual analysis of the symptoms and root causes …

### Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge
- **2605.10805** · 2026-05-11 · cs.AI
- Wenbo Zhang, Lijinghua Zhang, Liner Xiang et al.
- [`pdfs/2605.10805_reasoning-is-not-free-robust-adaptive-cost-efficient-routing-for-llm-a.pdf`](pdfs/2605.10805_reasoning-is-not-free-robust-adaptive-cost-efficient-routing-for-llm-a.pdf) · [abs](https://arxiv.org/abs/2605.10805)

Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational…

### Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution
- **2605.11229** · 2026-05-11 · cs.CR
- Neil Fendley, Zhengyu Liu, Aonan Guan et al.
- [`pdfs/2605.11229_comment-and-control-hijacking-agentic-workflows-via-context-grounded-e.pdf`](pdfs/2605.11229_comment-and-control-hijacking-agentic-workflows-via-context-grounded-e.pdf) · [abs](https://arxiv.org/abs/2605.11229)

Automation platforms such as GitHub Actions and n8n are increasingly adopting so-called agentic workflows, which integrate Large Language Model (LLM) agents for tasks such as code review and data synchronization. While bringing convenience for developers, this integration exposes a new risk: An adversary may control and craft certain inputs, such as GitHub issue comments, to manipulate the LLM agent for unwanted actions, such as credential exfiltration and arbitrary command execution. To our kno…

### Grounded Satirical Generation with RAG
- **2605.10853** · 2026-05-11 · cs.CL
- Oona Itkonen, Yuxin Su, Linyao Du et al.
- [`pdfs/2605.10853_grounded-satirical-generation-with-rag.pdf`](pdfs/2605.10853_grounded-satirical-generation-with-rag.pdf) · [abs](https://arxiv.org/abs/2605.10853)

Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for grounded satire generation that uses Retrieval-Augmented Generation (RAG) over current news to produce satirical dictionary definitions in the Finnish context. We also introduce a new task-specific evaluation framework and annotate 100 generated definitions with six human annotator…

### VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection
- **2605.09461** · 2026-05-10 · cs.AI
- Wenxin Tang, Xiang Zhang, Junliang Liu et al.
- [`pdfs/2605.09461_vultriage-triple-path-context-augmentation-for-llm-based-vulnerability.pdf`](pdfs/2605.09461_vultriage-triple-path-context-augmentation-for-llm-based-vulnerability.pdf) · [abs](https://arxiv.org/abs/2605.09461)

Automated vulnerability detection is a fundamental task in software security, yet existing learning-based methods still struggle to capture the structural dependencies, domain-specific vulnerability knowledge, and complex program semantics required for accurate detection. Recent Large Language Models (LLMs) have shown strong code understanding ability, but directly prompting them with raw source code often leads to missed vulnerabilities or false alarms, especially when vulnerable and benign fun…

### SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications
- **2605.09610** · 2026-05-10 · cs.MA
- Abhinav Goel, Agostino Capponi, Alfio Gliozzo et al.
- [`pdfs/2605.09610_smarteval-a-benchmark-for-evaluating-llm-generated-smart-contracts-fro.pdf`](pdfs/2605.09610_smarteval-a-benchmark-for-evaluating-llm-generated-smart-contracts-fro.pdf) · [abs](https://arxiv.org/abs/2605.09610)

We introduce SmartEval, a benchmark for systematically evaluating the quality of Solidity smart contracts generated by large language models (LLMs) from natural language specifications. SmartEval provides a corpus of 9,000 generated contracts paired with expert-written ground-truth implementations drawn from the FSMSCG dataset, a five-dimensional evaluation rubric covering functional completeness, variable fidelity, state-machine correctness, business-logic fidelity, and code quality, and a repr…

### Evaluating LLM-Generated Code: A Benchmark and Developer Study
- **2605.09059** · 2026-05-09 · cs.SE
- Joanna Szych, Anne Schwerk
- [`pdfs/2605.09059_evaluating-llm-generated-code-a-benchmark-and-developer-study.pdf`](pdfs/2605.09059_evaluating-llm-generated-code-a-benchmark-and-developer-study.pdf) · [abs](https://arxiv.org/abs/2605.09059)

Code generation is one of the tasks for which the use of Large Language Models is widely adopted and highly successful. Given this popularity, there are many benchmarks dedicated to code generation that can help select the best model. However, they primarily focus on measuring solution correctness, leaving other aspects, such as code quality and usability, behind. This paper aims to describe a custom tree-fold evaluation methodology for code generated by Large Language Models that bridges this g…

### CREST: Curvature-Regulated Event-Centric Sampling for Efficient Long-Video Understanding
- **2605.09223** · 2026-05-09 · cs.CV
- Mehrajul Abadin Miraj, Abdul Mohaimen Al Radi, Shariful Islam Rayhan et al.
- [`pdfs/2605.09223_crest-curvature-regulated-event-centric-sampling-for-efficient-long-vi.pdf`](pdfs/2605.09223_crest-curvature-regulated-event-centric-sampling-for-efficient-long-vi.pdf) · [abs](https://arxiv.org/abs/2605.09223)

Selecting informative frames from long videos is a combinatorial problem that existing methods address either through efficient heuristics without explicit modeling of query-conditioned temporal structure, or through multi stage retrieval pipelines with substantial preprocessing cost. We propose \textbf{CREST}, a training-free frame selection method grounded in the temporal geometry of query--frame relevance. CREST is based on the observation that relevance over time exhibits structured local va…

### MathlibPR: Pull Request Merge-Readiness Benchmark for Formal Mathematical Libraries
- **2605.07147** · 2026-05-08 · cs.LO
- Zixuan Xie, Xinyu Liu, Shangtong Zhang
- [`pdfs/2605.07147_mathlibpr-pull-request-merge-readiness-benchmark-for-formal-mathematic.pdf`](pdfs/2605.07147_mathlibpr-pull-request-merge-readiness-benchmark-for-formal-mathematic.pdf) · [abs](https://arxiv.org/abs/2605.07147)

The ecosystem of Lean and Mathlib has become the de facto standard for large language model (LLM) assisted formal reasoning with remarkable successes in recent years. Those successes, however, only consume Mathlib as an essential dependency but do not directly contribute to it. In the meantime, the growth of Mathlib has recently been bottlenecked by the review process, which requires human reviewers to judge whether proposed pull requests (PRs) follow the Mathlib's conventions and are worth inte…

### Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software
- **2605.07737** · 2026-05-08 · cs.SE
- Bowei Ning, Xuejun Zong, Lian Lian et al.
- [`pdfs/2605.07737_securing-the-dark-matter-a-semantic-enhanced-neuro-symbolic-framework.pdf`](pdfs/2605.07737_securing-the-dark-matter-a-semantic-enhanced-neuro-symbolic-framework.pdf) · [abs](https://arxiv.org/abs/2605.07737)

Automated vulnerability detection in critical-infrastructure software confronts a fundamental barrier: industrial software is routinely deployed as stripped, symbol-free binaries that deprive conventional Software Composition Analysis of the source-level transparency it requires. Existing binary analysis techniques close this Semantic Gap only partially -- graph-based detectors preserve structural syntax but discard behavioral semantics, while large language models supply rich semantic cues at t…

### Magis-Bench: Evaluating LLMs on Magistrate-Level Legal Tasks
- **2605.08437** · 2026-05-08 · cs.CL
- Ramon Pires, Thales Sales Almeida, Celio Larcher Junior et al.
- [`pdfs/2605.08437_magis-bench-evaluating-llms-on-magistrate-level-legal-tasks.pdf`](pdfs/2605.08437_magis-bench-evaluating-llms-on-magistrate-level-legal-tasks.pdf) · [abs](https://arxiv.org/abs/2605.08437)

Existing benchmarks for legal AI focus primarily on tasks where LLMs must produce legal arguments or documents, yet the capacity to \emph{judge} such arguments -- weighing competing claims, applying doctrine to facts, and rendering reasoned decisions -- is arguably as fundamental to a well-functioning legal system as advocacy itself. We introduce Magis-Bench, a benchmark for evaluating LLMs on magistrate-level writing tasks derived from recent Brazilian competitive examinations for judicial posi…

### ReasonEdit: Towards Interpretable Image Editing Evaluation via Reinforcement Learning
- **2605.07477** · 2026-05-08 · cs.CV
- Honghua Chen, Zitong Xu, Huiyu Duan et al.
- [`pdfs/2605.07477_reasonedit-towards-interpretable-image-editing-evaluation-via-reinforc.pdf`](pdfs/2605.07477_reasonedit-towards-interpretable-image-editing-evaluation-via-reinforc.pdf) · [abs](https://arxiv.org/abs/2605.07477)

Recent text-guided image editing (TIE) models have achieved remarkable progress, however, many edited results still suffer from artifacts, unintended modifications, and suboptimal aesthetics. Although several benchmarks and evaluation methods have been proposed, most existing approaches rely on scalar scores and lack interpretability. This limitation largely stems from the absence of high-quality interpretation datasets for TIE and effective reward models to train interpretable evaluators. To ad…

### Goal-Conditioned Supervised Learning for LLM Fine-Tuning
- **2605.16345** · 2026-05-08 · cs.LG
- Shijun Li, Kaiwen Dong, Xiang Gao et al.
- [`pdfs/2605.16345_goal-conditioned-supervised-learning-for-llm-fine-tuning.pdf`](pdfs/2605.16345_goal-conditioned-supervised-learning-for-llm-fine-tuning.pdf) · [abs](https://arxiv.org/abs/2605.16345)

Large language models often require fine-tuning to better align their behavior with user intent at deployment. Existing approaches are commonly divided into online and offline paradigms. Online methods, such as RL-based alignment, can directly optimize outcome quality but typically rely on external reward models and iterative rollouts, making them costly and difficult to deploy in many cases. Offline methods are more efficient, but prevailing approaches such as supervised fine-tuning (SFT) and d…

### SmellBench: Evaluating LLM Agents on Architectural Code Smell Repair
- **2605.07001** · 2026-05-07 · cs.SE
- Ion George Dinu, Marian Cristian Mihăescu, Traian Rebedea
- [`pdfs/2605.07001_smellbench-evaluating-llm-agents-on-architectural-code-smell-repair.pdf`](pdfs/2605.07001_smellbench-evaluating-llm-agents-on-architectural-code-smell-repair.pdf) · [abs](https://arxiv.org/abs/2605.07001)

Architectural code smells erode software maintainability and are costly to repair manually, yet unlike localized bugs, they require cross-module reasoning about design intent that challenges both developers and automated tools. While large language model agents excel at bug fixing and code-level refactoring, their ability to repair architectural code smells remains unexplored. We present the first empirical evaluation of LLM agents on architectural code smell repair. We contribute SmellBench, a …

### ScarfBench: A Benchmark for Cross-Framework Application Migration in Enterprise Java
- **2605.06754** · 2026-05-07 · cs.SE
- Advait Pavuluri, Bridget McGinn, Ashita Saxena et al.
- [`pdfs/2605.06754_scarfbench-a-benchmark-for-cross-framework-application-migration-in-en.pdf`](pdfs/2605.06754_scarfbench-a-benchmark-for-cross-framework-application-migration-in-en.pdf) · [abs](https://arxiv.org/abs/2605.06754)

Java remains central to enterprise software, and many applications outlive their original architecture. Migrating them across frameworks is a behavior-preserving refactoring spanning build configuration, dependency injection, persistence, request handling, and deployment. Existing software-engineering benchmarks cover bug fixing, feature implementation, and language or version modernization, but leave cross-framework refactoring largely unmeasured. We introduce ScarfBench, a benchmark for behavi…

### Evaluating Non-English Developer Support in Machine Learning for Software Engineering
- **2605.05902** · 2026-05-07 · cs.SE
- Jonathan Katzy, Yongcheng Huang, Gopal-Raj Panchu et al.
- [`pdfs/2605.05902_evaluating-non-english-developer-support-in-machine-learning-for-softw.pdf`](pdfs/2605.05902_evaluating-non-english-developer-support-in-machine-learning-for-softw.pdf) · [abs](https://arxiv.org/abs/2605.05902)

Large Language Models are increasingly used in software engineering, but both code generation and its evaluation remain predominantly English-centric. This leaves a major gap in our understanding of how well current tools support multilingual development, where code contains non-English natural language. In this paper, we investigate non-English code comment generation and the reliability of current methods for evaluating such outputs. We evaluate five code LLMs (CodeGemma, CodeLlama, CodeQwen1.…

### Preference Instability in Reward Models: Detection and Mitigation via Sparse Autoencoders
- **2605.16339** · 2026-05-07 · cs.LG
- Shunchang Liu, Xin Chen, Belen Martin Urcelay et al.
- [`pdfs/2605.16339_preference-instability-in-reward-models-detection-and-mitigation-via-s.pdf`](pdfs/2605.16339_preference-instability-in-reward-models-detection-and-mitigation-via-s.pdf) · [abs](https://arxiv.org/abs/2605.16339)

Preference learning in large language models relies on reward models as proxies for human judgment. However, these models frequently exhibit preference instability, producing contradictory preference assignments in response to subtle, meaning-preserving input variations. We analyze this instability at the representation level under three semantic-preserving perturbation types: paraphrasing, pattern injection, and backdoor triggers. We attribute this instability to over-reliance on predictive yet…

### Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions
- **2605.06279** · 2026-05-07 · cs.SE
- Chengjie Wang, Jingzheng Wu, Xiang Ling et al.
- [`pdfs/2605.06279_correct-code-vulnerable-dependencies-a-large-scale-measurement-study-o.pdf`](pdfs/2605.06279_correct-code-vulnerable-dependencies-a-large-scale-measurement-study-o.pdf) · [abs](https://arxiv.org/abs/2605.06279)

Large language models (LLMs) are now largely involved in software development workflows, and the code they generate routinely includes third-party library (TPL) imports annotated with specific version identifiers. These version choices can carry security and compatibility risks, yet they have not been systematically studied. We present the first large-scale measurement study of version-level risk in LLM-generated Python code, evaluating 10 LLMs on PinTrace, a curated benchmark of 1,000 Stack Ove…

### Exploring the Effectiveness of Abstract Syntax Tree Patterns for Algorithm Recognition
- **2605.06098** · 2026-05-07 · cs.SE
- Denis Neumüller, Florian Sihler, Raphael Straub et al.
- [`pdfs/2605.06098_exploring-the-effectiveness-of-abstract-syntax-tree-patterns-for-algor.pdf`](pdfs/2605.06098_exploring-the-effectiveness-of-abstract-syntax-tree-patterns-for-algor.pdf) · [abs](https://arxiv.org/abs/2605.06098)

The automated recognition of algorithm implementations can support many software maintenance and re-engineering activities by providing knowledge about the concerns present in the code base. Moreover, recognizing inefficient algorithms like Bubble Sort and suggesting superior alternatives from a library can help in assessing and improving the quality of a system. Approaches from related work suffer from usability as well as scalability issues and their accuracy is not evaluated. In this paper, w…

### SiblingRepair: Sibling-Based Multi-Hunk Repair with Large Language Models
- **2605.06209** · 2026-05-07 · cs.SE
- Xinyu Liu, Jiayu Ren, Yusen Wang et al.
- [`pdfs/2605.06209_siblingrepair-sibling-based-multi-hunk-repair-with-large-language-mode.pdf`](pdfs/2605.06209_siblingrepair-sibling-based-multi-hunk-repair-with-large-language-mode.pdf) · [abs](https://arxiv.org/abs/2605.06209)

Developers often make similar mistakes across code locations implementing related functionalities. These locations, called siblings, share similar issues and require similar fixes. Accurately identifying siblings and consistently repairing them are crucial for automated program repair. Hercules is a SOTA technique designed for sibling repair. However, it is limited by strong assumptions about sibling locations and commit-history availability, rigid AST-based sibling matching, and inflexible temp…

### Pest-Thinker: Learning to Think and Reason like Entomologists via Reinforcement Learning
- **2605.06121** · 2026-05-07 · cs.CV
- Xueheng Li, Yu Wang, Tao Hu et al.
- [`pdfs/2605.06121_pest-thinker-learning-to-think-and-reason-like-entomologists-via-reinf.pdf`](pdfs/2605.06121_pest-thinker-learning-to-think-and-reason-like-entomologists-via-reinf.pdf) · [abs](https://arxiv.org/abs/2605.06121)

Pest-induced crop losses pose a major threat to global food security and sustainable agricultural development. While recent advances in Multimodal Large Language Models (MLLMs) have shown strong potential for visual understanding and smart agriculture, their direct application to pest recognition remains limited due to the domain's unique challenges such as high inter-species complexity, intra-species variability, and the scarcity of expert-annotated data. In this work, we introduce Pest-Thinker…

### Joint Consistency: A Unified Test-Time Aggregation Framework via Energy Minimization
- **2605.06219** · 2026-05-07 · cs.AI
- Yunzhen Yao, Hongye Wang, Yahong Wang et al.
- [`pdfs/2605.06219_joint-consistency-a-unified-test-time-aggregation-framework-via-energy.pdf`](pdfs/2605.06219_joint-consistency-a-unified-test-time-aggregation-framework-via-energy.pdf) · [abs](https://arxiv.org/abs/2605.06219)

This paper studies test-time aggregation, an approach that generates multiple reasoning traces and aggregates them into a final answer. Most existing methods rely on evaluation signals collected from candidate traces in isolation or answer frequencies, while ignoring comparative interactions among candidates. We propose Joint Consistency (JC), formulated as a constrained Ising-type energy minimization problem, where independent evaluation signals act as external fields and pairwise comparisons a…

### Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges
- **2605.06161** · 2026-05-07 · cs.AI
- Shihao Weng, Yang Feng, Xiaofei Xie
- [`pdfs/2605.06161_beyond-accuracy-policy-invariance-as-a-reliability-test-for-llm-safety.pdf`](pdfs/2605.06161_beyond-accuracy-policy-invariance-as-a-reliability-test-for-llm-safety.pdf) · [abs](https://arxiv.org/abs/2605.06161)

LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens to be worded. We argue that any trustworthy safety judge must satisfy a basic property we call policy invariance, and we operationalize it as three testable principles: rubric-semantics invariance under certified-equivalent rewrites, rub…

### Patterns of Developer Adoption of LLM-Generated Code Refactoring Suggestions
- **2605.04835** · 2026-05-06 · cs.SE
- David Schön, Faiza Amjad, Tehreem Asif et al.
- [`pdfs/2605.04835_patterns-of-developer-adoption-of-llm-generated-code-refactoring-sugge.pdf`](pdfs/2605.04835_patterns-of-developer-adoption-of-llm-generated-code-refactoring-sugge.pdf) · [abs](https://arxiv.org/abs/2605.04835)

Large language models (LLMs) have gained widespread popularity and have steadily improved over time, enabling software developers to use them for various code-related tasks. One common task is code refactoring, where the LLM suggests changes for the developer to apply to their code to improve quality attributes such as readability or maintainability. While current research focuses on evaluating LLM-generated refactoring suggestions, there is a limited understanding of how developers apply these …

### Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code
- **2605.05267** · 2026-05-06 · cs.SE
- Kaifeng He, Xiaojun Zhang, Peiliang Cai et al.
- [`pdfs/2605.05267_bridging-generation-and-training-a-systematic-review-of-quality-issues.pdf`](pdfs/2605.05267_bridging-generation-and-training-a-systematic-review-of-quality-issues.pdf) · [abs](https://arxiv.org/abs/2605.05267)

Large language models (LLMs) frequently generate defective outputs in code generation tasks, ranging from logical bugs to security vulnerabilities. While these generation failures are often treated as model-level limitations, empirical evidence increasingly traces their root causes to imperfections within the training corpora. Yet, the specific mechanisms linking training data quality issues to generated code quality issues remain largely unmapped. This paper presents a systematic literature rev…

### CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement
- **2605.04677** · 2026-05-06 · cs.SE
- Ajay Krishna Borra, Wenzhuo Yang, Samarth Arora et al.
- [`pdfs/2605.04677_codeevolve-llm-driven-evolutionary-optimization-with-runtime-enriched.pdf`](pdfs/2605.04677_codeevolve-llm-driven-evolutionary-optimization-with-runtime-enriched.pdf) · [abs](https://arxiv.org/abs/2605.04677)

We present CodeEvolve, an evolutionary framework for improving program performance and code quality with Large Language Models (LLMs). CodeEvolve extends OpenEvolve with runtime-guided target selection, Monte Carlo Tree Search (MCTS), automated code refinement, and language-specific evaluation pipelines for Java and Salesforce Apex. The system uses Java Flight Recorder (JFR) profiles to build weighted component graphs and select optimization targets that account for most execution cost, reducing…

### DiffCap-Bench: A Comprehensive, Challenging, Robust Benchmark for Image Difference Captioning
- **2605.04503** · 2026-05-06 · cs.CV
- Yuancheng Wei, Haojie Zhang, Linli Yao et al.
- [`pdfs/2605.04503_diffcap-bench-a-comprehensive-challenging-robust-benchmark-for-image-d.pdf`](pdfs/2605.04503_diffcap-bench-a-comprehensive-challenging-robust-benchmark-for-image-d.pdf) · [abs](https://arxiv.org/abs/2605.04503)

Image Difference Captioning (IDC) generates natural language descriptions that precisely identify differences between two images, serving as a key benchmark for fine-grained change perception, cross-modal reasoning, and image editing data construction. However, existing benchmarks lack diversity and compositional complexity, and standard lexical-overlap metrics (e.g., BLEU, METEOR) fail to capture semantic consistency or penalize hallucinations, which together prevent a comprehensive and robust …

### StoryAlign: Evaluating and Training Reward Models for Story Generation
- **2605.04831** · 2026-05-06 · cs.CL
- Haotian Xia, Hao Peng, Yunjia Qi et al.
- [`pdfs/2605.04831_storyalign-evaluating-and-training-reward-models-for-story-generation.pdf`](pdfs/2605.04831_storyalign-evaluating-and-training-reward-models-for-story-generation.pdf) · [abs](https://arxiv.org/abs/2605.04831)

Story generation aims to automatically produce coherent, structured, and engaging narratives. Although large language models (LLMs) have significantly advanced text generation, stories generated by LLMs still diverge from human-authored works regarding complex narrative structure and human-aligned preferences. A key reason is the absence of effective modeling of human story preferences, which are inherently subjective and under-explored. In this work, we systematically evaluate the modeling of h…

### The Single-File Test: A Longitudinal Public-Interface Evaluation of First-Output LLM Web Generation with Social Reach Tracking
- **2605.06707** · 2026-05-06 · cs.SE
- Diego Cabezas Palacios
- [`pdfs/2605.06707_the-single-file-test-a-longitudinal-public-interface-evaluation-of-fir.pdf`](pdfs/2605.06707_the-single-file-test-a-longitudinal-public-interface-evaluation-of-fir.pdf) · [abs](https://arxiv.org/abs/2605.06707)

This paper presents an eight-week observational comparison of 68 single-file HTML generations collected across 17 public experiments in the "HTML AI Battle" project between December 10, 2025 and February 4, 2026. Four reasoning model families, GPT, Gemini, Grok, and Claude, were compared under a fixed public-interface protocol with no custom instructions, no personality tuning, and no repair prompts. Each output was evaluated from a rendered browser video using human scores and a Gemini LLM-as-a…

### BIT.UA-AAUBS at ArchEHR-QA 2026: Evaluating Open-Source and Proprietary LLMs via Prompting in Low-Resource QA
- **2605.03618** · 2026-05-05 · cs.CL
- Richard A. A. Jonker, Alexander Christiansen, Alexandros Maniatis et al.
- [`pdfs/2605.03618_bit-ua-aaubs-at-archehr-qa-2026-evaluating-open-source-and-proprietary.pdf`](pdfs/2605.03618_bit-ua-aaubs-at-archehr-qa-2026-evaluating-open-source-and-proprietary.pdf) · [abs](https://arxiv.org/abs/2605.03618)

This paper presents the joint participation of the BIT.UA and AAUBS groups in the ArchEHR-QA 2026 shared task, which focuses on clinical question answering and evidence grounding in a low-resource setting. Due to the absence of training data and the strict data privacy constraints inherent to the healthcare domain (e.g. GDPR), we investigate the capabilities of Large Language Models (LLMs) without weight updates. We evaluate several state-of-the-art proprietary models and locally deployable open…

### UCSC-NLP at SemEval-2026 Task 13: Multi-View Generalization and Diagnostic Analysis of Machine-Generated Code Detection
- **2604.26990** · 2026-04-28 · cs.SE
- Kargi Chauhan, Sadiba Nusrat Nur
- [`pdfs/2604.26990_ucsc-nlp-at-semeval-2026-task-13-multi-view-generalization-and-diagnos.pdf`](pdfs/2604.26990_ucsc-nlp-at-semeval-2026-task-13-multi-view-generalization-and-diagnos.pdf) · [abs](https://arxiv.org/abs/2604.26990)

With the rapid growth of large language models for code generation, distinguishing between human-written and AI-generated code has become increasingly critical for academic integrity, hiring evaluations, and software security. We present our system for SemEval-2026 Task 13: Multilingual Machine-Generated Code Detection, participating in Subtask A (binary detection) and Subtask B (multi-class attribution across 10 LLM families). For Subtask A, we fine-tune UniXcoder-base with a multi-view trainin…

### AI-Assisted Code Review as a Scaffold for Code Quality and Self-Regulated Learning: An Experience Report
- **2604.23251** · 2026-04-25 · cs.SE
- Eduardo Oliveira, Michael Fu, Patanamon Thongtanunam et al.
- [`pdfs/2604.23251_ai-assisted-code-review-as-a-scaffold-for-code-quality-and-self-regula.pdf`](pdfs/2604.23251_ai-assisted-code-review-as-a-scaffold-for-code-quality-and-self-regula.pdf) · [abs](https://arxiv.org/abs/2604.23251)

Code review is central to software engineering education but hard to scale in capstone projects due to tight deadlines, uneven peer feedback, and limited prior experience. We investigate an LLM-as-reviewer integrated directly into GitHub pull requests (human-in-the-loop) across two cohorts (more than 100 students, 2023--2024). Using a mixed-methods design -- GitHub data, reflective reports, and a targeted survey -- we examine engagement and responsiveness as behavioral indicators of self-regulat…

### LLMSniffer: Detecting LLM-Generated Code via GraphCodeBERT and Supervised Contrastive Learning
- **2604.16058** · 2026-04-17 · cs.SE
- Mahir Labib Dihan, Abir Muhtasim
- [`pdfs/2604.16058_llmsniffer-detecting-llm-generated-code-via-graphcodebert-and-supervis.pdf`](pdfs/2604.16058_llmsniffer-detecting-llm-generated-code-via-graphcodebert-and-supervis.pdf) · [abs](https://arxiv.org/abs/2604.16058)

The rapid proliferation of Large Language Models (LLMs) in software development has made distinguishing AI-generated code from human-written code a critical challenge with implications for academic integrity, code quality assurance, and software security. We present LLMSniffer, a detection framework that fine-tunes GraphCodeBERT using a two-stage supervised contrastive learning pipeline augmented with comment removal preprocessing and an MLP classifier. Evaluated on two benchmark datasets - GPTS…

### Structured Safety Auditing for Balancing Code Correctness and Content Safety in LLM-Generated Code
- **2604.12088** · 2026-04-13 · cs.SE
- Honghao Tan, Haibo Wang, Shin Hwei Tan
- [`pdfs/2604.12088_structured-safety-auditing-for-balancing-code-correctness-and-content.pdf`](pdfs/2604.12088_structured-safety-auditing-for-balancing-code-correctness-and-content.pdf) · [abs](https://arxiv.org/abs/2604.12088)

Large language models (LLMs) for code generation are typically evaluated on functional correctness alone, overlooking whether generated code propagates harmful content embedded in the prompt. Prior work has shown that most Code LLMs reproduce offensive identifiers from injected renaming instructions without warning, yet existing approaches focus on detecting harmful content, neglecting functional correctness. Grounded in the Theory of Dual Channel Constraints (which states that code is a dual-ch…

### DynamicsLLM: a Dynamic Analysis-based Tool for Generating Intelligent Execution Traces Using LLMs to Detect Android Behavioural Code Smells
- **2604.10661** · 2026-04-12 · cs.SE
- Houcine Abdelkader Cherief, Florent Avellaneda, Naouel Moha
- [`pdfs/2604.10661_dynamicsllm-a-dynamic-analysis-based-tool-for-generating-intelligent-e.pdf`](pdfs/2604.10661_dynamicsllm-a-dynamic-analysis-based-tool-for-generating-intelligent-e.pdf) · [abs](https://arxiv.org/abs/2604.10661)

Mobile apps have become essential of our daily lives, making code quality a critical concern for developers. Behavioural code smells are characteristics in the source code that induce inappropriate code behaviour during execution, which negatively impact software quality in terms of performance, energy consumption, and memory. Dynamics, the latest state-of-the-art tool-based method, is highly effective at detecting Android behavioural code smells. While it outperforms static analysis tools, it s…

### Bigger Isn't Always Better: A Comparative Evaluation of LLMs for Automated Code Review
- **2606.15689** · 2026-04-09 · cs.SE
- Shivam Pankaj Kumar, Swati Bararia, Kislay Raj
- [`pdfs/2606.15689_bigger-isn-t-always-better-a-comparative-evaluation-of-llms-for-automa.pdf`](pdfs/2606.15689_bigger-isn-t-always-better-a-comparative-evaluation-of-llms-for-automa.pdf) · [abs](https://arxiv.org/abs/2606.15689)

We present a systematic evaluation of five large language models on automated code review, comparing Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.4 mini, Minimax M2.7, and GLM-5 Turbo across 150 code review samples - 100 synthetic mutation-injected bugs and 50 real bug-fix pull requests mined from eight major open-source repositories. Our principal finding is that Claude Haiku 4.5, a smaller and cheaper model, consistently outperforms the larger Claude Sonnet 4.6, achieving higher F1 (0.365 vs. 0.…

### SWE-PRBench: Benchmarking AI Code Review Quality Against Pull Request Feedback
- **2603.26130** · 2026-03-27 · cs.SE
- Deepak Kumar
- [`pdfs/2603.26130_swe-prbench-benchmarking-ai-code-review-quality-against-pull-request-f.pdf`](pdfs/2603.26130_swe-prbench-benchmarking-ai-code-review-quality-against-pull-request-f.pdf) · [abs](https://arxiv.org/abs/2603.26130)

We introduce SWE-PRBench, a benchmark of 350 pull requests with human-annotated ground truth for evaluating AI code review quality. Evaluated against an LLM-as-judge framework validated at kappa=0.75, 8 frontier models detect only 15-31% of human-flagged issues on the diff-only configuration, demonstrating that AI code review remains far below human expert performance despite strong results on code generation benchmarks. Pull requests are drawn from active open-source repositories, filtered from…

### Factors Influencing the Quality of AI-Generated Code: A Synthesis of Empirical Evidence
- **2603.25146** · 2026-03-26 · cs.SE
- Vehid Geruslu, Zulfiyya Aliyeva, Eray Tüzün
- [`pdfs/2603.25146_factors-influencing-the-quality-of-ai-generated-code-a-synthesis-of-em.pdf`](pdfs/2603.25146_factors-influencing-the-quality-of-ai-generated-code-a-synthesis-of-em.pdf) · [abs](https://arxiv.org/abs/2603.25146)

Context: The rapid adoption of AI-assisted code generation tools, such as large language models (LLMs), is transforming software development practices. While these tools promise significant productivity gains, concerns regarding the quality, reliability, and security of AI-generated code are increasingly reported in both academia and industry. --Objective: This study aims to systematically synthesize existing empirical evidence on the factors influencing the quality of AI-generated source code a…

### Gendered Prompting and LLM Code Review: How Gender Cues in the Prompt Shape Code Quality and Evaluation
- **2603.24359** · 2026-03-25 · cs.SE
- Lynn Janzen, Üveys Eroglu, Dorothea Kolossa et al.
- [`pdfs/2603.24359_gendered-prompting-and-llm-code-review-how-gender-cues-in-the-prompt-s.pdf`](pdfs/2603.24359_gendered-prompting-and-llm-code-review-how-gender-cues-in-the-prompt-s.pdf) · [abs](https://arxiv.org/abs/2603.24359)

LLMs are increasingly embedded in programming workflows, from code generation to automated code review. Yet, how gendered communication styles interact with LLM-assisted programming and code review remains underexplored. We present a mixed-methods pilot study examining whether gender-related linguistic differences in prompts influence code generation outcomes and code review decisions. Across three complementary studies, we analyze (i) collected real-world coding prompts, (ii) a controlled user …

### More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests
- **2601.21276** · 2026-01-29 · cs.SE
- Haoming Huang, Pongchai Jaisri, Shota Shimizu et al.
- [`pdfs/2601.21276_more-code-less-reuse-investigating-code-quality-and-reviewer-sentiment.pdf`](pdfs/2601.21276_more-code-less-reuse-investigating-code-quality-and-reviewer-sentiment.pdf) · [abs](https://arxiv.org/abs/2601.21276)

Large Language Model (LLM) Agents are advancing quickly, with the increasing leveraging of LLM Agents to assist in development tasks such as code generation. While LLM Agents accelerate code generation, studies indicate they may introduce adverse effects on development. However, existing metrics solely measure pass rates, failing to reflect impacts on long-term maintainability and readability, and failing to capture human intuitive evaluations of PR. To increase the comprehensiveness of this pro…

### HalluJudge: A Reference-Free Hallucination Detection for Context Misalignment in Code Review Automation
- **2601.19072** · 2026-01-27 · cs.SE
- Kla Tantithamthavorn, Hong Yi Lin, Patanamon Thongtanunam et al.
- [`pdfs/2601.19072_hallujudge-a-reference-free-hallucination-detection-for-context-misali.pdf`](pdfs/2601.19072_hallujudge-a-reference-free-hallucination-detection-for-context-misali.pdf) · [abs](https://arxiv.org/abs/2601.19072)

Large Language models (LLMs) have shown strong capabilities in code review automation, such as review comment generation, yet they suffer from hallucinations -- where the generated review comments are ungrounded in the actual code -- poses a significant challenge to the adoption of LLMs in code review workflows. To address this, we explore effective and scalable methods for a hallucination detection in LLM-generated code review comments without the reference. In this work, we design HalluJudge t…

### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
- **2601.19264** · 2026-01-27 · cs.SE
- Syed Mehedi Hasan Nirob, Shamim Ehsan, Moqsadur Rahman et al.
- [`pdfs/2601.19264_whitespaces-don-t-lie-feature-driven-and-embedding-based-approaches-fo.pdf`](pdfs/2601.19264_whitespaces-don-t-lie-feature-driven-and-embedding-based-approaches-fo.pdf) · [abs](https://arxiv.org/abs/2601.19264)

Large language models (LLMs) have made it remarkably easy to synthesize plausible source code from natural language prompts. While this accelerates software development and supports learning, it also raises new risks for academic integrity, authorship attribution, and responsible AI use. This paper investigates the problem of distinguishing human-written from machine-generated code by comparing two complementary approaches: feature-based detectors built from lightweight, interpretable stylometri…

### Beyond Strict Rules: Assessing the Effectiveness of Large Language Models for Code Smell Detection
- **2601.09873** · 2026-01-14 · cs.SE
- Saymon Souza, Amanda Santana, Eduardo Figueiredo et al.
- [`pdfs/2601.09873_beyond-strict-rules-assessing-the-effectiveness-of-large-language-mode.pdf`](pdfs/2601.09873_beyond-strict-rules-assessing-the-effectiveness-of-large-language-mode.pdf) · [abs](https://arxiv.org/abs/2601.09873)

Code smells are symptoms of potential code quality problems that may affect software maintainability, thus increasing development costs and impacting software reliability. Large language models (LLMs) have shown remarkable capabilities for supporting various software engineering activities, but their use for detecting code smells remains underexplored. However, unlike the rigid rules of static analysis tools, LLMs can support flexible and adaptable detection strategies tailored to the unique pro…

### RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian
- **2601.01129** · 2026-01-03 · cs.SE
- Kla Tantithamthavorn, Yaotian Zou, Andy Wong et al.
- [`pdfs/2601.01129_rovodev-code-reviewer-a-large-scale-online-evaluation-of-llm-based-cod.pdf`](pdfs/2601.01129_rovodev-code-reviewer-a-large-scale-online-evaluation-of-llm-based-cod.pdf) · [abs](https://arxiv.org/abs/2601.01129)

Large Language Models (LLMs)-powered code review automation has the potential to transform code review workflows. Despite the advances of LLM-powered code review comment generation approaches, several practical challenges remain for designing enterprise-grade code review automation tools. In particular, this paper aims at answering the practical question: how can we design a review-guided, context-aware, quality-checked code review comment generation without fine-tuning? In this paper, we presen…

### AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration
- **2512.20159** · 2025-12-23 · cs.SE
- Ruiqi Wang, Xinchen Wang, Cuiyun Gao et al.
- [`pdfs/2512.20159_axiom-benchmarking-llm-as-a-judge-for-code-via-rule-based-perturbation.pdf`](pdfs/2512.20159_axiom-benchmarking-llm-as-a-judge-for-code-via-rule-based-perturbation.pdf) · [abs](https://arxiv.org/abs/2512.20159)

Large language models (LLMs) have been increasingly deployed in real-world software engineering, fostering the development of code evaluation metrics to study the quality of LLM-generated code. Conventional rule-based metrics merely score programs based on their surface-level similarities with reference programs instead of analyzing functionality and code quality in depth. To address this limitation, researchers have developed LLM-as-a-judge metrics, prompting LLMs to evaluate and score code, an…

### A Causal Perspective on Measuring, Explaining and Mitigating Smells in LLM-Generated Code
- **2511.15817** · 2025-11-19 · cs.SE
- Alejandro Velasco, Daniel Rodriguez-Cardenas, Dipin Khati et al.
- [`pdfs/2511.15817_a-causal-perspective-on-measuring-explaining-and-mitigating-smells-in.pdf`](pdfs/2511.15817_a-causal-perspective-on-measuring-explaining-and-mitigating-smells-in.pdf) · [abs](https://arxiv.org/abs/2511.15817)

Recent advances in large language models (LLMs) have accelerated their adoption in software engineering contexts. However, concerns persist about the structural quality of the code they produce. In particular, LLMs often replicate poor coding practices, introducing code smells (i.e., patterns that hinder readability, maintainability, or design integrity). Although prior research has examined the detection or repair of smells, we still lack a clear understanding of how and when these issues emerg…

### Benchmarking LLMs for Fine-Grained Code Review with Enriched Context in Practice
- **2511.07017** · 2025-11-10 · cs.SE
- Ruida Hu, Xinchen Wang, Xin-Cheng Wen et al.
- [`pdfs/2511.07017_benchmarking-llms-for-fine-grained-code-review-with-enriched-context-i.pdf`](pdfs/2511.07017_benchmarking-llms-for-fine-grained-code-review-with-enriched-context-i.pdf) · [abs](https://arxiv.org/abs/2511.07017)

Code review is a cornerstone of software quality assurance, and recent advances in Large Language Models (LLMs) have shown promise in its automation. However, existing benchmarks for LLM-based code review face three major limitations. Lack of semantic context: most benchmarks provide only code diffs without textual information such as issue descriptions, which are crucial for understanding developer intent. Data quality issues: without rigorous validation, many samples are noisy-e.g., reviews on…

### Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection
- **2510.02934** · 2025-10-03 · cs.SE
- Thanh Trong Vu, Tuan-Dung Bui, Thu-Trang Nguyen et al.
- [`pdfs/2510.02934_model-agnostic-correctness-assessment-for-llm-generated-code-via-dynam.pdf`](pdfs/2510.02934_model-agnostic-correctness-assessment-for-llm-generated-code-via-dynam.pdf) · [abs](https://arxiv.org/abs/2510.02934)

Large Language Models (LLMs) have demonstrated impressive capabilities in code generation and are increasingly integrated into the software development process. However, ensuring the correctness of LLM-generated code remains a critical concern. Prior work has shown that the internal representations of LLMs encode meaningful signals for assessing code correctness. Nevertheless, the existing methods rely on representations from pre-selected/fixed layers and token positions, which could limit its g…

### Developer-LLM Conversations: An Empirical Study of Interactions and Generated Code Quality
- **2509.10402** · 2025-09-12 · cs.SE
- Suzhen Zhong, Ying Zou, Bram Adams
- [`pdfs/2509.10402_developer-llm-conversations-an-empirical-study-of-interactions-and-gen.pdf`](pdfs/2509.10402_developer-llm-conversations-an-empirical-study-of-interactions-and-gen.pdf) · [abs](https://arxiv.org/abs/2509.10402)

Large Language Models (LLMs) are becoming integral to modern software development workflows, assisting developers with code generation, API explanation, and iterative problem-solving through natural language conversations. Despite widespread adoption, there is limited understanding of how developers interact with LLMs in practice and how these conversational dynamics influence task outcomes, code quality, and software engineering workflows. To address this, we leverage CodeChat, a large dataset …

### Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis
- **2508.14727** · 2025-08-20 · cs.SE
- Abbas Sabra, Olivier Schmitt, Joseph Tyler
- [`pdfs/2508.14727_assessing-the-quality-and-security-of-ai-generated-code-a-quantitative.pdf`](pdfs/2508.14727_assessing-the-quality-and-security-of-ai-generated-code-a-quantitative.pdf) · [abs](https://arxiv.org/abs/2508.14727)

This study presents a quantitative evaluation of the code quality and security of five prominent Large Language Models (LLMs): Claude Sonnet 4, Claude 3.7 Sonnet, GPT-4o, Llama 3.2 90B, and OpenCoder 8B. While prior research has assessed the functional performance of LLM-generated code, this research tested LLM output from 4,442 Java coding assignments through comprehensive static analysis using SonarQube. The findings suggest that although LLMs can generate functional code, they also introduce …

### Static Analysis as a Feedback Loop: Enhancing LLM-Generated Code Beyond Correctness
- **2508.14419** · 2025-08-20 · cs.SE
- Scott Blyth, Sherlock A. Licorish, Christoph Treude et al.
- [`pdfs/2508.14419_static-analysis-as-a-feedback-loop-enhancing-llm-generated-code-beyond.pdf`](pdfs/2508.14419_static-analysis-as-a-feedback-loop-enhancing-llm-generated-code-beyond.pdf) · [abs](https://arxiv.org/abs/2508.14419)

Large language models (LLMs) have demonstrated impressive capabilities in code generation, achieving high scores on benchmarks such as HumanEval and MBPP. However, these benchmarks primarily assess functional correctness and neglect broader dimensions of code quality, including security, reliability, readability, and maintainability. In this work, we systematically evaluate the ability of LLMs to generate high-quality code across multiple dimensions using the PythonSecurityEval benchmark. We int…

### Is LLM-Generated Code More Maintainable \& Reliable than Human-Written Code?
- **2508.00700** · 2025-08-01 · cs.SE
- Alfred Santa Molison, Marcia Moraes, Glaucia Melo et al.
- [`pdfs/2508.00700_is-llm-generated-code-more-maintainable-reliable-than-human-written-co.pdf`](pdfs/2508.00700_is-llm-generated-code-more-maintainable-reliable-than-human-written-co.pdf) · [abs](https://arxiv.org/abs/2508.00700)

Background: The rise of Large Language Models (LLMs) in software development has opened new possibilities for code generation. Despite the widespread use of this technology, it remains unclear how well LLMs generate code solutions in terms of software quality and how they compare to human-written code. Aims: This study compares the internal quality attributes of LLM-generated and human-written code. Method: Our empirical study integrates datasets of coding tasks, three LLM configurations (zero-s…

### Automated Code Review Using Large Language Models with Symbolic Reasoning
- **2507.18476** · 2025-07-24 · cs.SE
- Busra Icoz, Goksel Biricik
- [`pdfs/2507.18476_automated-code-review-using-large-language-models-with-symbolic-reason.pdf`](pdfs/2507.18476_automated-code-review-using-large-language-models-with-symbolic-reason.pdf) · [abs](https://arxiv.org/abs/2507.18476)

Code review is one of the key processes in the software development lifecycle and is essential to maintain code quality. However, manual code review is subjective and time consuming. Given its rule-based nature, code review is well suited for automation. In recent years, significant efforts have been made to automate this process with the help of artificial intelligence. Recent developments in Large Language Models (LLMs) have also emerged as a promising tool in this area, but these models often…

### Detecting LLM-generated Code with Subtle Modification by Adversarial Training
- **2507.13123** · 2025-07-17 · cs.SE
- Xin Yin, Xinrui Li, Chao Ni et al.
- [`pdfs/2507.13123_detecting-llm-generated-code-with-subtle-modification-by-adversarial-t.pdf`](pdfs/2507.13123_detecting-llm-generated-code-with-subtle-modification-by-adversarial-t.pdf) · [abs](https://arxiv.org/abs/2507.13123)

With the rapid development of Large Language Models (LLMs), their powerful code-generation capabilities have been widely applied in tasks like code completion and automated development, demonstrating the value of improving coding efficiency. However, the extensive use of LLM-generated code also raises several new challenges. On the one hand, issues such as the regulation of code provenance, copyright disputes, and code quality have become increasingly concerning. How to effectively detect LLM-ge…

### SwiftEval: Developing a Language-Specific Benchmark for LLM-generated Code Evaluation
- **2505.24324** · 2025-05-30 · cs.LG
- Ivan Petrukha, Yana Kurliak, Nataliia Stulova
- [`pdfs/2505.24324_swifteval-developing-a-language-specific-benchmark-for-llm-generated-c.pdf`](pdfs/2505.24324_swifteval-developing-a-language-specific-benchmark-for-llm-generated-c.pdf) · [abs](https://arxiv.org/abs/2505.24324)

In recent years, large language models (LLMs) have showcased significant advancements in code generation. However, most evaluation benchmarks are primarily oriented towards Python, making it difficult to evaluate other programming languages, such as Swift, with high quality. By examining widely established multilingual benchmarks like HumanEval-XL and MultiPL-E, we identified critical issues specific to their Swift components, making them insufficient or even irrelevant for assessing LLM coding …

### MCTS-Judge: Test-Time Scaling in LLM-as-a-Judge for Code Correctness Evaluation
- **2502.12468** · 2025-02-18 · cs.LG
- Yutong Wang, Pengliang Ji, Chaoqun Yang et al.
- [`pdfs/2502.12468_mcts-judge-test-time-scaling-in-llm-as-a-judge-for-code-correctness-ev.pdf`](pdfs/2502.12468_mcts-judge-test-time-scaling-in-llm-as-a-judge-for-code-correctness-ev.pdf) · [abs](https://arxiv.org/abs/2502.12468)

The LLM-as-a-Judge paradigm shows promise for evaluating generative content but lacks reliability in reasoning-intensive scenarios, such as programming. Inspired by recent advances in reasoning models and shifts in scaling laws, we pioneer bringing test-time computation into LLM-as-a-Judge, proposing MCTS-Judge, a resource-efficient, System-2 thinking framework for code correctness evaluation. MCTS-Judge leverages Monte Carlo Tree Search (MCTS) to decompose problems into simpler, multi-perspecti…

### Bridging LLM-Generated Code and Requirements: Reverse Generation technique and SBC Metric for Developer Insights
- **2502.07835** · 2025-02-11 · cs.SE
- Ahilan Ayyachamy Nadar Ponnusamy
- [`pdfs/2502.07835_bridging-llm-generated-code-and-requirements-reverse-generation-techni.pdf`](pdfs/2502.07835_bridging-llm-generated-code-and-requirements-reverse-generation-techni.pdf) · [abs](https://arxiv.org/abs/2502.07835)

The rise of Large Language Models (LLMs) in software engineering, particularly in code generation, has garnered significant attention. However, assessing the quality of AI-generated code remains a challenge due to the inherent complexity of programming tasks and the lack of robust evaluation metrics that align well with human judgment. Traditional token-based metrics such as BLEU and ROUGE, while commonly used in natural language processing, exhibit weak correlations with human assessments in co…

### BitsAI-CR: Automated Code Review via LLM in Practice
- **2501.15134** · 2025-01-25 · cs.SE
- Tao Sun, Jian Xu, Yuanpeng Li et al.
- [`pdfs/2501.15134_bitsai-cr-automated-code-review-via-llm-in-practice.pdf`](pdfs/2501.15134_bitsai-cr-automated-code-review-via-llm-in-practice.pdf) · [abs](https://arxiv.org/abs/2501.15134)

Code review remains a critical yet resource-intensive process in software development, particularly challenging in large-scale industrial environments. While Large Language Models (LLMs) show promise for automating code review, existing solutions face significant limitations in precision and practicality. This paper presents BitsAI-CR, an innovative framework that enhances code review through a two-stage approach combining RuleChecker for initial issue detection and ReviewFilter for precision ve…

### CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models
- **2501.03288** · 2025-01-06 · cs.SE
- Zhenyu Xu, Victor S. Sheng
- [`pdfs/2501.03288_codevision-detecting-llm-generated-code-using-2d-token-probability-map.pdf`](pdfs/2501.03288_codevision-detecting-llm-generated-code-using-2d-token-probability-map.pdf) · [abs](https://arxiv.org/abs/2501.03288)

The rise of large language models (LLMs) like ChatGPT has significantly improved automated code generation, enhancing software development efficiency. However, this introduces challenges in academia, particularly in distinguishing between human-written and LLM-generated code, which complicates issues of academic integrity. Existing detection methods, such as pre-trained models and watermarking, face limitations in adaptability and computational efficiency. In this paper, we propose a novel detec…

### Automated Code Review In Practice
- **2412.18531** · 2024-12-24 · cs.SE
- Umut Cihan, Vahid Haratian, Arda İçöz et al.
- [`pdfs/2412.18531_automated-code-review-in-practice.pdf`](pdfs/2412.18531_automated-code-review-in-practice.pdf) · [abs](https://arxiv.org/abs/2412.18531)

Code review is a widespread practice to improve software quality and transfer knowledge. It is often seen as time-consuming due to the need for manual effort and potential delays. Several AI-assisted tools, such as Qodo, GitHub Copilot, and Coderabbit, provide automated reviews using large language models (LLMs). The effects of such tools in the industry are yet to be examined. This study examines the impact of LLM-based automated code review tools in an industrial setting. The study was conduct…

### Prompting and Fine-tuning Large Language Models for Automated Code Review Comment Generation
- **2411.10129** · 2024-11-15 · cs.SE
- Md. Asif Haider, Ayesha Binte Mostofa, Sk. Sabit Bin Mosaddek et al.
- [`pdfs/2411.10129_prompting-and-fine-tuning-large-language-models-for-automated-code-rev.pdf`](pdfs/2411.10129_prompting-and-fine-tuning-large-language-models-for-automated-code-rev.pdf) · [abs](https://arxiv.org/abs/2411.10129)

Generating accurate code review comments remains a significant challenge due to the inherently diverse and non-unique nature of the task output. Large language models pretrained on both programming and natural language data tend to perform well in code-oriented tasks. However, large-scale pretraining is not always feasible due to its environmental impact and project-specific generalizability issues. In this work, first we fine-tune open-source Large language models (LLM) in parameter-efficient, …

### DeVAIC: A Tool for Security Assessment of AI-generated Code
- **2404.07548** · 2024-04-11 · cs.SE
- Domenico Cotroneo, Roberta De Luca, Pietro Liguori
- [`pdfs/2404.07548_devaic-a-tool-for-security-assessment-of-ai-generated-code.pdf`](pdfs/2404.07548_devaic-a-tool-for-security-assessment-of-ai-generated-code.pdf) · [abs](https://arxiv.org/abs/2404.07548)

Context: AI code generators are revolutionizing code writing and software development, but their training on large datasets, including potentially untrusted source code, raises security concerns. Furthermore, these generators can produce incomplete code snippets that are challenging to evaluate using current solutions. Objective: This research work introduces DeVAIC (Detection of Vulnerabilities in AI-generated Code), a tool to evaluate the security of AI-generated Python code, which overcomes t…

### Improving Automated Code Reviews: Learning from Experience
- **2402.03777** · 2024-02-06 · cs.SE
- Hong Yi Lin, Patanamon Thongtanunam, Christoph Treude et al.
- [`pdfs/2402.03777_improving-automated-code-reviews-learning-from-experience.pdf`](pdfs/2402.03777_improving-automated-code-reviews-learning-from-experience.pdf) · [abs](https://arxiv.org/abs/2402.03777)

Modern code review is a critical quality assurance process that is widely adopted in both industry and open source software environments. This process can help newcomers learn from the feedback of experienced reviewers; however, it often brings a large workload and stress to reviewers. To alleviate this burden, the field of automated code reviews aims to automate the process, teaching large language models to provide reviews on submitted code, just as a human would. A recent approach pre-trained…

### Fine-Tuning and Prompt Engineering for Large Language Models-based Code Review Automation
- **2402.00905** · 2024-02-01 · cs.SE
- Chanathip Pornprasit, Chakkrit Tantithamthavorn
- [`pdfs/2402.00905_fine-tuning-and-prompt-engineering-for-large-language-models-based-cod.pdf`](pdfs/2402.00905_fine-tuning-and-prompt-engineering-for-large-language-models-based-cod.pdf) · [abs](https://arxiv.org/abs/2402.00905)

Context: The rapid evolution of Large Language Models (LLMs) has sparked significant interest in leveraging their capabilities for automating code review processes. Prior studies often focus on developing LLMs for code review automation, yet require expensive resources, which is infeasible for organizations with limited budgets and resources. Thus, fine-tuning and prompt engineering are the two common approaches to leveraging LLMs for code review automation. Objective: We aim to investigate the …

### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
- **2401.03676** · 2024-01-08 · cs.SE
- Wei Hung Pan, Ming Jie Chok, Jonathan Leong Shan Wong et al.
- [`pdfs/2401.03676_assessing-ai-detectors-in-identifying-ai-generated-code-implications-f.pdf`](pdfs/2401.03676_assessing-ai-detectors-in-identifying-ai-generated-code-implications-f.pdf) · [abs](https://arxiv.org/abs/2401.03676)

Educators are increasingly concerned about the usage of Large Language Models (LLMs) such as ChatGPT in programming education, particularly regarding the potential exploitation of imperfections in Artificial Intelligence Generated Content (AIGC) Detectors for academic misconduct. In this paper, we present an empirical study where the LLM is examined for its attempts to bypass detection by AIGC Detectors. This is achieved by generating code in response to a given question using different variants…
