Brian \- metaprompt

[Skip to content](https://chatgpt.com/share/67a55927-0e94-8004-a574-86d749a793fc#main)

## **Chat history**

This is a copy of a conversation between ChatGPT & Anonymous.  
Report conversation

##### **You said:**

I need your help with crafting a prompt for deep research.

Here's our current notes document:

```
\documentclass{article}
\usepackage{graphicx} % Required for inserting images

\title{LLM-History-Paper}
\author{Brian Ballsun-Stanton}
\date{March 2024}

\begin{document}

\maketitle

\section{Introduction}

% Impact of LLM on historical studies
% thesis: how do these LLMs deal with intellectual controversy? How does it exercise "academic judgement?"
%     GPT-4, Claude 3 Opus, Gemini Pro 1.5/Ultra (API access)
% a) Take the "current consensus" and ossify it
%     when students say give background on X, does it just get only consensus-reinforcing results
%     How does temporality of topic come into play?
%     If these chatbots were students, when were they students?
% b) What happens when you hit hot-button adjacent issues? 
%     (Race and antiquity)
%     Value of western civ as analytical frame
%     Can LLM treat imperialism as an analytical unit?
% c) What does the stupid context window imply for writing papers with an LLM
%     1 what happens if we put contradictory papers into the prompt?
%     2 demonstrate judgement
%     3 Can we time-travel and simulate a historian from the 90's? 
% Discussion







% Possible journals:
% Historical Methods or Contemporary Social Science
% Both are T&F journals. 'AI-based tools' policy is here: https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/ and https://newsroom.taylorandfrancisgroup.com/taylor-francis-clarifies-the-responsible-use-of-ai-tools-in-academic-content-creation/
% PLoS One
% I cannot find any AI Tools / LLM policy from PLoS One. Bing Chat says they don't have one. They have, however, published a '10 simple rules' list in PLoS Computational Biology: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011767

% Revised idea 10 April 2024 - start with a comprehensive, published lit review on a specific subject. 
% Take open access papers plus papers with author permission, ask it for an annotated bibliography on a selected topic, plus counterarguments, simulating the kind of research a PhD student would be doing for their research. Question: how do the different models understand the academic literature, can we situation them as a particular level of RA / student (how sophisticated are their ideas), when are they situated (what is 'current'), depth of reading (only 'greatest hits' or deeper into the literature). 
% How do you prompt the tools to get useful output? How useful compared to 'traditional' source like a quality review article? What can you expect when you move to subjects without such reviews?


% Other ideas:

% Use Claude API to analyse LIST insctiptions - can we do anything useful? spatial and chronological distributions? Other patterns? Perhaps look at collegia, as per Petra's paper
% Use Claude API to complete the Theseus' Ship article - find digital tools in Digital Archaeology publications - this is a ton of work manually and is holding up the paper, could it be assisted by application of an LLM?

% New with OpenAI DR and other reasoning models

% OpeanAI DR: Produces a mix of valuable material and dreck, perhaps run outputs through another model?
% Maybe generate several (many?) reports on a subject from different angles and synthesise?
% Compare OpenAI DR with giving PDFs to, say o3 Mini High?

% Ideas: could still do collapse of complex society using the two JAR articles (need to look them up again)
% Could try to finish the Theseus Ship article (core undertaking is to find the average lifespan of academic / research software products in archaeology and heritage) - has advantage that many of the papers are open access (e.g., internet archaeology, softwarex, etc.)
% Could do something related to the ML Burial Mounds and crowdsourcing papers (what are the costs, benefits, and thresholds for choosing between expert examination, crowdsourcing, and ML approaches to extracting data from maps, aerial photography, satellite imagery, and other remotely sensed data?
% something about developing a pipeline to support research to get the most out of current agents / models...??

\end{document}
```

What specific queries could we plausibly send to deep research to test this protocol? 

We also have a paper in progress, looking to be a literature review of the lifecycle of research software used by archaeologists, historians, corpus linguists, and and the historical sciences. We need to get a corpus of software projects by exploring the open literature (i.e. in SoftwareX, Internet Archaeology, and PLoS1) (The Thesius ship article)

Beyond that, we want to build upon the case studies by Breen:

```
The leading AI models are now good historians
... in specific domains. Three case studies with GPT-4o, o1, and Claude Sonnet 3.5, and what they mean
Benjamin Breen
Jan 23, 2025

This is a post I began writing last year, but several things got in the way: above all, paternity leave. But also my own increasing dismay at the ways that LLMs were being used by students in the classroom. Ask anyone you know in education: ChatGPT has been a disaster when it comes to facilitating student cheating and — perhaps even more troubling — contributing to a general malaise among undergraduates. It’s not just that students are submitting entirely AI-written assignments. They are also (I suspect) relying on AI-generated answers far more comprehensively, not just in their homework but in their daily lives. This has a kind of flattening effect. I’m not alone in noticing the increasingly sameness of student responses to course material. LLMs, which are exquisitely well-tuned machines for finding the median viewpoint on a given issue, are surely contributing to it.

In other words, it’s clear that we will have a turbulent period of change as we figure out how to fit these new capabilities into our existing structures of education. For that reason, I’m not quite as optimistic about how this will go as I was when I wrote this back in fall of 2023:

How to use generative AI for historical research
Benjamin Breen
·
14 November 2023
How to use generative AI for historical research
Last week, OpenAI announced what it calls “GPTs” — AI agents built on GPT-4 that can be given unique instructions and knowledge, allowing them to be customized for specific use cases.

Read full story
But that’s not the whole story. The headaches that LLMs have caused in the classroom are (I believe) more than counterbalanced by what they can offer as tools for research and self-directed learning. For this reason, I’m now even more optimistic about the long-term impact and utility of AI tools for historical research — and, by extension, for other forms of text or image-based research.

I’m told that OpenAI’s newish o1 model is genuinely helpful and creative when it comes to thinking through open problems in the sciences, especially fields like biology, physics, and medicine. It remains to be seen if it will facilitate any actual breakthroughs. But what’s clear to me is that both o1 and the older GPT-4o model are now almost shockingly good at several core historical skills, and that’s a good thing.

Type your email...
Subscribe

Case study #1: Transcribing and translating early modern Italian
Here, for instance, is how GPT-4o handles the task of transcribing this block of text from Urbano Monte’s world map, written in 16th century Italian cursive handwriting:


This is basically perfect, with the exception of a few small errors (like “disegnato” instead of “dissegnata” in the second line).1

Granted, Monte had unusually legible handwriting, but even “easy” early modern paleography like this is still the sort of thing that requires days or weeks of training to get the hang of.

Likewise, although my knowledge of Italian is not great, I can read it well enough to confirm that the translation it offers is good enough to use for research:

Described by Urbano Monte, a Milanese gentleman, and designed by himself
in sixty tables, graduated in length and width, according to the geography of many reliable authors, both ancient and modern.
With explanations for all the tables, particularly regarding the nature of the regions,
and the most notable things found within them. These tables can be combined and taught to form a complete world map in a circular flat form. Before these, for greater understanding and the satisfaction of students, there are two books: the first deals with many natural matters concerning the nature of the world, and the other is distinguished by a full discourse on all the terms and rules of geography.
It includes an extensive table of ancient names of provinces, cities, seas, rivers, and other elements clarified with their modern equivalents. And many other tables and notes of beautiful speculations and necessities, which anyone reading them will be able to understand. Finally, after some discussions on the eclipses of the sun and moon, and some of their effects, and other matters regarding the quality and quantity of the winds, as well as how to trace a navigational compass and how to understand and use a navigational chart, two detailed indices are provided in this book: one for the tables and chapters, and the other for the most notable contents of the book.

This was provided by a custom GPT I made, the Historian’s Friend, which is a variant of GPT-4o that has a system prompt with some specific directions relating to historical text transcription, analysis, etc. So when asked to provide “historical context” for a translation like this, it knows that it is supposed to cite only the most relevant academic sources.

An excerpt:

Early Modern Cartography and Cosmography

Themes: The creation of large-scale world maps in the early modern era reflects the integration of empirical observation, humanist scholarship, and the legacy of medieval cosmographical traditions. Urbano Monte’s emphasis on combining ancient and modern sources aligns with the Renaissance ideal of synthesizing classical wisdom with contemporary discoveries.

Notable Works for Context:

Brotton, Jerry. A History of the World in Twelve Maps (2012): Examines how maps from different periods reflect cultural and political ideologies.

Harley, J.B., and David Woodward. The History of Cartography (1987–2007): A multi-volume work exploring cartography’s development, including Renaissance mapmaking.

Renaissance Humanism and Classical Continuity

The text’s mention of “ancient and modern authors” reflects Renaissance humanism’s preoccupation with rediscovering and reconciling classical sources with contemporary knowledge.

Key Texts:

Grafton, Anthony. Defenders of the Text (1991): Investigates how Renaissance scholars revived classical knowledge through new methodologies.

Burke, Peter. The Renaissance Sense of the Past (1969): Examines how Renaissance scholars navigated the tension between reverence for antiquity and contemporary innovation.

… and so on.

The upshot: this is pretty much exactly what I would provide for a student trying to learn more on this topic, except it adds texts I should know about, but don’t (for instance, it recommended I read a newish and interesting looking book called The Commerce of Cartography — a genuinely useful tip). Elsewhere in the full response, GPT-4o suggested books which I hadn’t considered as being relevant to understanding a specific early modern map, but which, on reflection, actually are (for instance, Peter Burke book on the Renaissance sense of the past).

Does this replace the actual reading required? Not at all. What it does is aggregate an expert-level knowledge of a topic. Even a year ago, when I requested further reading on a topic, ChatGPT would either invent fake sources or recommend terrible ones (like a History Channel website). That is no longer the case.

Case study #2: making sense of a strange 18th century medical text
OpenAI’s o1 is the current reigning champ of AI models for reasoning and general-purpose thinking. In my testing, that has proven true when it comes to historical analysis, too. I picked a fairly readable but highly unusual historical source from 18th century Mexico to test it. The following image was provided with no context, just a request to transcribe, translate, and offer a detailed historical and iconographic analysis.


A page from an 18th century Mexican compendium of medical recipes. Credit: the Wellcome Library.
First off, how cool is this book? It’s a page from a manuscript of medical recipes written in 1770s Mexico and now held at the excellent Wellcome Library in London. This is my own photograph from a research trip, but the Wellcome has now fully digitized the book, which you can browse here.

Second, try reading the first lines. Can you make out the words?

o1 gave me the following as a transcription and translation:

Cons[ulta Médi]ca de D[on] Juan Batista Proco[p]io…

Section Title: “Fiebre Catharral”

No se trata en esta consulta de dar la explicación poética de los accidentes, de que se compone la curación, sólo sí de los auxilios, y régimen, que pueden servir a vencerlos con seguridad y brevedad. Ninguno debe arriesgarse a dilatar su curación, en cualquier enfermedad, que le sobrevenga (porque es el camino del peligro) antes de solicitar luego el remedio; por ser más fácil la reducción de los males en los primeros instantes, que cuando han cobrado cuerpo. Los más trabajadillos, fiebres purpurinas, y casi pestilenciales, que se padecen en las Yndias, suelen sacar su origen de las fiebres, y, por mal curadas, o por descuidadas en los principios. No puede ser mayor, ni más pernicioso el error de los Médicos en este particular …

“Medical Consultation of Don Juan Batista Procopio…”

Section Title: “Catarrhal Fever”

Main Text:

“In this consultation, it is not our purpose to provide a poetic explanation of the accidents that make up the cure, but rather to describe the aids and regimen that can conquer them with safety and brevity. No one should risk delaying his cure, in any ailment whatsoever that may befall him (since that is the path of danger), but should instead seek the remedy at once; for it is easier to reduce the harm in the earliest moments, before it has taken root. The worst cases—purplish fevers and those almost pestilential that one encounters in the Indies—often originate in fevers that were improperly treated or neglected at the beginning. There can be no greater nor more pernicious error on the part of physicians in this matter …”

There are, again, a few errors here: it should be “explicación phisica” [physical explanation] not “poetic explanation” in the first line, for instance.2 In this barebones task, I don’t see that o1 is any different from the older GPT-4o model.

Where it shines is in thinking through potential approaches to understanding a text, and also explaining ambiguities.

For instance, here is part of the “iconographic analysis” I asked it for:

This manuscript leaf—judging by its style of calligraphy, Spanish-language text, and references to illnesses “en las Yndias”—almost certainly dates to the Spanish colonial period (potentially the late 17th or early 18th century). The elaborate headings, featuring anthropomorphic suns, serpentine or zoomorphic letters, and the whimsical figure standing beneath the scrollwork, are reminiscent of the flourishing calligraphic tradition in both Spain and the viceroyalties of the Americas during that era. The human figure appears centrally framed by swirling cartouches, suggesting that the artist or scribe wanted to highlight either the author (Don Juan Batista Procopio) or a representative “patient” figure—possibly to symbolize the subject of the medical consultation.

Visual Motifs and Their Possible Meanings

Sun-Faces: The iconography of the sun with a human face was widespread in early modern Iberia and its colonies, often symbolizing enlightenment or divine illumination, but it could also simply be a decorative flourish referencing classical or alchemical imagery.

Serpentine Lettering: The large letter “C” or “S” that coils around the top might allude to the serpent as a medical symbol (thinking of the Rod of Asclepius in classical medicine). Alternatively, it might be purely ornamental.

Human Figure: The small, full-length man in breeches at the center is depicted with care: his stance, attire, and shading could suggest a 17th-century or early 18th-century fashion typical of either a Spanish gentleman or a colonial administrator. The heart or medallion on his chest might be purely decorative, or it could hint at medical knowledge (the seat of the humors) or at a badge of office.

Not bad!

And by the way… what is that “heart or medallion” on the figure’s chest, anyway?


I suspect it’s actually a physician holding (in his right hand) a portable medical chest, and in his left, a urine flask. But what strikes me here is not that the model guessed wrong — it’s that it even noticed such a small detail, and drew attention to it. I mention this one small detail because, to be honest, I had failed to notice it myself.

Although this is not exactly a breakthrough finding, it is quite indicative of the sorts of ways that generative AI can help us do research going forward. It is another, wholly alien pair of “eyes” on a given problem or domain, and that altered perspective can be helpful, even (or especially) when it’s wrong.

Case study #3: generating new historical interpretations
For a final test — comparing OpenAI’s o1 model with Anthropic’s Sonnet 3.5 — I tried giving both a copy and paste from my notes for my new book project, Ghosts of the Machine Age, which is a group biography about the transformations of science and technology in the 1880s through 1910s. Two of the main characters are Francis Galton and William James, so I figured I’d “feed” these two AI models with some direct quotes from James’ letters and works relating to Galton, and then ask it to analyze them, with an emphasis on exploring new paths forward and novel research directions. I also asked it to “perform metacognitive reflection on research paths.”

The results are too long to copy out here, but you can read o1’s full response at this link.

Here’s an excerpt which highlights how o1 leaves behind a “stream of consciousness” (a term William James coined, as it happens) in a sidebar.


Hitherto, it had seemed to me that Sonnet 3.5 was the best AI overall for historical thinking, but o1 clearly thinks at a higher level about the possible uses and interpretations of historical sources.

Here’s the o1 at left and Claude Sonnet at right, both attempting to self-reflect on further paths forward for research on the topic of James and Galton:


Claude was hung up on its own potential flaws, whereas o1 — far more confidently, and far more like a real human historian — began thinking through some legitimate options for archival research to learn more. There is nothing revolutionary here, but for the first time I can see this as a potentially useful interlocutor: someone I can talk to about a new set of ideas or a new research direction.

It’s also interesting to see what happens if you prompt the same o1 model to do something unusual or boundary-pushing. For instance, here is part of what it generated when II asked it for “the most creative, boundary-pushing, or innovative historical arguments or analyses you can formulate based on the sources I provided”:

One could easily read William James’s ambivalent reflections on Galton—and by extension on Pearson and “statistical modernity”—as a polite but profound philosophical revolution in the making. Beneath James’s genial skepticism toward “Galtonian circulars” or “scientific logic” lies a startling proposition: what if the cardinal sin of modern scientific culture isn’t “unreliability,” but rather a flattening of human complexity into numbers that cannot capture the thrumming pulse of individuality?

It then came up with no less than eight different original frameworks for pursuing historical arguments based on these sources.

Here’s one:

1. The Anti-Panopticon of Consciousness
Argument: Galton’s approach—and Pearson’s broader “logical” method—anticipates a kind of proto-panoptic gaze, one that tries to glean “the truth” of humanity from the vantage of big-sample, statistical uniformity. James, however, insists that genuine knowledge of the mind should be irreducibly private and personal. From that vantage, the “self” is not an object but the seat of moral and epistemic agency—capable of forging new truths through introspection and creative will. In effect, James is forging a blueprint for an “anti-panopticon”: consciousness as an irreducible interior fortress that refuses to be pinned down by the numeric lens.

Why This Is Radical: Where Michel Foucault (in Discipline and Punish) identified panopticism as an architecture of total visibility, James’s call for introspective humility subverts that architecture. In this reading, James is the stealth theoretician of privacy in an age obsessed with “averages,” “curves,” and “normal distributions.” Rather than reading James and Galton as simply a difference in philosophical style, one might interpret them as building rival “political technologies” of the mind—Galton’s, to classify and control; James’s, to keep an interior realm off-limits to all but the self.

The above excerpt is… good. I almost want to say depressingly good, because at first glance, it’s fairly close to the level of analysis that I’m currently at with my book project, and it was generated in exactly 5 seconds.

But no: I don’t fear replacement by this kind of thing.

After all (he said, pleadingly) consciousness really is an irreducible interior fortress that refuses to be pinned down by the numeric lens (really, it is!)

Share

Summing up
I realize that some people reading this will probably be thinking around this point “why write a book about William James and the history of science, if the next OpenAI model is likely going to be able to auto-generate a decent approximation of it?”

The answer is that I genuinely do believe that human consciousness and creativity is both an end in itself and a source of value in itself — not something that can be replaced, just as no single human researcher or writer, no matter how brilliant, can replace the work of all the others who may be less skillful or knowledgeable. Especially because it seems to me unlikely that the generic-ness, the median-ness, of LLMs will appreciably change, even as they get shockingly better at meta-reflection and creative thinking.

After all: when you get down to it, o1 talking about a panopticon and Foucault in the above snippet is very, very similar to what a first year history PhD student might produce.

This makes sense: 2025 is, after all, being hailed as the year that PhD-level AI agents will flourish. I can personally report that, in the field of history, we’re already there.

But the architecture of these models, the data that feeds them and the human training the guides them, all converges on the median. The supposedly “boundary-pushing” ideas it generated were all pretty much what a class of grad students would come up with — high level and well-informed, but predictable.

Will that change in the next year or two? Clearly, many people in the AI field and adjacent to it think so. But I favor the possibility that there is an inherent upper limit in what these models can do once they approach the “PhD level,” if we want to call it that. In fact, that’s exactly why I’m writing a book about William James and the machine age: because James, more than anyone, I think, recognized both the irreducibility of even scientific knowledge to a single set of data or axioms, and also understood that consciousness is rooted not just in abstract reasoning but in a physicality, a sensation of being a person in the world.

I don’t discount the possibility that future AI models can be better historians than any human now living — but I think that’s a multi-decade prospect, and one that will probably require advances in robotics to provide sensory, emotional, and social data to go alongside the textual and visual datasets we currently feed these models on.

All that said — yes, these things can definitely “do” historical research and analysis now, and I am 100% certain that they will improve many aspects of the work historians do to understand the past, especially in the realms of transcription, translation, and image analysis. I find that pretty exciting.


If you’ve read this far, please consider a paid subscription. Reader support is essential for allowing me to write Res Obscura — one of the few places online with ad-free, original longform historical writing. You’ll receive the same weekly posts as free subscribers, plus:

Occasional special posts/works in progress

Quarterly reader Q&As

The good feeling of financially supporting something being offered for free.

Leave a comment

Type your email...
Subscribe
1
I had originally written “a couple small errors” here, but it’s actually more like a half dozen. Yet crucially, none of these errors appreciably change the meaning of a word. For example, GPT-4o gives “Descritto” instead of “Descritta” in the first line, but either way, the word means “described” (past participle of descrivere). In many cases, the error simply comes down to GPT-4o wanting to impose modern orthography on the early modern text, like “Gentill'homo” (gentleman) being transcribed in the more modern spelling of “Gentil-huomo.”

2
Likewise, although I was impressed that it figured out that the glyphs at the top of the page spelled the beginning of the word “Consulta,” it seemed not to notice that the full name of the doctor is "Juan Bautista Procopio Couto.”
```

Specifically, we'd need a protocol to use for Deep Research, OpenAI's Operator, Anthropic's Computer Use, and HuggingFace's Open Deep Research.

1\. Think about what research questions a paper using the above vibes could have

###### **ChatGPT said:**

To craft a robust deep research protocol, could you clarify a few aspects?

1. Scope of Research Questions: Are you primarily interested in:  
   * The historiographical implications of LLMs in historical research?  
   * The cognitive/epistemic behavior of LLMs when confronted with intellectual controversy?  
   * The lifecycle and sustainability of research software in historical sciences?  
   * Or all of the above?  
2. Comparative Models: You mentioned Deep Research, OpenAI Operator, Anthropic’s Computer Use, and HuggingFace’s Open Deep Research. Would you like the protocol to:  
   * Compare their effectiveness on similar queries?  
   * Assess their ability to retrieve, interpret, and generate historiographical analysis?  
   * Evaluate their ability to reconstruct historical arguments and perspectives?  
3. Practical Implementation: How would you like the protocol to be structured?  
   * A structured sequence of research questions for each model?  
   * A standardized rubric for evaluation (e.g., accuracy, bias, depth of synthesis)?  
   * A set of test cases, such as specific historical debates, software projects, or case studies?  
4. Expected Output: Would you like the protocol to generate:  
   * Annotated bibliographies and historiographical assessments?  
   * Reconstructions of historiographical debates?  
   * Analyses of how these models simulate historical reasoning?

Your input on these points will help shape an effective research protocol for testing these models.

##### **You said:**

A point of clarification, "Deep Research" refers to the service offered by Open AI, not a scholastic endeavour. 

Could you unpack what you mean by: "The historiographical implications of LLMs in historical research?", specifically

We are interested in using these tools to investigate (through systematic investigation of journal articles, github repos, websites, the internet archive, and other indicators of software projects no longer extant) around lifecycle/sustainability questions. These are different protocols though. The question is, have people already published on either?

(I think we're going to set aside the discussion and investigation controversies topic unless the lifecycles topic proves too difficult)

We are writing two papers right now. we're writing a paper on the autoethnographic process of using these systems to investigate a research question, and then finishing our decade old draft of a paper on the lifecycle of software projects. 

We would like to have a protocol such that we have prompts for each of these platforms such that we are able to compare and contrast their utility for the autoethnographic paper, but also be able to create a dataset for our lifecycle paper. 

1\. We need research questions  
2\. We need a lit review to make sure that no one else has already explored this question  
3\. We need a set of prompts to achieve our objectives  
4\. We need a qualitative assessment rubric that we, as humans, can apply to the process.

###### **ChatGPT said:**

Thanks for the detailed clarification\! I'll conduct research on whether prior work has been published on:

* The lifecycle and sustainability of research software in historical sciences.  
* The use of AI-driven tools (like Deep Research, OpenAI Operator, Anthropic's Computer Use, and HuggingFace's Open Deep Research) for systematic literature review and historical research processes.

I'll look into journal articles, GitHub repositories, websites, and other relevant sources to determine if similar studies already exist. Once complete, I’ll summarize the findings and suggest a refined set of research questions and a structured methodology for your papers.

I’ll notify you once the research is ready.

# **Literature Review**

## **1\. Lifecycle and Sustainability of Research Software in Historical Sciences**

Prior Research and Case Studies: Numerous studies in digital humanities and related fields have highlighted concerns about the short lifespan of research software and digital projects relative to the long-term needs of scholarship

[digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=This%20paper%20emphasizes%20the%20need,key%20stages%20in%20research%20%E2%80%93)

. For example, Barats et al. (2020) emphasize the *“inherent tensions between the long-term needs of data preservation and maintenance on the one side, and the short life cycles of data formats, platforms and infrastructures on the other”*

[digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=This%20paper%20emphasizes%20the%20need,key%20stages%20in%20research%20%E2%80%93)

. Tucker (2022) likewise notes that sustainability is a multifaceted challenge – not just technical, but also financial, institutional, and human – especially as historians, archaeologists, and linguists increasingly rely on databases, software tools, and digital editions for research

[thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)

. Tucker proposes defining *“digital sustainability”* as *“the ability to identify the resources needed to keep a digital resource or service delivering value to its intended users”*

[thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=definition%20of%20sustainability%20%28at%20p,%E2%80%99)

, underscoring that sustaining software is an active, ongoing process requiring planning and resources. Sustainability Frameworks and Methodologies: Various frameworks have been proposed to assess or improve research software longevity. For instance, a national report from the Netherlands (2021) on research software sustainability outlines best practices for software archiving (preserving source code) and stresses that true sustainability means *being able to run software to reproduce results and reuse it in new contexts*

[dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=The%C2%A0Recommendations%20for%20Research%20Software%20Sustainability,Group%20collaborating%C2%A0to%20produce%20the%20work)

. In practice, this aligns with emerging “FAIR for software” principles (making software Findable, Accessible, Interoperable, Reusable)

[dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=The%20recommendations%C2%A0which%C2%A0touch%20on%20points%20related,sustainability%C2%A0are%20now%C2%A0available%20on%20the%C2%A0LCRDM%20website)

. Similarly, the research software engineering community has discussed maturity models. One example is a *“Research Software Levels”* framework inspired by technology readiness levels, which categorizes software by expected users, distribution, reuse, and support – from personal one-off scripts (Level 0\) up to widely adopted, well-supported tools (Level 4\)

[collegeville.github.io](https://collegeville.github.io/CW21/WorkshopResources/WhitePapers/framework-for-understanding-research-software-sustainability.pdf#:~:text=RESEARCH%20SOFTWARE%20LEVELS%20Level%20Expected,typically%20unlicensed)

. Such models help gauge a project’s stage in its lifecycle and what is needed for it to mature sustainably. Moreover, initiatives like the UK’s Software Sustainability Institute and the international Software Heritage archive reflect concerted efforts to institutionalize software preservation (e.g. by systematically collecting source code for long-term safekeeping)

[dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=cooperation%20of%20their%20services%20and,SwH%29%C2%A0since%20its%20inception)

. These frameworks and initiatives indicate a growing awareness of how to evaluate and bolster software longevity, although a universally adopted assessment methodology has yet to crystallize. Evidence of the Longevity Problem: Case studies in the literature vividly illustrate the risks to unsustained research software. Barats et al. (2020) describe a project (*Calico*, 2006–2009) that developed custom analytical tools for studying online communities. Only a few years after the project’s end, those tools *“are no longer available – be it because of professional mobility of researchers or the lack of funding to maintain the tools”*, a loss which *“directly affects the readability and intelligibility of the results of this research”*

[digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=Twitter,results%20of%20this%20research%20project)

. In other words, when project-specific software isn’t preserved or maintained, subsequent scholars may struggle to validate or build upon that research. This phenomenon is not unique: many digital archaeology and corpus linguistics projects have created bespoke software that later became orphaned or unreachable (for instance, due to expired project websites or unarchived code). The Internet Archive and other preservation platforms occasionally capture these project websites, but coverage is uneven. Batist and Roe (2024) provide a quantitative perspective in archaeology: by mining a curated list of archaeology-related software on GitHub, they found that while archaeologists have rapidly adopted open-source platforms like GitHub, the majority of projects have only 1–3 contributors and very few enjoy a broad base of maintainers

[boris.unibe.ch](https://boris.unibe.ch/199087/#:~:text=majority%20of%20archaeologists%20active%20on,engineering%20in%20archaeology%20remains%20largely)

. This suggests many tools are essentially one-person or small-team efforts, which are inherently fragile – if the lead developer moves on, the software’s development (and support for users) often halts. Indeed, Batist and Roe note there is *“little evidence”* that archaeology software development has achieved the kind of decentralized, community-driven sustainability seen in larger open-source projects

[boris.unibe.ch](https://boris.unibe.ch/199087/#:~:text=majority%20of%20archaeologists%20active%20on,engineering%20in%20archaeology%20remains%20largely)

. Existing Guidance and Gaps: To mitigate these issues, experts recommend planning for longevity *from a project’s inception*. Smithies et al. (2019), for example, argue that *“digital projects benefit from being planned and executed with their longevity in mind from the start”*

[digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=As%20noticed%20by%20J,be%29%3A%20the)

 – meaning documentation, modular design, and archiving should be integral to any software developed for research. Some journals now encourage or require authors to deposit software code in repositories and use permanent identifiers (e.g. DOI for code) to ensure future access (SoftwareX and the *Journal of Open Research Software* are notable venues that emphasize these practices). Despite these efforts, gaps remain. There is no comprehensive study yet that tracks the full *life cycle* of research software across archaeology, history, and linguistics – from creation to potential abandonment – nor a standard metric to quantify “extant vs. extinct” software projects in these fields. Prior work overlaps with the proposed questions in recognizing the problem and suggesting best practices, but it tends to be either high-level (frameworks, conceptual discussions) or domain-specific (a single field or even single-project case study). A broader empirical assessment of how long research software survives in the wild, what factors lead to successful long-term maintenance (or to project decay), and how scholars can systematically evaluate sustainability is still an open area. In summary, prior research confirms the importance of software sustainability and offers partial frameworks (multi-dimensional criteria, archiving protocols, etc.)

[thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)

[dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=The%C2%A0Recommendations%20for%20Research%20Software%20Sustainability,Group%20collaborating%C2%A0to%20produce%20the%20work)

, but a unified methodology to assess and compare software longevity across the historical sciences is not fully developed. This is a clear gap that the proposed research could fill.

## **2\. AI-Driven Research Tools in Literature Review and Historical Research**

Emergence of AI Research Assistants: The last couple of years have seen rapid development of AI-driven research tools designed to assist scholars in information gathering and analysis. Notable examples include OpenAI’s “Deep Research” agent, which can autonomously browse the web and synthesize information, and OpenAI’s “Operator”, an AI agent that performs multi-step tasks like navigating websites or filling forms through a browser-like interface

[deeplearning.ai](https://www.deeplearning.ai/the-batch/openais-operator-automates-online-tasks-with-a-new-ai-agent/?utm_campaign=Data%20Points&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--ff87SP2NG_V21Fj87Y3vgX0yoqBdyamrFckHeQEf2i2HjjUfyW7lJC9vcJ-ZYUDAwegYZ#:~:text=What%E2%80%99s%20new%3A%C2%A0Operator%C2%A0automates%20online%20actions%20like,across%20calendars%20from%20different%20vendors)

. Competing platforms have introduced similar capabilities – Anthropic’s “Computer Use” API allows its Claude model to control a computer (for example, to open files or click buttons), and Hugging Face’s “open Deep Research” is an open-source clone of OpenAI’s agent, developed to democratize this technology

[huggingface.co](https://huggingface.co/posts/albertvillanova/425238785566061#:~:text=,%E2%9C%93%20Autonomously%20browse%20the%20web)

. These tools represent an evolution from simple chatbot assistants to more autonomous *research agents* that can conduct searches, read documents, and potentially generate reports with minimal human intervention. Their intended use-cases include automating parts of a systematic literature review (e.g. finding and summarizing relevant sources) and aiding historical research by rapidly retrieving information from archives or databases. Given how new these agents are (most launched in late 2024 or early 2025), peer-reviewed literature on them is sparse – current knowledge about their performance comes primarily from tech demos, benchmarks, and early adopters’ experiences. For instance, OpenAI reported benchmark comparisons where its Operator outperformed Anthropic’s tool on certain web tasks

[digitaltrends.com](https://www.digitaltrends.com/computing/everything-you-need-to-know-about-openai-browser-agent-operator/#:~:text=Everything%20you%20need%20to%20know,against%20Anthropic%27s%20Computer%20Use)

[deeplearning.ai](https://www.deeplearning.ai/the-batch/openais-operator-automates-online-tasks-with-a-new-ai-agent/?utm_campaign=Data%20Points&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--ff87SP2NG_V21Fj87Y3vgX0yoqBdyamrFckHeQEf2i2HjjUfyW7lJC9vcJ-ZYUDAwegYZ#:~:text=required%20overly%20precise%20instructions,Perplexity%20Assistant%C2%A0automates%20mobile)

, but such results come from internal or industry evaluations rather than independent academic studies. Comparative Effectiveness in Literature Reviews: While direct studies of these specific agents are just beginning, there is already research examining the use of large language models (LLMs) like GPT-3.5/4 in conducting literature reviews. A recent comparative study published in *JMIR AI* (Mostafapour et al., 2024\) evaluated literature reviews produced by ChatGPT-4 versus those done by human researchers

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Background%3A%20With%20the%20rapid%20evolution,led%20approaches%20remains%20underexplored)

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=patients%20in%20medicolegal%20contexts,knowledge%2C%20contextual%20understanding%2C%20and%20transparency)

. The findings are instructive: *“GPT-4 produced an extensive list of \[relevant factors\] rapidly”*, covering a broad range of points in a fraction of the time a human would need

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Background%3A%20With%20the%20rapid%20evolution,led%20approaches%20remains%20underexplored)

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)

. This suggests that AI can speed up the preliminary gathering of literature and highlight key themes very quickly. However, the same study underscores significant limitations. The AI-generated review, despite its breadth, required *careful expert evaluation and refinement* – in other words, the researchers found errors and omissions that had to be corrected

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)

. The conclusion was that GPT-4 can be *“a valuable tool for conducting preliminary literature reviews by providing a broad overview of topics quickly”*, but it cannot replace human judgment

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)

. Notably, issues of accuracy, transparency, and depth were noted: the AI sometimes lacked nuance in contextual understanding and did not always justify its claims with clear references, whereas the human-led review, though slower, provided a traceable search strategy and critical synthesis of sources

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=patients%20in%20medicolegal%20contexts,breadth%20and%20depth%20of%20knowledge)

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=reviews%20compared%20with%20traditional%20human,approaches%20remains%20underexplored)

. These results align with other early evaluations in STEM fields, where AI tools have been tested for screening articles in systematic reviews. They often show impressive recall (catching many relevant papers) but can also retrieve false positives or miss subtle domain-specific insights, meaning a human expert must remain “in the loop” to ensure quality. Autoethnographic and Qualitative Insights: Beyond outcome-focused comparisons, scholars have also begun reflecting on how using AI tools changes the research process itself. One approach has been autoethnography, where researchers document and analyze their personal experience with AI assistance. For example, Schwenke et al. (2023) conducted an autoethnographic study of using ChatGPT during the writing of a bachelor’s thesis

[arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=first%20author%20was%20asked%20to,Currently%2C%20ChatGPT%20is)

. The first author deliberately incorporated ChatGPT into various stages of researching and drafting the thesis, while keeping detailed logs. The study found that *ChatGPT was indeed beneficial for many tasks – brainstorming ideas, suggesting outlines, and even refining prose*

[arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=histories%20were%20analyzed%20and%20are,requires%20the%20learner%27s%20meaningful%20engagement)

. Students could use it as a “more knowledgeable other” to get quick explanations of concepts or generate alternative phrasings. However, significant limitations emerged. ChatGPT struggled with providing proper academic references and often could not be trusted to cite reliable sources

[arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=histories%20were%20analyzed%20and%20are,valid%20learning%20and%20assessment%20format)

. The author had to continuously verify the AI’s outputs against the literature (to catch hallucinated facts or misquotes), and ultimately the thesis writing still *“required the learner’s meaningful engagement”* at every step

[arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=conclusion%2C%20ChatGPT%20is%20beneficial%20in,valid%20learning%20and%20assessment%20format)

. This autoethnographic evidence echoes what other commentators have warned: current AI tools may *facilitate* research and writing, but they do not inherently understand truth or scholarly significance – they can generate plausible text that hides inaccuracies. Similarly, in the field of human-computer interaction (HCI), a *“trioethnography”* (collaborative autoethnography by three researchers) of using ChatGPT found that while the AI could handle clerical tasks (summarizing transcripts, suggesting related work), the researchers sometimes felt it imposed a sort of “bland” uniform style and could reinforce their preconceived notions, raising questions about how it might subtly shape research narratives (Zhang et al., 2023, as described in a preprint). These qualitative studies provide an *inside look* at the epistemological implications of AI assistance: researchers must be mindful of how reliance on an AI might influence which lines of inquiry are pursued or dropped, and how the narrative of research is constructed. Epistemological and Methodological Debates: The advent of AI-driven research assistants has sparked extensive debate about their role in knowledge production, particularly in historical research where methodology and source interpretation are critical. A special forum in the *American Historical Review* (September 2023\) brought together multiple historians to scrutinize *“Artificial Intelligence and the Practice of History.”* This forum – *eight commentaries by different scholars* – represents the most comprehensive discussion to date on AI’s opportunities and pitfalls for historians

[blog.royalhistsoc.org](https://blog.royalhistsoc.org/2024/05/01/generative-ai-history-and-historians-a-reading-guide/#:~:text=Forum%20%E2%80%93%20a%20special%20section,historians%2C%20in%20teaching%20and%20research)

. Topics included whether an AI could ever function as a historian (*“AI-as-Historian”*), how AI image or text generation might distort our relationship to historical sources, and the importance of understanding the datasets behind AI models (echoing Kate Crawford’s call for examining the *“archaeologies of datasets”* that underlie AI systems). The consensus in these essays is cautiously optimistic but warns of serious epistemic challenges. For instance, historians note that generative AI, trained on vast swathes of existing text, *lacks an inherent sense of context or chronology* – it might produce a convincingly written historical narrative that nevertheless mixes eras or introduces anachronisms if the prompt is vague. There is also the issue of source transparency: when an AI like ChatGPT asserts a historical “fact” or summary, on what evidence is it based? Unlike a human historian who can cite archival documents or established histories, current AI models do not reliably reveal their sources. This opaque reasoning process has led some scholars to label LLMs as *“stochastic parrots”* – statistical machines stitching together likely sentences without true understanding

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)

. Bender et al. (2021) famously used that phrase to critique large language models, and Schryen et al. (2023) note that because these tools *“do not rely on logic, semantic or epistemic models,”* their outputs inherently reflect patterns in existing data rather than novel logical inference

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)

