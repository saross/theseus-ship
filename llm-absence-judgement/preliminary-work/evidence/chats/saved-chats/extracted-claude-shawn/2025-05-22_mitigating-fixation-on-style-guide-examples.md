# Mitigating Fixation on Style Guide Examples

## Metadata
- **UUID:** `cc2dcd29-94f9-433d-a22f-714368b17005`
- **URL:** https://claude.ai/chat/cc2dcd29-94f9-433d-a22f-714368b17005
- **Date:** 2025-05-22 11:00:44

---

## Conversation

### Human (10:56:41)

Hi Claude, when deploying the writing style guide, it sometimes impacts the content of your writing, causeing you to fixate too much on FAIMS (likely due to the example). How do you think we can mitigate this tendency?

---

### Assistant (10:57:00)

The user is pointing out an interesting issue with the writing style guide I've been provided. They're noticing that when I apply the style guide, I sometimes get too focused on FAIMS content, probably because the example in the style guide uses FAIMS as the subject matter for demonstrating the enhanced writing style.

This is a good observation about how examples can inadvertently bias AI responses. The style guide includes a specific example about FAIMS Mobile and database identifiers, and it seems like when I'm applying the style guide, I might be unconsciously drawing too heavily on that specific content area rather than just the stylistic principles.

Let me think about solutions:

1. **Separate style principles from content examples**: The style guide could include the principles but use more varied examples, or more generic placeholder examples rather than domain-specific ones.

2. **Explicit reminder about content independence**: Add a note in the style guide that the examples are purely for stylistic demonstration and shouldn't influence topic focus.

3. **Multiple domain examples**: Instead of just the FAIMS example, include examples from different research domains to show the style principles apply broadly.

4. **Meta-instruction about avoiding content bleed**: Include an explicit instruction for me to focus on the stylistic principles while keeping content completely independent of the examples.

5. **Abstract the example**: Replace the specific FAIMS example with a more generic technical writing example that demonstrates the same principles.

This is a really useful piece of feedback about how example content in guidelines can create unintended biases in AI responses.That's an excellent observation about how the example content can inadvertently bias my focus. The FAIMS example in the style guide, while demonstrating good stylistic principles, seems to be creating a cognitive anchor that pulls my attention toward that specific domain even when we're discussing completely different topics.

Here are several ways we could mitigate this:

## **Immediate Solutions**

1. **Add a meta-instruction** to the style guide explicitly stating: "Apply these stylistic principles to any content domain. The FAIMS example demonstrates technique only—do not let it influence topic selection or emphasis."

2. **Replace the domain-specific example** with something more generic, like:
   > **Original**: "The system generates identifiers using standard protocols..."
   > **Enhanced**: "The system generates identifiers using standard protocols. We initially investigated using formal specification X, but interactions between our core database and the extension modules limited us to shorter alternatives."

## **Structural Improvements**

3. **Multiple micro-examples** from different domains (archaeology, environmental science, software development) to show the principles apply broadly.

4. **Separate the principles from examples** entirely—have a "Principles" section followed by a distinct "Examples" section with clear boundaries.

5. **Use placeholder content** like "[Technical Process A] incorporates [Component B] into each [Unit C]..." to demonstrate structure without domain content.

## **Process Solution**

6. **Two-step application**: First, I identify the core stylistic principles needed for your specific content, then apply them without referencing the guide's examples.

Which approach appeals to you most? I suspect option 1 (adding the meta-instruction) might be the quickest fix, while option 4 (structural separation) might be most robust long-term.

---

### Human (10:58:25)

These are great suggestions. Let's try replacing the single example with multiple examples from different domains. Can you generate some from the examples of my writing attached in 'Project Knowledge'?

---

### Assistant (10:58:47)

The user wants me to replace the single FAIMS example in the writing style guide with multiple examples from different domains, drawn from the documents they've provided. Let me look through the documents to find good examples that demonstrate the writing principles.

Looking at the documents:

