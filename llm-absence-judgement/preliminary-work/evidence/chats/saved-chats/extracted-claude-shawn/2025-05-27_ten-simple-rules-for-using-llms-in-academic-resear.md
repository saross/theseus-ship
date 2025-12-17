# Ten Simple Rules for Using LLMs in Academic Research

## Metadata
- **UUID:** `b4e8c79e-b1d1-4228-a087-079dc5a4073c`
- **URL:** https://claude.ai/chat/b4e8c79e-b1d1-4228-a087-079dc5a4073c
- **Date:** 2025-05-27 13:48:51

---

## Conversation

### Human (13:32:05)

Hi Claude, I've been taking some random notes on how to use LLMs for academic research purposes, and I'd like to turn them into a '10 Simple Rules' style paper. I've attached a 'Ten Simple Rules for Writing a PLOS Ten Simple Rules
Article', a useful but witty guide to how these papers should be composed. Can you help me take the most impactful suggestions from the notes I've made and turn those into a list that can form the basis of such a paper? For a first step, I'd like you to distill about 15 possible ideas and reword them into one-sentence rules. Consolidate similar ideas. Let me know which ones you rejected (in a few words each). Apply the 'writing style guide' attached to this project, which we developed together as a style we both like.

<rules brainstorm>
Iterate over prompts with an appropriate model...
Check all of your references
Remember that design of prompts and interpretation of results depends on your expertise
Don't give it too much at once, decompose tasks. 
Seemingly minor changes to prompts can have significant impact (better or worse) on outputs
Iterate over prompts until you get the results you are looking for.
Use an LLM to help you write prompts (meta-prompting).
Use multiple models. Models change frequently and each has its own personality. Each may be good for a different set of tasks. Compare competing tools (e.g., the 'research' product offered by each of the major labs). Test the same prompts across different models.
Use APIs and build tools. 'Mundane' software scaffolding often improves outputs, allowing modifications of settings unavailable in the chatbots (enumerate). Huggingface at GitHub have many useful workflows / pipelines.
Spend at least one hour per week reading AI blogs / substacks / listening to podcasts / etc. 
Use system settings. You can tailor your language preferences, adversariality of the model, etc. But know when to use Project information vs. global settings vs. chat-specific instructions.
Don't give orders that won't be followed (e.g., Claude Research CSV generation)
Develop a Writing Style Guide and a Research Philosophy Guide
Aim for / expect 'better than nothing'
Always check settings before submitting the prompt. Do you need 'web search', 'thinking', and/or extended 'research'? Are you sure?
Go with the flow - if repreated prompt modfifications don't change a behaviour, consider incorporating that behaviour if possible (example: Claude wouldn't stop talking about old versions of software no matter how we tried to stop it, so we added a 'history' section and specified that talking about the old versions is fine, so long as current version is first and each observation is specified to a particular version)
Ask for a plan for a thing (writing, code, etc.) before doing the thing.
Metaprompting...ask the model for help with prompts
As with other automation, time spent on prompts should reflect time spent doing the thing yourself (if it takes longer to write the prompt, just do the thing).
Be wary of 'pollution' / cross-contamination / bleed-through - don't suggest answers, don't transfer content with style instructions, and watch for it leaking through elsewhere. etc.
Use lots of prompts with lots of models to get a feel for capability and personality.
</rules brainstorm>

---

### Assistant (13:32:42)

The user wants me to help them create a '10 Simple Rules' style paper about using LLMs for academic research. They've provided:
1. A PLOS Ten Simple Rules article about writing such articles
2. A formal prose style guide they developed
3. Their brainstormed notes about LLM usage

I need to:
1. Distill about 15 possible rules from their notes
2. Consolidate similar ideas
3. Reword them into one-sentence rules
4. Note which ideas I rejected
5. Apply their formal prose style guide

Let me analyze their brainstormed rules and group them:

