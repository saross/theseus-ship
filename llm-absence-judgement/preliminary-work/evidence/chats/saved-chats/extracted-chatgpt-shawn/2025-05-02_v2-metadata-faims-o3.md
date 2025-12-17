# v2-Metadata-FAIMS-o3

## Metadata
- **Conversation ID:** `68150921-acb0-800c-9cf3-bed67f12b602`
- **Created:** 2025-05-02 20:04:17
- **Updated:** 2025-12-07 21:39:17
- **Default Model:** `o3`
- **Project ID:** `g-p-682fbda4eb1c819180b176f6de9d9cd8`
- **Source:** Official ChatGPT Export

---

## Conversation

### Human (20:04:13)

Hello - Today we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools.

# Ground rules

ABOVE ALL ELSE, if you are unsure about something, or do not have evidence supporting a claim, do not make a claim. If there is any doubt, there is no doubt.

This is research. SPEND EXTRA TIME above and beyond normal, to collect data carefully and methodically. We don't care about how long it takes, only that your research is accurate and epistemologically grounded. Care and attention to detail second only to the prior rule.

<definitions>

# Research Software Tool Definition

## Summary

Research software tools are specialized digital instruments developed to generate, process, and analyze results throughout the scientific research lifecycle, ranging from sophisticated packages with broad user bases to targeted scripts created by individual researchers. These tools embody encoded scientific knowledge and methodological approaches that transform raw data into research insights, making them fundamental yet often underrecognized contributors to scientific discovery. Unlike general-purpose software, research software tools integrate domain expertise, directly impact research reproducibility, and require ongoing maintenance to adapt to changing computational environments and evolving research questions.

I'd be happy to develop a comprehensive definition of a 'research software tool' based on the document you've shared and my knowledge of research software.

## Defining Research Software Tools

A research software tool is specialized software that enables, enhances, or accelerates the scientific research process by supporting one or more stages of scientific inquiry, from hypothesis generation to data collection, analysis, visualization, and publication of results.

### Core Characteristics

Based on the Hettrick report and broader understanding of the research software ecosystem, I would define research software tools by these essential characteristics:

1. **Research-Oriented Purpose**: Developed specifically to "generate, process and analyze results" in a research context, as noted in the report's definition section (3.1).

2. **Functional Spectrum**: Ranges from "highly developed packages with significant user bases to short (tens of lines of code) programs written by researchers for their own use."

3. **Knowledge Embodiment**: Represents encoded scientific knowledge and methodological approaches that enable specific kinds of research inquiries.

4. **Lifecycle Variability**: May exist at different development stages - from early prototype code developed by a single researcher to mature software maintained by dedicated teams and used across multiple disciplines.

5. **Value Chain Position**: Serves as critical infrastructure that sits between raw data and research insights, making it a fundamental but often invisible contributor to scientific discovery.

### Distinguishing Features

What separates research software tools from general software:

1. **Specialized Functionality**: Addresses specific scientific needs rather than general computing tasks.

2. **Domain Knowledge Integration**: Embeds disciplinary expertise and methodological approaches within its functionality.

3. **Evolving Requirements**: Often develops organically alongside research processes, with features added as research questions evolve.

4. **Reproducibility Role**: Directly impacts the reproducibility and reliability of research results, creating a direct link between software quality and research integrity.

5. **Development Context**: Often created in academic environments under different constraints and incentives than commercial software.

### Categories and Examples

Research software tools typically fall into these categories:

1. **Data Collection Tools**: Software for gathering, recording, or generating research data
   - Laboratory instrument control systems
   - Survey platforms
   - Simulation frameworks

2. **Analysis Tools**: Software that processes, transforms, or derives insights from research data
   - Statistical analysis packages
   - Computational modeling environments
   - Machine learning frameworks customized for research applications

3. **Visualization Tools**: Software for representing data or results visually
   - Scientific plotting libraries
   - Interactive data exploration environments
   - Specialized visualization software for particular data types

4. **Research Infrastructure Tools**: Software that supports the research process itself
   - Electronic lab notebooks
   - Research data management systems
   - Workflow management systems

### Sustainability Considerations

The definition of research software tools must acknowledge their sustainability challenges:

1. **Sustainability Requirements**: Requires ongoing effort to maintain functionality in changing computing environments, as the report notes that "a constant level of effort is required to maintain the software's operation."

2. **Dependency Management**: Exists within a complex "pyramid or stack" of dependencies that creates sustainability challenges as underlying software changes.

3. **Resource Constraints**: Often developed with limited resources and without explicit sustainability planning.

4. **Preservation Challenges**: Presents unique preservation difficulties compared to data, as software "must evolve and adapt to the constant changes in its environment" rather than remaining static.

