# v8-SASSA-metadata

## Metadata
- **UUID:** `233f429a-4b06-4e3f-b8a4-62beb887fa53`
- **URL:** https://claude.ai/chat/233f429a-4b06-4e3f-b8a4-62beb887fa53
- **Date:** 2025-05-31 00:29:26

---

## Conversation

### Human (23:56:37)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (23:56:56)



I understand your request completely. I'll use the detailed instructions to research and assemble metadata about specific software tools for archaeology, history, and other historical studies disciplines. I'll apply the Writing Style Guide to ensure academic clarity, appropriate tone, and consistent formatting throughout.

For the report title, I'll follow the convention: "[Tool Name]: [Primary Function] for [Application Domain]"

I won't ask follow-up questions and will execute the prompt directly when you provide the name or acronym of the first tool. If I encounter any ambiguity about which specific tool you're referring to, I'll consult the 'Tool disambiguation' section and prioritize the software most relevant to archaeological/historical research.

I'm ready to begin when you provide the first tool name.

---

### Human (23:57:06)

SASSA

---

### Assistant (23:57:14)



Let me research SASSA to provide you with comprehensive metadata about this research software tool.

I'll launch a detailed research process to gather all the necessary information about SASSA in archaeology and historical studies.
```
This block is not supported on your current device yet.
```

Your archaeological soil analysis system research is ready. It examines SASSA, a 2005-2007 web-based tool from University of Stirling that helped archaeologists interpret soil findings. The report covers its MediaWiki and XML architecture, soil interpretation capabilities, limited user engagement, current abandoned status, and comparison with modern alternatives like QGIS and ArcGIS Survey123.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (00:25:14)

please also produce the requested csv

---

### Assistant (00:26:22)

I'll now produce the CSV output that contains all the necessary metadata about SASSA according to the requirements in the prompt. I'll ensure it follows the required format with header row and properly escaped data, using the information from my research.

The CSV should include these columns:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "License", "Tags", "AI-tags", "First-release-date", "Last-update-date", "Current-version", "Development-status", "Institutional-backing", "Authors", "Development-team-size", "Original-discipline", "Original-purpose", "Documentation-quality", "Usage-indicators", "Lifecycle-stage", "Type", "Category", "Language", "Platform", "Open-Archaeo-Platform", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives"

Let me prepare the data for each field based on my research:

Tool: "SASSA"

Description: A summary of what SASSA does, focused on its purpose as a Soil Analysis Support System for Archaeologists.

History: Chronological development from 2005-2007 and any subsequent updates.

Technical-discussion: Details on the MediaWiki and XML implementation, LAMP stack, etc.

Access-date: Today's date in YYYY-MM-DD format.

Tool-status: Based on my evaluation, this would be "yes" as it meets the essential criteria for research software.

Tool-status-reasoning: Explanation of how SASSA meets the criteria.

DVCS-repo: There doesn't appear to be a public repository, so this would be empty.

CRAN/PyPi: Empty as SASSA is not a package for these platforms.

Other-URL: The original URL would be "https://www.sassa.org.uk" though it appears to be no longer maintained.

License: Based on the research, this would likely be an open license, but specific details may not be available.

Tags: Appropriate tags from the controlled list.

AI-tags: Five generated tags to characterize the tool.

First-release-date/Last-update-date: Based on the research timeline.

Current-version: The final version released, if known.

Development-status: "Abandoned" based on research showing no updates since around 2009.

Institutional-backing: University of Stirling and NERC funding.

Authors: The primary developers/researchers.

Development-team-size: Based on the research, likely "Small (2-5)".

Original-discipline: "Archaeology" or "Geoarchaeology".

Original-purpose: "Project-specific" for archaeological soil analysis.

Documentation-quality: Based on the detailed publications, likely "Comprehensive".

Usage-indicators: Summary of the limited usage statistics available.

Lifecycle-stage: Relevant stages from the controlled list.

Type: "research-specific" as it was developed specifically for archaeological research.

Category: "Stand-alone software" as it was a web-based system.

Language: Programming languages used in development.

Platform: Web-based, with support for various devices.

Open-Archaeo-Platform: Empty as it's not a package/library.

Interoperability: Information on data formats and exchange capabilities.

Strengths: Assessment of advantages including academic rigor, etc.

Weaknesses: Assessment of limitations including lack of maintenance.

Survivability: Assessment of long-term viability (poor in this case).