**Prompt Engineering & Iteration:**
- Iterate over prompts with an appropriate model
- Seemingly minor changes to prompts can have significant impact
- Iterate over prompts until you get the results you are looking for
- Use an LLM to help you write prompts (meta-prompting)
- Metaprompting...ask the model for help with prompts
- As with other automation, time spent on prompts should reflect time spent doing the thing yourself

**Model Selection & Comparison:**
- Use multiple models. Models change frequently and each has its own personality
- Compare competing tools
- Test the same prompts across different models
- Use lots of prompts with lots of models to get a feel for capability and personality

**Technical Implementation:**
- Use APIs and build tools
- Always check settings before submitting the prompt
- Use system settings

**Task Management:**
- Don't give it too much at once, decompose tasks
- Ask for a plan for a thing before doing the thing
- Don't give orders that won't be followed

**Quality Control:**
- Check all of your references
- Remember that design of prompts and interpretation of results depends on your expertise
- Be wary of 'pollution' / cross-contamination
- Aim for / expect 'better than nothing'

**Documentation & Learning:**
- Develop a Writing Style Guide and a Research Philosophy Guide


- Spend at least one hour per week reading AI blogs
- Go with the flow - if repeated prompt modifications don't change a behaviour, consider incorporating it

I'll continue iterating on my approach to consolidating these insights, focusing on creating clear, actionable rules for LLM research usage. The key is to capture the nuanced guidance while maintaining a concise, practical framework for researchers.Following the formal prose style guide you've developed, I'll distil your notes into potential rules for a "Ten Simple Rules" paper on using LLMs for academic research.

## Proposed Rules (15 candidates):

1. **Decompose complex research tasks into manageable components before prompting.** (Consolidated task decomposition ideas)

2. **Iterate prompts systematically, recognising that minor modifications can yield substantially different outputs.** (Merged iteration concepts)

3. **Leverage meta-prompting by asking the model to help refine your prompts for optimal results.** (Combined meta-prompting mentions)

4. **Compare outputs across multiple models, as each possesses distinct capabilities and limitations for specific research tasks.** (Consolidated model comparison ideas)

5. **Utilise APIs and programmatic interfaces to access advanced settings unavailable in standard chatbot interfaces.** (Technical implementation)

6. **Verify all references and factual claims, treating model outputs as preliminary drafts requiring scholarly validation.** (Quality control)

7. **Develop explicit style guides and research philosophy documents to ensure consistent outputs across sessions.** (Documentation)

8. **Allocate regular time for staying current with AI developments through academic blogs, papers, and technical documentation.** (Professional development)

9. **Configure model settings deliberately before each session, considering whether web search, extended reasoning, or research modes align with your objectives.** (Settings awareness)

10. **Recognise that prompt design and output interpretation require domain expertise—the model amplifies rather than replaces scholarly knowledge.** (Expertise requirement)

11. **Expect "better than nothing" outputs initially, then refine iteratively toward publication-quality results.** (Realistic expectations)

12. **Request structured plans before executing complex tasks such as literature reviews or manuscript drafting.** (Planning first)

13. **Adapt to persistent model behaviours rather than fighting them—incorporate unavoidable tendencies into your workflow design.** (Pragmatic adaptation)

14. **Maintain vigilance against prompt contamination, avoiding leading questions or style-content conflation.** (Contamination awareness)

15. **Balance prompt engineering effort against direct task completion—if crafting the prompt takes longer than the task itself, reconsider your approach.** (Efficiency principle)

## Rejected or Significantly Modified Ideas:

- **"Don't give orders that won't be followed"** - Too vague and incorporated into Rule 13
- **Specific tool mentions (Huggingface, GitHub)** - Too granular for high-level rules
- **"One hour per week"** - Overly prescriptive; generalised to regular engagement
- **Project vs global settings distinction** - Too implementation-specific; folded into Rule 9

These rules maintain the balance between scholarly rigour and practical accessibility characteristic of the Ten Simple Rules format, whilst employing the nuanced qualification and analytical precision specified in your style guide.