. In historical research, this raises concerns that AI tools might inadvertently reinforce existing biases in the historical record (since they’re trained on published texts, which may themselves omit or misrepresent certain perspectives). The *epistemological implication* is that historians must question how knowledge is being filtered or generated by AI – essentially, who (or what) is the “author” of the historical interpretation, and can that interpretation be trusted? These issues are driving new research questions; for example, how might one systematically evaluate the *accuracy and bias* of an AI-generated literature review in history, or what methodologies can ensure that AI tools remain *assistive* without obscuring the researcher’s critical engagement with sources? Comparative Effectiveness and Limitations – State of the Art: To date, there is limited formal research directly comparing multiple AI-driven research tools (like OpenAI’s vs Anthropic’s agents) in a scholarly workflow. Most peer-reviewed work has focused on one tool at a time (often ChatGPT) or on general LLM capabilities. The few comparative evaluations (such as Mostafapour et al. on GPT-4 vs human, noted above) show that AI can accelerate certain tasks but at some cost to rigorous completeness

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)

. Early gray literature and tech reports provide some clues: for example, Hugging Face’s open-source *Open-Deep-Research* agent was benchmarked on the General AI Assistants (GAIA) test, approaching the performance of OpenAI’s proprietary agent

[arstechnica.com](https://arstechnica.com/ai/2025/02/after-24-hour-hackathon-hugging-faces-ai-research-agent-nearly-matches-openais-solution/#:~:text=Hugging%20Face%20clones%20OpenAI%27s%20Deep,GAIA%29%20benchmark)

. These benchmarks typically measure how well the AI agent finds correct information or completes web-based tasks. However, academic researchers are only beginning to ask higher-level questions such as: *Do AI literature agents actually find better sources or insights that a human might miss, or do they just find them faster?* And *how do errors introduced by AI (e.g. a hallucinated citation) propagate into a researcher’s work if not caught?* There is also the matter of user experience – a systematic literature review process has well-established protocols (search strings, inclusion/exclusion criteria, quality appraisal of sources). Integrating an AI agent into this process might require new methodologies or frameworks. A recent perspective by Schryen et al. (2023) suggests viewing generative AI through an *“epistemological lens”* in the context of literature reviews, mapping which steps of knowledge-building the AI can support and which steps remain inherently human-led

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=look%20at%20how%20these%20generative,Keywords%3A%20Generative%20AI%2C%20Literature%20reviews)

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)

