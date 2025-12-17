# Crafting an Impactful "Whoami" Slide

## Metadata
- **UUID:** `4408f2f9-2d40-48e1-a171-896e35a30296`
- **URL:** https://claude.ai/chat/4408f2f9-2d40-48e1-a171-896e35a30296
- **Created:** 2025-02-16 10:13:29
- **Updated:** 2025-02-16 10:51:24
- **Source:** Brian's Claude export

---

## Conversation

### Human (10:13:31)

Hi Claude. 

For this slide deck:

I need to do an edit, and I need to work out my whoami page. (I'm including that as a joke since the folks at the research data alliance may appreciate it...)

I need to figure out how to bullet my intro text:

<intro_blurb>
Dr Brian Ballsun-Stanton is leading Macquarie University's Faculty of Arts understanding, policy, teaching, and research initiatives around the techniques and appropriate uses of Generative AI. With a PhD in Philosophy of Data that enables him to bridge theoretical frameworks with practical implementations, he has developed the university's "Guidance Note: Using Generative Artificial Intelligence in Research" and pioneered AI integration across multiple disciplines, winning the 2024 Faculty of Arts Educational Leadership Award for his innovative work in AI-enhanced learning. His implementations span Languages, Security Studies, and Law, each featuring unique aspects such as AI-optional and AI-required assessments, cross-model critical evaluation, and simulations. He teaches the effective use and techniques of generative AI to undergraduate and post-graduate students, reaching more than 1,500 students through various initiatives.Brian has conducted invited workshops and presentations on LLMs for staff, postgraduate students, and external stakeholders internationally, in Europe and the United States. He has presented his "Introduction to LLM" workshop to early-career researchers and postgraduate students across Australia, the United States, and Europe on more than 20 occasions and has advised organisations from the University of Tasmania to NBNco on AI policy and implementation. His work on effective AI use has led to invitations from IEEE Silicon Valley and multiple Australian universities to present and consult on policy and practical pedagogy.He has more than 15 years of experience as a data scientist, educator, sysadmin, and data security specialist, with particular expertise in natural language processing and social network analysis. He has served as Chief Investigator on grants and projects in humanities, social sciences, and security studies totalling over AUD$3,559,083, and has led a big data investigation of violent extremism using tens of millions of social media posts. As Technical Director for the FAIMS Project, he has delivered more than 70 field data collection modules since 2013, bridging the needs of archaeology, geology, ecology, and oral history projects. Brian is an internationally respected researcher in the Digital Humanities with 18 peer-reviewed publications, commissioned reports, newspaper articles, book chapters, and conference presentations, including recent publications on AI policy and implementation in higher education.In the digital humanities, he has established himself as a mentor and leader, guiding researchers and emerging scholars in the effective use of technology for digitally enabled research. His experience implementing theoretically informed technical solutions while accommodating diverse research practices has made him a key figure in bridging technological innovation with humanities scholarship, university AI policy, and educational leadership.
</intro_blurb>

What 3-4 bullets do you recommend for that intro slide, besides linking to my orcid?

---

### Assistant (10:13:42)

 Let me help you distill that comprehensive introduction into 3-4 impactful bullet points that would work well on your "whoami" slide, keeping with the command-line theme.

Based on your extensive background, here are the recommended bullet points that capture your key roles and expertise while maintaining a balance between technical and academic leadership:

* Solutions Architect (Digital Humanities) for the Faculty of Arts
* Leading MQ's AI integration in teaching and research (2024 Faculty Educational Leadership Award)
* Technical Director of FAIMS Project (70+ field data collection modules)
* 15+ years experience bridging theoretical frameworks with practical implementations in data science and digital humanities

You could also include a link to your ORCID as:
* ORCID: [your-orcid-number]

These bullets capture your current role, leadership in AI implementation, major project leadership, and breadth of experience. They also create a natural flow from your current position to your broader impact and expertise.

Would you like me to suggest alternative formulations or focus on different aspects of your background?

---

### Human (10:22:37)

Ok, let's go for the next slide. I need to crunch down:

<slide>
* Preprint - Fundamental thing: the output is purely the function of the prompts (system, user, assistant) plus a small amount of random number generation. 
   * No default access to "facts"
   * They operate on information tacitly encoded in the prompts (build a grimoire!)
   * Tool use is *interpreted* – **THERE ARE NO DATABASES**
* There is no judgement
* These are vibe machines,
   * Shockingly useful when considered as present-at-hand tools. 
   * Dangerous when invisible as ready-to-hand extensions 
These things are **not **your "plastic pal who is fun to be with." **(Adams)**
</slide>

---

### Assistant (10:22:45)

 Looking at this slide about LLMs not being search engines, I'll help restructure it while maintaining the key points and philosophical references. Here's a suggested revision that keeps the core message but tightens it up:

* LLMs transform prompts into output via:
   * No inherent factual knowledge
   * Pattern matching from training data
   * Interpreted tool use (no real databases)
* These are "vibe machines":
   * Powerful when used mindfully
   * Risky when treated as transparent tools
* Not your "plastic pal who is fun to be with" (Adams)

This restructuring:
- Maintains the key technical points about LLM functionality
- Preserves the Heideggerian present-at-hand/ready-to-hand distinction while making it more accessible
- Keeps the Douglas Adams reference as a powerful closing point
- Removes some redundancy while maintaining the critical warnings

Would you like me to suggest alternative phrasings or emphasize different aspects?

---

### Human (10:40:27)

And next

<slide>
* Effective use requires:
   * Control over the system prompt - vibes and guardrails
   * Control over the user **prompts**
      * Establish context
      * Set role, expected feedback
      * Functional decomposition of task
      * One single thing to accomplish per prompt
   * Control over the LLM's responses
      * Edit/delete/iterate
      * Everything is part of the context window, consider these your content
* Interface has affordances baked in
   * Many providers set their system prompts (less useful for some tasks)
   * Ensure you know if it's trying to use tools/search
</slide>

---

### Assistant (10:40:32)

 Let me help streamline this slide about effective LLM use while maintaining the key hierarchical structure. Here's a suggested revision:

* Three levels of control needed:
   * System prompt: Sets boundaries and behavior
   * User prompts:
      * Clear context and role
      * One task per prompt
      * Decompose complex tasks
   * Response management:
      * Iterative refinement
      * Context window awareness

* Interface considerations:
   * Provider-set system prompts
   * Tool/search integration checks

This restructuring:
- Maintains the three-level control framework
- Simplifies the nested structure while preserving key points
- Reduces redundancy in the user prompts section
- Keeps the important interface warnings
- Makes it more scannable for presentation

Would you like me to suggest alternative organizations or emphasize different aspects?

---

### Human (10:51:18)

and

<slide>
* **Privacy:** Different modalities of use are covered by different terms of service.
* **Budget:** Paying for tokens tends to be most privacy preserving (by contract) and much cheaper than monthly subscriptions.
* **Provenance: **Terms of service update every few months, they tend to be most researcher-friendly with API use.
* **Control: **Maximum control over system, user, and assistant prompts
* **Scale: The API allows automation**
</slide>

(This one already fits, but...

---

### Assistant (10:51:24)

 For this slide about API usage benefits, let's tighten it while maintaining the clear SPCS (Scale, Privacy, Control, Scale) framework. Here's a slightly refined version:

* **Privacy:** Distinct terms of service per usage mode
* **Budget:** Token-based pricing - cheaper and more private
* **Provenance:** Most researcher-friendly ToS in API mode
* **Control:** Full prompt control (system/user/assistant)
* **Scale:** Enables automation and batch processing

The changes are subtle but:
- Makes each bullet more concise
- Standardizes the format
- Adds a bit more detail to "Scale" since it was previously the shortest
- Maintains the emphasis on research context
- Keeps the parallel structure

Would you like me to suggest alternative phrasings or a different organization?

---
