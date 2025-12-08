# v8-archeoViz-metadata

## Metadata
- **UUID:** `bd5e93fc-9501-48b0-9345-01c4ed2b3572`
- **URL:** https://claude.ai/chat/bd5e93fc-9501-48b0-9345-01c4ed2b3572
- **Date:** 2025-05-05 21:14:12

---

## Conversation

### Human (20:37:42)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
A 'Writing Style Guide' is attached to this Project, please apply it to your report and the CSV. 
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
## Title **Format & Structure**: For the title (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" pattern for the name and title of your Report

---

### Assistant (20:37:49)



I understand your requirements completely. I'll follow the detailed guidelines in the prompt to collect metadata about research software tools used in archaeology, history, and other historical studies disciplines. I'll apply the Writing Style Guide to ensure consistency in the format and structure of both the report and CSV output.

When you provide a tool name or acronym, I'll conduct extensive research across repositories, documentation, academic literature, and community sources to compile comprehensive metadata according to the specifications.

I'll present my findings in the required CSV format with all the specified columns, following the controlled vocabulary lists and evaluation framework provided.

I'm ready to begin researching the first tool you'd like me to analyze.

---

### Human (20:37:55)

archeoViz

---

### Assistant (20:38:00)



I'll research archeoViz to create comprehensive metadata about this archaeological research software tool. Starting my research now!
```
This block is not supported on your current device yet.
```

Your archeoViz research report is ready. It covers this R Shiny application for archaeological visualization, including its purpose for creating interactive 3D/2D visualizations of archaeological spatial data, technical implementation details, development history, institutional support from CNRS, community adoption (66+ instances), and its decentralized approach to data sharing. The analysis includes strengths, limitations, alternative tools, and assessment of long-term viability.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (20:52:03)

please also generate the requested csv

---

### Assistant (20:52:59)



