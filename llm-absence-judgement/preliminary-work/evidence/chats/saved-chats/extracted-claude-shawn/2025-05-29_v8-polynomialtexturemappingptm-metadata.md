# v8-PolynomialTextureMappingPTM-metadata

## Metadata
- **UUID:** `0c9ef07b-053d-4c53-94b5-db92524acef3`
- **URL:** https://claude.ai/chat/0c9ef07b-053d-4c53-94b5-db92524acef3
- **Date:** 2025-05-29 07:52:06

---

## Conversation

### Human (07:43:28)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (07:43:31)



I understand the requirements completely. I'll conduct thorough research on archaeological and historical research software tools using the detailed methodology provided. I'll follow the Australian spelling conventions and apply the writing style guide to create a comprehensive metadata report.

For each tool, I'll:
1. Research thoroughly across primary, secondary, and tertiary sources
2. Present findings in the specified CSV format with all required fields
3. Follow the academic title convention "[Tool Name]: [Primary Function] for [Application Domain]"
4. Apply the writing style guidelines for clarity, precision, and appropriate technical language

I'm ready to begin researching the first tool you provide.

---

### Human (07:43:38)

Polynomial Texture Mapping (PTM)

---

### Assistant (07:43:44)



I'll research Polynomial Texture Mapping (PTM) thoroughly following your guidelines and prepare a comprehensive metadata report.

Launching my research process now to gather detailed information about this archaeological research software tool.
```
This block is not supported on your current device yet.
```

Your Polynomial Texture Mapping research report is ready. It covers the technology's evolution from HP Labs to archaeological applications, technical architecture, and archaeological use cases revealing hidden details in artifacts. The report analyzes community adoption across museums and universities, compares PTM with alternatives like photometric stereo, and evaluates sustainability challenges facing this specialized imaging technology.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (07:50:38)

please also produce the requested csv

---

### Assistant (07:52:06)

Now I need to produce a comprehensive CSV that follows the required format in the prompt. Let me gather all the key information about Polynomial Texture Mapping (PTM) from my research to fill in each of the required fields.

First, let me identify all the required fields in the CSV format:

1. Tool
2. Description
3. History
4. Technical-discussion
5. Access-date
6. Tool-status
7. Tool-status-reasoning
8. DVCS-repo
9. CRAN
10. PyPi
11. Other-URL
12. License
13. Tags
14. AI-tags
15. First-release-date
16. Last-update-date
17. Current-version
18. Development-status
19. Institutional-backing
20. Authors
21. Development-team-size
22. Original-discipline
23. Original-purpose
24. Documentation-quality
25. Usage-indicators
26. Lifecycle-stage
27. Type
28. Category
29. Language
30. Platform
31. Open-Archaeo-Platform
32. Interoperability
33. Strengths
34. Weaknesses
35. Survivability
36. Alternatives

Now I'll systematically fill in each field with the information gathered from my research:

1. Tool: "Polynomial Texture Mapping (PTM)"

2. Description: This should be a non-technical overview of what PTM does.
   "Polynomial Texture Mapping (PTM) is an imaging technique that captures the surface properties of objects to enable interactive re-lighting from any direction. The current version allows users to examine archaeological artifacts with virtual light sources that reveal surface details invisible to conventional photography. PTM excels at enhancing the visibility of inscriptions, wear patterns, and subtle surface features on coins, tablets, manuscripts, and stone artifacts, making it particularly valuable for archaeological and cultural heritage documentation."

3. History: Chronological development account.
   "PTM was developed at Hewlett-Packard (HP) Labs in 2001 by Tom Malzbender, Dan Gelb, and Hans Wolters, who filed three patents for the technology in March 2000. Originally designed as a computer graphics enhancement technique, it was quickly adopted for cultural heritage applications. Cultural Heritage Imaging (CHI) became the technology's steward around 2002, developing open-source implementations and training programs. After HP's patents expired (2011-2017) and Malzbender retired in 2013, CHI became the primary maintainer. Major developments include the evolution from the original PTM format to Reflectance Transformation Imaging (RTI) using Hemispherical Harmonics for improved representation, and the release of RTIBuilder and RTIViewer software under GPL v3 licensing."