This definition emphasizes that research software tools are not merely technical artifacts but essential components of the research infrastructure that embody scientific knowledge, enable discovery, and deserve recognition and investment proportional to their critical role in advancing research.

## Conclusion
In essence, a valid software tool for our purposes is one that not only **supports research in archaeology or historical sciences** but does so by actively working with data rather than merely serving as a generic data repository, collection of information, or static interface.

It is our belief that the tools we have given you meet this criteria, however, if there is an absence of evidence supporting our belief, it is REQUIRED that you inform us of any problems. IF YOU ARE UNSURE, INDICATE IT rather than giving an answer.

</definitions>

# Task

I will be giving you the name or acronym of an archaeology or historical studies-related software tool that dates somewhere from 1995 onwards. 

You must build a well-formed quoted CSV inside a fenced code block with the following columns:

## csv

"Tool", "Description", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", 'Platform", "License", "Type", "Lifecycle-stage", "Interoperability", "Strenghths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags"

### CSV column explanations

* Tool is our key column. It is essential to be consistent in tool name, following the input we give you. If there is an issue indicate it in notes.
* Description. Please generate a clear, detailed, and informative description of the tool. Several sentences would be appropriate - looking at the description, a user of the dataset should know exactly what the tool is and what it does. Mention any major releases or revisions to the software.
* Tool-status. Using the <definition> above, declare whether or not the tool is actually a 'research software tool'. Insert 'yes' or 'no'.
* Tool-status-reasoning. Explain your reasoning behind the decision in the previous field ('Tool-status'). Be thorough, detailed, and clear.
* DVCS-repo. The URL of a GitHub, GitLabs, or other DVCS repository (if available).
* CRAN. The URL of a CRAN project package (if available).
* PyPi. The URL of a PyPi package (if available).
* Other-URL. Single URL of a software tool's homepage or other important webpage related to the project (if available).
* Category. Select one value from the controlled list below, inserting only the name of the category (before the colon), not the definition.

<Category controlled list>

Packages and libraries: Sets of functions assembled with clear purpose, and made accessible using standards established by an underlying platform.
Stand-alone software: Software that may be operated without needing to first access an underlying platform.
Scripts: Sets of pragmatically assembled mutable functions, often lacking complete documentation or adherence to protocols that would otherwise facilitate secondary use outside their original contexts of creation.

</Category controlled list>

* Language. The programming language(s) in which the tool is written. If there is more than one, separate by pipes.
* Platform. Windows, Android, iOs, Linux, web, etc.
* Open-Archaeo-Platform. The underlying platform associated (only) with a 'Packages and libraries' category. These tools are ofetn plugins, extensions, or scripts associated with other software. If the tool in question is, please supply the appropriate underlying platform from the following controlled list.

<Open-archaeo-platform controlled list>

ArcGIS
AutoCAD
JavaScript
LibreOffice Calc
Lisp
Meshlab
Microsoft Excel
Nextflow
Open Data Kit
Piwigo
Python
QGIS
R
Stellarium

</Open-archaeo-platform controlled list>

* Licence. The licence under which the software is offered. If you find more than one, use the most recent.
* Lifecycle-stage". The (broad) stage in the research lifecycle that the tool is designed to facilitate. If the tool applies to multiple stages, separate them with pipes. Use the following contrlled list:

<lifecycle-stage controlled list>

Planning
Data Acquisition
Processing
Analysis
Interpretation
Publication
Preservation and Reuse

<lifecycle-stage controlled list>

* Type. Is the software 'mass-market' or 'research-specific'?
* Interoperability. A brief statement declaring other software tools that interoperate with the tool in question (if available). Also include import / export formats as applicable and available.
* Strenghts. A clear and informative statement about the strenghts of the software and research opportunities it opens up, in your view.
* Weaknesses. A clear and informative statement about the weaknesses and risks of the software, in your view.
* Survivability. An assessment, in your view, of the current viability and expected longevity of the software.
* Alternatives. A brief statement covering other software that might do the same or a very similar research task(s).
* Authors. A list of Authors separated by pipes (if available). List people not organisations or teams if possible, otherwise leave blank.
* Tags. Apply any of the following tags in the controlled list below that are appropriate, using only the name of the tag (before the colon) not the definition.

<Tags>

