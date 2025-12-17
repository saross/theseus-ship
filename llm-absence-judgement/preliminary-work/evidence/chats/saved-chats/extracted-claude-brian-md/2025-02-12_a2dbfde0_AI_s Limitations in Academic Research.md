# AI's Limitations in Academic Research

## Metadata
- **UUID:** `a2dbfde0-ce04-42e9-b0ff-6388c965190b`
- **URL:** https://claude.ai/chat/a2dbfde0-ce04-42e9-b0ff-6388c965190b
- **Created:** 2025-02-12 21:20:32
- **Updated:** 2025-02-12 21:46:49
- **Source:** Brian's Claude export

---

## Conversation

### Human (21:20:32)

Hi Claude. Today I am going to be dictating my thoughts for an academic paper as I walk. For context,here are the notes I have so far.

<Notes>
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{parskip}

\title{An Absence of Judgment: On AI's Fundamental Limitations in Research}
\author{}
\date{}

\begin{document}

\maketitle

\section{Introduction}
Large language models are fundamentally incapable of judgment, despite their ability to mimic the language of judgment. This distinction necessitates examining not only their linguistic output but also the concrete actions and outcomes that their words produce. However, this lack merely prevents us from treating them as true agents, \textit{not} as extracting mundane utility from them as tools. This paper is an investigation into the creation of a research-grade dataset using OpenAI's Deep Research in February 2025, acting as a case study --- and our ``autoethnographic'' reflection upon the use of this tool for what Zvi Moshowitz calls ``mundane utility."

Here, we will also give our understanding of the necessary prerequsities for an ``agentic'' tool, and why we believe that this infrastructure, at this time, does not satisfy that criteria. We will also discuss the fundamental lack of judgement that these models exhibit, and why it is this core incapability which prevents an accumulation of patterns-shaped-like-knowledge to answer Dwarkesh's question to Cohen: ``what do you make of the fact that these things have basically the entire corpus of human knowledge memorized and they haven’t been able to make a single new connection that has led to a discovery? Whereas if even a moderately intelligent person had this much stuff memorized, they would notice — Oh, this thing causes this symptom.'' We assert that the lack of induction exhibited by even currently accessible frontier models like o3-mini-high, answers this question. To be clear, this paper is a description of what we have experienced in our attempt to actively use these models to research and answer an academic question --- not merely to conduct a \textit{descriptive} literature review, but to find that central spark of insight which represents a contribution to the literature. We do not say that these capabilities are forever barred to these models, merely that they do not exhibit them yet and that the common errors in estimating the capabilities of these models based on \textit{what they say} rather than \textit{how they act} can lead to confusion as to their actual capabilities and hinder finding places of mundane utility in our use of these tools. 


\section{Agentic Systems}

#  "Agentic" Systems vs Normal Software

## Goal-Related Characteristics
1. Goal Following vs Goal Setting
   - Agentic systems are goal-following systems
   - This contrasts with AGI, which can set its own goals
   - Key distinction: Agentic systems require external input for goals

## Agentic Characteristics
1. Goal Processing Capabilities
   - Accept external goals as input
   - Collaborate with users to operationalize goals
   - Functionally decompose goals into manageable components

2. Execution Capabilities
   - Create plans for goal completion
   - Invoke appropriate software and APIs
   - Monitor and assess progress

3. Assessment and Reporting
   - Make judgments about goal completion
   - Provide reports to users (like Claude)
   - Include success/failure evaluation based on system's judgment

\section{Deep Research and AI Capabilities}

\subsection{Current State}
The implementation of O3 for research purposes, while advanced, reveals fundamental limitations. This connects to broader discussions, as highlighted in Cohen's repost of DAKISH regarding AI's inability to produce truly groundbreaking research. While these systems demonstrate acceptable fluency and solid domain knowledge, they lack crucial elements of genuine research capability.

% One question I had for you while we were talking about the intelligence stuff was, as a scientist yourself, what do you make of the fact that these things have basically the entire corpus of human knowledge memorized and they haven’t been able to make a single new connection that has led to a discovery? Whereas if even a moderately intelligent person had this much stuff memorized, they would notice — Oh, this thing causes this symptom. This other thing also causes this symptom. There’s a medical cure right here.

% Shouldn’t we be expecting that kind of stuff?

% It’s a very good question. In 2023, I quipped, “I think they have, we just haven’t asked them.” Maybe, but less clear today. Dwarkesh reports that there have been no good answers.
% https://feeds.feedblitz.com/~/912665402/0/marginalrevolution~Dwarkeshs-Question.html


\subsection{Fundamental Limitations}
\begin{itemize}
    \item Absence of goal-setting and goal-following behavior
    \item Constraint to the Next Token paradigm
    \item Limited self-reflexivity, characterized by:
        \begin{itemize}
            \item Simple search execution
            \item Information synthesis without true comprehension
        \end{itemize}
    \item Inability to genuinely evaluate goal accomplishment
        \begin{itemize}
            \item System assumes task completion at each output
            \item Lacks true self-assessment capability
        \end{itemize}
\end{itemize}

\subsection{Comparative Analysis}
Using a first-week PhD student as our prototypical target, we observe that while AI systems can mimic goal-following behavior, they fundamentally lack the authentic research capabilities demonstrated by even novice human researchers.

\section{Practical Applications}

\subsection{Literature Reviews}
Initial applications in literature review processes have shown promising results, particularly in:
\begin{itemize}
    \item Dataset preparation and collection for research purposes
    \item Improvement over previous superficial review methodologies
\end{itemize}

\section{Future Development}
\subsection{Areas Requiring Further Investigation}
\begin{itemize}
    \item The Normal Intuitive Pattern concept requires elaboration
    \item Connection between mundane utility and tool-using behavior
    \item Precise definition of agentic behavior in research contexts
    \item Concrete manifestations of judgment absence in research outputs
\end{itemize}


\end{document}

---

### Assistant (21:20:37)

 I'll help you develop your academic paper through dictation. From your notes, I can see you're working on a thoughtful analysis of AI's limitations in research contexts, particularly focusing on the distinction between linguistic capability and true judgment/agency. Would you like to start dictating your thoughts? I can help organize them and suggest ways to develop the arguments further.

I notice a few interesting threads in your current draft that could be expanded:

1. The connection between "mundane utility" and the absence of true agency
2. Your comparison to first-week PhD students as a benchmark
3. The role of judgment in making novel connections across domains

Where would you like to begin? I can also ask clarifying questions about specific sections if that would be helpful for your dictation process.

---

### Human (21:26:03)

Research yesterday. Sure. Insofar as Insofar as it presents mundane utility, where we are giving it a emotional task It is not We operational as agents Hi. Right. So Thank you.

---

### Assistant (21:26:09)

 Let me help structure what I understand from your dictation. You seem to be focusing on the concept of "mundane utility" and the distinction between operational tasks versus true agency. Let me articulate this more clearly:

The distinction lies in how we utilize AI systems for operational tasks versus expecting them to act as true agents. When we assign an AI system what appears to be an evaluative task, it's crucial to understand that we're not actually engaging with judgment in the true sense. Rather, we're leveraging its pattern-matching capabilities for operational outcomes.

Would you like to continue developing this thought? I can help organize your ideas as you walk. Some potential directions we could explore:

1. Specific examples of what constitutes "mundane utility" in research contexts
2. The operational boundaries between pattern-matching and true judgment
3. How this relates to your earlier points about Deep Research

Feel free to continue dictating your thoughts, even if they come in fragments - I'll help structure them into coherent academic prose.

---

### Human (21:28:53)

Message garbled, trying again

---

### Assistant (21:28:56)

 I see your message was cut off. Would you like to try dictating your thoughts again? I'm ready to help organize and capture your ideas for the academic paper based on the draft you shared earlier.

---

### Human (21:31:56)

Okay. So Thinking about the failure of deep research yesterday, generating a newspaper article. We can absolutely assert That'd be detail here is not of judgment. And and, of course, the necessary induction which maps to judge It does not

---

### Assistant (21:32:01)

 I notice you're dictating thoughts about deep research's failure specifically regarding newspaper article generation, and touching on concepts of judgment and induction. However, some parts were unclear - could you try rephrasing the key point about judgment and induction again? 

From what I understood, you're suggesting that:
1. There was a specific failure case with deep research generating a newspaper article
2. This demonstrates a lack of judgment
3. There's a connection between judgment and induction

Would you like to elaborate on any of these points? I'm particularly interested in the specific failure case you observed, as it could serve as a concrete example in your paper.

---

### Human (21:35:38)

So insofar as it produced a newspaper article that looked like a newspaper article. But Didn't follow the guidelines. I've quite literally the 2 elements that we, provided before. Like, we we made an article, and Claude We made an article in o one pro without search. And so deep research, even though it demonstrated no. Deep research, even though it purports to have agentic behavior, Doesn't. And so, therefore, here's where we need to to define Here's where we need to define what it means to be agentic. Because if we are to treat this like anything If we are to treat this like anything beyond a marketing term, We have to have very clear definitions. And so Edgentic machine. As a precursor to whatever we call AGI, is something that is goal following. For something to be goal following, it must be able to both Figure out when it is appropriate No. It must be able to figure out if it solved the problem. At the end of the day, I A goal following machine is a machine that Not only performs functional decomposition on any given task. Right? And so so that that functional decomposition is fine. But iOS machine that can judge. There's that word again. It's a machine that can judge if it has accomplished the task and moreover, if it has accomplished the task well, I e Has it not has it produced words, that vaguely mapped the vibes of the input, but has it generalized from the, specific data of the input. The actual problem that is trying to be solved and can it judge if it has solved that prob? And so deep research isn't agenic. And it's not agentic because it cannot take a goal as input and help to achieve that goal. Now to be clear, they're not particularly saying that it can, and and we can we can narrow Right? We can say, okay. This is narrowly scoped. This is Only for lit reviews, quote, unquote. Pausing here to reset.

---

### Assistant (21:35:47)

 Let me help organize these key points about agency and judgment that you're dictating. I'll structure them to potentially fit into your paper's section on "Agentic Systems":

<antThinking>This dictation builds on the agentic systems section from the notes, adding crucial definitional clarity. I should organize this while maintaining the academic tone.</antThinking>

The core argument you're developing seems to be:

1. Deep Research's failure case with the newspaper article demonstrates a fundamental issue:
   - It can produce content that superficially resembles the target format
   - But it failed to follow explicit guidelines, showing lack of true goal-following behavior

2. This leads to a necessary refinement of what "agentic" means in AI systems:
   - An agentic machine (as a precursor to AGI) must be fundamentally goal-following
   - True goal-following requires:
     a. Functional decomposition of tasks (which current systems can do)
     b. Ability to judge task completion
     c. Ability to judge task completion quality
     d. Capacity to generalize from specific inputs to understand the underlying problem

3. The key distinction:
   - Current systems can "produce words that vaguely map the vibes of the input"
   - But they cannot generalize from specific data to understand and evaluate if they've solved the actual underlying problem

4. Therefore, Deep Research isn't truly agentic because:
   - It cannot meaningfully take a goal as input
   - It cannot effectively help achieve that goal
   - Even in its narrowly scoped domain of literature reviews

Would you like to continue developing any of these points further? I notice this builds particularly well on your paper's existing section about goal-related characteristics of agentic systems.

---

### Human (21:37:06)

And so even if they say even if this is narrowly scoped, even if this is only for lit reviews, and and we we also have to to say that this is a descriptive lit review, which lacks the spark of insight that makes a literature review useful. As in, why did you so a literature, for it to be useful, to go why did you choose these sources? What message are you trying to communicate? If you're merely regurgitating source That is That is the performance of literature review. Without any of the real substance of literature review. Because you are describing. You are not producing insight. Again, it's the lack of insight. It's the lack of induction because a literature review by virtue of how a thing is grouped, a literature review by virtue of what is selected and what is not selected. And a literature review by virtue of its organization supports a broader Claude. It supports the story. Or it supports research or whatever you wanna say there. And so because literature review

---

### Assistant (21:37:13)

 Let me help develop this crucial point about the nature of meaningful literature reviews and how it relates to your broader argument about AI limitations. You're articulating an important distinction between superficial performance and genuine insight in literature reviews:

1. The Nature of Meaningful Literature Reviews:
   - Not merely a collection of sources
   - Defined by intentional choices in:
     - Source selection and exclusion
     - Organization and grouping
     - Supporting a broader narrative or research agenda

2. Deep Research's Fundamental Limitation:
   - Can perform "descriptive" literature reviews
   - But lacks the crucial elements that make reviews useful:
     - Purpose-driven source selection
     - Intentional organization
     - Generation of novel insights
     - Inductive reasoning to support broader claims

3. The "Spark of Insight" Problem:
   - Current AI systems can regurgitate and reorganize
   - But cannot provide the critical "why" behind:
     - Source selection
     - Organization choices
     - Connection to broader scholarly conversations

This seems to connect strongly to your earlier points about judgment and induction. Would you like to continue developing how this specific limitation in literature reviews exemplifies the broader problem of AI's lack of true agency?

---

### Human (21:41:51)

And so because literature review As produced by deep research, it uses words adequately. Like, it's not it's not an interesting literature review, but all the words are there, and they're in the right order, and it's long enough to be orders of magnitude better than prior models. It is a useful tool. It is something that will take in a prompt, Decompose decompose that prompt into a series of searches. These fairly large context fairly large context in the in the vibe of a to to synthesize and stitch together points. But It is the negative space where the problem lies. Is we don't see it being systematic. So so in our observations, we see it running some searches, and then effectively getting bored. And we never see it questioning if its present attempt is appropriate. And so what we see, therefore, Is when we tell deep research to do something, It will and this is this is the common failure mode of LMS, and this is the common failure mode of deep research. That it will always produce an output. Right? It will it will always produce an output, and it will never go, oh, wait. I like, it it will never question the assumptions. And it will never go, oh, I just did all of this research, just did all of this research onto the wrong thing. Did you mean this, that, or the other? And so because it cannot forget, because it cannot judge the appropriateness, of its models. Yay. Not models. Choking to the context window. It is something that Takes as gospel It's first search results. And so it quote, knows, end quote, how to search. It runs a bunch of searches. It dithers about in the thinking, we never see it making an outline. We never see it revising an outline. We never see it Cutting Right? Like, the fact that The fact that it didn't includes by default everything that it searches for and never has a winnowing pass of, oh, this wasn't right. Is the uncanny valley of research for deep research. Oh, I like that quote. The uncanny valley of Let's make sure that that gets into the paper.

---

### Assistant (21:41:59)

 Let me help organize this significant observation about Deep Research's behavior and the "uncanny valley of research" concept you've identified. This builds on your earlier points about agency while adding specific behavioral observations:

1. Surface-Level Competence:
   - Produces coherent, well-formed text
   - Can perform basic functional decomposition
   - Handles large context windows
   - Represents significant improvement over prior models

2. The "Uncanny Valley of Research" (excellent phrase):
   - Key behavioral limitations observed:
     - Never questions its assumptions
     - Never revises its approach mid-process
     - No evidence of outline creation or revision
     - Lacks winnowing or filtering process
     - Takes initial search results as "gospel"
     - "Gets bored" rather than being systematic
     - Always produces output regardless of appropriateness

3. Critical Missing Elements:
   - No self-questioning
   - No mid-process correction
   - No adaptation based on intermediate results
   - No recognition of potential misalignment with intended goals

This observation about Deep Research always producing output without questioning assumptions seems to connect strongly to your earlier points about judgment and agency. Would you like to develop the "uncanny valley of research" concept further? It could serve as a powerful central metaphor for your paper's argument about the gap between superficial competence and true research capability.

---

### Human (21:46:40)

Okay. Eastern Archaeology. I've never used to before to do your bike That is turned off at So far. But then Issue for iOS There's 64 issues. The correct change 2 would have been starting issue 1, and just if you buy this, I wanna have to do that. I'm sorry. Oh, that's so put that down as a 2 day. I need to rerun the IP search. Maybe, like, walks at 5. Because now that I'm thinking about it, it never actually Well, best thing is it either never So Update or it never said Is that Because the increase goes by the 5th of instruction we give and not the instructions we give, It's actually not paid That construction site. Okay. Because might not This is the operation. Oh, It's not usually operationalized at school, and So so if it I'll start it at 1. It would be better if we didn't answer that. That's fine. It would be aware of its inefficient size. As a researcher, The reason why we haven't done this research previously. Is because it's boring before. Right. Just dial in. Cuba. But because it cannot stay on task for a sustained period, It is not agenda. It is an it is in the unhanded balance.

---

### Assistant (21:46:49)

 I'm having some trouble following parts of your dictation clearly - it seems there might have been some garbling or background noise. Let me focus on the key points I could understand:

1. There seems to be an issue about search scope or parameters:
   - Something about 64 issues
   - A suggestion that starting from issue 1 would have been better
   - A need to rerun some searches

2. An important observation about operational limitations:
   - The system follows instructions but not necessarily in the most efficient way
   - There's something about it not being properly "operationalized"

3. A key point about sustained attention:
   - The system cannot "stay on task for a sustained period"
   - This relates to your earlier points about it not being truly agentic
   - You mentioned something about it being "in the unhanded balance"

Would you mind clarifying some of these points, particularly about the operational aspects and what specific search issue you encountered? This seems like it could be another concrete example of the system's limitations.

Also, you mentioned something about why this research hasn't been done previously - could you elaborate on that point?

---