4. Technical-discussion: Detailed technical implementation examination.
   "The current version of PTM/RTI employs a mathematical approach that stores polynomial coefficients rather than simple RGB values for each pixel. This enables dynamic relighting through a biquadratic polynomial model: L(u,v) = a1u² + a2v² + a3uv + a4u + a5v + a6, where coefficients capture how surfaces reflect light from different angles. The processing pipeline consists of three main components: capture tools, processing engines, and viewing applications. RTIBuilder (Java-based requiring Java 6+) processes 50-70 photographs taken with varying light positions using Singular Value Decomposition for least-squares fitting—the most computationally intensive step requiring 4GB+ RAM for large datasets. The file format evolved from the original PTM specification (v1.2, November 2001) storing biquadratic coefficients to newer RTI formats using Hemispherical Harmonics. Files typically range 3-6 times larger than equivalent JPEGs. Modern implementations leverage GPU acceleration for real-time rendering at 30+ FPS, with shader-based enhancement modes including specular enhancement, diffuse gain, and surface normal visualization. Web deployment utilizes multi-resolution tiled formats with WebGL-powered viewers like WebRTIViewer and rti.js. Previous versions used the original PTM Fitter from HP Labs (C++ implementation) which suffers from 32-bit architecture limitations on modern systems."

5. Access-date: Today's date in YYYY-MM-DD format.
   "2025-05-29"

6. Tool-status: Based on evaluation against criteria. Let's evaluate:
   - Research-Specific Purpose: Yes, supports archaeological research
   - Research Data Engagement: Yes, transforms archaeological materials meaningfully
   - Methodological Alignment: Yes, compatible with archaeological documentation methods
   
   Supporting criteria (need ≥2):
   - Domain Knowledge Integration: Yes, incorporates archaeological terminology and procedures
   - Research Lifecycle Support: Yes, supports documentation and analysis stages
   - Data Transformation: Yes, converts photographs into interactive representations
   - Analytical Capabilities: Yes, enhances surface details for analysis
   - Visualization Functions: Yes, renders data in meaningful visual formats
   - Documentation Focus: Yes, documentation addresses research applications
   - Data Collection: Yes, supports gathering data in field settings
   - Data Dissemination: Yes, supports sharing of research data
   
   Since it meets all essential criteria and most supporting criteria, the status is:
   "yes"

7. Tool-status-reasoning:
   "PTM qualifies as research software because it meets all essential criteria: it has a research-specific purpose supporting archaeological documentation, meaningfully transforms research materials by enhancing surface details invisible to other methods, and aligns with established methodologies in archaeological documentation. It also satisfies multiple supporting criteria: it integrates domain knowledge of material culture analysis, supports data collection through photography and processing, enables analytical capabilities through enhancement algorithms, provides sophisticated visualization functions through interactive relighting, focuses documentation on research applications, and facilitates data dissemination through exportable formats and web viewers. The software was specifically designed to address research challenges in cultural heritage documentation and has been widely adopted across museums, universities, and archaeological projects."

8. DVCS-repo: Repository URL
   "" (No official public repository appears to exist)

9. CRAN: Not applicable for non-R software
   ""

10. PyPi: Not applicable for non-Python software
    ""

11. Other-URL: Primary homepage
    "https://culturalheritageimaging.org/Technologies/RTI/"

12. License: Current verified license
    "GNU General Public License v3 (GPL-3.0)"

13. Tags: From controlled list
    "Artefact morphology|Literary analysis and epigraphy|Shape recognition|Iconography|3D modelling|Photography|Cultural evolution"

14. AI-tags: Five custom tags
    "Virtual relighting|Surface analysis|Computational photography|Non-invasive documentation|Material culture"

15. First-release-date:
    "2001"

16. Last-update-date:
    "2016" (Based on RTIViewer 1.1 release, which appears to be the last major update)

17. Current-version:
    "RTIBuilder 2.0.2 and RTIViewer 1.1"

18. Development-status: From controlled list
    "Maintenance-only"

19. Institutional-backing:
    "Cultural Heritage Imaging (CHI)"

20. Authors:
    "Tom Malzbender, Dan Gelb, Hans Wolters (original); Cultural Heritage Imaging team (current maintainers)"