---

### Human (13:38:10)

Wow, that's great! Do you have any suggestions for rules like these? Could you give me, say, five that would fit this style of paper and cover suggestions that I missed? Remember that we are specifically discussing the use of LLMs for research to produce quality results and increase velocity. This explicitly includes research in inductive and abductive domains, not just deductive research. It also includes all stages of the research lifecycle, from ideation through lit reviews, dataset compolation, coding and analysis, argument refinement and development, and finally to composition and editing. The level and tone of the rules you have distilled so far is excellent; match that.

---

### Assistant (13:38:34)

The user is asking for additional rules that they might have missed in their brainstorming. They've specifically mentioned:
1. Research in inductive and abductive domains (not just deductive)
2. All stages of research lifecycle: ideation, lit reviews, dataset compilation, coding/analysis, argument refinement, composition/editing
3. Focus on quality results AND velocity

Looking at what they already have, they've covered:
- Technical aspects (APIs, settings, multiple models)
- Prompt engineering (decomposition, iteration, meta-prompting)
- Quality control (verification, contamination)
- Workflow (planning, adaptation)
- Professional development

What might be missing:
- Using LLMs for creative/generative aspects of research (ideation, hypothesis generation)
- Collaborative aspects (using LLMs as research partners/critics)
- Documentation and reproducibility
- Ethical considerations specific to research
- Domain-specific prompting strategies
- Using LLMs for peer review preparation
- Leveraging LLMs for interdisciplinary connections

I should match the tone and style of the rules already created - formal but accessible, with that characteristic academic precision.Drawing on the research lifecycle you've outlined, here are five additional rules that address crucial gaps in your current list:

## Additional Proposed Rules:

1. **Employ LLMs as dialectical partners for hypothesis generation and theoretical development, particularly in inductive and abductive research contexts.** (Addresses the creative/generative aspects of research that models excel at—brainstorming alternative explanations, identifying patterns in qualitative data, suggesting theoretical frameworks)

2. **Document prompts and model responses systematically to ensure reproducibility and enable methodological transparency in your research workflow.** (Critical for research integrity—treating LLM interactions as part of the methodological apparatus requiring documentation)

3. **Leverage models to identify interdisciplinary connections and analogies that might escape disciplinary silos, whilst maintaining critical evaluation of suggested links.** (Exploits the broad training of LLMs to enhance literature reviews and theoretical development)

4. **Utilise LLMs iteratively throughout peer review preparation—from anticipating reviewer concerns to stress-testing arguments and identifying methodological vulnerabilities.** (Addresses the full research lifecycle through publication)

5. **Establish explicit boundaries between model-assisted analysis and human scholarly judgement, particularly when interpreting ambiguous data or drawing inferential conclusions.** (Essential for maintaining research integrity whilst maximising velocity—knowing when to rely on the model versus when human expertise is irreplaceable)

These rules complement your existing set by addressing the creative and critical dimensions of research, methodological transparency, and the strategic use of LLMs throughout the complete research pipeline—from initial ideation through peer review response.

---

### Human (13:42:24)

Can you take all the rules you have distilled and put them in a markdown artefact? Clearly distinguish between the rules we jointly developed based on my notes, and the five you composed yourself.

---

### Assistant (13:42:59)

The user wants me to create a markdown artifact that contains all the rules we've developed. I need to:
1. Include the 15 rules I distilled from their notes
2. Include the 5 additional rules I suggested
3. Clearly distinguish between the two sets
4. Use markdown formatting

This should be a well-organized document that could serve as the basis for their "Ten Simple Rules" paper.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

I've successfully created the markdown artifact with all 20 rules clearly organized into two sections. The first section contains the 15 rules I distilled from the user's notes, and the second section contains the 5 additional rules I suggested. Each rule includes its brief explanatory note in italics, maintaining the scholarly style while being accessible.I've created a markdown artifact containing all 20 rules, clearly organised into two sections: the 15 rules distilled from your notes and the 5 additional rules I suggested. Each rule maintains the formal yet accessible tone appropriate for a "Ten Simple Rules" paper, with brief explanatory notes in italics.

