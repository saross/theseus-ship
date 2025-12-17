# v8-PhotoModeler-metadata

## Metadata
- **UUID:** `d2c9ebb9-1de2-416f-83e5-9332cb7408e0`
- **URL:** https://claude.ai/chat/d2c9ebb9-1de2-416f-83e5-9332cb7408e0
- **Date:** 2025-05-29 07:21:49

---

## Conversation

### Human (07:12:52)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (07:13:00)



I understand your request. I'll use the detailed prompt to collect metadata about research software tools in archaeology and historical studies, following the Writing Style Guide principles and the specified title convention format: "[Tool Name]: [Primary Function] for [Application Domain]".

I'll organize my research according to the guidelines, ensuring thorough investigation of primary sources (repositories, documentation), secondary sources (academic literature), and tertiary sources (community discussions) until reaching information saturation.

For the CSV output, I'll follow the specified format with all required columns, using pipe separators for multiple values and ensuring proper escaping.

I'm ready to begin researching the first tool you provide.

---

### Human (07:13:16)

Photomodeller

---

### Assistant (07:13:26)



I'll research Photomodeller thoroughly to create a comprehensive metadata collection following the guidelines provided. I'm launching a detailed research process now to gather all the necessary information about this tool.
```
This block is not supported on your current device yet.
```

Your PhotoModeler software analysis is ready. It examines this 35-year-old photogrammetry tool's applications in archaeology, pricing ($995-$3,000), technical capabilities, and competition from Agisoft Metashape. The report details PhotoModeler's coded target precision advantages, Windows-only limitations, small development team risks, and why automated alternatives now dominate archaeological documentation despite PhotoModeler's professional-grade accuracy.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (07:19:38)

please also produce the requested csv

---

### Assistant (07:20:39)

I need to compile all the research information about PhotoModeler into the specified CSV format with all the required fields. Let me organize the data methodically:

### Essential Information
- **Tool**: PhotoModeler
- **Description**: A comprehensive overview focusing on what it does, especially for archaeology/historical uses
- **History**: Chronological development including major versions and updates
- **Technical-discussion**: Technical implementation details
- **Access-date**: Today's date (2025-05-29)
- **Tool-status**: Based on the evaluation framework, likely "yes" as it meets research criteria
- **Tool-status-reasoning**: Explanation of classification
- **DVCS-repo**: No public repository (proprietary software)
- **CRAN/PyPi**: Not applicable (not distributed through these channels)
- **Other-URL**: Main website URL
- **License**: Commercial/proprietary
- **Tags**: Relevant tags from the controlled list
- **AI-tags**: Five custom tags to characterize the tool

### Development and Organization
- **First-release-date**: January 1994
- **Last-update-date**: December 6, 2024 (most recent version 2025.0.0)
- **Current-version**: 2025.0.0
- **Development-status**: "Active"
- **Institutional-backing**: PhotoModeler Technologies (formerly Eos Systems Inc.)
- **Authors**: Alan Walford and team
- **Development-team-size**: "Small (2-5)"
- **Original-discipline**: Engineering/Computer Vision
- **Original-purpose**: "General-purpose" for measurement and 3D modeling
- **Documentation-quality**: "Excellent"
- **Usage-indicators**: Usage metrics paragraph

### Technical and Assessment
- **Lifecycle-stage**: Multiple stages (Data Acquisition, Processing, Analysis, etc.)
- **Type**: "research-specific"
- **Category**: "Stand-alone software"
- **Language**: Proprietary (likely C++ based on Windows application)
- **Platform**: Windows only
- **Open-Archaeo-Platform**: Not applicable (standalone software)
- **Interoperability**: File formats and exchange capabilities
- **Strengths**: Evidence-based advantages
- **Weaknesses**: Limitations and challenges
- **Survivability**: Long-term viability assessment
- **Alternatives**: Similar tools comparison