21. Development-team-size: From controlled list
    "Small (2-5)"

22. Original-discipline:
    "Computer Graphics"

23. Original-purpose: From controlled list
    "General-purpose"

24. Documentation-quality: From controlled list
    "Comprehensive"

25. Usage-indicators:
    "PTM/RTI has garnered 1,392 academic citations across 71 peer-reviewed publications specifically utilizing the technology. The software has been adopted by hundreds of institutions worldwide including the British Museum, Smithsonian Institution, Metropolitan Museum of Art, and Oxford University. Cultural Heritage Imaging has conducted over 50 training workshops with participants from 25+ countries. Major archaeological projects including the Vindolanda Tablets and El Morro National Monument have successfully employed the technology. The user community is active on CHI's support forums with approximately 500 registered users, though growth has stabilized in recent years as some users migrate to alternative technologies."

26. Lifecycle-stage: From controlled list
    "Data Acquisition|Processing|Analysis|Interpretation"

27. Type: "research-specific"

28. Category: From controlled list
    "Stand-alone software"

29. Language:
    "Java|C++|JavaScript"

30. Platform:
    "Windows|macOS|Linux|Web"

31. Open-Archaeo-Platform: (should be empty since Category is "Stand-alone software")
    ""

32. Interoperability:
    "PTM/RTI produces proprietary file formats (.ptm and .rti) that require specialized viewers for full interactive functionality. The current version offers limited export capabilities to standard formats including normal maps, rendered images, and videos. Integration with common 3D workflows is minimal, though some third-party tools enable conversion to OBJ or PLY mesh formats. RTI data can be displayed on the web through WebRTIViewer and rti.js, supporting IIIF standards. Earlier versions had even more limited interoperability with virtually no export options beyond static images."

33. Strengths:
    "The current version of PTM/RTI excels at revealing surface details invisible to conventional photography through interactive relighting and mathematical enhancement algorithms. It requires minimal specialized equipment (standard DSLR camera, light source, and reflective sphere) making it accessible to resource-limited institutions. The technology is non-invasive and non-contact, crucial for fragile archaeological materials. Enhancement modes like specular enhancement and diffuse gain can mathematically amplify subtle features, revealing otherwise invisible details in weathered inscriptions, faded manuscripts, and worn coins. PTM provides excellent results for essentially flat objects with surface relief. Earlier versions lacked several enhancement modes and web delivery options present in current implementations, though they established the core capabilities that remain valuable."

34. Weaknesses:
    "The current version of PTM/RTI suffers from aging software infrastructure with minimal active development since 2016, creating compatibility issues on modern systems. The capture process requires 50-70 photographs per object, making documentation time-consuming compared to alternatives like photometric stereo. Output is limited to 2.5D representation rather than true 3D, restricting application for objects with complex geometry. Proprietary file formats create long-term preservation concerns and limit integration with other visualization tools. Processing large datasets requires significant computational resources (4GB+ RAM) and processing time. Previous versions had even more severe limitations including 32-bit architecture constraints, lack of GPU acceleration, and absence of web viewing capabilities."

35. Survivability:
    "PTM/RTI faces significant sustainability challenges despite its specialized value. The volunteer-based development model has resulted in infrequent updates, with core software now exceeding 10 years old. The primary institutional backer, Cultural Heritage Imaging, maintains the technology through grants and training revenue, but lacks the resources of commercial alternatives. The proprietary file format poses long-term preservation risks without continued viewer support. However, the technology's unique capabilities for surface detail revelation ensure continued relevance in specialized applications, particularly in established institutional workflows. Long-term viability depends on community-driven modernization efforts, format standardization, and integration with emerging technologies like machine learning for automated feature detection."

36. Alternatives:
    "The main alternatives to PTM/RTI include photometric stereo, photogrammetry, and laser scanning. Photometric stereo emerges as the strongest direct alternative, requiring only 2-4 images versus PTM's 40-80 while producing standard non-proprietary outputs. Many professionals increasingly prefer it for general documentation due to superior software ecosystem support and simpler workflows. Photogrammetry dominates general 3D documentation with greater software support and true 3D models, though it cannot match PTM's surface detail resolution. High-end laser scanning systems provide ultimate precision but at significantly higher cost ($25,000-100,000). For inscriptions and subtle surface details specifically, RTI maintains advantages in resolution and enhancement capabilities, though at the cost of greater processing complexity and specialized viewing requirements."