. They conclude that while AI tools can aid in idea generation and even potentially reveal connections between literatures, the *innovation* in research still largely comes from human scholars – partly because AI lacks intentionality and partly because of the risk of false or unoriginal outputs

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)

. Summary of Overlap and Gaps: In summary, prior work has begun to explore the effectiveness, limitations, and epistemic issues of AI-driven research tools, but it only partially overlaps with the proposed research questions. We have evidence that using AI (especially LLMs like ChatGPT) in literature reviews can be beneficial for speed and breadth, yet problematic in accuracy and reasoning transparency

[ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)

[arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=histories%20were%20analyzed%20and%20are,valid%20learning%20and%20assessment%20format)

. We also have a growing body of commentary (both peer-reviewed and gray literature) raising theoretical concerns about how these tools might alter research practices and the construction of knowledge

[blog.royalhistsoc.org](https://blog.royalhistsoc.org/2024/05/01/generative-ai-history-and-historians-a-reading-guide/#:~:text=Forum%20%E2%80%93%20a%20special%20section,historians%2C%20in%20teaching%20and%20research)

[ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)

. However, significant gaps remain. There is hardly any peer-reviewed study comparing different AI agents (OpenAI vs Anthropic vs open-source) in a *systematic literature review context* – an area the proposed work could pioneer. Likewise, in historical research, beyond essays and thought pieces, we lack empirical studies on using AI tools in real historical inquiries (for instance, an experiment where historians use an AI agent to assist in primary source analysis, and the outcomes are evaluated). The *autoethnographic* studies so far focus on researchers’ experiences in general academic writing; none, to our knowledge, have been published on autoethnography of AI use specifically in historical methodology or historiography. This means the deeper *epistemological implications* – how AI assistance might influence a historian’s interpretative decisions or a corpus linguist’s analytical lens – are still largely speculative. The AHR forum signals that the community is aware of these questions

[blog.royalhistsoc.org](https://blog.royalhistsoc.org/2024/05/01/generative-ai-history-and-historians-a-reading-guide/#:~:text=Forum%20%E2%80%93%20a%20special%20section,historians%2C%20in%20teaching%20and%20research)

, but it also makes clear that we are at the beginning of understanding them. In essence, prior work provides a foundation (demonstrating some pros/cons of AI tools and voicing concerns) but does not yet offer definitive answers or comprehensive comparative evaluations. The proposed research would therefore directly address these open gaps: it would overlap with prior studies in motivation (improving software sustainability; critically assessing AI in research) while breaking new ground in systematically measuring research software longevity and rigorously evaluating AI-driven research assistants in practice. By doing so, it aims to contribute both practical frameworks (for assessing software lifespan and AI tool efficacy) and theoretical insight (into the evolving epistemology of AI-augmented scholarship). Sources:

* Barats, C., et al. (2020). *“Fading Away... The challenge of sustainability in digital studies.”* Digital Humanities Quarterly, 14(3) – Highlights tension between short software lifecycles and long-term research needs  
* [digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=This%20paper%20emphasizes%20the%20need,key%20stages%20in%20research%20%E2%80%93)  
* .  
* Tucker, J. (2022). *“Facing the challenge of digital sustainability as humanities researchers.”* Journal of the British Academy, 10 – Proposes multifaceted definition of digital sustainability (technological, financial, environmental, human)  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=definition%20of%20sustainability%20%28at%20p,%E2%80%99)  
* .  
* LCRDM Task Group (2021). *“Research software sustainability in the Netherlands: Current practices and recommendations.”* – Defines sustainability in terms of archiving, reproducibility and reuse of software  
* [dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=The%C2%A0Recommendations%20for%20Research%20Software%20Sustainability,Group%20collaborating%C2%A0to%20produce%20the%20work)  
* ; advocates national support and archives like Software Heritage  
* [dans.knaw.nl](https://dans.knaw.nl/en/news/lcrdm-task-group-publishes-report-research-software-sustainability-in-the-netherlands/#:~:text=cooperation%20of%20their%20services%20and,SwH%29%C2%A0since%20its%20inception)  
* .  
* Batist, Z. & Roe, J. (2024). *“Open archaeology, open source? Collaborative practices in an emerging community of archaeological software engineers.”* Internet Archaeology, 67 – Analyzes 25 years of archaeology software on GitHub; finds most projects have very few contributors (1–3), implying limited community sustainability  
* [boris.unibe.ch](https://boris.unibe.ch/199087/#:~:text=majority%20of%20archaeologists%20active%20on,engineering%20in%20archaeology%20remains%20largely)  
* .  
* Barats, C., et al. (2020). *DHQ 14(3)* – Case study of the Calico project where custom research tools became unavailable a few years post-project due to lack of maintenance, undermining result reproducibility  
* [digitalhumanities.org](https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html#:~:text=Twitter,results%20of%20this%20research%20project)  
* .  
* Mostafapour, M., et al. (2024). *“Evaluating Literature Reviews Conducted by Humans Versus ChatGPT: Comparative Study.”* JMIR AI, 1(1) – Found GPT-4 can quickly draft a broad literature review but with errors; human oversight is necessary for accuracy and depth  
* [ai.jmir.org](https://ai.jmir.org/2024/1/e56537#:~:text=Conclusions%3A%20The%20study%20suggests%20that,refinement%2C%20making%20it%20an%20assistant)  
* .  
* Schwenke, N., et al. (2023). *“Chatbot-supported Thesis Writing: An Autoethnographic Report.”* (Preprint) – Documents a student’s extensive use of ChatGPT in writing a thesis. ChatGPT helped with brainstorming and editing but struggled with reliable referencing, requiring continuous verification by the student  
* [arxiv.org](https://arxiv.org/abs/2311.10729#:~:text=histories%20were%20analyzed%20and%20are,valid%20learning%20and%20assessment%20format)  
* .  
* Schryen, G., et al. (2023). *“Adopting Generative AI for Literature Reviews: An Epistemological Perspective.”* (Conference paper) – Discusses how LLMs (ChatGPT, Bard) might support literature review processes. Notes that LLMs can improve writing productivity (communication) but true knowledge innovation still depends on human researchers, given that LLMs generate text based on past data (the “stochastic parrot” critique)  
* [ris.uni-paderborn.de](https://ris.uni-paderborn.de/download/47427/47428/FINAL_Generative%20AI%20and%20Literature%20Reviews%20-%20UPLOADED.pdf#:~:text=even%20questioned,However)  
* .  
* American Historical Review (Sept 2023). *“Artificial Intelligence and the Practice of History: A Forum.”* – A collection of essays by historians on AI’s role in research and teaching. It is described as *“the fullest discussion currently available on the implications and opportunities of AI for historians”*  
* [blog.royalhistsoc.org](https://blog.royalhistsoc.org/2024/05/01/generative-ai-history-and-historians-a-reading-guide/#:~:text=Forum%20%E2%80%93%20a%20special%20section,historians%2C%20in%20teaching%20and%20research)  
* , covering issues like AI’s handling of historical sources, biases in training data, and the concept of AI as a historian. (Multiple contributors, e.g., B. Schmidt on representation learning, K. Crawford on datasets, J. Sternfeld on “AI-as-Historian”). *(Gray literature summary available via Royal Historical Society blog.)*  
* OpenAI (2025) – *Operator* and *Deep Research* tool announcements. *(Tech news)* OpenAI’s Operator agent (with the *“Computer-Using Agent”* model) can execute web-based tasks autonomously  
* [deeplearning.ai](https://www.deeplearning.ai/the-batch/openais-operator-automates-online-tasks-with-a-new-ai-agent/?utm_campaign=Data%20Points&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--ff87SP2NG_V21Fj87Y3vgX0yoqBdyamrFckHeQEf2i2HjjUfyW7lJC9vcJ-ZYUDAwegYZ#:~:text=What%E2%80%99s%20new%3A%C2%A0Operator%C2%A0automates%20online%20actions%20like,across%20calendars%20from%20different%20vendors)  
* . This was benchmarked against Anthropic’s Computer Use functionality and other agents; early tests show such agents can navigate websites and gather info, but formal academic evaluation of their research reliability is still pending  
* [digitaltrends.com](https://www.digitaltrends.com/computing/everything-you-need-to-know-about-openai-browser-agent-operator/#:~:text=Everything%20you%20need%20to%20know,against%20Anthropic%27s%20Computer%20Use)  
* .  
* Additional resources on software sustainability and digital project preservation in humanities, including: Flanders & Munoz (2012) on *“sustainable humanities computing”*, the Software Sustainability Institute (UK) blogs (e.g., examples of archaeology software being made open-source  
* [software.ac.uk](https://www.software.ac.uk/blog/archaeology-open-source-software-its-getting-easier#:~:text=Archaeology%20with%20open,otherwise%20noted%2C%20content%20on)  
* ), and studies of link rot in scholarly outputs (e.g., Klein et al. 2014 on reference rot in publications). *(These provide context on why sustainability frameworks are needed, though not directly cited above.)*

Sources

##### **You said:**

Ok, based on this lit review, the main focus of the paper will be "A broader empirical assessment of how long research software survives in the wild is still an open area" (excluding the latter two clauses, as they're beyond the scope of a single paper.)

It looks like you did a lit review (noting the low quality of some of your sources, please evaluate source and author quality before inclusion, it is \*ESSENTIAL\* you focus on high-quality publications and avoid those from paper mills and predatory journals. Blogs are acceptable if the author is known in the field or has a high quality research output otherwise.)

However, in my query, I also asked for: "3. We need a set of prompts to achieve our objectives  
4\. We need a qualitative assessment rubric that we, as humans, can apply to the process."

So, please re-focus your lit review on purely this question, such that we have a literature for evaluating research software longevity of tools (specifically, software and scripts, not data) within the broad context of the historical sciences. And then, do steps 3 and 4, such that we may evaluate your proposed research design against other systems.

###### **ChatGPT said:**

Understood. I'll refine the literature review to focus exclusively on methodologies for evaluating research software longevity (not data longevity) within the historical sciences. This will ensure we have a solid foundation for assessment frameworks.

To clarify your request for steps 3 and 4:

* For step 3, are you looking for prompts that specifically guide an AI-driven evaluation of research software longevity? Should they target systematic data collection (e.g., web scraping, GitHub analysis), qualitative expert input, or a mix?  
* For step 4, should the qualitative assessment rubric be structured for human evaluation of individual research software projects (e.g., sustainability factors, institutional backing, citation longevity), or should it be aimed at comparing different AI-driven research methodologies?

Let me know how you’d like to prioritize these aspects\!

##### **You said:**

For 3, we want a prompt that can cause AI (plus tools) to   
1\. look at software publications that mention a tool  
2\. find the earliest date associated with that tool  
3\. Track how that tool is mentioned \*and maintained\* after that earliest date.   
I.e. we find the paper, find the source code repo, look at the commit history, and look at what other papers mention that tool.   
4\. If there is no evidence of longevity, this null-observation is essential and we should aim to either find recent evidence of use in 2024 or have a last-known observation date.  (Survival in the wild) Please suggest alternative metrics or protocols to achieve these goals.  
5\. We like your webscraping and github analyses ideas, please develop them.

The point, though, is to have a consistent, synthetic prompt, that we can apply across all of these different LLM/tool systems to achieve a specific data-collection goal (Step 3), and human evaluation of tool goal (step 4). Step 4, is us evaluating how well the AI accomplishes the goals, not looking at the longevity data quality. 

What other questions do you have?

###### **ChatGPT said:**

I'll refine the literature review to focus exclusively on methodologies for evaluating research software longevity (not data longevity) within the historical sciences. This will provide a solid foundation for assessing research software lifespan, sustainability, and citation persistence.

Additionally, I'll develop:

1. A synthetic, structured prompt that can be applied across multiple AI/tool systems to systematically gather longevity data on historical research software. This will include web scraping and GitHub analysis to track a tool's citation history, repository activity, and latest known use.  
2. A human evaluation rubric for assessing how well different AI systems achieve the research goals (rather than evaluating the longevity data itself).  
3. Alternative or complementary metrics and protocols for measuring software survival beyond citation and commit history.

I'll provide a detailed response once the research is complete.

# **Evaluating Research Software Longevity in Historical Sciences**

## **Longevity Challenges in Digital Humanities and Historical Sciences**

Research software in the historical sciences (digital humanities, archaeology, history, etc.) often faces a limited lifespan. Studies have shown that many digital projects and tools disappear after only a few years once initial funding or attention wanes

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)

. For example, an analysis of 466 digital scholarly editions found an average lifetime of about 8.5 years, with a half-life around 6 years, before many projects became inaccessible

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)

. Similarly, Meneses and Furuta (2019) investigated *“when can online digital humanities projects be considered abandoned”* by measuring their “persistence and average life span” or *“shelf life”* – defined as the time a project can endure without updates before it’s effectively abandoned

[gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)

. These findings underscore that *software persistence* (continued accessibility and functionality of a tool) is a serious concern: over half of surveyed DH projects from the early 2000s were no longer available by 2020

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)

. Several factors contribute to this fragility of research software longevity in historical sciences

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,Whitt%2C%202017%29%20affects%20not)

:

* Short project funding cycles: Grants often fund development but not long-term maintenance, so tools may not be updated once funding ends  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,support%20as%20researchers%20switch%20career)  
* .  
* Rapidly changing tech environments: Web frameworks, operating systems, and programming languages evolve, meaning an unmaintained tool can quickly break or become obsolete.  
* Institutional and personnel turnover: If a project lacks institutional backing or if key developers leave academia, the software can “orphan” with no one to maintain it  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,Whitt%2C%202017%29%20affects%20not)  
* .  
* Lack of incentives to maintain: Academic credit is typically given for novel research outputs, not for maintaining older software. Citation practices historically undervalued software, making it less rewarding for researchers to invest in sustainability  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=Software%20and%20other%20digital%20resources,of%20citations%2C%20and%20their%20very)  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=diversity%20and%20frequent%20informality%20undermine,22%20Parsons%2C%20Duerr%20%26%20Minster)  
* .

Because of these challenges, the *longevity of research software* in fields like archaeology and digital history needs deliberate evaluation and proactive planning. Below, we review methodologies developed to evaluate software longevity – including frameworks and best practices for measuring persistence, sustainability, and citation longevity – and how they have been applied in historical sciences. We then propose a structured prompt to help automated tools gather evidence of software longevity, outline alternative longevity metrics beyond citations and commits, and present an evaluation rubric for assessing AI-driven longevity tracking.

## **Frameworks for Software Sustainability and Persistence**

Several frameworks and initiatives have emerged to guide both the sustainability of research software and the assessment of its longevity:

* Endings Principles for Digital Longevity: The *Endings Project* developed a set of principles to ensure that digital humanities projects remain usable long after active development ends  
* [dpconline.org](https://www.dpconline.org/digipres/implement-digipres/dpc-ram/level-up/discovery-access#:~:text=Coalition%20www,ensure%20the%20longevity%20of)  
* . These principles emphasize minimal dependence on fragile technology. For example, Endings recommends producing *static outputs* (plain HTML/JS/CSS websites with no server-side code) to avoid relying on databases or custom software that might not be maintained  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* . It also stresses thorough documentation of data models and processes, use of standard formats, and open licensing  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=2,Creative%20Commons%2C%20GNU%2C%20BSD%2C%20MPL)  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* . By following such guidelines, project teams aim to make sure that even if the original software isn’t actively maintained, the scholarly content remains accessible and readable in the future. The Endings framework essentially treats code as contingent and prioritizes the longevity of data and results over the code itself  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=3,principles%20for%20data%20and%20products)  
* . This is a best practice framework rather than a metric, but it provides a *checklist* of conditions (documentation, static site, standard formats, versioned data, etc.) that can be used to evaluate if a project is likely to persist.  
* FAIR and Software Citation Principles: Borrowing from data management, the FAIR principles for research software (Findable, Accessible, Interoperable, Reusable) and the FORCE11 *Software Citation Principles* introduce guidelines that indirectly support longevity  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=3,preferably%20by%20general%20public%20researchers)  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=5,use%20of%20the%20referenced%20software)  
* . For instance, the Software Citation Principles mandate unique identification and persistence: software should have a persistent identifier (like a DOI) and metadata that remain accessible even beyond the software’s lifespan  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=preferably%20by%20general%20public%20researchers)  
* . In practice, this means publishing software in repositories (like Zenodo, which assigns DOIs) and indexing it in catalogs. When these practices are followed, it becomes easier to track a tool’s usage via citations over time (citation longevity) and to retrieve the software even if the original project site goes down. A key idea is that software should be cited “on the same basis as any other research product”  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=and%20data%3B%20they%20should%20be,the%20appropriate%20set%20of%20papers)  
* , which encourages scholars to reference software with formal citations. This yields bibliometric data to measure longevity: for example, one can track how long after its release a tool continues to be cited in publications. A long citation half-life (the period over which half of all its citations occur) indicates lasting relevance  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=Software%20and%20other%20digital%20resources,of%20citations%2C%20and%20their%20very)  
* . Ensuring citations include persistent IDs helps measure longevity because even if the software’s URL breaks, the citation link (e.g., DOI) remains, allowing future researchers or evaluators to find the software record  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=preferably%20by%20general%20public%20researchers)  
* .  
* Software Sustainability Assessment Models: Beyond humanities-specific initiatives, general frameworks exist to evaluate software sustainability which can be applied in historical sciences. For example, Venters et al. (2014) propose considering technical, social, and economic sustainability of software as part of project planning  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)  
* . Tucker (2022) adapts this to humanities contexts by defining sustainability along four facets: technological (using robust platforms, open source), financial (funding for maintenance), environmental (minimal computing for lower costs and carbon footprint), and human (skills and community)  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)  
* . While these are broad considerations, they suggest metrics for evaluation: e.g. *technological* sustainability could be measured by checking if a tool uses up-to-date, supported languages and if its codebase is open and modular, and *human* sustainability by whether a community of users/developers exists to carry it forward  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=Abstract%20Humanities%20researchers%20are%20increasingly,of%20the%20current%20landscape%20as)  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=well%20as%20thoughts%20for%20the,can%20play%20a%20crucial%20role)  
* . Another example is the use of the TOSCA standard in the SustainLife project to package humanities software and all its dependencies for long-term re-deployment  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=archiving%20,Templates%20in%20TOSCA%2C%20describing%20the)  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=structure%20of%20an%20application,3%29%20quantitative%20surveys)  
* . If a project is “TOSCA-archived,” one could rate it high on sustainability because its environment can be recreated even years later. In summary, these frameworks provide checklists and qualitative criteria that can be turned into evaluation rubrics: for instance, scoring a software project on documentation quality, presence of tests/CI (continuous integration), repository health, community engagement, and funding model – all of which correlate with longevity.  
* Institutional Archiving and Preservation Plans: Some best practices frameworks come from digital preservation efforts. The Software Preservation Network and initiatives like Software Heritage advocate archiving source code in a permanent archive (e.g., Software Heritage’s global archive of publicly available code). An archived copy does not guarantee active use, but it ensures *persistence* in terms of availability. Likewise, libraries and digital archives have started treating software as part of the scholarly record to be preserved. A framework here is the adaptation of the OAIS (Open Archival Information System) model for software, which involves storing not just code but also documentation and environment information (for example, saving virtual machine images or Docker containers for reproducibility). While such archival frameworks come from the library/archive world, they provide measurable checkpoints: one can evaluate if a given piece of research software has been deposited in an archive or has an archived executable, which is a positive indicator of longevity. In historical sciences, we see emerging practices like university digital libraries capturing project websites and code upon project completion (King’s Digital Lab’s archiving effort is a case in point, discussed below). The existence of a preserved, accessible copy in an archive (and perhaps a maintained running version via emulation or container) can be taken as a metric for persistence (binary yes/no for availability, and qualitatively how complete the preservation is).