Let me now format this information according to the CSV structure specified, ensuring all fields are properly populated with the research findings.Here's the requested CSV metadata about PhotoModeler:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"PhotoModeler","PhotoModeler is a professional photogrammetry software that creates accurate 3D models and measurements from photographs. The software enables users to extract precise dimensional data from ordinary photographs by identifying common points across multiple images. The current version offers two main workflows: a manual approach where users mark corresponding points across images, and a more automated approach using SmartMatch technology and coded targets. In archaeology, PhotoModeler has been used for site documentation, artefact recording, excavation mapping, and architectural documentation of heritage structures. Archaeological applications include cave art documentation at Spain's Ekain Cave UNESCO site, Pompeii architectural recording, and creating accurate 3D models of artefacts for museum displays and research. While originally developed for engineering and industrial applications, PhotoModeler has maintained relevance in archaeological contexts where high precision measurements are required, though it has faced increasing competition from more automated alternatives.","PhotoModeler was developed by Alan Walford who founded Eos Systems Inc. (now PhotoModeler Technologies) in 1990. The software was first released as QMeasure in beta form in October 1993, with PhotoModeler 1.0 commercially launched in January 1994. Initially focused on desktop photogrammetry for non-specialists, the software has undergone continuous development for over 30 years. Major developments include: Version 3 (1998) which added surface modeling capabilities, Version 4 (2000) introducing automatic coded target detection, Version 5 (2004) with improved camera calibration, Version 6 (2008) adding SmartMatch automation, PhotoModeler Scanner (2009) introducing dense surface modeling, Version 2012 with improved SmartPoints, and subsequent annual releases. The company rebranded from Eos Systems to PhotoModeler Technologies around 2015. In 2020, the product line was simplified to two versions (Standard and Premium), and subscription options were introduced alongside perpetual licenses. The software has maintained consistent development with annual major releases and regular minor updates throughout its three-decade history.","PhotoModeler is a Windows-only 64-bit application developed with a proprietary codebase. The current version (2025.0.0) employs a combination of photogrammetric techniques including bundle adjustment for camera calibration and orientation, feature-based matching for automation, and dense multi-view stereo reconstruction for surface generation. The software utilizes a point-based modeling approach where corresponding points in multiple photographs are identified (either manually or automatically) to establish 3D coordinates through triangulation. PhotoModeler's coded target system provides sub-pixel measurement accuracy through specially designed printed targets with unique identifiers that can be automatically detected and matched. The software architecture includes separate modules for project management, photo handling, 3D modeling, measurement, and export. Processing is primarily CPU-based with some GPU acceleration for dense surface modeling in the Premium version. For extensibility, PhotoModeler provides comprehensive API access through Windows Dynamic Data Exchange (DDE), supporting integration with Visual Basic, C/C++, Java, Python and other languages. The software employs a modular licensing system that enables different capability sets based on the purchased version. Technical constraints include its Windows-only platform and hardware requirements that scale with project complexity. The Premium version's SmartMatch and Dense Surface Modeling features require more powerful systems for processing large datasets efficiently.","2025-05-29","yes","PhotoModeler qualifies as research software by meeting all essential criteria and multiple supporting criteria. It has a clear research-specific purpose in enabling measurement and documentation of archaeological sites and artifacts. It directly engages with research data by transforming photographs into measurable 3D models, supporting archaeological methodologies for documentation and analysis. Supporting criteria met include: domain knowledge integration through specialized measurement tools for archaeological contexts; research lifecycle support spanning data acquisition, processing, and analysis; data transformation capabilities converting photos to 3D models; analytical capabilities for measurement and comparison; visualization functions generating 3D models and orthophotos; documentation explicitly addressing archaeological applications; and data collection functionality specifically for field research.","","","","https://www.photomodeler.com","Commercial proprietary","3D modelling|Photogrammetry|Site mapping|Data collection|Data management","close-range photogrammetry|precision measurement|coded targets|archaeological documentation|heritage digitization","1994-01-01","2024-12-06","2025.0.0","Active","PhotoModeler Technologies (formerly Eos Systems Inc.)","Alan Walford and team","Small (2-5)","Engineering/Computer Vision","General-purpose","Excellent","PhotoModeler has documented use in archaeological contexts since 1996. Usage metrics include: continuous commercial availability for over 30 years; adoption across multiple industries including archaeology, engineering, forensics, and manufacturing; regular citation in academic literature, though less frequently than competitors like Agisoft Metashape in recent years; inclusion in educational programs for cultural heritage documentation, though not as widely as alternatives; and notable archaeological projects including UNESCO World Heritage site documentation. The software is used by universities, museums, archaeological consulting firms, and heritage organizations, though specific customer numbers are not publicly disclosed. Community engagement appears primarily through company-managed support channels rather than independent user communities. The trend over the past decade shows stable usage in specialized applications requiring high precision, but decreasing market share in general archaeological documentation as more automated alternatives have gained prominence.","Data Acquisition|Processing|Analysis|Visualization","research-specific","Stand-alone software","Proprietary (likely C++)","Windows","","PhotoModeler exports to numerous formats including DXF, OBJ, STL, FBX, and KML/KMZ, enabling integration with CAD systems, GIS platforms, and 3D visualization tools. Import capabilities include various image formats, LIDAR data (Premium version), and control point information from total stations and GPS systems. The current version supports direct georeferencing through GPS data embedded in photographs. File exchange is primarily through standard 3D formats rather than specialized APIs, though the software does offer scripting capabilities for workflow automation. While the software lacks direct web publishing capabilities, exported models can be converted for web display through third-party platforms. PhotoModeler maintains consistent backward compatibility with earlier file versions.","PhotoModeler offers several significant strengths that maintain its relevance despite competition from newer alternatives. The current version provides exceptional measurement accuracy through its coded target system, achieving sub-millimeter precision for close-range applications. The software offers unparalleled manual control over the modeling process, allowing specialists to verify and adjust each step of reconstruction for maximum reliability. PhotoModeler's extensive documentation and mature, stable codebase reflect 35 years of continuous development and refinement. The software provides reproducible workflows with comprehensive audit trails, supporting scientific rigor in archaeological documentation. Its hybrid approach combining automated features with manual verification options allows adaptation to varying project requirements and challenging photographic conditions. For archaeological applications specifically, PhotoModeler's support for external control points enables integration with traditional survey methods, maintaining continuity with established archaeological recording practices.","Despite its strengths, PhotoModeler faces several significant limitations in the current archaeological software landscape. The software's steep learning curve requires substantial time investment compared to more automated alternatives, presenting a barrier for projects with limited technical expertise. The Windows-only platform excludes macOS and Linux users, limiting adoption in mixed computing environments common in academic settings. PhotoModeler's relatively high cost (starting at $995 for Standard version, approximately $3,000 for Premium) exceeds most archaeological project budgets, especially compared to competitors like Agisoft Metashape ($179 standard/$59 educational). The manual workflow, while precise, requires significantly more processing time than fully automated alternatives, creating efficiency challenges for large-scale documentation projects. The current version's limited cloud processing capabilities and reliance on local computing resources restricts scalability for extensive site documentation. From a technical perspective, the proprietary closed-source nature prevents customization for specialized archaeological needs and raises concerns about long-term access and data preservation. These limitations have contributed to PhotoModeler's declining market share in archaeological applications despite its technical capabilities.","PhotoModeler demonstrates moderate to good long-term viability based on several factors. The software's 35-year continuous development history shows remarkable stability in the volatile software market. Regular annual releases with consistent feature improvements indicate ongoing commitment to product development. The established customer base across multiple industries provides diversified revenue streams beyond archaeology alone. However, several factors present sustainability concerns: the very small development team (2-5 people) limits capacity and creates key person dependencies, particularly on founder Alan Walford without clear succession planning. The company faces increasing competition from both commercial alternatives with larger development resources and improving open-source options. The Windows-only platform may become increasingly limiting as computing environments diversify. The higher price point and specialized nature restrict market growth potential compared to more accessible alternatives. While PhotoModeler likely remains viable for the near to medium term based on its established position and consistent development, its long-term prospects depend on addressing competition from more accessible alternatives and planning for eventual leadership transition. For archaeological users specifically, the software represents a moderate sustainability risk compared to more widely adopted alternatives with larger user communities.","The primary alternative to PhotoModeler in archaeological contexts is Agisoft Metashape (formerly PhotoScan), which has become the dominant photogrammetry solution in archaeology offering more automated processing at significantly lower cost ($179 standard/$59 educational). Metashape's workflow emphasis on automation rather than manual control makes it more accessible to non-specialists. Reality Capture provides the fastest processing speeds among commercial options and is now free for users earning under $1M annually (through Epic Games acquisition). Pix4D offers specialized solutions for drone mapping with subscription pricing ($38-360/month). Open-source alternatives include Meshroom (based on AliceVision) and COLMAP, which provide free solutions though with steeper technical requirements. Web-based services like Sketchfab and Polycam offer increasingly capable photogrammetry with minimal technical barriers. For specialized measurement applications similar to PhotoModeler's core strength, iWitnessPRO and PhotoModeler's own UAS version offer alternatives. Post-processing tools MeshLab (free) and CloudCompare (free) have become essential complements to any photogrammetry workflow. These alternatives typically employ automated feature detection rather than PhotoModeler's coded targets, trading some precision for significantly faster workflows and lower costs."
```

---