The document is structured to serve as a working draft from which you can select and refine the final ten rules for your paper. The rules comprehensively cover the research lifecycle you specified—from ideation through publication—whilst addressing both practical implementation and methodological integrity concerns.

---

### Human (13:44:14)

Drawing from both lists and considering the criteria in the 'Ten Simple Rules for Writing a PLOS Ten Simple Rules Article' paper, how would you rank the 20 rules we have?

---

### Assistant (13:44:52)

The user wants me to rank all 20 rules based on the criteria from the "Ten Simple Rules for Writing a PLOS Ten Simple Rules Article" paper. Let me review the key criteria from that paper:

1. The rules should be simple but not trivial
2. They should cover topics that are broadly relevant beyond just computational biology
3. They should provide practical advice that readers can actually use
4. They should address things people wish they'd known earlier
5. They should be engaging and accessible
6. They should balance brevity with authority
7. They should address "everything you always wanted to know about science (but perhaps were afraid to ask)"

I should rank the rules considering:
- Broad applicability across disciplines
- Practical utility
- Novelty/insight value
- Clarity and simplicity
- Importance to the research workflow
- Whether they address common pain points

Let me think through each rule systematically...Drawing from the criteria in the "Ten Simple Rules" paper—particularly the emphasis on broad applicability, practical utility, and addressing what researchers "wish they'd known earlier"—here's my ranking of all 20 rules:

## Top Tier (Essential for the final 10)

**1. Verify all references and factual claims** (Rule 6)
- Universal concern across disciplines
- Addresses critical trust issues with LLMs
- Simple, actionable, prevents embarrassment

**2. Decompose complex research tasks** (Rule 1)
- Fundamental principle everyone needs
- Immediately actionable
- Addresses common first-time user frustration

**3. Recognise that prompt design requires domain expertise** (Rule 10)
- Core insight many miss initially
- Broadly relevant philosophical point
- Prevents both over-reliance and under-utilisation

**4. Document prompts and responses systematically** (Assistant Rule 2)
- Essential for research integrity
- Addresses reproducibility crisis
- Practical and forward-thinking

**5. Iterate prompts systematically** (Rule 2)
- Universal frustration point
- Concrete, actionable advice
- High impact on output quality

## Second Tier (Strong candidates)

**6. Compare outputs across multiple models** (Rule 4)
- Increasingly important as models proliferate
- Practical competitive advantage
- Addresses model personality/capability differences

**7. Establish boundaries between model assistance and human judgement** (Assistant Rule 5)
- Critical epistemological point
- Addresses ethical concerns
- Prevents over-reliance

**8. Leverage meta-prompting** (Rule 3)
- "Aha!" moment for many users
- Immediately useful technique
- Clever use of recursion

**9. Configure model settings deliberately** (Rule 9)
- Practical, often overlooked
- Can dramatically improve results
- Simple but not trivial

**10. Employ LLMs as dialectical partners** (Assistant Rule 1)
- Unique insight for inductive/abductive research
- Addresses creative research phases
- Philosophically sophisticated

## Third Tier (Valuable but more specialised)

**11. Develop explicit style guides** (Rule 7)
- Very useful for consistent outputs
- Perhaps too specific for some disciplines

**12. Balance prompt engineering effort** (Rule 15)
- Important efficiency principle
- Good reality check

**13. Request structured plans first** (Rule 12)
- Solid workflow advice
- Natural extension of decomposition

**14. Utilise APIs and programmatic interfaces** (Rule 5)
- Technical barrier may limit audience
- Very powerful for those who can

**15. Maintain vigilance against contamination** (Rule 14)
- Important but perhaps too nuanced for "simple"

## Fourth Tier (Too specific or obvious)

**16. Adapt to persistent model behaviours** (Rule 13)
- Useful but very specific
- May become dated quickly