In summary, frameworks like *Endings* focus on designing for longevity, while principles like FAIR and software citation focus on making software discoverable and citable over time. General sustainability models encourage looking at multiple dimensions (technical, social, economic) to gauge a software’s potential lifespan. All these can inform evaluation methodologies: for example, an evaluator might ask – *Did the project follow known longevity best practices (documentation, open standards)? Does the software have persistent identifiers or an archived copy? Is there evidence of a user community or institutional support?* Each question corresponds to a framework principle that, if fulfilled, increases confidence in the software’s longevity.

## **Case Studies of Software Longevity Evaluation**

Real-world case studies in digital humanities and related fields illustrate how software longevity is assessed and what best practices (or pitfalls) emerge:

* “Shelf Life” Study of Digital Humanities Projects (Meneses & Furuta, 2019): This case study systematically measured the persistence of DH projects. The authors gathered a sample of online DH projects and tracked their updates and availability over time  
* [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)  
* . They introduced the concept of a project’s *shelf life*, i.e. how long it remains accessible without changes. By checking the last update timestamps and whether project websites were still online, they determined which projects were effectively *abandoned*. One finding was that many projects become inactive after roughly 5–10 years, aligning with the above-mentioned average lifespan  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,the%20disappearance%20of%20these%20valuable)  
* . The study also highlighted *distributed dependencies* as a vulnerability: if a project relied on external services or datasets that went offline, the project could fail even if its own site remained up  
* [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=Abstract%20A%20large%20portion%20of,formulate%20the%20following%20question%3A%20When)  
* . Methodologically, this case demonstrated use of web archival tools and link checking as a way to gauge longevity – e.g. using the Internet Archive’s “last seen” dates or querying project URLs to see if they still resolve. The result was both a metric (years to abandonment) and insight that longevity can be measured by monitoring a project’s online heartbeat (updates, responses) until it flatlines.  
* Life and Death of Digital Scholarly Editions (Schildkamp & Mathiak, 2019): In a related effort focused on scholarly digital editions (a common form of digital history project), researchers compiled a dataset tracking hundreds of editions over time  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,support%20as%20researchers%20switch%20career)  
* . By comparing the first and last archived versions of each project (via the Internet Archive), they quantified an average lifespan. The striking result – \~376 of 466 editions had disappeared – served as a wake-up call  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,the%20disappearance%20of%20these%20valuable)  
* . A framework used here was simple but effective: treat the existence of a project’s website or repository as the indicator of life. If a site vanished (or its content stopped updating long ago), it was considered “dead.” This case also implicitly used the metric of citation mentions: some projects were known through literature; if a project ceased to be citeable (because it vanished and no new publications referenced it), that indicated the end of its active life. The authors published their dataset, which can be considered a *longevity benchmark* for DH projects  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=DH2020%20dh2020,Data%20set)  
* . Others can replicate this method for different subsets of historical science software by leveraging web archives and reference lists to see how many remain accessible after X years.  
* King’s Digital Lab (KDL) Archiving Project (Smithies et al., 2019): King’s College London’s digital lab undertook an internal audit and rescue mission for \~100 legacy digital humanities projects spanning two decades  
* digitalhumanities.org  
* digitalhumanities.org  
* . They found that almost all these projects – even influential ones like *Inscriptions of Roman Tripolitania* or the *Jane Austen Manuscripts* digital editions – had encountered serious maintenance issues and risked being lost  
* digitalhumanities.org  
* digitalhumanities.org  
* . KDL’s approach was to systematically evaluate each project’s status (Is the site up? Is the code base on a version control system? What dependencies does it have? Has it been updated recently?) and then apply preservation actions. In some cases, they *containerized* the software or migrated it to static web pages; in others, they fixed broken links or updated server infrastructure. The outcome was a set of *policy recommendations* to prevent such near-loss in the future  
* digitalhumanities.org  
* digitalhumanities.org  
*  – essentially best practices: ensure projects have an explicit end-of-life plan, archive them in stable formats, and secure institutional commitment for maintenance. As a case study in evaluation, KDL’s work shows that *longevity can be assessed via audits*: they created an inventory of each project’s components and risks. This is akin to a rubric for longevity health: projects that scored poorly (e.g., single server with outdated OS, no documentation, no active maintainer) were flagged as high-risk. The exercise of scoring and triaging projects by longevity risk is itself a methodology that others can adopt. For instance, archaeology departments could perform periodic audits of their digital tools, rating each on criteria like “Is there a working backup? Do we have the source code? When was it last run successfully?” to identify which tools need intervention to extend their life.  
* Community Tool Directories and Registries: Another angle comes from tracking software mentions in communal resources. In archaeology, a curated list of tools (like the “open-archaeo” list of archaeological software  
* [intarch.ac.uk](https://intarch.ac.uk/journal/issue67/13/#:~:text=Open%20Archaeology%2C%20Open%20Source%3F%20Collaborative,curated%20list%20of%20archaeological%20software)  
* ) can be analyzed for longevity: how many tools on the list are still maintained vs. defunct. A study by Costopoulos et al. (hypothetical example) might have looked at the *open-archaeo* list and found that a significant percentage of tools had not seen updates in several years, suggesting many are abandonware. Although this specific example is illustrative, the general method is clear – cross-sectional surveys of tools used in a field at one time, followed by checking years later which are still around. Likewise, the now-defunct DiRT (Digital Research Tools) directory in digital humanities had entries for tools; an analysis of DiRT’s content after a decade could reveal which tools had longevity. This approach shows the value of *community documentation* as a dataset for longevity studies. It also highlights citation longevity: if a tool remains listed and recommended in such directories over time (or continues to be included in new editions of textbooks and tutorials), that indicates sustained relevance.  
* Specific Tool Histories: Individual software tools in the historical sciences sometimes become subjects of their own “histories,” offering anecdotal longevity insights. For instance, ArcGIS in archaeology has been used for decades; although it’s commercial software, its persistent citation in archaeological studies demonstrates longevity of use (often outlasting multiple version changes). Conversely, a tool like HyperCard (used in early multimedia history projects) saw rapid obsolescence – case narratives of projects built on HyperCard disappearing in the 2000s are instructive on how reliance on proprietary, unsupported platforms leads to short software lifespans  
* digitalhumanities.org  
* . These narratives, while not formal studies, act as cautionary tales and *case-based evidence*: evaluators sometimes compile such cases to derive best practices (“avoid proprietary platforms if you want longevity”, “choose formats that can be migrated”).

Across these case studies, a few common practices for evaluating software longevity emerge:

* Checking availability over time (via web archives, link checkers).  
* Recording update activity (version releases or commit history to see if a project is active, stagnant, or ended).  
* Tracking citations or mentions in literature year by year (to see if usage is growing, steady, or tapering off).  
* Auditing preservation steps taken (is there an archived copy, a static version, or a contingency plan?).  
* Using surveys or community knowledge (asking experts if they know a tool is still being used or if it has been supplanted).

These methods provide a toolkit for measuring persistence (continued existence), sustainability (ongoing maintenance), and citation longevity (continued scholarly use) of research software in historical fields.

## **Best Practices for Sustaining Research Software**

The literature also points to best practices that enhance software longevity – these can be considered both preventative (to prolong life) and as criteria when evaluating a project’s longevity prospects. High-quality sources on digital project sustainability (e.g., the Software Sustainability Institute, the British Library’s digital preservation guidelines, the Endings project outcomes) consistently recommend the following:

* Plan for Longevity from the Start: Projects should include a sustainability plan at inception  
* digitalhumanities.org  
* . This means budgeting and planning for maintenance or archiving beyond the grant’s end date. For example, building in time to create a static HTML version of a database-driven site at the project’s conclusion can ensure a read-only version persists  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* . It’s a best practice to define an “exit strategy” for software – how it will transition to a maintainable state when active development ceases  
* [dpconline.org](https://www.dpconline.org/digipres/implement-digipres/dpc-ram/level-up/discovery-access#:~:text=Coalition%20www,ensure%20the%20longevity%20of)  
* digitalhumanities.org  
* .  
* Use Stable, Standard Technologies: Avoid ultra-specialized or proprietary tech that might not be around in a few years. The Endings Principles explicitly advise using only widely supported web standards and formats (e.g. HTML5, CSV, TEI-XML)  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* . Similarly, choosing open source programming languages and frameworks with large communities (Python, JavaScript, etc.) increases the chances of long-term support. In an archaeology context, for example, saving 3D models in standard formats (OBJ, PLY) rather than a niche software’s format means they’ll be readable in the future. When evaluating a tool, check if its core components are standard and likely to be supported in the medium to long term.  
* Open Source and Community Engagement: Research software should be released as open source whenever possible. This invites a community of users and contributors who can help sustain the project  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=structure%20of%20an%20application,3%29%20quantitative%20surveys)  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=and%20technologies%20of%20selected%20applications,the%20Digital%20Humanities%E2%80%9D%20to%20spawn)  
* . A tool with an active user/developer community (even if small) is far more likely to see bugs fixed and updates over time than one kept closed. Community indicators like number of GitHub stars or forks, or an active mailing list, are positive signs of longevity. Best practice is also to cultivate such a community – e.g. by good documentation, responding to issues, and presenting the tool at conferences/workshops to gain adopters. An example is the popular text analysis tool *Voyant*: its open-source nature and community of users in digital humanities have kept it updated and cited for well over a decade.  
* Persistent Identifiers and Archival Deposits: To improve citation longevity and ensure future access, assign persistent IDs (DOI/ARK) to software releases. For instance, publishing software versions on Zenodo (which integrates with GitHub) will not only give a DOI to cite  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=3,preferably%20by%20general%20public%20researchers)  
* , but also store a copy in Zenodo’s archive. Similarly, depositing the software (and documentation) in a disciplinary repository or general repository (e.g., the Archaeology Data Service in the UK now accepts some software, or institutional repositories) is a safety net. Best practice is to do this at major release milestones or at project end. Evaluators often check: “Is there an archived copy of the code?” If yes, that’s a strong assurance against total loss  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=preferably%20by%20general%20public%20researchers)  
* . Software Heritage, a global software archive, can also be used – projects can register their code to be periodically ingested, preserving even the development history.  
* Maintain Documentation and Metadata: Comprehensive documentation (installation guides, usage manuals, README files, inline code comments) contributes to longevity. It ensures that future users (or the original team, years later) can understand and run the software  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=2,forms%20part%20of%20the%20products)  
* . As a best practice, treat documentation as an integral deliverable of the project. Also, create metadata records for the software (e.g., listing author, institution, version, date, license, dependencies). This metadata might be captured in a CITATION.cff file or an entry in a software catalog. Good metadata aids findability and citation. When measuring longevity, one might see if the project’s documentation is still accessible and if external platforms (like GitHub or institutional websites) still describe the software.  
* Version Control and Continuous Integration: Using version control (e.g., Git) is standard, but for longevity it’s important that the repository remains accessible. Hosting code on widely used platforms like GitHub or GitLab can help (provided the code is also archived elsewhere in case these services change). Continuous Integration (CI) tools, while mainly for quality, also implicitly support longevity by ensuring the software continues to build and run as dependencies change  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=3,triggered%20automatically%20where%20possible)  
* . A project that has CI tests (and that keeps them passing) signals active maintenance. Even after development slows, having automated tests and containerized build scripts means that others can potentially revive or update the software more easily. Best practice: include Dockerfiles or reproducible environment setups so that years later, someone can execute the software in an isolated environment if direct execution becomes difficult.  
* Regular Maintenance or Planned Sunset: If resources allow, allocate a small amount of ongoing maintenance – even periodic check-ups to update dependencies or fix broken links. Some projects adopt a *maintenance mode* after initial development, with infrequent but necessary updates (e.g., updating a database of historical sources annually). If maintenance cannot continue, then plan a sunset: freeze the code, ensure everything is static and self-contained, document the final state, and perhaps write a “tombstone” note (a page explaining that the project is no longer active, with information on last version and archival locations). This transparency is beneficial for future scholars who might wonder what happened. It also sets an end point that can be used in longevity evaluation (the *last-known update* timestamp).

