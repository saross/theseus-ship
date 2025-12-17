# v8-ArchIScan-metadata

## Metadata
- **UUID:** `6fe826fa-967c-4354-b08d-7c96a6540f9c`
- **URL:** https://claude.ai/chat/6fe826fa-967c-4354-b08d-7c96a6540f9c
- **Date:** 2025-05-05 11:49:23

---

## Conversation

### Human (10:31:35)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
Note that a 'Writing Style Guide' is attached to this Project, please apply it to your report and the CSV.

---

### Assistant (10:31:40)



I understand that we'll be collecting metadata about research software tools used in archaeology, history, and related historical studies disciplines. The detailed prompt you've provided gives me a comprehensive framework for researching and documenting these tools.

When you provide me with the name or acronym of a tool, I'll:

1. Research it thoroughly using multiple sources
2. Collect the required metadata following the specifications
3. Present my findings in the CSV format requested
4. Apply the writing style from the guide you've attached

I'll focus on thoroughly researching each tool until I reach information saturation, documenting all relevant aspects while maintaining academic clarity, directness, and appropriate technical precision.

I'm ready to begin with the first tool whenever you'd like to provide it.

---

### Human (10:32:07)

Arch-I-Scan

---

### Assistant (10:32:13)



I'll research Arch-I-Scan thoroughly to collect comprehensive metadata according to the framework you've provided. This appears to be an archaeological research software tool that I should investigate in depth. I'll start my research process right away!
```
This block is not supported on your current device yet.
```

Your Arch-I-Scan research report is ready. It covers how this AI-powered tool revolutionizes Roman pottery analysis using smartphone-based image recognition. The report details the technology's machine learning approach, development history, technical implementation, real-world applications, strengths and limitations, comparable technologies, and long-term viability in archaeological research.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (10:49:55)

please also produce the requested CSV

---

### Assistant (10:50:49)



