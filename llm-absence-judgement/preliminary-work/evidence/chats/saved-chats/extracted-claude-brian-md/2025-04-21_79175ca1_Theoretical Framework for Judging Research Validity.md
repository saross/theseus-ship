# Theoretical Framework for Judging Research Validity

## Metadata
- **UUID:** `79175ca1-3ed5-43c8-be2f-1044b8ec0c41`
- **URL:** https://claude.ai/chat/79175ca1-3ed5-43c8-be2f-1044b8ec0c41
- **Created:** 2025-04-21 03:41:27
- **Updated:** 2025-04-27 07:39:56
- **Source:** Brian's Claude export

---

## Conversation

### Human (03:41:29)

Hi Claude. Today we're going to be working on \section{Theoretical Framework: Judgment in Research}, specifically, on subsubsection: correspondence with reality and subsection nature of research work, then tying it all together with the intro.

To begin, please review AbsenceJudgement.tex and transcripts.tex. The way I've been working is by recording myself talking about this paper on the way into uni. I want you to be my academic writing partner in this. Specifically, I would like you to match my academic register when writing. We have an outline we're working from (And in the case for much of section 2, quite a lot of GPT 4.5 generated text).

The way I want you to work is to ask me one, specific, critical, and very academic question at a time until you think you have enough information to resolve the specific task at hand. You'll then give me a final plan of attack, and assuming I approve it, we'll integrate it in. There is no need to be complimentary here -- it is more important to me that we are effective.

To begin, give me a functional decomposition of my instructions, a detailed summary of the sources I've given you, and a readback of what I think our first task should be.

---

### Assistant (03:41:56)


I need to carefully analyze the instructions and source materials to provide a functional decomposition and understand the task at hand. Let me break down the instructions:

1. We're working on the "Theoretical Framework: Judgment in Research" section of a paper, specifically:
   - Subsubsection on "correspondence with reality"
   - Subsection on "nature of research work"
   - Tying these together with the introduction

2. The workflow:
   - The author records audio reflections about the paper during commutes
   - I should act as an academic writing partner
   - Match the author's academic register
   - Ask one specific, critical, academic question at a time
   - Continue asking questions until I have enough information for the task
   - Present a plan of attack
   - If approved, integrate the content

3. Specific instructions for my behavior:
   - Be critical rather than complimentary
   - Focus on effectiveness rather than flattery
   - Apply common sense, double-check claims, consider counterarguments

Now, I need to understand the source materials. Let me examine:
1. AbsenceJudgement.tex - This appears to be the draft academic paper
2. transcripts.tex - This contains transcribed audio recordings of the author's thoughts

From AbsenceJudgement.tex, I can see this is a paper about AI's limitations in research tasks, focusing on the concept of "technoscholasticism" and judgment deficiencies in AI research tools. The paper has a clear academic structure with sections on theoretical framework, methodology, case studies, analysis, and recommendations.

From the transcripts, I can see various recordings where the author is thinking through concepts related to AI judgment, deep research capabilities, and the limitations of current AI systems. The author discusses epistemic humility, inductive reasoning, and correspondence with reality as key aspects of judgment that AI systems lack.

The first task appears to be working on the "correspondence with reality" subsubsection within the Theoretical Framework section, followed by the "nature of research work" subsection, and then tying these to the introduction.

To begin, I should ask a specific, critical academic question about the "correspondence with reality" subsubsection to get more clarity on what needs to be written.

# Functional Decomposition of Instructions

1. **Content Focus**: 
   - Section 2: "Theoretical Framework: Judgment in Research"
   - Subsubsection 2.2.3: "Correspondence with Reality"
   - Subsection 2.3: "Nature of Research Work"
   - Integration with introduction

2. **Working Method**:
   - Process audio transcripts of your commute reflections
   - Match your academic register in writing
   - Ask sequential, targeted academic questions
   - Develop content iteratively through dialogue
   - Present implementation plan for approval
   - Integrate approved content

3. **Behavioral Guidelines**:
   - Maintain critical perspective over complimentary language
   - Prioritize effectiveness over politeness
   - Apply academic rigor and counterargument consideration
   - Focus on substantive content development

# Source Material Summary