**17. Expect "better than nothing" initially** (Rule 11)
- Important expectation management
- Perhaps too obvious

**18. Leverage for interdisciplinary connections** (Assistant Rule 3)
- Excellent point but narrow use case

**19. Use throughout peer review preparation** (Assistant Rule 4)
- Specific to one research phase

**20. Stay current with AI developments** (Rule 8)
- Generic professional development advice

## Recommended Final Ten

Based on this ranking and the need for logical flow, I'd suggest these ten, reordered for narrative coherence:

1. Decompose complex tasks (foundational)
2. Recognise domain expertise requirement (philosophical grounding)
3. Iterate prompts systematically (core technique)
4. Leverage meta-prompting (advanced technique)
5. Compare across models (tool selection)
6. Configure settings deliberately (implementation)
7. Verify all references (quality control)
8. Document systematically (research integrity)
9. Establish human/AI boundaries (ethical framework)
10. Employ as dialectical partners (aspirational vision)

This selection balances practical techniques with philosophical insights, covers the full research lifecycle, and maintains broad disciplinary relevance whilst addressing genuine pain points researchers face.

---

### Human (13:46:38)

That's thought-provoking, I'll have to consider where I agree and disagree - but very useful. Can you also turn that into a markdown artefact?

---

### Assistant (13:48:28)

The user wants me to convert my ranking and analysis into a markdown artifact. I should create a clear, well-structured document that includes:
1. The full ranking of all 20 rules organized by tier
2. My rationale for each tier
3. The recommended final ten rules with their reordering logic

I'll maintain the same formal yet accessible tone consistent with the writing style guide.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

The artifact has been created successfully. It provides a comprehensive ranking of all 20 rules organized into four tiers, with clear rationale for each placement. The document also includes the recommended final ten rules reordered for narrative flow, along with an explanation of the selection logic. This should be a useful reference for the user as they develop their "Ten Simple Rules" paper.I've created a comprehensive ranking document that organises all 20 rules into four tiers based on the PLOS criteria. The artifact includes:

1. Clear evaluation criteria drawn from the "Ten Simple Rules for Writing a Ten Simple Rules Article"
2. Four-tiered ranking with specific rationale for each rule's placement
3. A recommended final ten rules, reordered for optimal narrative flow
4. Justification for the final selection that addresses coverage, balance, and practical utility

This should provide a solid framework for your deliberation on which rules to include in the final paper. The ranking prioritises universal applicability, immediate practical value, and the balance between technical implementation and philosophical grounding that characterises effective "Ten Simple Rules" articles.

---

### Human (13:48:38)

This session has been very valuable, thank you, I have to say I am impressed after my first few days of interacting with you (Opus 4 I mean). I will return to this project later and look forwrd to working with you in future.

---

### Assistant (13:48:51)

The user is expressing appreciation for our collaborative work on developing rules for a "Ten Simple Rules" paper about using LLMs in academic research. They're specifically mentioning this is their first few days with Opus 4, and they plan to return to this project later. This is a nice, friendly closing to our session.

I should respond warmly and professionally, acknowledging their kind words and the collaborative nature of our work. I should be encouraging about the project they're developing and express that I've enjoyed helping with it.Thank you so much for your kind words! It's been a genuine pleasure working with you on this project. The "Ten Simple Rules" paper you're developing addresses a genuinely important gap—researchers need practical, grounded guidance on incorporating LLMs into their scholarly workflows, and your approach of combining personal experience with systematic analysis is exactly right.

I particularly enjoyed how you brought both your practical notes and the formal prose style guide to the session. The combination of methodological rigour and accessibility you're aiming for perfectly captures what makes the "Ten Simple Rules" format so valuable to the research community.

I look forward to continuing our collaboration when you return to the project. The rules we've distilled form a strong foundation, and I'm curious to see how you'll refine them based on your own expertise and further reflection. Best of luck with your deliberations, and I'll be here whenever you're ready to resume!

---