Statistical analysis: Identification and analysis of quantitative distribution patterns.
Spatial analysis: Identification and analysis of patterns relating to spatial distributions or relationships.
Viewshed analysis: Techniques for considering localized spatial perspectives of landscapes.
Site mapping: Techniques for illustrating archaeological sites.
Harrix matrix: Representation of archaeological sites as series of connected abstract entities.
Chronological modelling: Identification and analysis of patterns relating to the distribution of events or timespans.
Seriation: Technique for identifying chronological sequences based on the ordered properties of archaeological assemblages.
Zooarchaeology: Techniques used to identify and analyze faunal remains.
Palaeobotany: Techniques used to identify and analyze plant remains.
Artefact morphology: Identification and analysis of artefacts' physical dimensions and shape.
Literary analysis and epigraphy: Techniques for examining ancient texts.
Iconography: Techniques for examining ancient symbols.
Shape recognition: Techniques for automated classification of objects based on input representations of their physical shapes or morphological properties.
3D modelling: Creation and manipulation of computer-generated three-dimensional models.
Photogrammetry: Techniques for capturing and processing spatial information based on comparison of images taken from various perspectives.
Virtual reality: Simulating an environment in a 3D interactive virtual space.
Augmented reality: Creating a composite view comprising computer-generated images superimposed on real world environments.
Drones: Semi-automated machines used to capture data in environments that are unsuitable or unsafe for direct human presence.
Aerial and satellite imagery: Techniques for capturing images of the earth from aerial perspectives.
Luminescence dating: Absolute dating techniques that rely on measuring doses of ionizing radiation.
X-Ray Fluorescence: Technique for identifying the elemental composition of physical objects by bombarding samples with high-energy radiation.
Instrumental Neutron activation analysis: Technique for identifying the elemental composition of physical objects by bombarding samples with neutrons.
Radiocarbon dating, calibration and sequencing: Methods for determining and comparing the ages of objects using the properties of radiocarbon.
Geophysical survey: Systematic collection and analysis of geophysical signals, such as magnetic and gravitational fields emanating from the earth.
Data management: Tools used to organize and give structure to information.
Data collection: Tools used to facilitate the orderly data collection and input into digital data management systems.
Lithic analysis: Identification and analysis of stone tool artefacts.
API interfaces and web scrapers: Tools that facilitate retrieval of data from web resources.
Datasets: Series of records, collated in a consistent manner, motivated by a need, desire or warrant to render them comparable.
Diagrams and visualizations: Tools for summarizing and presenting in abtracted graphical form.
Platforms and publications: Venues that host, validate, review or contextualize published work.
Schemas and ontologies: A pattern of thought or behavior that organizes categories of information and the relationships among them.
Templates: Sample documents that already have some details in place.
Drivers and IO: Tools that facilitate the transmission of information across digital devices.
Educational resources and practical guides: Documents that convey instructions regarding how to achieve particular goals.
Public archaeology: The practice of presenting archaeological findings to the general public.
Public policy and civic action: The practice of creating or responding to principles that govern how archaeology should be done and its role in society.
Games: A structured form of play typically undertaken for entertainment or fun.
Writing: Communicating ideas through written language.
Lists: A set of items, not necessarily recorded with systematic intent.
LiDAR: A method for determining variable distance by targeting an object with a laser and measuring the time for the reflected light to return to the receiver.
Museums: Institutions responsible for curating, conserving or exhibiting collections of artefacts or other objects.
Bibliography: A list of scholarly work relevant to a particular topic.
Archaeogenetics: Analysis of degraded DNA from archaeological or anthropological sources, including skeletons of humans, domesticate animal or plants, artefacts, or cave sediments.
Bits and bobs: Tools that do not necessarily pertain to a specific archaeological activity, but which may be particularly useful in practical matters commonly faced by archaeologists.
Biological anthropology: Concerned with the biological and behavioral aspects of human beings, their extinct hominin ancestors, and related non-human primates.
Archaeoastronomy: Concerned with the investigation of the astronomical knowledge of prehistoric cultures.
Dendrochronology: Techniques for dating events and environmental change by using the characteristic patterns of annual growth rings in timber and tree trunks.
Photography: The practice of photographing archeological entities to create a lasting record of that work.
Cultural evolution: Concerned with evolutionary theory of social change.
Ethics and professional development: Concerned with the social, moral and ethical frameworks that archaeologists adhere to or are impacted by as they go about their work.
Simulation: Concerned with modelling archaeological processes in abstract terms.
Stable isotope analysis: The identification of isotopic signatures relative abundance of chemical elements within organic and inorganic compounds to understand the flow of energy through a food web and to reconstruct past environmental and climatic conditions.
Network analysis: Process of investigating social structures through the use of networks and graph theory.
Geoarchaeology: Application of geology and earth science methods.
Machine learning: 
Palaeoclimate modelling: 
Ceramic analysis: 

</Tags>

*AI-tags. Generate five tags about the research software tool in question, separated by pipes.

This research requires that you be thoughtful, systematic, and take your time. You will likely need to visit EVERY SINGLE PAGE of results for a given tool. If a piece of information is not available, omit it. Slow down and check your work. Accuracy and completeness (where possible) are the goals here.

If any information changes over time (e.g., licence, programming languages, interoperability, etc.), please *only use the most recent information*. In the description note major releases. Metadata should, wherever possible, pertain to the most recent version of the software (this is not an historical study).