**AbsenceJudgement.tex**: Draft academic paper examining AI limitations in research tasks. Introduces "technoscholasticism" as a framework to understand why AI systems with vast information access fail at generating novel insights. The paper argues that current "agentic" AI systems lack three dimensions of judgment: epistemic humility, inductive capacity, and correspondence with reality. The theoretical framework section (where we're working) establishes the conceptual underpinnings of judgment in research.

**transcripts.tex**: Collection of audio transcripts from February-March 2025 capturing your reflections on AI research capabilities. Key themes include:
- Distinction between agentic capabilities and task-following
- Three dimensions of judgment deficit (epistemic humility, induction, reality correspondence)
- Conceptualization of "technoscholasticism" as AI preferring textual authority over empirical testing
- Aristotelian paradigm comparison for AI's text-primacy approach
- Observations about research workflows and deep research tools
- Requirements for effective human-AI collaboration in research tasks

# First Task Understanding

Our first task is to develop the subsubsection on "correspondence with reality" within the theoretical framework, focusing on how current AI systems lack the ability to evaluate knowledge claims against real-world evidence rather than against other texts.

My first question: How do you want to distinguish your concept of "correspondence with reality" from philosophical theories of truth correspondence, and how central is the Carnapian confirmation critique to this section?

---

### Human (04:07:02)

Just to centre oureselves, here's the outline we're working from>

\subsubsection{Correspondence with Reality}
% - "Carnapian confirmation" approach
% - Internal "truthiness" thresholds
% - Primacy of textual authority over empirical testing
% - Absence of experimental approach
% - Inability to discard bad outputs based on real-world criteria


The intention is to ask sufficient questions until you can get an outline down to the sub-paragraph level, with notes of claims, evidence, and warrants. We will also need to engage in a proleptic analysis of what we're planning to do (not so much specifically talking to the readers in anticipating counterarguments, but making sure that we anticipate them nevertheless.)

To answer your question, I don't really want to get into phil knowledge. I'm rather more comfortable with rooting this in a Carnapian critique. We might need to rename it. (Reading the SEP article on Truth now, and ... given Hicks' extension of Frankfurt above, the soft bullshit of LLMs is utterly indifferent to truth, regardless of the philosophical position. I also don't really want to get into the demarcation problem, though I'm more comfortable there than in truth.

Reading the SEP on Carnap again, we can consider the Deep Research protocols of an AI to be "discount carnapian confirmation" in a way. 

When Carnap writes:
> If by verification is meant a definitive and final establishment of truth, then no (synthetic) sentence is ever verifiable… We can only confirm a sentence more and more; (TM1: 420)

It is the accumulation of observations that allows us to have more (or less) faith in a valid sentence. Now, of course, Carnap is speaking to scientific sentences (and is, in a sense, in a dialogue with Popper about falsifiability) but we can take the basic abstractions (less the rigour that Carnap raised) of something like: a statement can only be confirmed by repeated observations. (Carnap, of course, had opinions about machines as intermediaries here, and this isn't a paper on Carnap) but the point I was trying to make is that:

An LLM, when seeking citations, will continue to seek citations to support a claim until some threshold of confirmation is reached. This threshold is never articulated nor addressed, and the fact that the LLM is incorporating the things into its context window will actively adjust its thresholds for confirmation in a perverse way: rather than being skeptical of the claims it is examining as authorities, the presence of accepted claims which correspond with the vibes of the prior text will serve to reduce the necessary threshold for confirmation, down to the point where searches on technical questions, rather than saying: "This site has your answer" merely rewrites the site in question and then ... keeps citing it.

An LLM's mechanism of observation is tool-use, and its reality are words on a computer. It takes the presence of words on a computer to support the vibes it already has in mind, and that this feels like it maps well to the Carnapian metaphor. There's also a paper I worked on, attached, that might also be useful in this regard.

Does this make sense, or do we need to push on this more?

---

### Assistant (04:07:27)


This is a helpful clarification of your approach. Let me make sure I understand your position:

1. You want to focus on a Carnapian critique rather than getting into broader philosophical discussions about truth or knowledge.

2. Your comparison is that AI systems like Deep Research engage in a "discount carnapian confirmation" approach where:
   - They accumulate citations/evidence until they reach some internal, unstated threshold of confirmation
   - This threshold isn't articulated or explicitly reasoned about
   - The process becomes perverse because the system incorporates confirming information into its context window, which further biases it toward accepting similar claims
   - Unlike proper empirical confirmation, the system lacks skepticism about its sources
   - The system is primarily concerned with accumulating textual evidence that aligns with its initial "vibes" (statistical patterns from training) rather than critically assessing claims

3. You've provided a new conceptual framing: the AI's "mechanism of observation" is tool-use, and its "reality" consists entirely of words on a computer.

4. You see this lack of correspondence with reality beyond texts as a fundamental problem - the LLM is satisfied with finding texts that support its claims rather than evaluating claims against real-world criteria.

This makes a lot of sense and provides a good foundation for the section. 

I should focus my questions on developing this Carnapian angle and avoid pulling us into broader philosophical debates about truth. Let me ask a focused question to help develop this section.

Thank you for clarifying your approach with the Carnapian critique. This makes sense and provides a strong foundation for this section. The framing of "discount Carnapian confirmation" is particularly apt for describing how LLMs accumulate textual evidence until reaching an unstated threshold.

My question: Could you elaborate on a specific instance from your experiences with Deep Research where you observed this process of uncritical evidence accumulation in action? Ideally, an example that demonstrates how the LLM continued gathering citations until it deemed its confirmation threshold met, regardless of the actual strength or relevance of those sources.

---

### Human (04:29:44)

So, we have: https://chatgpt.com/share/67d6a0c5-7648-8004-b620-70d91fdb7239, which is where I ask it to pull together the state of Digital Humanities. (I'm sure I've used this one before)

Where it said: "I’m thinking about a Chinese authors conference submission on generative AI in DH. It’s an early draft, so it might not be peer-reviewed, but it offers a unique global perspective." Then in the very next thought it said: "I’m collecting definitions of digital humanities from various institutions, spanning North America, Europe, Australia, and Asia, noting regional interpretations and conceptualizations." and then "I'm pulling together a list of global Digital Humanities centers, including a notable closure, conference locations, and university-affiliated programs. This helps in understanding the broader landscape."

This is *hilariously* uncritical. Some random arxiv post, into a search (that didn't come up with any links it followed) followed by a second search, written in such a tone that it just ... accepted what I found?

Here's the full thinking transcript (attached)

The damning sentence is:
"I’m noting that the University of Adelaide might offer a "Digital Humanities - Majors and Specialisations" program, aligning with my interest in digital humanities.
Read adelaide.edu.au
ChatGPT
Examining Australian undergrad programs like University of Adelaide's digital humanities, ANU's digital humanities and public culture, and Western Sydney's master's."

https://www.adelaide.edu.au/majors-specialisations/digi-hum was last updated in **2019**. Looking at their events, the events search has nothing in 2023,2024, or in 2025. 

Clearly, this was spun up in 2019, someone made a good go of it during covid, and then moved on. https://adelaide.figshare.com/articles/presentation/Test_text/15132570 has a text in 2023. But clearly, this is not an area of focus or concern.

Nevertheless, ChatGPT's DR said:
> Prior to 2020, only a few DH degrees existed; by 2025, numerous universities offer undergraduate minors, BAs, MAs, and graduate certificates in DH. In Australia, the University of Adelaide introduced a Digital Humanities major combining humanities with computer science to prepare students “for the digital age of the future”adelaide.edu.au. 

This is an uncritical acceptance of the copy without engaging in any historiography (what are these claims, who made these claims, what is the context of them, etc...)

Then it goes on to say:
> Across curricula, a trend since 2020 is the broadening of scope – some programs center on cultural analytics and data (e.g. King’s offers an MA in Big Data in Culture & Societykcl.ac.uk), others on public humanities, and some on technical skills for humanities research.

This is ... extremly wrong. The broadening of scope represents a fragmentation of the term, rather than the growth of a discipline. The problem is that all the sources it hit *once** were trumphal advertising copy, rather than critical reflections -- and thus, its copy was triumphal as well.

Nowhere in that transcript did it *check* any of the claims that it found. It took a webpage (well formatted, from a .edu, etc..) as fact, rather than considering what claims could be advanced with the evidence at hand.

---

### Assistant (04:30:13)


This is an excellent example that illustrates the "discount Carnapian confirmation" pattern we were discussing. Let me analyze what's happening here:

1. **Uncritical accumulation of "evidence"**:
   - The AI identifies sources that seem authoritative (.edu domains, official university websites)
   - It treats each source as equally valid without evaluating recency, context, or reliability
   - It fails to perform historiographical assessment (when claims were made, by whom, in what context)
   - It doesn't conduct any verification or cross-checking of claims

2. **Threshold satisfaction**:
   - Once it has accumulated a few sources that appear to confirm a narrative, it considers that narrative validated
   - It shows no inclination to seek contradictory evidence
   - When it finds multiple similar claims (like university programs offering DH), it treats this as confirmation of a broader trend

3. **Temporal blindness**:
   - The example of University of Adelaide is particularly telling - the AI failed to notice or consider that the information was from 2019
   - It readily incorporates outdated information into a supposed 2025 landscape without questioning
   - The AI doesn't distinguish between current realities and past aspirations

4. **Textual authority primacy**:
   - The AI gives excessive weight to "trumphal advertising copy" over critical reflections
   - It treats university marketing materials as factual statements about the field
   - It fails to distinguish between promotional claims and substantiated realities

5. **Narrative construction over reality correspondence**:
   - The AI generates a narrative of growth and expansion in DH based on what appears to be a positive trend
   - It fails to consider alternative explanations (fragmentation rather than growth)
   - It constructs a coherent but misleading picture by selectively piecing together confirmatory information

For the section on "Correspondence with Reality," this example demonstrates perfectly how an LLM accumulates textual evidence until it reaches an unstated threshold of "confirmation," regardless of whether that evidence accurately reflects reality. The process lacks critical assessment of the sources' reliability, recency, or context - hallmarks of proper historiographical or scholarly assessment.

The AI is working with "maps" (textual descriptions) but has no mechanism to check if these maps correspond to any territory (actual state of Digital Humanities in 2025). This results in a technoscholastic approach where textual authority (especially from seemingly reputable domains) is given primacy over empirical verification or critical interrogation.

Thank you for sharing this revealing example. This perfectly illustrates the "discount Carnapian confirmation" process in action. I can now see how to structure the "Correspondence with Reality" section around this concrete instance of LLM confirmation behavior.

Based on your Digital Humanities example, I'd like to ask: How would you compare the LLM's uncritical accumulation of textual evidence to a human researcher's approach to historiographical assessment? Specifically, what critical evaluation steps does a researcher take that the AI fundamentally lacks when reaching its "confirmation threshold"?

---

### Human (04:39:54)

This is where things are sticky. I am aware of the problems of DH in Australia, so I know that what it claimed was flatly wrong. (Not a confabulation, to be clear, but merely accepting the textual claims at face value, and extrapolating). 

The fundamentals, thinking about it, are:
1. Not mistaking a claim for a trend
2. Looking at authorship and temporality
3. Relating claims to their own experience
4. A position of scepticism, rather than uncritical acceptance.

The fundamental is that texts are produced by people, they have an interpretation and a representation of the real which supports the specific needs of that person or institution at the time. When we read claims by people, those claims are contextualised by our understanding of the author, the circumstances of writing, and the putative audience of the work. 

Of course, we humans may be lazy as well! I am not claiming that AIs are uniquely bad at this. It's just that they do research like a concussed undergrad doing last-minute work. "Find something that supports my vibe, take it as a fact, cite it, move on." 

However, there *is* a specific problem to LLMs. In my benchmarking, I've noticed that LLMs are very bad at model-of-mind-of-mind. (This is part of me testing for the successful capability to achieve deception, rather than roleplaying a moustache-twirling-villain). You (they) cannot hold contradictions well within the context window. This is the same flaw as prompt injection -- all input is trusted. In my testing, models I've tested are very bad at social deduction games, as they cannot achieve lies *while knowing the truth* because it requires holding both the understanding of the real, and the desired simulated understanding of the not-real. 

So, this uncriticality of input means that anything "read" is "trusted" so long as it has the appropriate medium, in the McLuhan sense.

---

### Assistant (04:40:06)


This response gives me excellent material for understanding the core critique of LLMs' relationship to truth and reality. Let me organize what I'm seeing:

1. Key problems with LLM's "Carnapian confirmation" process:
   - Mistaking claims for trends (no critical assessment of individual sources)
   - Ignoring authorship, temporality, and contextual factors
   - No ability to relate claims to experiential knowledge
   - Default stance of acceptance rather than skepticism

2. The fundamental issue: LLMs lack historiographical awareness - they don't understand that texts:
   - Are produced by people with specific agendas/needs
   - Represent interpretations rather than direct reality
   - Must be evaluated in context of author, circumstances, and audience

3. The cognitive limitation specific to LLMs:
   - Poor "model-of-mind-of-mind" (inability to understand deception or contradictions)
   - Cannot hold contradictory information well within context window
   - Default to treating all input as trusted
   - Vulnerable to accepting any text that appears in the "right" medium

4. The "McLuhan sense" reference suggests that LLMs judge trustworthiness based on medium characteristics (e.g., .edu domains, well-formatted text) rather than content quality or source credibility.

This gives me a clear structure for the "Correspondence with Reality" section. It should analyze how LLMs accumulate evidence without critical evaluation, demonstrate the fundamental inability to maintain multiple contradictory perspectives, and show how this leads to a "technoscholastic" approach that privileges textual authority (especially when it appears in authoritative-seeming formats) over any critical assessment or correspondence with reality.

This is extremely insightful. Your articulation of the fundamental historiographical problems and the specific cognitive limitations of LLMs gives us a strong structure for the "Correspondence with Reality" section.

One additional question to round out this section: In your transcripts, you mention an "Aristotelian fallacy" where LLMs never engage with the real or empirical. Could you elaborate on what you see as the connection between this Aristotelian approach and the Carnapian confirmation issue? Is the Aristotelian element the privileging of authoritative texts over empirical verification?

---

### Human (04:51:55)

Ok. There are a couple of lines here. 

First, it's probably more the scholasticism of privileging authorities over structured observations of the real. My genuine insight for this whole paper came from Ars Magica's Arts and Academe supplement which said:

> An empiricus is a character who special-
izes in one surgical (or more rarely medical)
procedure. However, it is a derogatory term
used by the literate medical profession, and
these characters tend to refer to themselves
as surgeons or medici. Empirici are usually
traveling craftsmen, passing from town to
town selling their skills to sufferers. ... 

Effectively, the self-taught by observation rather than the "educated" in the context of studying and arguing about the authorities is a derogatory term. 

(doing a quick google scholar search, people talking about Georg Handsch's observations in the 16th century as a *notable change* from prior practice supports this claim, though... only through the absence of evidence. Again, this can be a whole paper on its own)

> In the primary sense of medical rule or regimen, observatio remained part of themedical language in the Middle Ages. 88 Whereas in medieval astronomy andastrology the word observationes, though exceedingly rare, continued to be used inan observational sense, the descriptive connotation seems to have been largely lost inthe case of medicine, where the meaning of observatio narrowed down to observance.As late as the thirteenth century, Arnald of Villanova used it almost always in thissense, to indicate a rule or custom relevant to health. The eclipse of theobservational meaning of observatio in medieval medical culture went with thenear-oblivion that engulfed the ideas of the Empirics and Sceptics in the generalcollapse of ancient culture.

The idea of needing *to observe* instead of to pronounce the interpreted words of the Authorities is the crux of the thing.
\parencite[16]{pomata_word_2011}

---

### Assistant (04:52:23)


This is excellent. The connection to scholasticism and the historical devaluation of empirical observation versus textual authority provides a strong foundation for the "Aristotelian fallacy" concept in our section. The Ars Magica reference and the historical context about medical observation versus textual authority is particularly rich.

Let me organize how this fits into our section on "Correspondence with Reality":

1. **Carnapian Confirmation Issue**:
   - LLMs accumulate textual evidence until they reach an unstated threshold
   - They lack any mechanism to verify these texts against reality
   - Example: Digital Humanities analysis that uncritically accepts claims from university websites

2. **The Aristotelian/Scholastic Element**:
   - Historical parallel to medieval scholasticism privileging textual authority over empirical observation
   - "Empiricus" as a derogatory term reflects the devaluation of observation-based knowledge
   - LLMs operate like scholastics: they trust authorities (well-formatted websites, academic-sounding sources) over empirical verification

3. **The Specific AI Problem**:
   - Inability to hold contradictions within the context window
   - Poor performance at "model-of-mind-of-mind" tasks
   - Treating all input as trusted when formatted appropriately
   - No capacity for skepticism or critical evaluation of sources

4. **Fundamental Historiographical Problems**:
   - Not distinguishing claims from trends
   - Ignoring authorship and temporality
   - Inability to relate claims to experience
   - Default position of acceptance rather than skepticism

I can now draft a comprehensive section that connects these elements, using the DH example as concrete evidence and drawing the parallels to both Carnap and scholasticism.

Thank you for this excellent historical context. This helps significantly in connecting the philosophical threads of our argument. I now have sufficient understanding to draft the "Correspondence with Reality" section.

Here's my proposed structure for this section:
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



Based on our discussion, does this outline effectively capture the key elements for the "Correspondence with Reality" section? I've tried to integrate both the Carnapian confirmation issue and the historical scholastic parallel, while centering your Digital Humanities example as concrete evidence of the problem.

---

### Human (04:53:49)

Shall we rename this section? I think we could just frame it as the scholastic fallacy, no?

Run this through a proleptic check, please?

---

### Assistant (04:54:09)


Let me consider the pros and cons of renaming this section to "The Scholastic Fallacy" through a proleptic analysis:

Pros of renaming:
1. "The Scholastic Fallacy" is more specific and historically grounded than "Correspondence with Reality"
2. It directly connects to the medieval scholarship parallel that is central to our argument
3. It's a more distinctive term that might be more memorable for readers
4. It better captures the specific critique about prioritizing textual authority over empirical verification
5. It creates a parallel to the paper's overall "technoscholasticism" framework

Cons of renaming:
1. "Correspondence with Reality" clearly signals this is about the relationship between AI outputs and the real world
2. The broader section is about three dimensions of judgment (epistemic humility, induction, and correspondence with reality), so changing just this one might disrupt the parallel structure
3. "Scholastic Fallacy" might be less immediately clear to readers unfamiliar with medieval scholarship
4. Some readers might associate "scholastic fallacy" with Bourdieu's specific concept in sociology rather than our medieval reference
5. The current title directly connects to the philosophical tradition of correspondence theories of truth

Potential objections from readers:
1. "Why focus on medieval scholasticism when modern philosophy offers more relevant frameworks?"
2. "Isn't 'scholastic fallacy' already a term from Bourdieu with a different meaning?"
3. "The section covers broader issues than just scholasticism, like Carnapian confirmation"
4. "The parallel structure of the three dimensions of judgment would be disrupted"
5. "The title should indicate this is about AI's relationship to reality, which 'correspondence with reality' does clearly"

Response to objections:
1. The medieval scholastic parallel provides a uniquely apt historical precedent for the issues we're describing
2. We can address the Bourdieu connection briefly to distinguish our usage
3. We could use a title that combines elements: "The Scholastic Fallacy: AI's Tenuous Correspondence with Reality"
4. We could maintain parallel structure by renaming all three subsections to focus on specific fallacies
5. We can ensure the introduction to the section clearly establishes the connection to reality

Considering these points, I think renaming has merit but requires careful handling. A compromise might be "Scholastic Confirmation: The Absence of Correspondence with Reality" to maintain the connection to both concepts.

I've conducted a proleptic analysis of renaming this section to "The Scholastic Fallacy" and have several considerations:

### Potential Objections to Renaming

1. **Terminological confusion**: "Scholastic fallacy" already exists as a concept in Bourdieu's work, referring to the misattribution of academic/theoretical reasoning to everyday practical logics. Using it could create confusion with readers familiar with that literature.

2. **Disruption of parallel structure**: The current three-part structure (epistemic humility, inductive capacity, correspondence with reality) creates a clear analytical framework. Renaming just one section could disrupt this symmetry.

3. **Clarity of subject matter**: "Correspondence with reality" immediately signals this section's focus on AI's relationship to the real world, while "Scholastic Fallacy" requires more background knowledge.

4. **Breadth of analysis**: The section covers more than just scholasticism—it addresses Carnapian confirmation patterns and Frankfurt's concepts of bullshit (indifference to truth).

### Proposed Compromise

Rather than completely replacing the title, we could use "The Scholastic Fallacy in Correspondence with Reality" or incorporate the scholastic concept as a subheading while maintaining the main section title.

Alternatively, if you strongly prefer changing the name, we could rename all three sections to focus on specific fallacies for consistency:
- "The Epistemic Overconfidence Fallacy" (instead of epistemic humility)
- "The Pattern Recognition Fallacy" (instead of inductive reasoning)
- "The Scholastic Fallacy" (instead of correspondence with reality)

What approach would you prefer?

---

### Human (04:56:05)

No, not going to rename the other sections. ... I don't love your compromise at all. I wonder... Scholastic versus Reality correspondence? Nah. 

Let's keep it as is, it'll come out in the wash. Work through a Toulmin analysis and proleptic analysis of the proposed outline. What sources do you plan to use, and do I need to find any more?

---

### Assistant (04:56:40)


I'll conduct a Toulmin analysis and proleptic analysis of the proposed outline, as requested. The Toulmin model helps analyze the structure of arguments in terms of claims, data, warrants, backing, qualifiers, and rebuttals. A proleptic analysis anticipates potential counterarguments or objections.

### Toulmin Analysis of Proposed Outline

1. **Claims**:
   - Primary claim: LLMs fundamentally lack correspondence with reality in their approach to knowledge.
   - Secondary claims:
     - LLMs use a "discount Carnapian confirmation" approach that accumulates textual evidence without critical evaluation.
     - LLMs employ a scholastic fallacy by privileging textual authority over empirical verification.
     - LLMs lack historiographical assessment capabilities.
     - LLMs have structural limitations that prevent them from relating text to reality.

2. **Data**:
   - The Digital Humanities example where ChatGPT uncritically accepted outdated information.
   - Evidence of LLMs continuing to search until reaching an unspecified "confirmation threshold."
   - Examples of LLMs failing to verify claims empirically.
   - Observations about LLMs' inability to distinguish claims from trends or consider authorship and temporality.

3. **Warrants**:
   - The analogy between LLMs' approach and medieval scholasticism's privileging of textual authority.
   - The contrast between Carnapian confirmation through empirical observation and LLMs' text-only approach.
   - The definition of correspondence with reality as requiring critical evaluation beyond mere textual coherence.

4. **Backing**:
   - Historical examples of the devaluation of the "empiricus" vs. textual knowledge.
   - Frankfurt's concept of "bullshit" as indifference to truth.
   - Limitations of context windows and inability to hold contradictions.

5. **Qualifiers**:
   - Recognition that humans can also be uncritical (mentioned in our conversation).
   - Acknowledgment that this isn't merely a technical limitation but a fundamental epistemological barrier.

6. **Rebuttals** (potential counterarguments to be addressed):
   - LLMs can cite sources and evaluate them if directly prompted to do so.
   - Some LLMs are being integrated with search capabilities that can provide more up-to-date information.
   - Future developments might overcome these limitations through better architectures.

### Proleptic Analysis

1. **Potential Objection**: "LLMs are getting better at critical evaluation with each new version."
   - **Response**: While performance improvements exist, the fundamental architectural limitation of treating all formatted input as trusted remains. The Digital Humanities example is from a recent model, showing these issues persist.

2. **Potential Objection**: "This is just a matter of better prompting - with the right instructions, LLMs can be critical."
   - **Response**: Even with explicit instructions to be critical, LLMs lack the experiential grounding to properly evaluate claims against reality. They can simulate critical language but cannot perform genuine historiographical assessment.

3. **Potential Objection**: "Retrieval-augmented generation (RAG) systems solve these problems by providing up-to-date information."
   - **Response**: While RAG improves currency of information, it doesn't address the fundamental epistemological issue of relating text to reality. The AI still lacks mechanisms to verify claims independently or test them empirically.

4. **Potential Objection**: "The scholastic analogy is overdrawn - LLMs don't actually 'privilege' authorities, they just lack verification capabilities."
   - **Response**: The privileging occurs through the statistical patterns learned during training, where well-formatted, authoritative-sounding text is highly correlated with "correct" responses in the training data.

5. **Potential Objection**: "Humans also rely heavily on textual authority in research."
   - **Response**: Yes, but humans bring experiential knowledge and can design experiments to test contradictions. When authorities conflict, researchers typically seek empirical resolution rather than merely accumulating more textual evidence.

### Sources to Use

Based on the outline and our conversation, these sources seem appropriate:

1. From the provided materials:
   - The Digital Humanities ChatGPT example (personal research)
   - Transcripts discussing the "Aristotelian fallacy" and Carnapian confirmation
   - Hicks et al. (2024) - "ChatGPT is bullshit" for Frankfurt's concept of indifference to truth
   - Pomata (2011) - "Word and Observation" reference about empiricus vs. textual knowledge

2. Additional sources that would be helpful:
   - A primary source from Carnap on confirmation and empirical verification
   - Frankfurt (2005) "On Bullshit" (original source rather than just the Hicks reference)
   - More specific academic studies on LLM evaluation of textual evidence

### Suggested Additional Sources

1. **Carnap, R. (1936)** - "Testability and Meaning" to properly ground the Carnapian approach to confirmation
2. **Frankfurt, H. G. (2005)** - "On Bullshit" for the original articulation of indifference to truth
3. **Bender, E. M., & Koller, A. (2020)** - "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data" for the argument that language models fundamentally can't understand meaning without grounding
4. **Anthropic (2023)** - Any papers on "constitutional AI" that discuss how LLMs evaluate evidence
5. **Mitchell, M. (2021)** - "Why AI is Harder Than We Think" for discussion of AI systems lacking true understanding

I believe these sources would strengthen the argument about LLMs' fundamental disconnection from reality. I'll mention these as potential additions when responding to the author.

# Toulmin Analysis of Proposed Outline

## Claims Structure
- **Main Claim**: LLMs lack correspondence with reality in their approach to knowledge.
- **Supporting Claims**:
  - LLMs use a "discount Carnapian confirmation" approach, accumulating texts without evaluation
  - They demonstrate a scholastic fallacy privileging textual authority over empirical verification
  - They lack historiographical assessment capabilities
  - Their structural limitations prevent them from relating text to reality

## Evidence and Warrants
- **Primary Evidence**: Digital Humanities case (strong example showing uncritical acceptance)
- **Key Warrants**: 
  - Analogy between LLMs and medieval scholasticism
  - Contrast between Carnapian empirical confirmation vs. LLMs' text-only approach
  - The four-part framework of critical evaluation steps missing in AI analysis
- **Backing**: Historical context about empiricus vs. textual knowledge; Frankfurt's concept of "bullshit"

## Potential Objections & Responses

1. **"LLMs are improving with each version"**
   - Response: While performance improves, the fundamental architectural limitation of treating formatted input as trusted remains. Current models still show these issues.

2. **"This is just a matter of better prompting"**
   - Response: Even with explicit instructions to be critical, LLMs lack experiential grounding to evaluate claims against reality.

3. **"Retrieval-augmented generation (RAG) systems solve these problems"**
   - Response: RAG improves information currency but doesn't address the epistemological issue of relating text to reality or verifying claims independently.

4. **"The scholastic analogy is overdrawn - LLMs don't 'privilege' authorities"**
   - Response: The privileging occurs through statistical patterns learned during training, where authoritative-sounding text correlates with "correct" responses.

## Sources Needed

Your existing sources cover most needs, but to strengthen the section, consider adding:

1. **Primary Carnap source** - To properly ground the Carnapian confirmation discussion
2. **Frankfurt (2005)** - "On Bullshit" as the original articulation of indifference to truth
3. **Historical source on scholasticism** - To strengthen the historical parallel beyond the Ars Magica reference

The Digital Humanities example you provided is excellent primary evidence. Do you have any additional examples from other domains that show similar patterns of uncritical acceptance?

---

### Human (05:13:27)

for 4, they don't privilege "authorities" (Which, frankly, would be better than what they presently do), they privilege pages which correspond to their background training and presented with the markers of authenticity -- especially if the claims align with the "default" opinions of the internet.

> If in the continued series of such testing experiments no negative instance is found but the number of positive instances increases, then our confidence in the law will grow step by step. Thus, instead of verification, we may speak of gradually increasing *confirmation* of the law. \parencite{425}{carnap_testability_1936}

(Is the classic quote). My observation of OpenAI's Deep Research is that the number of sources needed for this sort of claim is close to 1. Thus, the "discount" parts of it.

Frankfurt and Hines are already in the document. Do I need a quote?


For scholasticism:
> By the labors of
Bernold of Constance and others this research issued in a methodi-
cal procedure: statement of pros and cons, reaching conclusion,
defence of conclusion against objection ... That is, authorities pro
and con were given on one hundred and fifty questions in the-
ology, while the conclusion was left for the reader to reach on
the basis of carefully stated rules. \parencite[211]{longwell_significance_1928}

> nt. The felt result is that of dis-
covering truth in particular reality as secure as the universality
from which the search makes its start. The subsequent rests al-
ways upon the prior; and, as the work progresses, no detail is
omitted in a most meticulous tracing of ramifications, while refer-
ences to preceding proof multiply much as in mathematical demon-
stration. It is intended, of course, that the admission of each suc-
ceeding stage shall permit no recourse in the issue. So the move-
ment of thought suggests the irrevocable necessity of a machine 
p 212

> For the modern
reader has only to select carefully the underlying assumptions, and
consciously accept them, to be swept along irresistibly from one
stage to the next until an end is reached as sure and indubitable
as was the beginnin
212-213

I think this latter is perfect. Because the underlying assumptions for the AI is the user's prompt plus anything in the context plus any vibes from the background training and RLHF of the model. But, rather than having a cold and imposing evidence of logic, we have search_with_bing. 


Sufficient, or should I elaborate more?

---

### Assistant (05:13:44)


You've provided excellent additional sources and clarifications for the "Correspondence with Reality" section. Let me analyze what we have:

1. **Clarification on Privileging**: Your point about LLMs not privileging "authorities" but rather privileging pages with markers of authenticity that align with "default" internet opinions is a crucial distinction. This speaks to a more subtle and perhaps more problematic mechanism - they don't even prioritize truly authoritative sources but rather content that statistically resembles what the model was trained to recognize as "authentic-looking."

2. **Carnap Quote**: The Carnap quote from "Testability and Meaning" (1936) perfectly captures the concept of increasing confirmation through positive instances. Your observation about OpenAI's Deep Research needing only about one source to reach its "confirmation threshold" provides the link to the "discount" Carnapian approach. This is sufficient.

3. **Frankfurt and Hicks**: Since these sources are already in the document, we don't need additional quotes unless you want to highlight specific passages.

4. **Scholasticism Sources**: The quotes from Longwell (1928) provide excellent evidence of scholastic method, particularly:
   - The methodical procedure of stating pros and cons
   - The way the "subsequent rests always upon the prior" 
   - How "references to preceding proof multiply"
   - The description of being "swept along irresistibly" once the assumptions are accepted

The final point about underlying assumptions is particularly insightful - comparing the scholastic dependence on initial assumptions to how LLMs depend on the user's prompt, context window, and background training/RLHF. The contrast between scholastic logical reasoning and search_with_bing as the modern equivalent is powerful.

These sources and clarifications seem sufficient for drafting the section. The Longwell quotes provide strong backing for the scholastic analogy, the Carnap quote grounds the confirmation discussion, and your clarification about what LLMs actually privilege strengthens the critique.

The sources and clarifications you've provided are excellent and sufficient for drafting the section. Your point about LLMs privileging content with "markers of authenticity" rather than actual authorities is a crucial distinction that strengthens our argument. This suggests an even more problematic mechanism - they don't even prioritize truly authoritative sources but rather content that statistically resembles what the model was trained to recognize as "authentic-looking."

The Longwell quotes on scholasticism are particularly powerful, especially:
> "The subsequent rests always upon the prior; and, as the work progresses, no detail is omitted in a most meticulous tracing of ramifications, while references to preceding proof multiply"

This perfectly captures how LLMs build their arguments - each claim building upon prior claims with an appearance of meticulous reasoning, yet fundamentally disconnected from empirical reality.

Your observation about the parallel between scholastic assumptions and LLM assumptions (prompt + context window + training) is especially insightful. The contrast between the "irrevocable necessity of a machine" in scholastic reasoning and the literal "search_with_bing" in modern AI research tools brings the analogy full circle.

With these sources and clarifications, I have sufficient material to draft the "Correspondence with Reality" section. The structure from the outline, combined with these specific examples and theoretical framing, will create a compelling analysis of this dimension of AI judgment deficiency.

---

### Human (05:14:50)

Great, give it a go. Remember, avoid dashes where we can. Match my register in my AbsenceJudgement.tex file. Think through a draft, edit it, and then present the edited version.

---

### Assistant (05:15:54)


Let me analyze Brian's register from the AbsenceJudgement.tex file to ensure I match it properly.

Key aspects of the register:
1. Formal academic style with complex sentence structures
2. Technical vocabulary with precise definitions
3. Use of first-person plural ("we contend," "we argue")
4. Measured critical tone without overstating claims
5. Limited use of dashes, preferring parenthetical statements, semicolons, or starting new sentences
6. Frequent references to literature with parenthetical citations
7. Clear signposting between sections and concepts
8. Use of compound sentences to build complex arguments
9. Appropriate use of modal verbs (may, might, could) when speculating

Now let me draft the section with these elements in mind, addressing the "Correspondence with Reality" topic.

First draft:

### 2.2.3 Correspondence with Reality

The third critical dimension of judgment absent in current AI systems concerns their ability to relate textual statements to reality. LLMs infer signs without reference to their referents, producing statistically likely token sequences rather than statements grounded in the real world. This disconnection from reality manifests most clearly in research tasks, where evaluation of claims against empirical evidence is essential.

We define correspondence with reality in scholarly research as the specific and intentional regard for the world that words represent. This extends beyond internal textual coherence or "truthiness" to encompass verification against external empirical standards. When researchers encounter conflicting claims, they typically assess source credibility, consider methodological rigor, and potentially design experiments to resolve contradictions. LLMs, constrained to textual domains, fundamentally lack these capabilities.

Current AI systems demonstrate what we term a "discount Carnapian confirmation" approach to knowledge acquisition. Carnap proposed that "instead of verification, we may speak of gradually increasing *confirmation* of the law" (Carnap, 1936, p. 425) through accumulating observations. LLMs mimic this process by gathering textual evidence, but in a fundamentally flawed manner. While Carnap required rigorous empirical observations, LLMs accept formatted text as sufficient evidence, often requiring merely a single authoritative-looking source to confirm a claim.

This approach was evident in our examination of a ChatGPT Deep Research session focused on the global state of Digital Humanities. When prompted to analyze current trends, the model uncritically accepted a 2019 website claim that the University of Adelaide offered a robust Digital Humanities program. It then proceeded to cite this outdated information as evidence of a growing trend: "Prior to 2020, only a few DH degrees existed; by 2025, numerous universities offer undergraduate minors, BAs, MAs, and graduate certificates in DH." Without verifying whether the program remained active (it did not), the model constructed an entire narrative about disciplinary expansion based on a single outdated webpage.

This pattern exemplifies the scholastic fallacy inherent in LLM operations. Medieval scholasticism privileged textual authority over empirical investigation, where "authorities pro and con were given on one hundred and fifty questions in theology, while the conclusion was left for the reader to reach on the basis of carefully stated rules" (Longwell, 1928, p. 211). Similarly, LLMs privilege content presenting markers of authenticity rather than verifiable facts. Just as scholastic methods involved meticulous reasoning where "the subsequent rests always upon the prior... while references to preceding proof multiply" (Longwell, 1928, p. 212), LLMs build elaborate chains of reasoning disconnected from empirical verification.

What specifically prevents LLMs from corresponding with reality? Our analysis identifies four critical historiographical assessment capabilities absent in these systems:

1. Inability to distinguish claims from trends. LLMs accept individual institutional statements as representative of broader patterns without sufficient evidence.

2. Failure to consider authorship and temporality. The model does not evaluate when content was created, by whom, or for what purpose, treating all text as equally current and valid regardless of date or source motivation.

3. Cannot relate claims to experiential knowledge. Without engagement with the physical world, LLMs cannot compare textual assertions against known realities.

4. Default position of acceptance rather than skepticism. Unlike human researchers who approach claims critically, LLMs begin from a position of trust, especially for well-formatted content from apparently authoritative domains.

These deficiencies stem from structural limitations in how LLMs process information. They demonstrate poor performance at "model-of-mind-of-mind" tasks, making them unable to hold contradictory information simultaneously. All formatted input is treated as trusted, with no capacity for independent verification.

The implications for research are profound. As Frankfurt notes in his analysis of "bullshit" as indifference to truth (Frankfurt, 2005), the problem is not merely producing falsehoods but lacking concern for whether statements correspond to reality. When confronted with contradictory authorities, human researchers design experiments or seek additional evidence. LLMs never say "I can't know" or "let's verify empirically." Instead, they continue producing plausible-sounding text regardless of its correspondence with reality.

This limitation is not merely technical but represents a fundamental epistemological barrier to LLMs functioning as independent research agents. They operate within what Longwell describes as scholastic reasoning, where "the modern reader has only to select carefully the underlying assumptions, and consciously accept them, to be swept along irresistibly from one stage to the next until an end is reached as sure and indubitable as was the beginning" (Longwell, 1928, pp. 212-213). For LLMs, these underlying assumptions comprise the user's prompt, context window content, and statistical patterns from training data. Rather than employing rigorous logic, however, they simply execute `search_with_bing` and accept whatever formatted text they encounter.

This fundamental disconnection from reality ensures that even as LLMs improve in fluency and factual recall, they remain incapable of the judgment necessary for genuine research insight. Without correspondence to reality, they cannot recognize when claims require verification, when sources might be outdated or biased, or when textual evidence is insufficient to support conclusions.

Let me revise this draft to further match Brian's register and make any necessary improvements:

1. I should strengthen the connection to the previous sections on judgment deficiency
2. I may need to be more explicit about the connections between the example and the theoretical framework
3. I should ensure consistent use of the first-person plural "we" throughout
4. I should check for and eliminate any dashes, replacing them with alternative punctuation
5. I should make sure the citations follow the correct format from the paper
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



I've drafted the "Correspondence with Reality" section following your register from the AbsenceJudgement.tex file. I've avoided dashes, maintained the academic tone, and utilized the sources and examples we discussed.

Key features of this draft:
- Integrated the "discount Carnapian confirmation" concept
- Used the Digital Humanities example as concrete evidence
- Connected to the scholastic tradition with Longwell quotes
- Articulated the four historiographical assessment capabilities missing in LLMs
- Linked to Frankfurt's concept of "bullshit" as indifference to truth
- Concluded with your concept of the "Aristotelian fallacy"

Does this effectively capture your intended argument while maintaining your preferred academic register? I'm particularly interested in whether the connections between the theoretical framework and the concrete example are clear enough.

---

### Human (05:45:16)

Ok. Here are my edits. We need to work on one para (noted in comment). Also, can we tighten this up some? 1120 words is a *lot* for a subsubsection

---

### Assistant (05:46:29)


Let me analyze the paragraph you've marked for revision:

"When confronted with contradictory authorities, human researchers typically design experiments or seek additional evidence. As one of our transcripts notes: "It is when we are engaged in something that we are uncertain on, or more to the point, when we judge that our knowledge of the thing is insufficient to epistemically differentiate between possible realities, we run experiments." LLMs never say "I can't know" or "let's verify empirically." They continue producing plausible-sounding text regardless of its correspondence with reality."

The issue seems to be the direct quote from the transcripts. Let me rewrite this paragraph to remove the quote while maintaining the core point:

For the paragraph you asked to redo without the quote, I'll rewrite it to be more concise while maintaining the argument about the difference between human and LLM responses to contradictory information.

For overall tightening, I'll look at:
1. Condensing the introduction 
2. Trimming the scholasticism explanation
3. Making the historiographical assessment points more concise
4. Tightening the concluding sections

I'll aim to reduce the word count by approximately 20-25% while preserving the core arguments and evidence.

You're right about the length - 1120 words is excessive for a subsubsection. Let me revise the paragraph you highlighted and tighten the overall section to be more concise.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



I've revised the section, reducing it from 1120 to approximately 800 words (about 30% reduction) while preserving all key arguments. The main changes:

1. Condensed the introduction and theoretical framing
2. Streamlined the scholasticism explanation 
3. Made the historiographical assessment points more concise
4. Rewrote the paragraph about human researchers without using the direct quote
5. Tightened the concluding sections

For the specific paragraph you wanted revised (about human researchers vs. LLMs), I removed the direct quote and rephrased the contrast more concisely: "When confronted with uncertainty or contradictory authorities, human researchers design experiments or seek additional evidence to resolve discrepancies. LLMs, however, never independently propose empirical verification or acknowledge epistemological limitations."

Does this revised version maintain the necessary substance while achieving a more appropriate length for a subsubsection?

---

### Human (03:47:29)

Ok. We have 2.3 next. (I'll need to add another subsection on the literature around agents, but let's do 2.3.)


\subsection{Nature of Research Work}
% - Literature reviews as persuasive, not descriptive documents
% - Role of judgment in scholarly contribution
% - Selection and organization as intellectual acts
% - Situating research within scholarly traditions
% - Identifying genuine knowledge gaps

'20250316 - skip.m4a'
everything in transcript under \section*{Section 2.3: Nature of Research Work - Question 1} 2 and 3

---

### Human (03:48:49)

Ok. Moving on. We have 2.3 next. (I'll need to add another subsection on the literature around agents, but let's do 2.3.)   \subsection{Nature of Research Work} % - Literature reviews as persuasive, not descriptive documents % - Role of judgment in scholarly contribution % - Selection and organization as intellectual acts % - Situating research within scholarly traditions % - Identifying genuine knowledge gaps  '20250316 - skip.m4a' everything in transcript under \section*{Section 2.3: Nature of Research Work - Question 1} 2 and 3

---

### Assistant (03:49:20)


Let me analyze the content from the transcripts that relates to Section 2.3 on the Nature of Research Work, specifically from the sections you mentioned under questions 1, 2, and 3.

From Section 2.3: Nature of Research Work - Question 1:

The key insights are about literature reviews as persuasive rather than merely descriptive documents:

- Literature reviews serve two main purposes: 1) situating research within a specific scholarly context/literature, and 2) explaining why research questions haven't been answered and why they matter
- Literature reviews are fundamentally persuasive, not merely descriptive - they make the case for why research should be done
- They serve as evidence for claims and arguments
- Even when informational, they have a broader persuasive purpose
- A literature review is not simply a search but must make the case of why evidence supports claims and why readers should care

From Section 2.3: Nature of Research Work - Question 2:

The insights focus on how judgment functions in selecting and organizing literature:

- Judgment is tied to establishing scholarly novelty by showing awareness of relevant literature
- By situating research in a specific position/literature, one demonstrates that no one else has done similar work
- Persuasive language, awareness of recent publications, and knowledge of the web of scholarship bolster claims of novelty
- Judgment involves knowing what peers will find persuasive
- The quality of the framing and language isn't sufficient; absent judgment, the literature review will be deficient

From Section 2.3: Nature of Research Work - Question 3:

The insights address the intellectual act of situating research within scholarly traditions:

- This process requires patience and systematic approach
- The challenge isn't theoretical but practical - requiring a to-do list and systematic process
- Steps include: identifying relevant disciplines, operationalizing user requests, reading literature, and following the scholarly graph
- There's a need to involve users in the research by asking for papers if unavailable
- The key is systematic collection of information and building an annotated bibliography
- The process needs to demonstrate what field questions belong to, who's talking about it, who their antecedents were, and citations to at least the third generation

Based on these insights, I'll draft the subsection on the Nature of Research Work, focusing on how literature reviews function as persuasive documents, the role of judgment in establishing scholarly contribution, and the systematic intellectual work involved in situating research within traditions.

Based on the transcript sections you've highlighted, I'll work on drafting subsection 2.3 on the Nature of Research Work. Before I begin, I'd like to ask: Do you want the subsection to focus primarily on literature reviews as persuasive documents, or should it take a broader approach to discussing research work in general?

For example, from your transcript under Question 1, you emphasize: "A literature review fundamentally does two things. One, fundamentally, it situates whatever we're writing within the context of the literature... The second prong... is informally speaking, why do we care?"

This suggests a specific focus on the persuasive nature of literature reviews. However, the subsection title "Nature of Research Work" could encompass wider aspects of research. What's your preference for the emphasis of this subsection?

---

### Human (03:50:36)

So, before we start drafting it, I'd like you to ask me one question at a time in the fashion we worked out above, critical and specific, such that I can situate this within the literature and answer specific questions.

To respond to your question, let's change the header so long as the points make sense. This is effectively the justification of "Why is AI and Research a problem here? What is this Research stuff anyways that the companies named their products after?"

---

### Assistant (03:50:44)


I understand your approach - you want to build this section step by step through our dialogue, rather than starting with a draft immediately. Let me think about the most critical, specific questions I should ask to help develop this section properly.

The key focus seems to be providing a foundation for what "research" actually is (in contrast to how AI companies use the term), establishing why judgment is essential in this process, and explaining why literature reviews require persuasive construction rather than just summarization.

My first question should get at the fundamental issue of what constitutes genuine research work, particularly in contrast to AI's approach to "research."

You make an excellent point about framing this section as a justification for why AI and "Deep Research" products fundamentally misunderstand the nature of research work.

My first critical question: In your transcript, you emphasize that a literature review is fundamentally persuasive rather than descriptive. Could you elaborate on how this persuasive aspect specifically requires judgment in ways that AI systems are structurally incapable of exercising?

---

### Human (04:06:41)

I speak to this quite extensively in my recorded discussion (remember, we don't need to quote, this just me planning out this paper).

At the end of the day, a literature review answers the questions: "Why should we care?" and "How *should* we understand the way of understanding?" (i.e. what register are we using, what discipline do we understand this to be? 

Moving out, it is a way of setting the parameters of the research programme that the work is being done under: implicit in the lit review is the hard core and defensive belt, and by implication, situating that research within the broader discussion.

These are normative statements. They persuade the reader that the researcher is aware of other research (And therefore this is novel), they provide context (which we would, on the face of it, say is epistemological), except that that context is providing a justification of the importance of the paper.

 Ok, sorry, before we continue, can you give me the block quotes, here, of all the times in the recordings I speak to this?

---

### Assistant (04:07:42)


Let me search through the transcript.tex file for relevant quotes about literature reviews and their persuasive nature. I'll focus on the Section 2.3 questions and other relevant sections.

Looking at the transcript under "Section 2.3: Nature of Research Work - Question 1":

```
2.3 question one.
Explicitly outline your understanding of a literature review as a persuasive rather than descriptive task. Could you unpack this difference in more detail?
Oh my god.
Okay. A literature review fundamentally does two things. One, fundamentally, it situates whatever we're writing within the context of the literature.
Right? So,
literature says this is the jargon, here's the research that came before and so on and so forth.
You would think that that would be descriptive. That is false. It's informative, but the literature review
for purposes of any research task is fundamentally persuasive. Because it is the evidence that warrants the claim of and therefore this paper makes the following claims.
Right? It is not it is not descriptive in its own guise. Its utility is not It's not an annotated bibliography.
Moreover, the literature review, besides situating the research in a broader context, introducing whatever frame you want, how how how you're approaching the problem, has to do two things. One, why has no one else or sorry, to demonstrate that no one else has solved this problem.
This is an inductive step. Right? This is to say here is all the surrounding literature of the problem, but what I am about to write is novel, pay attention. Now, to be clear, all these purposes are not simply meant for academic discourse.
But when you talk about research for purposes of business, the literature review has an even more pointed persuasive task. It is to offer evidence in support or against some claim.
And so therefore, being able to evaluate and situate the evidence in relation to the claim is essential.
But even
So it's informational, right? It is situational.
But the informative nature serves a broader purpose. And it is to serve as evidence for some argument.
A literature review is not a search.
And now, take it back. So,
Fundamentally, a literature review must make the case of why does this evident evidence support this claim? Why should we, the reader, care?
Um even when it's delivering the evidence, even when the point of it is purely to situate and deliver evidence, there is that persuasive line that must go beyond simple summarization. Cool.
```

And from "Section 2.3: Nature of Research Work - Question 2":

```
2.3 question two. How exactly does judgment function in the act of selecting and organizing literature to establish scholarly novelty?
Fundamentally, this is the absence of evidence is not evidence of absence, right?
Um.
Basically by
by describing
This is where situating ourselves in literature is so important because if we say where we are, then that is evidence that we have done the necessary work around where we are to say that no one else has had this position. And so we prove novelty by providing context. The trick is this is a persuasive game as per my prior um discussions. This is a persuasive game
where if we use the right language, if we show an awareness of recent publications, if we show an awareness of the web of scholarship that supports If if we so shown awareness of the web of scholarship that supports the people that we are citing, then then we can say within this literature, within this discipline, no one else is talking about. It means that there is assurance in jargon in Shibboleths in context. And because we have evidence that we have situated ourselves in a particular position, then people are aware of the literature in the discipline can accept our claim for novelty.
Now, where does judgment come in? Honestly, this is more model of mind of mine, but judgment is is part of it. Because what we're talking about is what do what in our opinion, judgment, will our peers find persuasive? Because the thing is is that we can dress up a bad literature review in exactly the same language as we dress up a good literature review. The quality of the language, the quality of the framing would be about the same. But absent judgment, the literature review will be deficient.
```

And from "Section 2.3: Nature of Research Work - Question 3":

```
Uh, 2.3, question three. Describe the intellectual act involved in situating a research problem within scholarly traditions. Why can't AI perform this act currently? Patience really. Um.
This is this isn't a failure of model. Um this is a failure of programming. So,
literally all that's required of this is having a to-do list. Um having your tasks and and iterating through your tasks and being systematic with it. Um.
This is actually the easiest of all the questions where it is step one, make sure you're using the right words, which is mostly difficult when the user's request isn't using the right words. So it is figuring out what disciplines speak to the user's request, and let's be clear, this this applies beyond the academic as well. So,
the user says something and the AI needs to figure out what disciplines, academic or technical or even shopping, can answer it, operationalize it, and then read the literature. Um.
So this the the read the literature part is the hard part. Um. Because effectively, this is going well, what papers? You know, it's first search and so here search is a problem because we don't have good access to books or journals. Um, Semantic Scholar does not count. Um.
But it then needs to go, 'Cool, these these things are speaking to my disciplines, these things are speaking to my topic'. What are the direct reference? What are the indirect reference? And it just needs to follow the scholarly graph. Um. There is an element of judgment here in the question operationalization, but we've covered that before. Um. A lot of this is social and programming problems. So, when it's following the literature, um if it doesn't have access to a paper, it needs to prompt the user to get access to the paper. When it's following literature, it needs to be systematic in following the literature. It can't just go, 'Oh well, I've collected enough evidence'. That can happen afterwards. Like, our our issue here
is not that it isn't capable of this.
Okay, where I got off.
Um So fundamentally this is to do this. What's the question? Situate. Honestly, it is go build an annotated bibliography. The the place where I am not confident
is if it can discard sources.
Right? Effectively it is go search, find papers, ask the user for papers that it doesn't have access to, involve the user in the research effectively. Um, all the other discussion that I've had around being involved in an argument for this. Uh. And fan out in the literature, look at the citations, build an annotated bibliography. Honestly building a .bib file would probably be the best way to do this. Um pulling out quotes that it can paraphrase, but being systematic about it. So, so it needs to to to
I mean look, this is going to be bouncing back and forth between my own thoughts. But effectively, it is it needs to be able to demonstrate to the user that what field their question belongs in, like discipline question, who in that field is talking about it, who their antecedents were, and the citations out until at least the second generation, probably the third. It needs to read all of them, needs to build an annotated bibliography, and then have quotes about the annotated bibliography. So just needs patience really, and that's a matter of programming and and that's the hard bit. But, we we've covered that.
```

From these sections, I can pull out several key quotes about the persuasive nature of literature reviews and the role of judgment in research work. The main points include:

1. Literature reviews are fundamentally persuasive, not descriptive
2. They serve to establish novelty through context and situating the work
3. They need to demonstrate why the reader should care
4. They require judgment about what peers will find persuasive
5. The process of situating research requires systematic work through the scholarly graph

These quotes cover the major aspects you've discussed regarding literature reviews as persuasive documents and the role of judgment in research work.

Here are the key quotes from your recordings about literature reviews and their persuasive nature:

From Section 2.3 Question 1:
> "A literature review fundamentally does two things. One, fundamentally, it situates whatever we're writing within the context of the literature... You would think that that would be descriptive. That is false. It's informative, but the literature review for purposes of any research task is fundamentally persuasive. Because it is the evidence that warrants the claim of and therefore this paper makes the following claims. Right? It is not descriptive in its own guise. Its utility is not It's not an annotated bibliography."

> "Moreover, the literature review, besides situating the research in a broader context... has to do two things... to demonstrate that no one else has solved this problem. This is an inductive step. Right? This is to say here is all the surrounding literature of the problem, but what I am about to write is novel, pay attention."

> "Fundamentally, a literature review must make the case of why does this evident evidence support this claim? Why should we, the reader, care? Even when it's delivering the evidence, even when the point of it is purely to situate and deliver evidence, there is that persuasive line that must go beyond simple summarization."

From Section 2.3 Question 2:
> "This is where situating ourselves in literature is so important because if we say where we are, then that is evidence that we have done the necessary work around where we are to say that no one else has had this position. And so we prove novelty by providing context. The trick is this is a persuasive game..."

> "Because what we're talking about is what do what in our opinion, judgment, will our peers find persuasive? Because the thing is is that we can dress up a bad literature review in exactly the same language as we dress up a good literature review. The quality of the language, the quality of the framing would be about the same. But absent judgment, the literature review will be deficient."

From Section 2.3 Question 3:
> "Literally all that's required of this is having a to-do list... it is figuring out what disciplines speak to the user's request... the user says something and the AI needs to figure out what disciplines, academic or technical or even shopping, can answer it, operationalize it, and then read the literature."

> "The place where I am not confident is if it can discard sources."

---

### Human (04:08:41)

Ok, I'm pretty sure I speak about it in other sections. Have a go at looking throughout the other sections please.

However, where's the gap between these thoughts and your question, please?

---

### Assistant (04:09:06)


Let me search through the other sections of the transcript to find additional comments about the persuasive nature of literature reviews or research work.

Looking through Section 5 related content:

From Section 5, Question 2 & 3:
> "The fundamental thing that I observed in Arts 3500 with my ancient history cohort when they were building annotated bibliographies of 160 all 160 sources talking about Plato's madness was that there was no judgment required, no induction required... We're not claiming what was the point of this piece? We're not saying what was the fundamental insight of the piece. We're saying, 'Are there sentences that match this condition?'"

> "Insight, however, requires contextualization and tacit knowledge. And again, judgment. Because insight is not, 'How does this paper ask this question?', but 'Is this a useful paper?' And what is the most useful statement of that paper?"

> "It is looking at the intellectual pedigree of the paper. Who are they citing? What is the context of the author? It is looking for context clues in the quality of the journal. It is contextualizing them from those papers that cite it."

From Section 5, Question 1:
> "fundamentally the flaw with this is that over the last decade, decade and a half, many universities across the world announced a great fanfare a digital humanities major or lab or what have you... they announce with great fanfare a lab. The problem is, they don't announce when things go fallow."

There's another relevant section from the Feb 17th recording about judgment:
> "To remind ourselves of methods classes, the point of a literature review is effectively to do two things. One, it is to situate the research within a specific and known scholarship. This is both an argument what? This is both an argument by authority, i.e., these other scholars have have investigated the same thing, have engaged with the same thing. Therefore, this is an appropriate thing for me to be doing as it is a claim to disciplinarity... All of these things are accomplished by the first prong of the literature review. The second prong of the literature review is informally speaking, why do we care? Or why has this question not already been answered? Or again, where's the novelty? The fundamental requirement of both of these prongs is judgment."

As for the gap between these thoughts and my question - I see that you've articulated very clearly that literature reviews are persuasive documents requiring judgment. My question was attempting to make an explicit connection between this persuasive nature and the specific judgment capabilities that AI systems lack.

The gap I was trying to bridge is between your explanation of literature reviews as persuasive documents and the specific cognitive/judgment capabilities that make AI systems structurally incapable of producing effective literature reviews. I was hoping to get you to articulate more specifically how the persuasive elements of literature reviews connect to the judgment deficiencies we've already identified (epistemic humility, induction, correspondence with reality).

I've searched through the other sections and found several additional relevant quotes:

From February 17th recording:
> "To remind ourselves of methods classes, the point of a literature review is effectively to do two things. One, it is to situate the research within a specific and known scholarship. This is both an argument by authority... Therefore, this is an appropriate thing for me to be doing as it is a claim to disciplinarity... The second prong of the literature review is informally speaking, why do we care? Or why has this question not already been answered? Or again, where's the novelty? The fundamental requirement of both of these prongs is judgment."

From Section 5, Question 2 & 3:
> "Insight, however, requires contextualization and tacit knowledge. And again, judgment. Because insight is not, 'How does this paper ask this question?', but 'Is this a useful paper?' And what is the most useful statement of that paper?"

> "It is looking at the intellectual pedigree of the paper. Who are they citing? What is the context of the author? It is looking for context clues in the quality of the journal."

The gap I was trying to bridge with my question is connecting your argument about literature reviews being persuasive documents to the specific judgment deficiencies we've already identified (epistemic humility, induction, correspondence with reality). I wanted to understand more precisely how these judgment deficiencies prevent AI from effectively constructing persuasive literature reviews.

More specifically: How do the persuasive elements of literature reviews require forms of judgment that AI systems fundamentally lack?

---

### Human (05:04:37)

It's because: research is always fundamentally risky, it involves the unknown. Specifically, it requires the identification of *gaps* in the literature. An LLM will always predict words within its distribution, as a function of its training data and RLHF. Having an abductive sense (see prior discussion) of the *interesting* gaps is problematic -- especially when those gaps are *unstated* within the literature. There's the tension of "these folks have done relevant work" but "my work is new, interesting, and you should pay attention to it"

Thus the judgement required is threefold:
1. Model-of-mind: is what we are discussing relevant within the domains of the audience? (i.e. is it a salient question to the discipline in question?)
2. Finding the negative space: is this a genuine insight?
3. Questions of utility: is this a *useful* insight?

All of this requires of having a sense of the zeitgeist of the current literature. I've found that due to both atemporality and the regression to the most-popular-words, models are very bad at understanding time. 

Did I answer the question?

---

### Assistant (05:04:53)


Yes, you've answered the question and provided key insights about the relationship between judgment and persuasive literature reviews. Let me summarize the key points from your response:

1. Research inherently involves risk and the unknown - it requires identifying gaps in literature that may be unstated
2. LLMs are constrained to predict words within their distribution (training data + RLHF), making them ill-suited to identify truly novel, unstated gaps
3. The judgment required for persuasive literature reviews is:
   - Model-of-mind: Understanding relevance to a disciplinary audience
   - Finding negative space: Identifying genuine insights
   - Questions of utility: Determining if insights are useful
4. All of this requires understanding the zeitgeist of current literature
5. LLMs struggle with temporality and regress toward the most popular words/views, making them poor at understanding the historical development of disciplines

This connects well to our earlier discussions about AI's judgment deficiencies - particularly the inability to engage in genuine inductive reasoning to find patterns in negative space, and the lack of correspondence with reality that would help determine utility and relevance.

I now have sufficient information to draft subsection 2.3 on the Nature of Research Work, framing it as a persuasive enterprise that requires judgment in ways AI systems fundamentally lack.

Yes, you've answered my question perfectly. The connection between persuasive literature reviews and judgment deficiencies is now much clearer.

My next question: You mention that LLMs struggle with temporality and understanding the zeitgeist of current literature. Could you elaborate on how this specific issue manifests when AI attempts to situate research within scholarly traditions? For example, does it tend to flatten historical development or miss significant paradigm shifts?

---

### Human (05:29:46)

This is literally the thesis of technoscholasticism. Flattening isn't bad -- let's not bring Kuhn into this though. Moreso, it takes the literature, well formatted and written in an academic literature at face value. Its reality is the claims of the literature (by definition, being trained on it, with no other possible source of expertise in its training data). 

Models, by default, do not push back. They don't exhibit Peirce's surprise. They don't have conflict between what they expect and what is real, because they produce only what they expect.

---

### Assistant (05:30:01)


Thanks for that excellent clarification. This connects directly to the technoscholasticism concept and provides a clear link between the judgment deficiencies and literature review problems.

Key points for the subsection:
1. Literature reviews are fundamentally persuasive documents requiring judgment
2. They must identify gaps, demonstrate novelty, and make a case for why readers should care
3. AI systems lack the ability to:
   - Identify interesting gaps in negative space
   - Judge relevance to disciplinary concerns
   - Evaluate the utility of insights
   - Understand temporal development and zeitgeist
4. Their training means they can only recapitulate existing literature without pushing back
5. They accept claims at face value, taking the literature as reality
6. They don't experience Peirce's "surprise" or conflict between expectation and reality

I should structure the subsection to focus on literature reviews as a specific example of research work that requires judgment, connecting back to the judgment deficiencies established in previous sections. 

I'll title it "Literature Reviews and the Persuasive Nature of Research" to better reflect the focus and make it clear this section is about why "Deep Research" products fundamentally misunderstand what research actually is.

Thank you for this clarification. This concept of AI taking literature at face value without pushing back is indeed central to your technoscholasticism thesis.

One final question before drafting: When you describe AIs as missing "the persuasive line that must go beyond simple summarization," could you provide a concrete example of how this manifests in AI-generated literature reviews? Specifically, what would be missing from an AI-generated literature review compared to one created by a human researcher with proper judgment?

---

### Human (06:30:04)

Context and juxtaposition. "The point" -- it's more that the test runs I've made are simple summaries of what's out there. It's lit review by undergrad. It represents: "I've run these searches and these are how they are *shortened*" (note, not summarised). 

thoughts:
1. "Why is this here?" -- there's no sense of selection, about why certain items were chosen. (Obviously, they were chosen as a function of the search results, but... it feels haphazard)
2. "Why is this, by this person, here?" There's no sense of the academic's judgement of: yes, this is an appropriate paper to cite. It will lend authority to preprints (certainly, it will ask first, but given permission, it will treat them as full papers)
3. So: discernment. Basically the sense that reading these words is worth my time. There just is no discernment. Looking at a lit review for this very paper, when the followup prompt to DR was: "Peer reviewed, but preprints by *good scholars* are acceptable. We'll want 2023-2025 for sources that talk to LLM specific technologies. Just give me authors year titles, I'll search for them. (Or DOI if you have it.)" it gave me ... a blog post. There's just no discernment. Moreover, the first blog post was good, from researchers and ethicists on huggingface. The second ... "**Bryant University Library (2023). “ChatGPT: A Library Perspective.”** – *Krupp Library Blog*." is... a pattern match for me saying "it lacks authority" but it's a library blog. (It also got the citation wrong, since the author's name is at the bottom, but whatever). This was not a good response to my question about *authority* because this source is fundamentally not persuasive to scholars. Because it doesn't discern good and persuasive sources from ones that match the words, the utility is diminished.
All of these hold for "research" beyond academic research as well. There is some core problem that people are trying to solve. Without discernment as to the knowledge that the source can have, and the paradata and metadata of the source (how was it written, who for, by whom, how could they know what they know, what is the context of their writing, what was their intended message, how are they situated in the literature?) it means that these things are tools -- useful tools -- but tools none the less. There is none of the self-reflection that allows it to say "Yes, this accomplishes your goal."

---

### Assistant (06:30:24)


This response provides excellent insights into the concrete issues with AI-generated literature reviews. Let me organize the key points:

1. **Lack of selection rationale**: AI doesn't demonstrate why specific sources were chosen beyond surface-level search results matching. There's no underlying logic to the selection process.

2. **Inability to judge source quality**: AI fails to differentiate between authoritative sources and non-authoritative ones. It treats preprints, blog posts, and peer-reviewed articles with the same weight.

3. **No discernment of value**: AI cannot assess whether reading particular sources is worth the reader's time. It provides matches to search queries without evaluating scholarly significance.

4. **Missing context and paradata**: AI fails to consider who wrote the source, how they could know what they claimed, what their motivations were, and how they're situated within the broader literature.

5. **Equating pattern matching with authority**: AI confuses textual patterns that appear authoritative with actual scholarly authority, as demonstrated by including a library blog when asked for "good scholars."

These examples provide concrete manifestations of the judgment deficiency we've been discussing - especially the inability to make normative assessments about what constitutes good scholarship.

For the subsection on Nature of Research Work, I should focus on:
1. The persuasive rather than descriptive nature of literature reviews
2. How this persuasive function requires judgment that AI fundamentally lacks
3. The importance of discernment in selecting and contextualizing sources
4. The ways AI flattens scholarship by treating all text at face value
5. How this connects to technoscholasticism - taking literature at face value without pushing back

The section should be structured to highlight these limitations while explaining what proper research work entails.

Thank you for these detailed examples. I now have sufficient information to draft the "Nature of Research Work" subsection.

From your responses, it's clear that the core issue is discernment - AI systems can collect and reorganize information but fundamentally lack the ability to make value judgments about which sources are genuinely important, authoritative, or worth engaging with. They cannot identify "the point" behind including specific sources or recognize when something should be excluded despite superficial relevance.

The concrete example of AI citing a library blog when asked for "good scholars" perfectly illustrates this problem - pattern matching without genuine understanding of scholarly authority or persuasive value.

I'll draft this subsection focusing on:
1. Literature reviews as persuasive rather than descriptive documents
2. The essential role of judgment in selecting and contextualizing sources
3. The inability of AI to identify genuine gaps and novelty
4. The connection to technoscholasticism - taking texts at face value without critical engagement

Shall I proceed with drafting the subsection now?

---

### Human (06:31:12)

Please give me a paragraph by paragraph outline, looking at claims, warrants, and evidence.

---

### Assistant (06:31:39)


Let me outline the Nature of Research Work subsection with a focus on claims, warrants, and evidence for each paragraph:

Paragraph 1: Introduction and Definition
- Claim: Research work, particularly in literature reviews, is fundamentally persuasive rather than merely descriptive or informative.
- Warrant: Understanding this persuasive nature is essential to recognizing why AI systems fundamentally misunderstand research.
- Evidence: Will reference the marketing of "Deep Research" products that position AI as capable of research.

Paragraph 2: The Dual Purpose of Literature Reviews
- Claim: Literature reviews serve two essential persuasive functions: situating work within disciplinary context and establishing novelty/importance.
- Warrant: These functions require judgment that goes beyond information retrieval and summarization.
- Evidence: Will reference scholarly understanding of literature reviews as rhetorical documents that make claims to disciplinarity and novelty.

Paragraph 3: Judgment in Source Selection
- Claim: Effective research requires discernment in selecting which sources to include and exclude.
- Warrant: This selection process is an intellectual act requiring evaluation of authority, relevance, and persuasive value.
- Evidence: Example of AI citing library blog posts when asked for authoritative scholarly sources, demonstrating lack of discernment.

Paragraph 4: Identifying Genuine Knowledge Gaps
- Claim: Research requires identifying meaningful gaps in existing knowledge - what hasn't been answered or needs reconsideration.
- Warrant: This identification process requires abductive reasoning and understanding of disciplinary zeitgeist.
- Evidence: AI's inability to identify "interesting" gaps due to its fundamental limitation of only predicting within its training distribution.

Paragraph 5: Model-of-Mind and Audience Awareness
- Claim: Effective research requires understanding what questions are salient to the discipline and audience.
- Warrant: This requires model-of-mind capabilities to anticipate how work will be received.
- Evidence: AI's inability to differentiate between genuinely persuasive evidence for a scholarly audience versus pattern-matched content.

Paragraph 6: The Problem of Temporality
- Claim: Research requires understanding the historical development and current state of a field.
- Warrant: AI systems struggle with temporality and flatten historical development.
- Evidence: AI's inability to distinguish between outdated claims and current scholarship, treating all texts as equally relevant regardless of publication date.

Paragraph 7: Connection to Technoscholasticism
- Claim: AI's approach to research exemplifies technoscholasticism - taking texts at face value without critical engagement.
- Warrant: Without the ability to push back against claims or experience surprise at unexpected findings, AI cannot participate in genuine research.
- Evidence: AI's tendency to treat all well-formatted academic text as equally authoritative, with no capability for Peircean surprise or contradiction between expectation and reality.

Paragraph 8: Conclusion - Implications for AI in Research
- Claim: AI systems can be useful tools for information gathering but cannot independently perform genuine research.
- Warrant: The judgment-intensive nature of research work requires human oversight and direction.
- Evidence: Summary of the judgment deficiencies (no discernment, no sense of gaps, no awareness of audience, no temporal understanding) that prevent AI from being more than a tool.

# Nature of Research Work Subsection Outline

## Paragraph 1: Introduction - Research as Persuasion
- **Claim**: Research work, particularly literature reviews, is fundamentally persuasive rather than merely descriptive or informative.
- **Warrant**: This persuasive nature explains why AI's approach to research fundamentally misses the point.
- **Evidence**: Marketing terminology of "Deep Research" products that frame AI as capable of genuine research.

## Paragraph 2: Dual Purpose of Literature Reviews
- **Claim**: Literature reviews serve two essential persuasive functions: situating work within disciplinary context and establishing novelty/importance.
- **Warrant**: These functions require normative judgments about disciplinary boundaries and research value.
- **Evidence**: Your transcript statements on literature reviews answering "Why should we care?" and demonstrating novelty.

## Paragraph 3: Judgment in Source Selection
- **Claim**: Effective research requires discernment in selecting which sources to engage with or exclude.
- **Warrant**: Selection is an intellectual act requiring evaluation of authority and persuasive value.
- **Evidence**: Example of AI citing library blog posts when asked for "good scholars," demonstrating pattern matching without discernment.

## Paragraph 4: Identifying Knowledge Gaps
- **Claim**: Research requires identifying meaningful gaps in existing knowledge.
- **Warrant**: Finding gaps requires abductive reasoning that AI structurally lacks.
- **Evidence**: AI's limitation to predicting within its training distribution versus human ability to notice unexplored areas.

## Paragraph 5: The Flattening Problem
- **Claim**: AI exhibits "flattening" of the literature, treating all sources with equal weight.
- **Warrant**: This flattening stems from training on text without experiential grounding.
- **Evidence**: No sense of "why is this here?" or "why is this, by this person, here?" in AI-generated literature reviews.

## Paragraph 6: Connection to Technoscholasticism
- **Claim**: AI's approach to research exemplifies technoscholasticism.
- **Warrant**: Taking texts at face value without pushing back represents the core issue.
- **Evidence**: AI's inability to experience Peircean surprise or contradiction between expectation and reality.

## Paragraph 7: Conclusion - Implications
- **Claim**: AI systems remain tools that require human judgment for genuine research.
- **Warrant**: The threefold judgment required (model-of-mind, finding negative space, questions of utility) cannot be replicated by statistical models.
- **Evidence**: Summary of discernment failures that prevent independent AI research capability.

---

### Human (06:41:59)

I don't like para 1. Research *writing*, requires a literature review. Besides being informative -- justifying the context, giving the framework, associating with other scholarship, it has a fundamentally persuasive *element*: "This is a problem worth solving, and my research plausibly can solve it." 

Transcripts aren't evidence. They're just my thoughts when recorded. They are claims. (Let me know if I need more links to the literature)

Link para 4 back to earlier discussion about abduction.

This feels like we need more work.

---

### Assistant (06:42:19)


You've provided important feedback on the outline, pointing out several issues:

1. Para 1 mischaracterizes research - it's specifically research writing that requires literature reviews, and the persuasive element is just one part of it (alongside informative aspects).

2. You correctly point out that your transcripts shouldn't be treated as evidence but as claims that need proper academic support.

3. You want a stronger connection to the previous discussion on abduction in paragraph 4.

4. Overall, you feel the outline needs more development.

Let me revise this outline to address these concerns:

1. I'll reframe paragraph 1 to focus on research writing and the literature review's multiple functions.

2. I'll identify actual academic sources needed to support the claims rather than relying on transcripts.

3. I'll more explicitly connect paragraph 4 to the earlier discussion on abductive reasoning.

4. I'll strengthen the overall structure and connections to make a more cohesive argument.

For evidence, I should look at sources that discuss:
- The persuasive nature of literature reviews
- Judgment in scholarly writing
- Abductive reasoning in research
- Source selection as an intellectual act

Let me revise the outline:

You're absolutely right - this outline needs significant revision. Let me rethink the approach:

# Revised Nature of Research Work Subsection Outline

## Paragraph 1: Introduction - Research Writing and Literature Reviews
- **Claim**: Research writing, particularly literature reviews, serves both informative and persuasive functions.
- **Warrant**: Understanding these dual functions reveals why AI approaches to research are fundamentally limited.
- **Supporting Literature Needed**: Academic sources on rhetoric of science/scholarly writing (e.g., Bazerman, Swales)

## Paragraph 2: Beyond Information: The Persuasive Function
- **Claim**: Literature reviews establish that: (1) the research is situated within a discipline and (2) the question has not been adequately answered.
- **Warrant**: These persuasive elements require normative judgments about relevance and novelty.
- **Supporting Literature Needed**: Studies on rhetorical structure of literature reviews (e.g., Hart's "Doing a Literature Review")

## Paragraph 3: Source Selection as Intellectual Act
- **Claim**: Effective research requires discernment in source selection that goes beyond pattern matching.
- **Warrant**: Selection involves evaluating not just content but authority, context, and persuasive value within disciplinary conversations.
- **Supporting Literature Needed**: Work on scholarly judgment in source evaluation (e.g., scholarship from library science on authority)

## Paragraph 4: Abductive Reasoning and Gap Identification
- **Claim**: Research requires identifying meaningful gaps through abductive reasoning.
- **Warrant**: This connects directly to the inductive reasoning deficiency discussed in section 2.2.2.
- **Supporting Literature Needed**: Explicit connection to Peirce's work on abduction cited earlier in the paper

## Paragraph 5: The Problem of Context Flattening
- **Claim**: AI exhibits "flattening" of literature, treating all sources with similar textual features as equivalent.
- **Warrant**: This stems from training on text without human experience of disciplinary context.
- **Supporting Literature Needed**: Work on disciplinary knowledge construction (e.g., Becher & Trowler's academic tribes)

## Paragraph 6: Connection to Technoscholasticism
- **Claim**: AI's approach to research exemplifies technoscholasticism - privileging well-formatted text without critical engagement.
- **Warrant**: This directly connects to correspondence with reality deficit discussed in 2.2.3.
- **Supporting Literature Needed**: Research on critical reading practices in scholarship

## Paragraph 7: Conclusion - Research as Human Judgment
- **Claim**: AI systems remain tools requiring human judgment for genuine research.
- **Warrant**: The essential judgment functions (disciplinary relevance, identification of meaningful gaps, evaluation of utility) cannot be replicated by statistical models.
- **Supporting Literature Needed**: Philosophy of science on research as a human activity

Is this revised approach better aligned with your vision for the subsection? I've noted where we'll need additional academic sources rather than relying on the transcripts as evidence.

---

### Human (07:29:13)

Much better. Give me a todo list for things to get into Zotero, please? Main scholars/search terms?

---

### Assistant (07:29:33)


Let me create a comprehensive Zotero todo list based on the research gaps in our outline. This should include key scholars, search terms, and specific areas where we need literature to support our claims about research work and literature reviews.

For Paragraph 1 (Research Writing and Literature Reviews):
- Charles Bazerman (rhetoric of science)
- John Swales (genre analysis of academic writing)
- Academic writing handbooks on literature reviews
- Search terms: "rhetoric of science" "academic writing genres" "literature review purpose"

For Paragraph 2 (Persuasive Function):
- Chris Hart "Doing a Literature Review"
- Works on rhetorical structure of literature reviews
- Studies on disciplinary differences in literature reviews
- Search terms: "literature review rhetorical functions" "argumentation in literature reviews"

For Paragraph 3 (Source Selection as Intellectual Act):
- Library science scholarship on authority evaluation
- Critical information literacy scholars
- Work on citational practices and politics
- Search terms: "scholarly authority evaluation" "citational practices" "epistemology of citation"

For Paragraph 4 (Abductive Reasoning and Gap Identification):
- Additional works related to Peirce on abduction
- Contemporary applications of abductive reasoning in research
- Search terms: "research gap identification" "abductive reasoning research"

For Paragraph 5 (Context Flattening):
- Tony Becher & Paul Trowler "Academic Tribes and Territories"
- Work on disciplinary knowledge construction
- Research on tacit knowledge in scholarly communities
- Search terms: "disciplinary knowledge construction" "academic communities" "tacit knowledge scholarship"

For Paragraph 6 (Technoscholasticism):
- Research on critical reading practices in scholarship
- Work on hermeneutics in scholarly practice
- Search terms: "critical reading scholarly practice" "hermeneutics research"

For Paragraph 7 (Research as Human Judgment):
- Philosophy of science on human aspects of research
- Work on tacit knowledge in research practice
- Michael Polanyi on personal knowledge
- Search terms: "tacit knowledge research" "human judgment science" "personal knowledge Polanyi"

# Zotero Todo List for "Nature of Research Work" Section

## Rhetoric of Science / Academic Writing
- **Charles Bazerman**: Search for works on rhetoric of science and academic writing
- **John Swales**: Academic discourse analysis, especially "Genre Analysis: English in Academic and Research Settings"
- **Search terms**: "rhetoric of science" "academic writing genres" "literature review rhetorical functions"

## Literature Review Methodology
- **Chris Hart**: "Doing a Literature Review" (key text on purpose of literature reviews)
- **Search terms**: "literature review as argument" "persuasive function literature review" "literature review methodology"

## Source Selection and Authority
- **Patrick Wilson**: "Second-Hand Knowledge: An Inquiry into Cognitive Authority"
- **Library Science journals**: Articles on scholarly authority evaluation
- **Search terms**: "scholarly authority evaluation" "epistemology of citation" "source selection academic writing"

## Abductive Reasoning in Research
- **Additional Peirce scholarship**: Contemporary applications of Peircean abduction
- **Search terms**: "research gap identification methods" "abductive reasoning research practice"

## Disciplinary Knowledge Construction
- **Tony Becher & Paul Trowler**: "Academic Tribes and Territories"
- **Knorr Cetina**: Work on epistemic cultures
- **Search terms**: "disciplinary knowledge construction" "academic communities" "tacit knowledge scholarship"

## Critical Reading Practices
- **Search terms**: "critical reading scholarly practice" "hermeneutics research" "critical literacy academic research"

## Human Judgment in Research
- **Michael Polanyi**: "Personal Knowledge" and "The Tacit Dimension"
- **Harry Collins**: Work on tacit knowledge
- **Search terms**: "tacit knowledge research" "human judgment science" "personal knowledge research"

Would you like me to focus on any particular areas or scholars from this list as we develop the subsection?

---

### Human (07:39:23)

Argh, ok, we are at length limits. Please give me a *very long* message with full context of where we're up to so I can start a new chat.

---

### Assistant (07:39:56)


I'll create a comprehensive summary of our progress so far to help with continuing this work in a new chat. This will include:

1. The overall project status
2. The sections we've completed
3. The current section we're working on
4. The revised outline for the subsection 2.3
5. Sources and references we've discussed
6. Key points from our conversation that should inform the next steps

This will give a complete context for continuing the work in a new chat due to length limitations.

# Comprehensive Project Status Summary

## Overall Project
We are working on the paper "An Absence of Judgment: AI's Limitations in Deep Research tasks," specifically on section 2 which establishes the theoretical framework around judgment in research. We've completed subsubsection 2.2.3 on "Correspondence with Reality" and are now working on subsection 2.3 on "Nature of Research Work."

## Completed Work

### Section 2.2.3: Correspondence with Reality
This section (approximately 800 words) argues that LLMs lack correspondence with reality - the third critical dimension of judgment. Key points:

1. Defined correspondence with reality as "specific and intentional regard for the world that words represent"
2. Introduced "discount Carnapian confirmation" concept to describe how LLMs accumulate textual evidence without evaluation
3. Used Digital Humanities example as concrete evidence of uncritical acceptance of outdated claims
4. Connected to scholasticism with Longwell quotes
5. Identified four historiographical assessment capabilities missing in LLMs:
   - Inability to distinguish claims from trends
   - Failure to consider authorship and temporality
   - Cannot relate claims to experiential knowledge
   - Default position of acceptance rather than skepticism
6. Established structural limitations in LLM information processing
7. Concluded with the "Scholastic fallacy" concept

### Key Sources Used:
- Carnap (1936) on confirmation approach
- Frankfurt (2005) and Hicks (2024) on "bullshit" as indifference to truth
- Longwell (1928) on scholastic reasoning
- Ballsun-Stanton (2024) "Is the 'Calculator for Words' analogy useful for communicating about LLMs?"
- Willison (2023) on prompt injection attacks

## Current Work: Section 2.3 Nature of Research Work

We're developing the structure for this section, focusing on why research (particularly literature reviews) requires judgment that AI fundamentally lacks. Our current revised outline:

### Paragraph 1: Introduction - Research Writing and Literature Reviews
- **Claim**: Research writing, particularly literature reviews, serves both informative and persuasive functions.
- **Warrant**: Understanding these dual functions reveals why AI approaches to research are fundamentally limited.
- **Supporting Literature Needed**: Academic sources on rhetoric of science/scholarly writing

### Paragraph 2: Beyond Information: The Persuasive Function
- **Claim**: Literature reviews establish that: (1) the research is situated within a discipline and (2) the question has not been adequately answered.
- **Warrant**: These persuasive elements require normative judgments about relevance and novelty.
- **Supporting Literature Needed**: Studies on rhetorical structure of literature reviews

### Paragraph 3: Source Selection as Intellectual Act
- **Claim**: Effective research requires discernment in source selection that goes beyond pattern matching.
- **Warrant**: Selection involves evaluating not just content but authority, context, and persuasive value within disciplinary conversations.
- **Supporting Literature Needed**: Work on scholarly judgment in source evaluation

### Paragraph 4: Abductive Reasoning and Gap Identification
- **Claim**: Research requires identifying meaningful gaps through abductive reasoning.
- **Warrant**: This connects directly to the inductive reasoning deficiency discussed in section 2.2.2.
- **Supporting Literature Needed**: Explicit connection to Peirce's work on abduction cited earlier

### Paragraph 5: The Problem of Context Flattening
- **Claim**: AI exhibits "flattening" of literature, treating all sources with similar textual features as equivalent.
- **Warrant**: This stems from training on text without human experience of disciplinary context.
- **Supporting Literature Needed**: Work on disciplinary knowledge construction

### Paragraph 6: Connection to Technoscholasticism
- **Claim**: AI's approach to research exemplifies technoscholasticism - privileging well-formatted text without critical engagement.
- **Warrant**: This directly connects to correspondence with reality deficit discussed in 2.2.3.
- **Supporting Literature Needed**: Research on critical reading practices in scholarship

### Paragraph 7: Conclusion - Research as Human Judgment
- **Claim**: AI systems remain tools requiring human judgment for genuine research.
- **Warrant**: The essential judgment functions cannot be replicated by statistical models.
- **Supporting Literature Needed**: Philosophy of science on research as a human activity

## Key Insights for Section 2.3

From our discussion of literature reviews and research, we've established that:

1. Literature reviews have a fundamentally persuasive element: "This is a problem worth solving, and my research plausibly can solve it."

2. The judgment required for research is threefold:
   - Model-of-mind: is what we are discussing relevant within the domains of the audience?
   - Finding the negative space: is this a genuine insight?
   - Questions of utility: is this a useful insight?

3. AI systems demonstrate critical shortcomings in research:
   - No sense of selection, about why certain items were chosen
   - No sense of academic judgment about appropriate papers to cite
   - Lack of discernment about source quality and relevance
   - Taking literature at face value without pushing back (technoscholasticism)
   - Cannot identify genuinely novel gaps or valuable insights

4. Example of AI's research limitation: when prompted for "peer reviewed sources from good scholars," it included library blog posts, showing pattern matching without discernment.

5. The connection to technoscholasticism: AI takes literature at face value without experiencing Peirce's "surprise" or contradiction between expectation and reality.

6. We need to explicitly connect the discussion of abductive reasoning from section 2.2.2 to the identification of research gaps in this section.

7. We need additional academic literature to support these claims, particularly on:
   - Rhetoric of science and scholarly writing
   - Structure and purpose of literature reviews
   - Source evaluation and scholarly judgment
   - Disciplinary knowledge construction
   - Critical reading practices in scholarship
   - Philosophy of science on research as a human activity

The next step is to develop this section with appropriate academic sources while maintaining your academic register and style.

---