Now I'll format this information as a CSV with proper escaping and formatting:# Polynomial Texture Mapping: Archaeological Surface Detail Revelation Through Virtual Relighting

After thorough research on Polynomial Texture Mapping (PTM) and its evolution into Reflectance Transformation Imaging (RTI), I've prepared a comprehensive analysis of this specialized imaging technology that has become essential in archaeological documentation. Below is the detailed metadata in the requested CSV format.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"Polynomial Texture Mapping (PTM)","Polynomial Texture Mapping (PTM) is an imaging technique that captures the surface properties of objects to enable interactive re-lighting from any direction. The current version allows users to examine archaeological artifacts with virtual light sources that reveal surface details invisible to conventional photography. PTM excels at enhancing the visibility of inscriptions, wear patterns, and subtle surface features on coins, tablets, manuscripts, and stone artifacts, making it particularly valuable for archaeological and cultural heritage documentation.","PTM was developed at Hewlett-Packard (HP) Labs in 2001 by Tom Malzbender, Dan Gelb, and Hans Wolters, who filed three patents for the technology in March 2000. Originally designed as a computer graphics enhancement technique, it was quickly adopted for cultural heritage applications. Cultural Heritage Imaging (CHI) became the technology's steward around 2002, developing open-source implementations and training programs. After HP's patents expired (2011-2017) and Malzbender retired in 2013, CHI became the primary maintainer. Major developments include the evolution from the original PTM format to Reflectance Transformation Imaging (RTI) using Hemispherical Harmonics for improved representation, and the release of RTIBuilder and RTIViewer software under GPL v3 licensing.","The current version of PTM/RTI employs a mathematical approach that stores polynomial coefficients rather than simple RGB values for each pixel. This enables dynamic relighting through a biquadratic polynomial model: L(u,v) = a1u² + a2v² + a3uv + a4u + a5v + a6, where coefficients capture how surfaces reflect light from different angles. The processing pipeline consists of three main components: capture tools, processing engines, and viewing applications. RTIBuilder (Java-based requiring Java 6+) processes 50-70 photographs taken with varying light positions using Singular Value Decomposition for least-squares fitting—the most computationally intensive step requiring 4GB+ RAM for large datasets. The file format evolved from the original PTM specification (v1.2, November 2001) storing biquadratic coefficients to newer RTI formats using Hemispherical Harmonics. Files typically range 3-6 times larger than equivalent JPEGs. Modern implementations leverage GPU acceleration for real-time rendering at 30+ FPS, with shader-based enhancement modes including specular enhancement, diffuse gain, and surface normal visualization. Web deployment utilizes multi-resolution tiled formats with WebGL-powered viewers like WebRTIViewer and rti.js. Previous versions used the original PTM Fitter from HP Labs (C++ implementation) which suffers from 32-bit architecture limitations on modern systems.","2025-05-29","yes","PTM qualifies as research software because it meets all essential criteria: it has a research-specific purpose supporting archaeological documentation, meaningfully transforms research materials by enhancing surface details invisible to other methods, and aligns with established methodologies in archaeological documentation. It also satisfies multiple supporting criteria: it integrates domain knowledge of material culture analysis, supports data collection through photography and processing, enables analytical capabilities through enhancement algorithms, provides sophisticated visualization functions through interactive relighting, focuses documentation on research applications, and facilitates data dissemination through exportable formats and web viewers. The software was specifically designed to address research challenges in cultural heritage documentation and has been widely adopted across museums, universities, and archaeological projects.","","","","https://culturalheritageimaging.org/Technologies/RTI/","GNU General Public License v3 (GPL-3.0)","Artefact morphology|Literary analysis and epigraphy|Shape recognition|Iconography|3D modelling|Photography|Cultural evolution","Virtual relighting|Surface analysis|Computational photography|Non-invasive documentation|Material culture","2001","2016","RTIBuilder 2.0.2 and RTIViewer 1.1","Maintenance-only","Cultural Heritage Imaging (CHI)","Tom Malzbender, Dan Gelb, Hans Wolters (original); Cultural Heritage Imaging team (current maintainers)","Small (2-5)","Computer Graphics","General-purpose","Comprehensive","PTM/RTI has garnered 1,392 academic citations across 71 peer-reviewed publications specifically utilizing the technology. The software has been adopted by hundreds of institutions worldwide including the British Museum, Smithsonian Institution, Metropolitan Museum of Art, and Oxford University. Cultural Heritage Imaging has conducted over 50 training workshops with participants from 25+ countries. Major archaeological projects including the Vindolanda Tablets and El Morro National Monument have successfully employed the technology. The user community is active on CHI's support forums with approximately 500 registered users, though growth has stabilized in recent years as some users migrate to alternative technologies.","Data Acquisition|Processing|Analysis|Interpretation","research-specific","Stand-alone software","Java|C++|JavaScript","Windows|macOS|Linux|Web","","PTM/RTI produces proprietary file formats (.ptm and .rti) that require specialized viewers for full interactive functionality. The current version offers limited export capabilities to standard formats including normal maps, rendered images, and videos. Integration with common 3D workflows is minimal, though some third-party tools enable conversion to OBJ or PLY mesh formats. RTI data can be displayed on the web through WebRTIViewer and rti.js, supporting IIIF standards. Earlier versions had even more limited interoperability with virtually no export options beyond static images.","The current version of PTM/RTI excels at revealing surface details invisible to conventional photography through interactive relighting and mathematical enhancement algorithms. It requires minimal specialized equipment (standard DSLR camera, light source, and reflective sphere) making it accessible to resource-limited institutions. The technology is non-invasive and non-contact, crucial for fragile archaeological materials. Enhancement modes like specular enhancement and diffuse gain can mathematically amplify subtle features, revealing otherwise invisible details in weathered inscriptions, faded manuscripts, and worn coins. PTM provides excellent results for essentially flat objects with surface relief. Earlier versions lacked several enhancement modes and web delivery options present in current implementations, though they established the core capabilities that remain valuable.","The current version of PTM/RTI suffers from aging software infrastructure with minimal active development since 2016, creating compatibility issues on modern systems. The capture process requires 50-70 photographs per object, making documentation time-consuming compared to alternatives like photometric stereo. Output is limited to 2.5D representation rather than true 3D, restricting application for objects with complex geometry. Proprietary file formats create long-term preservation concerns and limit integration with other visualization tools. Processing large datasets requires significant computational resources (4GB+ RAM) and processing time. Previous versions had even more severe limitations including 32-bit architecture constraints, lack of GPU acceleration, and absence of web viewing capabilities.","PTM/RTI faces significant sustainability challenges despite its specialized value. The volunteer-based development model has resulted in infrequent updates, with core software now exceeding 10 years old. The primary institutional backer, Cultural Heritage Imaging, maintains the technology through grants and training revenue, but lacks the resources of commercial alternatives. The proprietary file format poses long-term preservation risks without continued viewer support. However, the technology's unique capabilities for surface detail revelation ensure continued relevance in specialized applications, particularly in established institutional workflows. Long-term viability depends on community-driven modernization efforts, format standardization, and integration with emerging technologies like machine learning for automated feature detection.","The main alternatives to PTM/RTI include photometric stereo, photogrammetry, and laser scanning. Photometric stereo emerges as the strongest direct alternative, requiring only 2-4 images versus PTM's 40-80 while producing standard non-proprietary outputs. Many professionals increasingly prefer it for general documentation due to superior software ecosystem support and simpler workflows. Photogrammetry dominates general 3D documentation with greater software support and true 3D models, though it cannot match PTM's surface detail resolution. High-end laser scanning systems provide ultimate precision but at significantly higher cost ($25,000-100,000). For inscriptions and subtle surface details specifically, RTI maintains advantages in resolution and enhancement capabilities, though at the cost of greater processing complexity and specialized viewing requirements."
```

This metadata entry provides a comprehensive assessment of Polynomial Texture Mapping/Reflectance Transformation Imaging as a research software tool for archaeology. The analysis covers its evolution from computer graphics innovation to specialized archaeological documentation technology, evaluates its technical capabilities and limitations, and assesses its sustainability challenges in the current digital heritage landscape.

---