Based on the comprehensive research I've conducted, I've compiled the metadata for Arch-I-Scan according to your specifications. Here's the completed CSV with all the requested information:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"Arch-I-Scan","Arch-I-Scan is an image recognition software that uses artificial intelligence to identify Roman pottery fragments via smartphone photography. The system enables archaeologists and non-specialists to photograph pottery vessels or fragments using ordinary smartphones, which the system then analyzes to provide accurate identifications of form and fabric type. The current version primarily focuses on Roman terra sigillata (samian ware), providing crucial data for understanding Roman foodways through more efficient pottery analysis. Developed at the University of Leicester through collaboration between archaeology and computer science, the tool significantly reduces the specialist-dependent bottleneck in processing archaeological ceramics.","Arch-I-Scan originated as part of the broader investigation into Roman eating and drinking practices. The project's development spans four main phases: (1) Conceptual foundation (2017-2018) through the 'Big Data on the Roman Table' research network with initial proof-of-concept experiments published in Internet Archaeology in 2018; (2) Full project development (2019-2022) with dedicated funding from the Arts and Humanities Research Council (grant reference AH/R004986/1) establishing partnerships with major UK museums and archaeological institutions; (3) Technical innovation phase (2021-2022) when the team published significant methodological advances in using synthetic data generation and 3D simulation techniques to enhance AI capabilities; and (4) Final phase (2022-2023) when the project transitioned from development to dissemination with datasets made available through GitHub repositories. Throughout its evolution, the project maintained its focus on Roman finewares, particularly terra sigillata, while expanding technical capabilities and institutional partnerships.","The current version of Arch-I-Scan employs convolutional neural networks (CNNs) similar to those used in facial recognition technology, implemented primarily in Python. The system architecture consists of five integrated components: (1) a mobile interface data acquisition layer for capturing pottery images in the field; (2) a processing layer for image preprocessing and feature extraction; (3) a neural network classification layer that identifies pottery types; (4) a database storage layer for training data and results; and (5) a user interface frontend for viewing and managing results. The system incorporates three notable technical innovations: transfer learning to overcome limited training data through pre-training on synthetic examples; synthetic data generation creating 3D simulations from published pottery drawings; and mobile-first design optimizing for field use on ordinary smartphones. The technical team addressed the common archaeological challenge of limited training data through a novel approach – generating 3D simulations from traditional drawings of pottery forms, dramatically expanding their training dataset beyond physically available specimens. This synthetic data generation proved critical for achieving sufficient accuracy with the limited number of physical specimens available. The system processes images through multiple stages: preprocessing to standardize input, feature extraction to identify diagnostic elements, and classification to match against known forms. Though deployed on mobile devices, the training architecture requires more substantial computing resources. For previous versions, the team experimented with different neural network architectures before settling on their current approach, which balances accuracy with the constraints of mobile deployment.","2025-05-05","yes","Arch-I-Scan fully qualifies as research software meeting all essential criteria and multiple supporting criteria. The tool has a clear research-specific purpose (analyzing Roman pottery), directly engages with research materials (transforming pottery photographs into identifications), and aligns with established archaeological methodologies. Additionally, it integrates domain knowledge (pottery classifications), supports the research lifecycle (data collection and analysis stages), performs analytical functions (pattern recognition in pottery forms), transforms data (from images to identifications), and includes visualization capabilities. Its documentation explicitly addresses research applications and it was developed specifically to support archaeological inquiry.","https://github.com/ArchiScn","","","https://le.ac.uk/archaeology/research/new-approaches-to-the-material-world/arch-i-scan","Unknown (Likely open research)","Ceramic analysis|Data collection|Artefact morphology|Shape recognition|Machine learning","archaeology-ai-integration|pottery-classification|mobile-field-tools|machine-vision|roman-ceramics","2018-06-01","2023-05-01","Unknown","Active","University of Leicester|Arts and Humanities Research Council|Museum of London|Museum of London Archaeology|University of Leicester Archaeological Services|The Vindolanda Trust|Colchester and Ipswich Museum Service","Penelope Allison|Ivan Tyukin|Eric Nordquist|Evgeny Mirkes|Shyha Gundakaram|Yi Sun|Yi Ren|Cristina Criado-Sirvent|Rosie Campbell|Alexander Ashton","Medium (6-20)","Archaeology","Project-specific","Comprehensive","Arch-I-Scan has established partnerships with several major UK museums and archaeological institutions, most notably cataloging Roman finewares in the Museum of London's collection. The project has produced at least 6 peer-reviewed publications in specialized journals including Internet Archaeology and the Journal of Computer Applications in Archaeology. The 2021 paper 'Learning from Scarce Information: Using Synthetic Data to Classify Roman Fine Ware Pottery' has been cited in multiple papers addressing machine learning applications in archaeology and cultural heritage. The project's GitHub repository shows ongoing development activity through 2023. Community engagement is evidenced through collaborative work with the Vindolanda Trust, where the system was tested during COVID-19 lockdown restrictions, enabling remote pottery classification. The tool's development was supported by a significant Arts and Humanities Research Council grant (AH/R004986/1).","Data Acquisition|Processing|Analysis","research-specific","Stand-alone software","Python","Android|iOS|Web","","The current version interoperates with standard image formats (JPG, PNG) captured by smartphone cameras. Outputs are stored in a database format that can be exported to CSV and other standard formats for integration with collection management systems. The system currently accepts standard 2D images but has been developed with the capability to utilize 3D models when available. Version compatibility is maintained across recent Android and iOS operating systems, with web interface options for desktop access to results.","The current version of Arch-I-Scan offers five significant strengths: (1) Accessibility through smartphone-based operation, enabling non-specialists to contribute to archaeological documentation; (2) Continuous improvement through machine learning capabilities that enhance accuracy as more examples are processed; (3) Scalability for processing larger pottery assemblages than traditional methods allow, potentially transforming understanding of Roman foodways through more comprehensive datasets; (4) Time efficiency by reducing specialist time spent on basic identification, allowing experts to focus on novel or challenging examples; (5) Knowledge sharing through freely available datasets for reference and comparison. The synthetic data approach represents a methodological innovation with potential applications beyond pottery, particularly valuable for archaeological subfields where training examples are limited. The system's transparent research methodology, with published algorithms and datasets, enhances reproducibility and allows independent verification of results.","Despite its innovations, the current version of Arch-I-Scan faces several limitations: (1) Training requirements necessitate extensive initial datasets before achieving optimal accuracy, creating a bootstrap challenge for new pottery types; (2) Developmental status means functionality is still evolving, with ongoing refinements to the machine learning models; (3) Specialized focus primarily on Roman terra sigillata limits immediate applicability to other pottery types without additional training; (4) Verification needs persist, as the system still requires expert validation for certain identifications; (5) Technical challenges in handling variable archaeological fragments, particularly weathered or atypical examples. The accuracy rates, while promising (reported at 80-85% for well-preserved examples), remain lower than expert human classification in certain contexts. The system's reliance on good lighting conditions and relatively standardized photography poses challenges in varied field environments. Previous versions showed more significant limitations in handling variations in vessel completeness, with performance decreasing substantially when working with small fragments rather than complete vessels.","Arch-I-Scan demonstrates good long-term survivability prospects due to several factors: (1) Institutional backing from the University of Leicester provides solid academic infrastructure; (2) Cross-disciplinary foundation through collaboration between archaeology and computing creates broader institutional investment; (3) Partnerships with major museums and archaeological services establish a stakeholder network with vested interest in the tool's continued development; (4) Open data approach with freely available datasets supports continued use even if active development slows; (5) Integration with educational initiatives at participating institutions embeds the technology within teaching practices. Challenges to sustainability include securing continued funding beyond the initial AHRC grant period, maintaining technical expertise as team members transition, and adapting to evolving mobile technologies and AI frameworks. The project's leadership by established academics with continuing positions at the University of Leicester provides some stability, and the interdisciplinary nature of the project increases potential funding sources across both humanities and technical domains.","The most comparable alternative is ArchAIDE (Archaeological Automatic Interpretation and Documentation of cEramics), funded by the European Union's Horizon 2020 program (2016-2019). ArchAIDE serves similar purposes but employs two distinct recognition methods: shape-based analysis of profiles and appearance-based analysis focusing on decorative features. It includes Roman Amphorae and various terra sigillata types, offering somewhat broader initial scope than Arch-I-Scan. Other alternatives include traditional methods of pottery documentation, such as manual drawing and photography, which provide high accuracy but at significantly lower speed. Earlier computer vision systems like those developed by Karasik and Smilansky (2008) use 3D scanning technologies but require more specialized equipment and lack Arch-I-Scan's mobile-first approach. General-purpose image recognition platforms could be adapted for pottery classification but would require extensive training and lack the specialized features for archaeological applications. Arch-I-Scan distinguishes itself through its focus on accessibility via ordinary smartphones and its specialized training for Roman finewares."
```

This metadata encompasses the full scope of Arch-I-Scan, covering its development history, technical implementation, institutional backing, strengths, weaknesses, and place within the archaeological technology landscape. The information has been structured according to your specifications, with careful attention to evidence-based assessment and version-specific details.

---

### Human (11:45:22)

Claude, in the reports you write, the titles are a little too...exuberant. I'd like descriptive titles that are interesting, but perhaps toned down a little / a little more formal. How can I adjust the prompt or the writing style guide to encourage that?

---

### Assistant (11:45:26)



---

### Human (11:45:34)

Claude, in the reports you write, the titles are a little too...exuberant. I'd like descriptive titles that are interesting, but perhaps toned down a little / a little more formal. How can I adjust the prompt or the writing style guide to encourage that?

---

### Assistant (11:45:50)


The user is giving me feedback about the tone of the titles in the reports I write - they find them too "exuberant" and would prefer more descriptive but formal titles. I need to suggest changes to either the prompt or the writing style guide to achieve this.

Let's analyze the title I created in my previous artifact:
"AI archaeology: how Arch-I-Scan revolutionizes Roman pottery analysis"

I can see how this could be considered somewhat exuberant with phrases like "AI archaeology" and "revolutionizes". It has an enthusiastic, almost journalistic tone rather than an academic one.

To achieve more formal, descriptive titles that remain interesting but are toned down, I can suggest adjustments to either:
1. The writing style guide
2. The prompting approach

Here are my suggestions:

You're absolutely right about the titles. The current one ("AI archaeology: how Arch-I-Scan revolutionizes Roman pottery analysis") is indeed too journalistic and sensationalized for formal research documentation. 

Here are specific adjustments you could make to achieve more formal, descriptive titles:

### Option 1: Add a section to the Writing Style Guide

You could add a specific "Title Conventions" section to your style guide:

```
## Title Conventions