1. **Sobotkova et al. - 2024 - Validating Predictions of Burial Mounds** - This is about machine learning and archaeological prospection
2. **Ross et al. - 2022 - FAIRer Data through Digital Recording** - This is about FAIR data principles and field recording systems
3. **Ross and Anderson - 2022 - Avoiding a digital dark age** - This appears to be about digital preservation and technology
4. **Sobotkova et al. - 2021 - Deploying an offline, multi-user mobile system** - This is about field recording systems in archaeology
5. **Sobotkova et al. - 2023 - Creating large, high-quality geospatial datasets** - This is about crowdsourcing and map digitisation
6. **Ballsun-Stanton et al. - 2018 - FAIMS Mobile** - This is about field research software
7. **Eftimoski et al. - 2017 - The impact of land use and depopulation** - This is about predictive modelling for cultural heritage
8. **Ross et al. - 2018 - The Tundzha Regional Archaeology Project** - This is about landscape archaeology

I should pick examples from different domains to show how the style principles apply across:
- Machine learning/computational archaeology
- Data management/digital humanities
- Predictive modelling/statistics
- Field methodology/survey archaeology

Let me find some good "before and after" examples that demonstrate the style principles like breaking up long sentences, using active voice, providing context for technical terms, etc.

From the ML paper, I could use something about CNN methodology.
From the data paper, something about FAIR principles.
From the predictive modelling paper, something about logistic regression.
From the field work paper, something about survey methodology.

Let me look for some passages that could be improved according to the style guide principles.Excellent idea! Here are multiple examples from different domains in your work that demonstrate the style principles:

## **Machine Learning/Archaeological Prospection**
(From the burial mounds ML validation paper)

**Original style**:
> "Automated object detection has been the holy grail of archaeological remote sensing for the last two decades. Machine learning (ML) models have proven able to detect uniform features across a consistent background, but more variegated imagery remains a challenge."

**Enhanced style**:
> "Automated object detection has been the holy grail of archaeological remote sensing for the last two decades. Machine learning models have proven capable of detecting uniform features across consistent backgrounds. However, more variegated imagery—landscapes with diverse vegetation, terrain, or land use—remains a significant challenge."

## **Data Management/Digital Humanities**
(From the FAIR data paper)

**Original style**:
> "The FAIMS approach to data storage provides flexibility and versioning at the expense of speed as the number of records increases. FAIMS therefore incorporates automated load testing to predict field performance."

**Enhanced style**:
> "The FAIMS approach to data storage provides flexibility and complete versioning, but processing speed decreases as record numbers increase. To address this trade-off, FAIMS incorporates automated load testing that predicts field performance under realistic conditions."

## **Predictive Modelling/Cultural Heritage**
(From the land use impact paper)

**Original style**:
> "This article uses an ordered logistic regression (logit) model to assess the vulnerability of ancient burial mounds to human activity in the Kazanlak Valley, Bulgaria."

**Enhanced style**:
> "This article uses an ordered logistic regression model to assess the vulnerability of ancient burial mounds to human activity in the Kazanlak Valley, Bulgaria. Logistic regression—often called 'logit'—provides a statistical framework for predicting categorical outcomes, in this case different levels of mound preservation."

## **Crowdsourcing/Collaborative Research**
(From the map digitisation paper)

**Original style**:
> "Crowdsourcing can expand the scope of map digitisation. In this context, crowdsourcing indicates the voluntary creation of geographic information by amateurs ('Volunteered Geographic Information'), using software that exposes a subset of GIS capabilities in a manner intuitive enough to be utilised by minimally trained actors."

**Enhanced style**:
> "Crowdsourcing can dramatically expand the scope of map digitisation. In this context, crowdsourcing means the voluntary creation of geographic information by non-specialists—termed 'Volunteered Geographic Information' or VGI. This approach uses software that exposes essential GIS capabilities through interfaces intuitive enough for minimally trained participants."

These examples demonstrate the key principles across different domains: breaking long sentences for clarity, defining technical terms contextually, using active voice strategically, and maintaining precision while improving accessibility.

---

### Human (11:00:30)

Those are great examples, can you put them in a fenced markdown block or artefact with a clear 'Examples' heading that I can add to the existing Style Guide?

---

### Assistant (11:00:44)

The user wants me to create a properly formatted section that they can add to their existing style guide. I should format this as a clear section with examples from their different research domains, using a fenced markdown block or artifact. Since this is substantial content that they plan to use as reference material, an artifact would be most appropriate.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



Perfect! This examples section draws from your actual research across multiple domains and includes the meta-instruction we discussed to prevent domain bias. You can now add this section to your existing style guide, replacing or supplementing the single FAIMS example.

---