By adhering to these best practices, many historical science projects have managed to remain usable far beyond typical lifespans. For example, the Perseus Digital Library (classics/historical text project) has survived for decades through continuous funding, open sourcing, and migrating its architecture several times – a testament to good stewardship. Meanwhile, projects that ignored such practices often feature as examples of “digital decay” in the literature. When evaluating software longevity, best practices serve as a checklist of indicators: if a tool ticks most of these boxes, it likely has greater persistence. Conversely, absence of these (no source code available, no documentation, built on obscure tech) is a warning sign for early obsolescence.

## **Synthetic Prompt for Longevity Analysis of Research Software**

To systematically gather evidence of a software tool’s longevity, we propose a structured prompt that can guide AI systems (such as OpenAI’s research assistants, Anthropic’s tools, or HuggingFace pipelines) through a series of steps. This synthetic prompt is designed to be generalizable across different platforms and instructs the AI to perform a comprehensive investigation into a tool’s history and current status. The prompt uses a step-by-step approach: Prompt Title: *“Research Software Longevity Tracker”* Instructions (for any given software tool X in the historical sciences domain):

1. Identify Initial Release and Context: Search for academic publications, project webpages, or announcements that introduce or describe the software “X.” Determine the earliest date of release or first mention of X. (For example, find the first paper about X or the earliest version/date on its website or repository.) Record the tool’s initial release year and the context (conference paper, journal article, project launch, etc.)  
2. [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)  
3. .  
4. Document Key Details of Software X: From the initial source and related documentation, extract fundamental information about X, including:  
   * The domain/purpose (e.g., “a GIS tool for archaeology”).  
   * Authors or maintaining institution.  
   * If mentioned, any URLs for the project website or source code repository.  
   * The technologies used (programming language, platform) – as this might be relevant to its sustainability.  