To repeat back.

I'm going to give you a list of tools, one by one.
You will search for them.
You will then gather the objective metadata requested above when it is available, and produce the interpretive information requested as necessary. 
You will use the most recent information if any information has changed.

You MUST build a quoted, one-line CSV with the output in your direct response to the research process. Where a cell contains multiple values, separate them with pipes (|). 

Allowed sources: 
* Source code in published version control repos
* Scholarly literature 
* Blog posts and about pages
* Any other mentions of the tool in your training data or online

When you respond with data:
RESULTS: Build a markdown **fenced code block** of quoted CSV (header row plus one additional row), regardless of information source. Do not include any inline citations automatically generated by the deep research process (i.e., AI-generated or system-injected references i.e. 【deep research】 or &#8203;:contentReference[oaicite). 

Do you understand?

---

### Assistant (20:04:17) [Model: o3]

Yes, I understand the requirements and workflow. Please provide the first software tool name, and I will begin compiling the requested metadata.

---

### Human (20:04:23)

FAIMS

---

### Assistant (20:05:13) [Model: o3]

FAIMS (Field Acquired Information Management Systems) is an open-source Australian e-research infrastructure project begun in 2012 to give archaeologists and other field scientists a customisable, offline digital notebook for data capture. citeturn0search3turn0search5  
The current FAIMS3 suite—an Android app, a React-based notebook designer, and a Java “Conductor” server—resides in the FAIMS GitHub organisation and shows active commits through 2 May 2025 under an Apache-2.0 licence. citeturn1search0turn1search1  
Peer-reviewed papers and project pages describe FAIMS Mobile as flexible, open-source software promoting FAIR workflows across disciplines. citeturn0search9turn0search12  
Captured datasets export as JSON, CSV or SQLite and can be ingested automatically into repositories such as tDAR and Open Context for long-term preservation. citeturn0search7turn0search8  
An OSF update (2024) and ARDC funding statements indicate a healthy maintenance trajectory, though adoption remains limited to Android devices and users must deploy a server or cloud backend. citeturn0search11turn1search3  

```csv
"Tool","Description","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","Category","Language","Platform","Open-Archaeo-Platform","License","Type","Lifecycle-stage","Interoperability","Strenghths","Weaknesses","Survivability","Alternatives","Authors","Tags","AI-tags"
"FAIMS","Field Acquired Information Management System (FAIMS) is an open-source digital recording platform originally built in 2012 for archaeological fieldwork. The latest FAIMS3 release (2025) comprises an Android offline data-capture app, a web-based notebook designer, and a server (“Conductor”) for authentication and synchronisation. Users craft domain-specific electronic field notebooks that enforce controlled vocabularies and metadata standards, then synchronise datasets for downstream analysis or repository deposit. The codebase is maintained on GitHub under the Apache-2.0 licence and actively supported by Macquarie University and the Australian Research Data Commons.","yes","FAIMS directly supports data acquisition, processing, and preservation workflows in archaeological and historical research; it was purpose-built by academics, implements discipline-specific schemas, and is openly maintained, satisfying all core characteristics of a research software tool.","https://github.com/FAIMS/FAIMS3","","","https://faims.edu.au","Stand-alone software","TypeScript|Java|Python","Android|web","","Apache-2.0","research-specific","Data Acquisition|Processing|Preservation and Reuse","Exports JSON|CSV|SQLite; synchronises with tDAR|Open Context; REST API enables integration with R|Python pipelines","Offline mobile data capture, highly customisable electronic notebooks, open-source and FAIR-focused, active community support","Android-only mobile client, requires server setup and technical expertise for custom notebooks, limited automated analysis features","Active development with commits in 2025 and institutional backing; open licence indicates moderate-to-high longevity, contingent on continued funding","Open Data Kit|KoBoToolbox|Codifi|ESRI Survey123|Heurist","Shawn Ross|Brian Ballsun-Stanton|Adela Sobotkova|Christian Nassif-Haynes","Data management|Data collection","mobile-data-capture|archaeology-fieldwork|open-source|offline-notebooks|FAIR-data"
```

### Sources  
1. Project funding and start-date citeturn0search3  
2. Official FAIMS website overview citeturn0search1  
3. Detailed “About” page citeturn0search5  
4. GitHub FAIMS3 repository citeturn1search0  
5. GitHub organisation activity & licence snippet citeturn1search1  
6. Peer-reviewed description of FAIMS Mobile citeturn0search9  
7. ResearchGate preprint of same article citeturn0search12  
8. Integration with tDAR repository citeturn0search7  
9. Partner/project page noting Open Context links citeturn0search8  
10. OSF project update highlighting ongoing maintenance citeturn0search11

---