- **Academic Precision**: Create titles that accurately describe the tool's function without sensationalism or journalistic embellishment
- **Descriptive Format**: Follow the pattern "[Tool Name]: [Primary Function] for [Application Domain]"
- **Neutral Tone**: Avoid emotionally charged terms like "revolutionary," "groundbreaking," or "game-changing"
- **Terminology Alignment**: Use discipline-specific terminology appropriate to the tool's field
- **Conciseness**: Keep titles under 12 words while maintaining clarity and information value
```

### Option 2: Add specific instructions to the prompt

Alternatively, you could add instructions directly to your prompt:

```
When reporting on research software tools, use formal academic titles that:
1. Clearly describe the tool's primary function
2. Avoid sensationalist terms (revolutionary, cutting-edge, etc.)
3. Follow a consistent "[Tool Name]: [Function] for [Domain]" format
4. Use appropriate technical terminology
5. Maintain professional tone appropriate for academic documentation
```

### Examples of improved titles:

Instead of "AI archaeology: how Arch-I-Scan revolutionizes Roman pottery analysis"

Better alternatives would be:
- "Arch-I-Scan: Computer Vision System for Roman Pottery Identification"
- "Arch-I-Scan: Mobile Image Recognition for Archaeological Ceramics Classification"
- "Arch-I-Scan: Automated Identification of Roman Terra Sigillata"

These maintain information value while adopting a more measured, academic tone suitable for formal research documentation.

---

### Human (11:48:21)

Yes, that's more like what I want. I will update the writing style guide. Since I often use this guide with long and complex prompts, it's important for it to be as consice as possible (while still accomplishing what needs to be accomplished). Can you suggest a more concise version of your new style guide text? We want to retain the impact, so if it can't be shortened without loss, that's fine, but if it can, please suggest a more concise version.

## Title Conventions - **Academic Precision**: Create titles that accurately describe the tool's function without sensationalism or journalistic embellishment - **Descriptive Format**: Follow the pattern "[Tool Name]: [Primary Function] for [Application Domain]" - **Neutral Tone**: Avoid emotionally charged terms like "revolutionary," "groundbreaking," or "game-changing" - **Terminology Alignment**: Use discipline-specific terminology appropriate to the tool's field - **Conciseness**: Keep titles under 12 words while maintaining clarity and information value

---

### Assistant (11:48:34)


The human is asking me to create a more concise version of the "Title Conventions" section I suggested for their writing style guide. They want to maintain the impact while reducing length.

Here's the original text:

## Title Conventions
- **Academic Precision**: Create titles that accurately describe the tool's function without sensationalism or journalistic embellishment
- **Descriptive Format**: Follow the pattern "[Tool Name]: [Primary Function] for [Application Domain]"
- **Neutral Tone**: Avoid emotionally charged terms like "revolutionary," "groundbreaking," or "game-changing"
- **Terminology Alignment**: Use discipline-specific terminology appropriate to the tool's field
- **Conciseness**: Keep titles under 12 words while maintaining clarity and information value

Let me create a more concise version while preserving the key points:

1. I can combine the "Academic Precision" and "Neutral Tone" points as they're related
2. I can make the bullet points themselves more concise
3. I can streamline the examples
4. I'll keep the format recommendation as it's essential

Here's my revised, more concise version:

Here's a more concise version of the Title Conventions section that preserves all the key requirements:

## Title Conventions
- **Format & Structure**: Use "[Tool Name]: [Primary Function] for [Application Domain]" pattern
- **Academic Tone**: Describe function precisely; avoid sensationalist terms ("revolutionary," "game-changing")
- **Technical Accuracy**: Employ discipline-specific terminology appropriate to the tool's field
- **Brevity**: Limit to under 12 words while maintaining clarity

This condensed version reduces word count by about 40% while maintaining all the essential guidance. It combines related concepts (academic precision with neutral tone) and streamlines the instructions without sacrificing the core requirements for creating appropriate titles.

---

### Human (11:49:17)

can you please provide that as a fenced markdown block?

---

### Assistant (11:49:23)


The user is asking me to provide the concise version of the Title Conventions section I just created, but in a fenced markdown block format. A fenced markdown block is created using triple backticks (```).

Here's the content I need to put in the fenced markdown block:

## Title Conventions
- **Format & Structure**: Use "[Tool Name]: [Primary Function] for [Application Domain]" pattern
- **Academic Tone**: Describe function precisely; avoid sensationalist terms ("revolutionary," "game-changing")
- **Technical Accuracy**: Employ discipline-specific terminology appropriate to the tool's field
- **Brevity**: Limit to under 12 words while maintaining clarity

I'll format this exactly as requested with the triple backticks.

```markdown
## Title Conventions
- **Format & Structure**: Use "[Tool Name]: [Primary Function] for [Application Domain]" pattern
- **Academic Tone**: Describe function precisely; avoid sensationalist terms ("revolutionary," "game-changing")
- **Technical Accuracy**: Employ discipline-specific terminology appropriate to the tool's field
- **Brevity**: Limit to under 12 words while maintaining clarity
```

---