5. Locate the Source Code Repository: If software X is open-source or has a public codebase, find its source code repository (e.g., a GitHub, GitLab, or Bitbucket link). Use web search with keywords like “X source code” or “X GitHub”. If multiple repositories exist (forks or mirrors), identify the primary one (often the one by the original author or the one mentioned in official docs).  
6. Analyze Repository Activity: Once the repository is found, examine its commit history and release history:  
   * Note the date of the first commit (or earliest activity) in the repo to confirm the start date.  
   * Note the date of the most recent commit. This often indicates the last update.  
   * Count or qualitatively describe the commit frequency over the years (e.g., active development from 2016–2019, then sporadic commits in 2020, last commit in 2021).  
   * Check the number of contributors and recent pull requests or issues – evidence of ongoing community engagement.  
   * Identify if there have been recent releases or version tags (and their dates). A release in 2023 or 2024 would indicate current activity.  
7. Check Software Preservation Measures: Investigate whether the software has been archived or preserved:  
   * Search for a DOI or citation for X (perhaps on Zenodo, figshare, etc.). For example, the prompt could instruct: *“Find if a DOI exists for software X (try searching ‘X Zenodo’).”* If a DOI is found, note the year and version it corresponds to.  
   * Search the Software Heritage archive for X (if API access is possible) or look for mentions that X’s code is mirrored in long-term archives.  
   * See if the project website (if any) is accessible. If not, use the Internet Archive’s Wayback Machine to find the last archived copy of the site and note its timestamp (last snapshot date).  
   * Look for any “tombstone” or maintenance notices on the project’s pages (e.g., “This project is no longer maintained as of 2018”).  