Alternatives: Modern alternatives like QGIS, ArcGIS Survey123, etc.

Now I'll compile all this into the properly formatted CSV.I'll now generate the complete CSV for SASSA according to your requirements:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"SASSA","SASSA (Soil Analysis Support System for Archaeologists) is a web-based knowledge management and decision support tool developed to assist field archaeologists in describing, interpreting and understanding archaeological soils and sediments. The system provides a comprehensive knowledge base of geoarchaeological terminology and concepts alongside a structured field tool that guides users through standardised soil description and analytical interpretation processes. SASSA was designed to bridge the knowledge gap between soil science and archaeology, enabling practitioners with limited soil science training to make more informed interpretations of archaeological contexts. The system comprises two main components: a MediaWiki-powered knowledge repository containing definitions, tutorials, and analytical method descriptions; and an XML-based field recording tool that implements decision trees to guide soil assessment and interpretation in field conditions.","SASSA was developed between 2005-2007 at the University of Stirling as part of a Natural Environment Research Council (NERC) funded knowledge transfer initiative. The project emerged from research indicating that many field archaeologists lacked confidence in describing and interpreting soils despite their importance to archaeological contexts. Development involved extensive consultation with both academic experts and commercial archaeological units to ensure practical relevance. The system was formally launched in 2007 with publication in Internet Archaeology (Issue 25) in 2008 detailing its development and implementation. Initial usage statistics from 2007 showed moderate adoption, with several thousand page views recorded for key sections. However, the development team reported challenges in fostering an active community of contributors to the wiki component. There is little evidence of substantial updates or maintenance after 2009, suggesting the project did not transition successfully from initial grant funding to sustained community support or institutional maintenance.","The current version of SASSA employs a two-tier architecture combining a MediaWiki knowledge base with an XML-based field tool. The system runs on a standard LAMP (Linux, Apache, MySQL, PHP) platform with MediaWiki providing the content management framework. The field tool component utilises XML data structures and decision trees to guide users through soil analysis workflows. This architecture supports both online operation and offline functionality when internet access is unavailable in field conditions. The technical implementation was sophisticated for its 2007 release, featuring XHTML forms for data entry, PDF generation capabilities for report creation, and mobile-optimised interfaces for field use on devices ranging from desktop PCs to PDAs and early smartphones. User authentication requires separate registration for the wiki and field tool components, with post-registration validation to ensure content quality. The MediaWiki implementation uses customised namespaces to organise content into categories including Tutorials, Field Recording, Analytical Methods, and Case Studies. The XML decision tree structure of the field tool enables complex conditional navigation through soil description protocols, with each decision point linked to relevant knowledge base entries. This modular design allows the field tool to operate independently when necessary while integrating with the wiki knowledge base when connectivity permits. The system does not appear to implement formal version control or automated testing procedures, which may have contributed to maintenance challenges as web technologies evolved beyond the 2007-2009 period.","2025-05-31","yes","SASSA clearly meets all three essential criteria for research software. It has a research-specific purpose, explicitly designed to support archaeological field investigations through systematic soil analysis. It directly engages with research data by transforming field observations of soils into structured interpretations with archaeological significance. The system aligns with established methodological approaches in geoarchaeology, implementing standardised soil description protocols and analytical frameworks. Additionally, SASSA satisfies multiple supporting criteria: it integrates domain knowledge through its comprehensive terminology database and geoarchaeological concepts; it supports multiple research lifecycle stages including data collection, analysis, and interpretation; it enables data transformation by converting field observations into standardised formats and interpretations; it provides analytical capabilities through its decision tree systems for soil interpretation; and its documentation explicitly addresses archaeological research applications with case studies demonstrating implementation in field contexts.","","","","https://www.sassa.org.uk","Unknown","Geophysical survey|Data collection|Data management|Geoarchaeology","soil science|archaeological recording|knowledge base|decision support|field tool","2007","2009","Unknown","Abandoned","University of Stirling|Natural Environment Research Council (NERC)","Clare Wilson|Donald Davidson|David Cairns","Small (2-5)","Archaeology","Project-specific","Comprehensive","Usage metrics for SASSA were modest but notable for its period. By June 2007, key pages had received several thousand views, with the soil forming processes page recording 6,568 views. However, the development team reported challenges in fostering active contribution, noting that despite registration requirements, few users actively contributed content to the wiki component. The project published extensively in academic literature, including a major article in Internet Archaeology (Issue 25) and several conference papers. The system appears to have been primarily adopted within UK archaeology, with limited evidence of international uptake. No recent citation metrics or usage statistics are available, suggesting minimal contemporary usage. There is no evidence of an active user community or ongoing development activity since approximately 2009.","Data Acquisition|Processing|Analysis|Interpretation","research-specific","Stand-alone software","PHP|XML|JavaScript","Web-based|Windows|Linux|Mac OS|Mobile (limited)","","SASSA used a proprietary data format for storing field observations through its XML-based recording system. The field tool could export data in PDF format for reporting purposes, but there is no evidence of integration with common archaeological database systems or GIS platforms. The wiki component used standard MediaWiki formatting for knowledge content. Earlier versions appear to have had the same limited interoperability features as the final version, with no indication of enhanced data exchange capabilities being implemented during the project lifecycle. The system's closed data ecosystem likely contributed to its limited adoption compared to more interoperable modern alternatives.","SASSA exhibited several significant strengths. The system was developed with strong academic rigor, involving extensive consultation with both academic experts and commercial archaeological units to ensure relevance and accuracy. Its knowledge base provided comprehensive, standardised terminology and concepts specifically tailored to archaeological soil interpretation, addressing a genuine knowledge gap in field archaeology. The decision tree approach offered structured guidance for non-specialists, enabling more consistent field recording and interpretation. The dual architecture supporting both connected and disconnected operation showed foresight about field conditions. SASSA's transparent development process and peer-reviewed documentation demonstrated exemplary scientific communication. The integration of tutorials with practical tools created an effective learning environment for archaeological soil science. Finally, the project pioneered digital knowledge transfer in archaeological soil science when most field recording remained paper-based, demonstrating innovation in applying web technologies to archaeological fieldwork.","SASSA suffered from several critical weaknesses that limited its long-term viability. The system lacked open source code release, preventing community maintenance or adaptation as technologies evolved. Its reliance on MediaWiki created unnecessary maintenance overhead without leveraging broader wiki communities. The project demonstrated poor sustainability planning, failing to transition from grant funding to ongoing support. User engagement remained passive rather than collaborative, with few contributors despite registration systems. The field tool's XML architecture proved inflexible compared to modern data collection frameworks. SASSA's web-centric approach predated effective mobile solutions, limiting field usability as smartphone technologies advanced. Integration with GIS and other archaeological software was minimal, creating workflow isolation. The system lacked version control and update mechanisms for field components. Finally, the specialized focus on soils without integration into broader archaeological recording systems limited its practical utility in commercial archaeology settings where efficiency demands unified recording systems.","SASSA demonstrates poor long-term survivability despite initial success. The project failed to transition from grant-funded development to sustainable maintenance, with no evidence of updates beyond 2009. Several critical factors contributed to this outcome: the absence of an open source code release prevented community-driven development; no clear versioning system or update mechanism existed; the project lacked transition planning from academic funding to either commercial or community support; and its specialized MediaWiki implementation created maintenance overhead without leveraging broader wiki development communities. The system's architecture became increasingly outdated as mobile technologies advanced rapidly after 2007-2009. Without institutional commitment to long-term hosting and technical updates, the web-based system became vulnerable to security issues and browser compatibility problems. The specialized nature of archaeological soil analysis also meant a relatively small potential user base, insufficient to sustain volunteer development. The project stands as an instructive example of how even well-designed research software can become unsustainable without explicit planning for long-term maintenance beyond initial funding periods.","Modern alternatives to SASSA offer significantly improved functionality and sustainability. QGIS with QField provides comprehensive GIS integration with offline field data collection capability and strong open-source community support. ArcGIS Survey123 delivers form-based field recording with enterprise-level integration and regular commercial updates. Open Data Kit (ODK) and its archaeological implementations offer flexible form creation with robust mobile support. Codifi's archaeological recording systems provide tailored solutions with professional maintenance. Field-specific tools like Intrasis combine GIS capabilities with archaeological recording frameworks. These alternatives address SASSA's limitations through active development communities, regular updates, mobile-first design, and cloud synchronization. They support high-precision GNSS integration, multimedia documentation, and standardized data exchange formats. Most importantly, they benefit from sustainable funding models through either commercial licensing, institutional commitment, or vibrant open-source communities. For specifically soil-focused analysis, modern archaeological applications typically integrate with laboratory information management systems and analytical databases rather than providing standalone soil interpretation tools."
```

---