I understand you'd like me to provide the CSV data for the archeoViz tool according to the metadata collection requirements. Here's the completed CSV output:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"archeoViz","archeoViz is an R package and web application designed specifically for the visualisation, exploration, and online communication of archaeological spatial data. The current version provides interactive 3D and 2D visualisations of archaeological excavation data, with capabilities for displaying object coordinates, cross-sections, and refitting relationships. It enables archaeologists to create visualisations accessible through web browsers without requiring advanced technical skills. The tool supports multiple languages and follows a decentralised approach to archaeological data sharing, where researchers maintain control over their datasets while making them accessible to others.","archeoViz was developed by Sébastien Plutniak at the CITERES laboratory (CNRS/University of Tours). Initial development began before 2022, with version 1.0.0 being the first formal release, establishing core visualisation functionality. In 2023, version 1.3.3 was published in August, followed by formal publication in the Journal of Open Source Software in September, and the establishment of the archeoViz Portal as a companion application. Development continued in 2024 with version 1.3.4 released in January and the current version 1.3.5 released in June. In November 2024, the project received the Open Science Free Software Award from the French Committee for Open Science, and the first formal training workshop was held in Tours.","The current version of archeoViz is implemented as an R package using the Shiny framework to create web-based interfaces. The application leverages plotly for interactive 3D and 2D visualisations, which are generated from CSV files containing spatial coordinates and object attributes. The software architecture implements several spatial analysis methods, including convex hull computation (via the cxhull package), regression surfaces (using generalised additive models from mgcv), and 2D kernel density estimation (via the kde2d function from MASS). The application supports multilingual interfaces in seven languages through a translation system. For data handling, archeoViz implements a modular approach where data validation is performed during import, and can be accessed either locally or via web deployment. The system generates shareable URLs that encode visualisation parameters, ensuring reproducibility. Current technical implementation allows for export to SVG format, interactive HTML outputs, and connections to third-party applications. Performance can be resource-intensive with large datasets, particularly when visualising uncertainty (when using ranges of coordinates). The software generates R commands for all visualisations, enabling users to reproduce and customise them in standalone R environments.","2025-05-05","yes","archeoViz clearly qualifies as research software as it meets all essential criteria. It has a research-specific purpose, directly engaging with archaeological data to transform it into interactive visualisations that support academic inquiry. The tool aligns with established methodological approaches in spatial archaeology and digital humanities. Furthermore, it meets multiple supporting criteria: it incorporates domain-specific terminology and classifications for archaeological finds, supports multiple stages of the research lifecycle from processing to publication, transforms coordinate data into meaningful visualisations, performs analytical calculations including convex hull and kernel density estimation, creates sophisticated 2D and 3D visualisations of archaeological contexts, and its documentation explicitly addresses archaeological research applications.","https://github.com/sebastien-plutniak/archeoviz","https://cran.r-project.org/package=archeoViz","","https://analytics.huma-num.fr/archeoviz/en/","GNU Affero General Public License v3.0 (AGPL-3.0)","3D modelling|Spatial analysis|Visualization|Data management|Statistical analysis","archaeological visualization|spatial data|R shiny application|interactive 3D|reproducible research","2022","2024-06","1.3.5","Active","CNRS (French National Center for Scientific Research)|CITERES laboratory (UMR7324)|Huma-Num (Very Large Research Infrastructure)|MASA+ Consortium|European SEADDA COST Action","Sébastien Plutniak (primary developer), with contributions from Renata Araujo, Laura Coltofean, Sara Giardino, Julian Laabs, and Nicolas Delsol","Small (2-5)","Archaeology","General-purpose","Comprehensive","archeoViz has demonstrated significant adoption within the archaeological community, with approximately 66 documented instances deployed as of 2024. The tool received the Open Science Free Software Award from the French Committee for Open Science in November 2024. The GitHub repository shows modest but consistent engagement metrics. The software has been formally published in the Journal of Open Source Software, enhancing its academic credibility. User community engagement is evidenced through a dedicated forum, mailing list (archeoviz-maintainers@services.cnrs.fr), and training sessions organised through the MASA+ consortium. Based on citation patterns and documented implementations, adoption appears strongest in French and European archaeological research communities, with growing international interest facilitated by its multilingual interface.","Processing|Analysis|Publication|Preservation and Reuse","research-specific","Stand-alone software","R","Windows|macOS|Linux|Web-based","R","archeoViz uses CSV files with specific schema requirements for input data, requiring coordinates and object attributes in a prescribed format. The current version produces visualisations that can be exported as SVG images or interactive HTML. The software generates R commands for all visualisations, enabling reproducibility in standalone R environments. It integrates with complementary tools in the archaeological ecosystem, including archeofrag for refitting analysis. The decentralised approach through the archeoViz Portal facilitates connections between datasets while preserving researcher control. Multilingual support in 7 languages (English, French, German, Italian, Portuguese, Romanian, Spanish) enhances international interoperability.","The current version of archeoViz demonstrates several notable strengths: 1) Accessibility - it significantly lowers technical barriers by providing sophisticated visualisation capabilities without requiring GIS expertise; 2) Decentralisation - the portal approach allows researchers to maintain control of their data while facilitating sharing; 3) Reproducibility - URL parameters and R command generation ensure analyses can be precisely replicated; 4) Multilingualism - interfaces in 7 languages makes it accessible internationally; 5) Integration - fits within archaeological workflows as a complement to other analytical tools. The software effectively bridges the gap between complex spatial analysis tools and the needs of archaeological researchers who may lack advanced technical skills, while maintaining scientific rigour.","The current version of archeoViz has several limitations: 1) Analytical depth - it is explicitly 'not intended to replace more sophisticated analysis tools' like GIS or specialised statistical packages; 2) Performance constraints - visualisation of uncertainty and processing of large datasets can be resource-intensive; 3) Export functionality - some export capabilities are only available when using online instances; 4) Specialised focus - addresses a specific niche rather than providing comprehensive archaeological tools; 5) Technical dependencies - relies on the R ecosystem, requiring some familiarity with this environment. These limitations are largely by design, as the tool is positioned as complementary to more comprehensive analytical platforms rather than as a replacement.","archeoViz has positive long-term viability prospects based on several factors: 1) It has active development with regular updates, with the latest version released in 2024; 2) Strong institutional backing from CNRS and other research organisations provides stability; 3) Growing adoption with 66 instances created since launch indicates user acceptance; 4) Academic recognition through peer-reviewed publication and award recognition enhances credibility; 5) Integration with complementary tools creates a broader ecosystem. Potential sustainability concerns include the concentration of development expertise in a small team and reliance on the R/Shiny ecosystem. However, the open-source nature of the project, clear documentation, and institutional support framework suggest continued development and maintenance are likely in the medium term.","Several alternatives to archeoViz exist, each with different emphases: SEAHORS (Spatial Exploration of ArcHaeological Objects in R Shiny) is a similar R Shiny application that focuses on intra-site spatial analysis with a complementary relationship to archeoViz. archeofrag is specialised in refitting analysis and is integrated with archeoViz. Virtual Poeymaü provides a similar R Shiny application model for site-specific visualisation. For more comprehensive functionality, QGIS offers an open-source GIS platform with extensive capabilities but requires more technical expertise. ArcGIS provides a commercial enterprise platform with extensive archaeological tools but at high licensing costs. Arches is a web platform specifically designed for cultural heritage data management. archeoViz occupies a specific niche as a specialised visualisation and communication tool that complements rather than replaces these alternatives."
```

---