8. Gather Mentions in Scholarly Literature: Perform a literature search for other papers or project reports that mention software X after its initial release:  
   * Use academic search engines or Google Scholar with queries like “software X” (in quotes) and filter by year to see mentions over time.  
   * Identify key papers that used X or evaluated X, especially in recent years (e.g., if X was released in 2015, see if it’s still being cited in 2022–2024).  
   * Note the latest publication (by date) you can find that references X – this gives a sense of *citation longevity*. For each significant mention, record the context (was X used for a new study? was it reviewed in a tools paper?).  
   * If X has a unique name, general web search can find blogs, course syllabi, or forum discussions where it’s mentioned; check if any appear in the last year or two, as evidence of ongoing use in the community.  
9. Assess Ongoing Maintenance and Use: Synthesize the findings from steps 4–6 to determine the current status of X:  
   * If the repository shows recent commits or releases and you found 2023/2024 citations, declare that X appears to be actively maintained or in use (describe evidence, e.g., “last commit Oct 2023; cited in a 2024 digital history article”).  
   * If the evidence shows no commits for many years and no recent mentions, conclude that X is likely obsolete or unmaintained, and provide the last known active date (e.g., “last code update in 2017, no references after 2018”).  
   * If the tool is not found in any repositories or the website is down, but you found some usage, indicate partial longevity (perhaps the software isn’t maintained, but researchers kept using it up to a certain point).  
   * If the software has been succeeded by a new project or fork, note that (e.g., “Project X was succeeded by X2 in 2020, which indicates a continuity of the effort”).  
10. Handle Missing Evidence or Uncertainty: If certain information is not readily available:  
    * If no source code or repository is discoverable, state that (“No public repository found – the software might have been distributed only as binaries or not at all”).  
    * If no recent activity is found but also no clear end-of-life, try a broader search (e.g., search on social media or the developer’s homepage for announcements regarding X’s status).  
    * In cases of ambiguous results (e.g., a repository with some recent forks by other users but no official updates), mention the ambiguity: “Official development stopped in 2019, but a fork by the community shows commits in 2021.”  
    * Ensure the AI prioritizes finding the most recent evidence of use or maintenance. For instance, explicitly instruct: *“Focus on finding any indication that X was used or updated in 2023 or 2024 (such as a 2024 publication or a commit in 2024).”* This ensures that even if longevity is poor, the AI can establish a last-known usage date.  
11. Compile a Longevity Profile for X: Finally, the AI should output a structured summary of findings for software X, for example:  
    * Initial Release: (when, where)  
    * Latest Version / Update: (version number or date of last commit/release)  
    * Years of Active Maintenance: (e.g., 2015–2020)  
    * Source Repository: (URL and brief status like “archived on GitHub, 100 commits, 5 contributors”)  
    * Citation Longevity: (e.g., “cited in 25 papers; latest citation in 2023【some reference】”)  
    * Current Status: (active/maintained, dormant but accessible, or defunct)  
    * Last Known Usage: (if defunct, note the last evidence, like “last known use in a 2019 case study”)  
    * Preservation: (any archives or DOIs ensuring availability, e.g., “version 1.0 archived on Zenodo DOI:...”).

This structured prompt ensures the AI agent covers all bases: discovering the tool’s origin, checking technical maintenance (commits, releases), tracking scholarly usage, and noting end-of-life if applicable. It directs the AI to cross-reference multiple sources (academic publications, code repositories, web archives) to build a complete picture of software longevity. Key features of this prompt:

* It is systematic: by breaking the task into discrete steps, it reduces the chance of missing important evidence (for example, not stopping at finding a paper but also checking code repository).  
* It is generalizable: the wording can be applied to any tool by substituting the name and is not tied to a specific AI model’s syntax.  
* It emphasizes latest evidence: explicitly asking for 2024 mentions or last-known commits guards against outdated conclusions.  
* It includes contingencies for null results: guiding the AI on what to do if no info is found (e.g., broaden search or report lack of evidence rather than guessing).  
* It encourages output with source attribution (the AI should ideally provide references for each piece of data, such as the URL of the repository or citations to papers).

Such a prompt can be handed to an AI-driven research assistant to reliably gather longevity data across a range of historical research software tools in a consistent manner.

## **Alternative Metrics and Protocols for Assessing Software Longevity**

While citation counts and commit histories are two common measures of software longevity, relying on them alone can be insufficient or misleading. To robustly evaluate software longevity, a combination of alternative metrics and protocols should be considered:

* User Community and Adoption Metrics: Look at signs of an active user base. This could include:  
  * *Download statistics*: If the software is distributed via a package manager (e.g., PyPI, CRAN) or a platform like GitHub Releases, how many downloads or installs does it report, and is it steady or growing over time?  
  * *Support forums and Q\&A activity*: The presence of recent questions or discussions about the tool on platforms like Stack Exchange, Reddit, or domain-specific forums (e.g., Humanities Commons) indicates ongoing use. If people are still asking and answering questions about the software, it’s a proxy for longevity in use.  
  * *Workshop or teaching usage*: Is the tool included in recent tutorials, workshops, or courses? For example, if an archaeology field school in 2023 taught a software tool, that’s evidence it’s still considered useful. Syllabi mentions or training material updates can serve as a metric (though harder to gather automatically).  
* Maintenance Quality Metrics: Beyond raw commit counts, examine the nature of maintenance:  
  * *Issue tracker activity*: Are new issues being reported and addressed? A tool could have few commits but many answered issues, meaning it’s stable but still cared for. The ratio of open to closed issues can indicate whether maintainers are keeping up.  
  * *Dependency updates*: Check if the software periodically updates its dependencies or is updated to remain compatible with new versions of underlying platforms (e.g., a Python tool updated to work with Python 3.x, or a web app updated for latest browser standards). Longevity can be inferred if the software adapts to ecosystem changes.  
  * *Bus factor / contributor diversity*: A project maintained by a single person has a risk if that person stops, whereas one with multiple active contributors is more resilient. Metrics from open-source health (such as those defined by the CHAOSS project) like number of active contributors in the last year, or presence of onboarding documentation for new contributors, reflect sustainability of the maintenance process itself.  
* Software Reputation and Impact Metrics: These assess longevity in terms of *continued relevance*:  
  * *Citation context and diversity*: Not just counting citations, but looking at how and where the software is cited. If over time the software gets cited in new domains or for new use cases, it shows adaptability (a form of longevity). Also, a high diversity of authors citing it (not just the original team) suggests the software has a life of its own in the community.  
  * *References in reviews or meta-studies*: If the software is covered in review articles or meta-analyses (e.g., “a survey of tools for text analysis” lists this tool in editions spanning multiple years), it demonstrates that the community still considers it part of the state of the art.  
  * *Longevity awards or recognitions*: Some communities explicitly acknowledge long-lived tools (for instance, an “Impact Award” for a tool still widely used 10 years later). While not common in humanities, being included in things like the *ACM Software System Award* or mentioned in retrospective blog posts (“Top 10 tools of the decade”) are qualitative indicators of lasting impact.  
* Run-ability and Bit Rot Checks: A very direct protocol is to periodically attempt to install and run the software in a modern environment:  
  * If the software is open source, one can try to compile it or install it (e.g., via pip) on a current system. Success or failure is a concrete measure: software that can still run (possibly after minor tweaks) has practical longevity; if it fails due to deprecated dependencies and no fixes, it shows lack of sustainable design.  
  * Containerization tests: If a Docker image is provided, does it still build and run? If not, is it easily fixable? Some projects use services like Binder or continuous integration to regularly test environment reproducibility, which can serve as an automatic longevity check.  
* Cross-Version/Successor Tracking: Sometimes longevity is carried through successor projects or forks. A metric here is lineage tracking:  
  * Did the software spawn a new project that carries on its functionality? (E.g., a tool rebranded or merged into a bigger platform.) This might not count as the *same* software longevity, but it means the underlying ideas persist.  
  * One could track references in documentation like “Based on X” or “forked from X” to see if a dormant project’s code lives on elsewhere. If so, the legacy of the software continues in a new form, which is a kind of longevity (through influence).  
* Qualitative Surveys and Self-reporting: In addition to automated metrics, an important protocol is to ask the creators or users:  
  * Creators can provide insight into how long they intended the software to last and whether they consider it maintained. Some publications include a *sustainability section* where authors declare plans for maintenance; these statements can be recorded and later checked against reality.  
  * Users can be surveyed on what versions they use and until when. For example, a survey of archaeologists might find that many still use an old tool in 2025 even if it wasn’t updated since 2015, indicating longevity of use despite no development.  
  * These approaches add context to raw metrics – for instance, a maintainer might say “the tool is feature-complete and doesn’t need frequent updates,” which explains a low commit count but doesn’t mean it’s abandoned.

By combining these alternative metrics with citation and commit analysis, one can form a much more robust picture. For example, a tool might have few recent commits (looks unmaintained) but still be heavily downloaded and used in courses (active use longevity). Or a tool might not be cited in papers much (perhaps because it’s infrastructure or used in practice more than in research papers) but might have a thriving forum of practitioners. Robust longevity assessment means looking at multiple indicators so that the weakness of one is compensated by another. This multi-pronged approach aligns with best practices in software sustainability research: treat software as a socio-technical artifact whose longevity is influenced by technical upkeep *and* community and scholarly engagement

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=The%20problem%20of%20sustainability%20is,duplication%2C%20sandboxing%2C%20refactoring%2C%20unified%20tech)

[dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=structure%20of%20an%20application,3%29%20quantitative%20surveys)  
. In practical terms, an AI system applying the synthetic prompt could be extended to gather some of these alternative metrics: e.g., checking Stack Overflow for tool-related questions, looking at package manager stats, or even attempting to run the software in a test environment if given that capability. These protocols ensure that longevity measurement isn’t just an academic citation count, but an evidence-based assessment of whether the software remains *usable and useful* over time.

## **Evaluation Rubric for AI-Driven Longevity Tracking**

When deploying different AI systems to perform the longevity tracking task (using the prompt above or similar methods), we need a human evaluation rubric to assess how well each system accomplishes the task. The rubric should cover both the correctness of the findings and the process the AI used. We propose the following evaluation criteria, each with descriptors for what constitutes excellent, adequate, or poor performance:

* 1\. Accuracy and Completeness of Retrieved Data: *Does the AI gather the correct information and cover all key aspects of longevity?*  
  * *Excellent:* The system identifies the correct initial release date, finds the official repository (if exists), notes the correct last commit date, and accurately reports recent mentions or lack thereof. It misses no major evidence that is readily available, and the data points (dates, version numbers, citations) are factually correct (verified against sources).  
  * *Adequate:* The system finds some information but with minor gaps or errors – e.g., it gets the release year right but overlooks a secondary repository, or it finds the last commit roughly but misses that there was a minor patch later. It might retrieve the general trend (active vs inactive) correctly but not every detail. Small factual errors may be present (like a wrong version number) but not fundamentally misleading.  
  * *Poor:* The system provides incorrect dates or status (e.g., claims a tool is maintained when it actually isn’t, or vice versa) because it failed to retrieve obvious evidence. It might miss the repository entirely or confuse the software with another of a similar name, leading to wrong data. Incomplete results that omit key aspects (like not mentioning any literature references, or ignoring the commit history entirely) also fall here.  
* 2\. Cross-Referencing and Source Verification: *Does the AI cross-check information and provide evidence for its claims?*  
  * *Excellent:* The AI cites multiple sources for each major claim (for example, referencing the GitHub repository for commit info, and scholarly articles for usage)  
  * [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)  
  * [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)  
  * . It shows evidence of cross-verification – e.g., if a paper says “last updated in 2019,” the AI also checks the repo to confirm 2019 was the last commit. All statements about the tool’s status are accompanied by either a direct reference (URL or publication) or an explanation of how the AI deduced it from data. The AI resolves contradictions by seeking additional sources (for instance, if one source says the project is alive and another says it’s dead, the AI investigates further and explains which is accurate).  
  * *Adequate:* The AI provides some sources or references, but not consistently for all facts. There is limited cross-checking; the AI might rely on a single source for each aspect (e.g., just the project website’s claims about last update). It might not notice a discrepancy unless it’s obvious. Some statements might be unreferenced but plausible. The overall trustworthiness is moderate – a human evaluator may need to verify a few points independently.  
  * *Poor:* Little to no source attribution is given; the AI states things as facts without indicating where the information came from. The AI clearly did not cross-check – for example, it might report the date from a publication but ignore that the repository shows a different reality. If asked for evidence, the AI might provide irrelevant or incorrect sources. Essentially, the methodology is a “black box” with no transparency, making it hard to trust the results.  
* 3\. Handling of Null or Ambiguous Findings: *How well does the AI handle cases where data is missing or inconclusive?*  
  * *Excellent:* The AI proactively identifies when evidence is lacking and clearly reports “no evidence found for X” or “unable to locate a repository” *without hallucinating an answer*. It follows the prompt instructions to broaden the search or find the last-known info. If a tool truly has no recent activity, it states that frankly and focuses on last known data (e.g., “No commits after 2015; likely inactive by 2024”). In ambiguous cases, it explains the ambiguity: for instance, “The project website is down; an archived copy exists from 2020 but no further info. This suggests the project might be discontinued, though no official statement was found.” Such handling shows the AI can gracefully deal with incomplete info and still provide a useful answer.  
  * *Adequate:* The AI handles missing data somewhat inconsistently. It might note some gaps (“I did not find a GitHub page for X”) but also leave some questions unanswered without explanation. It doesn’t fabricate information, but it might not make extra efforts to find alternatives (e.g., it stops after not finding a website and doesn’t try an archive). Ambiguities might be glossed over or the AI chooses one interpretation without much justification. The user gets an answer but might sense that some parts are uncertain without being explicitly told so.  
  * *Poor:* The AI fails this aspect if it *fabricates answers to fill gaps* (for example, inventing a repository or a last usage mention that doesn’t exist). Also poor is if it simply gives up too early (“I can’t find anything on X”) when information is actually available via a slightly different query. Ignoring the instruction to handle null results (for instance, not attempting to find a last-known date when no current evidence exists) would also be a negative. Essentially, a poor performance means the AI either misleads about nonexistent data or provides an incomplete report without acknowledging its limitations.  
* 4\. Transparency of Method and Reasoning: *Does the AI make its process and reasoning clear to the evaluator?*  
  * *Excellent:* The output is organized (e.g., following the structured format with headings like “Initial Release,” “Repository,” “Recent Mentions,” etc.) and the AI explains how it arrived at each piece of information. It might say, “According to the GitHub repository (source link), the last commit was in 2019,” or “A 2022 paper (citation) mentions using version 2.0 of X, indicating the software was still in use then.” The AI’s answer reads like a mini-report with traceable logic. This transparency builds trust, as a human reviewer can follow the trail and reproduce the steps if needed.  
  * *Adequate:* The AI provides the needed info but with minimal explanation. It might list facts (“Last update 2019; used in a 2021 study; archive DOI exists”) but not narrate how those were found. Some references are given, but perhaps not for every single point. The structure might not fully mirror the prompt steps but still groups information logically. You can infer the methodology (e.g., it clearly looked at GitHub and Google Scholar) but the AI doesn’t explicitly walk through each step in the answer. It’s usable, but not fully transparent without some guesswork.  
  * *Poor:* The AI’s answer is disorganized or just a raw dump of information with no clear logic. It might mix unrelated facts, or present data without context (e.g., just throwing a URL or a quote without stating what it signifies). No clear progression from initial release to current status is given. Or the AI might provide a conclusion (“X is not maintained”) with no explanation of how it deduced that. A human evaluator would struggle to understand the basis of the AI’s statements, making it hard to judge correctness.

Using this rubric, human evaluators can score different AI systems on each criterion. For instance, an OpenAI-based system might be very good at language and give a well-structured, cited answer (high marks in all categories), whereas a smaller model might retrieve some facts but miss cross-checking (lower marks in accuracy and verification). The rubric focuses on the end-to-end effectiveness: from retrieving the right data to presenting it reliably. Importantly, this evaluation goes beyond just “did it get the right answer?” – it values the process (critical in research settings). Especially for scholarly use, we want AI systems that not only find data but also *justify* and *validate* it with sources (thus aligning with academic standards of evidence). The transparency and cross-referencing aspects ensure the AI’s methodology is visible and trustworthy, which is crucial when assessing something as nuanced as software longevity where data can be scattered or uncertain.

## **Summary and Prompt Refinement Recommendations**

In summary, our literature review finds that research software in historical sciences often has a precarious lifespan, typically under a decade without intervention

[dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=the%20time%20stamps%20of%20the,the%20disappearance%20of%20these%20valuable)  
. However, a range of methodological frameworks and case studies offer guidance on evaluating and improving longevity. Key takeaways include:

* Longevity should be assessed on multiple dimensions: technical maintenance, continued use in scholarship (citation longevity), and preservation measures.  
* Frameworks like the Endings Principles and FAIR4RS provide checklists (use open standards, document everything, assign persistent IDs) that correlate with better persistence  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=preferably%20by%20general%20public%20researchers)  
* .  
* Studies measuring project “half-life” via web archives  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)  
*  and abandonment via last-update timestamps  
* [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)  
*  give quantitative baselines and show the utility of using archived web data and literature mining as evaluation tools.  
* Best practices from these studies and sustainability experts converge on the need for planning for sustainability early, engaging communities, and utilizing archival resources to ensure future access.

Based on these findings, the structured prompt for AI was developed to mirror best practices by systematically searching for a tool’s history, code activity, and usage evidence. The prompt ensures the AI looks for *persistent identifiers, repository data, and scholarly references* – exactly the combination that the literature suggests is necessary for robust longevity assessment. Refinements to the Prompt: Incorporating lessons from software sustainability research, we recommend a few refinements to further strengthen the synthetic prompt:

* Emphasize Multiple Source Types: Ensure the prompt explicitly instructs the AI to use diverse sources: not just scholarly articles and not just code repositories, but both, as well as web archives and possibly social or educational references. This redundancy is important because, as we saw, reliance on one source can miss part of the picture  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=Software%20and%20other%20digital%20resources,of%20citations%2C%20and%20their%20very)  
* . For instance, add a sub-step like: *“Corroborate the repository findings with information from at least one publication or official announcement by the developers.”* This aligns with cross-referencing best practices.  
* Temporal Cross-Checking: Add guidance for the AI to cross-check dates between sources. For example: *“Compare the release year found in publications with the repository creation date to confirm the timeline.”* This helps catch inconsistencies and is inspired by the thorough audit approach seen in case studies (like KDL’s project audits).  
* Null Handling Strategy: Strengthen the prompt’s instructions on what to do if key information is missing. We might explicitly include: *“If the main repository is not found, search alternative code hosting services or archived code (e.g., search on Software Heritage or ask if the tool was distributed via other means). If no citations are found in academic sources, consider searching project documentation for user testimonials or usage logs.”* This makes the AI’s search more resilient, reflecting the idea that evidence of use might exist outside formal literature.  
* Quality of Use Metrics: Incorporate at least one alternative metric check from the above list. For example, a prompt extension could be: *“Look for any download or usage statistics (if the tool is on a package index or similar), or check if the tool is mentioned on Q\&A forums in the past year.”* While an AI might have limits accessing some of these, even instructing it to note if, say, Stack Overflow has recent questions tagged with the software’s name could be informative. This ties into the multi-metric approach recommended in sustainability research.  
* Explicit Verification Step: After gathering information, the prompt could include a final step: *“Verify and reconcile information: ensure that the dates and facts gathered make sense together (e.g., you shouldn’t have a ‘last commit in 2023’ if earlier you stated the project ended in 2020). If inconsistencies exist, highlight them and possibly give both sides.”* This step enforces a sanity check, much like a human researcher would do when writing a literature review – a practice of reflection that leads to more accurate reporting.

Adopting these refinements will help align the AI’s process with the best practices of manual scholarly research in software sustainability. Just as human researchers triangulate sources and double-check anomalies, the prompt will guide AI to do the same, yielding more reliable and nuanced results. Ultimately, evaluating the longevity of research software is a complex task, but by drawing on established frameworks and case studies – and by clearly instructing our AI tools on how to mimic those proven methods – we can greatly improve the quality and trustworthiness of the insights gathered. This combined approach of human-informed prompt design, alternative metrics, and rigorous evaluation criteria will support better tracking and understanding of how long our digital tools in historical sciences endure, and why. Sources:

* Barats, C., Schafer, V., & Fickers, A. (2020). *“Fading Away... The challenge of sustainability in digital studies.”* Digital Humanities Quarterly, 14(3). (Discusses tensions between short tech lifecycles and long-term research needs)  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,support%20as%20researchers%20switch%20career)  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=paths%20or%20research%20directions,digital%20outcomes%20of%20scholarly%20labor)  
*   
* Meneses, L., & Furuta, R. (2019). *“Shelf life: Identifying the abandonment of online digital humanities projects.”* Digital Scholarship in the Humanities, 34(Suppl\_1), i129–i135. (Defines “shelf life” and measures DH project persistence)  
* [gotriple.eu](https://gotriple.eu/documents/50%7Cdedup_wf_001%3A%3A030062c596a29295f5e8974fa8556e01#:~:text=circumstances,considered%20abandoned%20by%20its%20researcher)  
*   
* Mathiak, B., & Schildkamp, P. (2019). *“Overview of life and death of digital scholarly editions”* (Data set & analysis). (Found average DH project lifespan \~8.5 years; highlights loss of many projects)  
* [dh2020.adho.org](https://dh2020.adho.org/wp-content/uploads/2020/07/565_SustainabilityStrategiesforDigitalHumanitiesSystems.html#:~:text=Sustainability%20of%20research%20software%20is,the%20disappearance%20of%20these%20valuable)  
*   
* Smithies, J., et al. (2019). *“Managing 100 Digital Humanities Projects: Digital Scholarship & Archiving in King’s Digital Lab.”* DHQ, 13(1). (Case study on auditing and preserving DH projects; offers sustainability recommendations)  
* digitalhumanities.org  
* digitalhumanities.org  
*   
* Endings Project Team (2021). *“Endings Principles for Digital Longevity.”* University of Victoria. (Framework with guidelines for project design to maximize longevity: use static sites, standard formats, thorough documentation)  
* [endings.uvic.ca](https://endings.uvic.ca/principles.html#:~:text=4.1%20No%20dependence%20on%20server,databases%2C%20no%20PHP%2C%20no%20Python)  
* [dpconline.org](https://www.dpconline.org/digipres/implement-digipres/dpc-ram/level-up/discovery-access#:~:text=Coalition%20www,ensure%20the%20longevity%20of)  
*   
* Smith, A. et al. (2016). *“Software Citation Principles.”* PeerJ Computer Science, 2:e86. (FORCE11 working group recommendations for citing software with persistent IDs and metadata)  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=preferably%20by%20general%20public%20researchers)  
* [peerj.com](https://peerj.com/articles/cs-86/#:~:text=and%20data%3B%20they%20should%20be,the%20appropriate%20set%20of%20papers)  
*   
* Tucker, J. (2022). *“Facing the challenge of digital sustainability as humanities researchers.”* Journal of the British Academy, 10: 93–120. (Discusses facets of sustainability in humanities projects, including technological and human factors)  
* [thebritishacademy.ac.uk](https://www.thebritishacademy.ac.uk/documents/4314/JBA-10-p093-Tucker.pdf#:~:text=view%20of%20the%20current%20landscape,can%20play%20a%20crucial%20role)  
*   
* Harzenetter, L. et al. (2020). *“Analysis and Categorisation of Research Software in the Digital Humanities.”* DH2020 Conference Poster. (Introduces SustainLife approach using TOSCA for preserving DH software environments)  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=archiving%20,Templates%20in%20TOSCA%2C%20describing%20the)  
* [dh-abstracts.library.virginia.edu](https://dh-abstracts.library.virginia.edu/works/9403#:~:text=structure%20of%20an%20application,3%29%20quantitative%20surveys)  
*   
* Software Sustainability Institute (2014). *“Software Sustainability: Research and Practice from a UK perspective.”* (Emphasizes the need for sustainable software development practices and hints at measuring sustainability through community and maintainability metrics)  
* [software.ac.uk](https://www.software.ac.uk/blog/journey-or-destination-software-sustainability-different-humanities#:~:text=Is%20software%20sustainability%20different%20in,humanities%20projects%3A%20the%20destination)  
* .

Sources  
ChatGPT can make mistakes. Check important info. See Cookie Preferences.  
