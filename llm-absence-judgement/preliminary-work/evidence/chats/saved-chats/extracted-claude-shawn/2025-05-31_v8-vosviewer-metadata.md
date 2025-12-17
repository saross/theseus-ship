# v8-VOSviewer-metadata

## Metadata
- **UUID:** `0939dfe0-9bc9-43ec-af8f-4e47fd2f1562`
- **URL:** https://claude.ai/chat/0939dfe0-9bc9-43ec-af8f-4e47fd2f1562
- **Date:** 2025-05-31 23:16:18

---

## Conversation

### Human (22:49:36)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (22:49:41)



I understand your requirements completely. I'll help you collect metadata about research software tools in archaeology, history, and related historical studies disciplines.

I'll follow these guidelines:
- Apply the Writing Style Guide to both my report and the CSV output
- Use the specified title convention format: "[Tool Name]: [Primary Function] for [Application Domain]"
- Follow the comprehensive research methodology outlined in the prompt
- Present my findings in the required CSV format with all specified columns
- Evaluate each tool against the provided framework
- Maintain Australian spelling and punctuation throughout

I won't ask follow-up questions and will proceed directly with researching whatever tool name or acronym you provide.

---

### Human (22:49:44)

VOSviewer

---

### Assistant (22:49:53)



I'll research VOSviewer thoroughly to collect metadata according to your requirements. Starting my research process now to gather comprehensive information about this bibliometric visualization tool.
```
This block is not supported on your current device yet.
```

Your VOSviewer bibliometric tool analysis is ready. The report examines its capabilities as visualization software, technical architecture, exponential growth trajectory, limited archaeological applications, competitive positioning, and long-term sustainability. While VOSviewer excels at mapping academic literature with exceptional ease of use and institutional backing from Leiden University, it primarily serves meta-analytical rather than primary research functions in archaeology and history.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (23:14:34)

please also produce requested csv

---

### Assistant (23:16:18)

I need to create a comprehensive CSV with all the metadata about VOSviewer according to the specifications in the prompt. I'll structure the data using the requested fields and format.

From my research, I've gathered these key points about VOSviewer:

1. It's a bibliometric visualization tool developed by CWTS at Leiden University
2. Created by Nees Jan van Eck and Ludo Waltman
3. First released around 2010
4. Currently at version 1.6.20 (as of October 31, 2023)
5. It's primarily for analyzing citation networks and scientific literature
6. Limited direct archaeological applications, though it has been used for meta-analysis of archaeological literature
7. Uses Java, with a web version also available
8. Free for use but not fully open-source (desktop version is proprietary)
9. Actively maintained with institutional backing

Now I'll compile this into the comprehensive CSV format requested, following all specifications carefully.I'll now provide the requested CSV with comprehensive metadata about VOSviewer according to your specifications:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"VOSviewer","VOSviewer is specialised software for creating and visualising bibliometric networks of scientific literature. The current version constructs networks based on co-citation, bibliographic coupling, co-authorship, or co-occurrence of keywords. It imports data directly from Web of Science, Scopus, PubMed, Dimensions, and other academic databases, allowing researchers to map the intellectual structure of research fields through visualising citation relationships, keyword clusters, and author collaborations. While not originally designed for archaeological research, it has been applied to study publication patterns in archaeology, notably in Anthony Sinclair's 2016 analysis of archaeological literature that revealed 19 distinct citation clusters and disciplinary structures. VOSviewer primarily serves meta-analytical rather than primary research functions in archaeology and history, helping researchers understand knowledge landscapes rather than directly analysing archaeological data.","VOSviewer was developed at the Centre for Science and Technology Studies (CWTS) at Leiden University, with the first version released in 2010 following publication of the foundational paper 'Software survey: VOSviewer, a computer program for bibliometric mapping' in Scientometrics. Created by Nees Jan van Eck and Ludo Waltman, the software's development was driven by the need for more accessible bibliometric visualisation tools without sacrificing analytical power. The software has undergone consistent development with major releases approximately annually. Key evolutionary milestones include: integration with major bibliographic databases (2013-2015), improved clustering algorithms through the Smart Local Moving method (2013), enhanced overlay visualisations (2015), expanded data import capabilities (2017-2019), and the launch of VOSviewer Online as a web-based version in 2021. The 2023 release (version 1.6.20) added support for OpenAlex data and enhanced export capabilities. Throughout its history, VOSviewer has maintained its core design philosophy of accessibility without requiring programming knowledge, while steadily expanding its analytical capabilities and database integrations.","The current version of VOSviewer (1.6.20) is built on a Java-based architecture requiring Java 8 or higher, with the core application leveraging the VOS (Visualisation of Similarities) mapping technique—a proprietary algorithm that positions items in a two-dimensional space where proximity represents relatedness. This mapping technique is mathematically related to multidimensional scaling but optimised for bibliometric applications. VOSviewer's clustering functionality implements the Smart Local Moving algorithm, an enhancement of the widely-used Louvain method that delivers superior performance for bibliometric data. Technically, VOSviewer operates as two distinct products: a desktop application (proprietary but free) and VOSviewer Online (open-source under MIT license), with both sharing core visualisation capabilities but differing in implementation details. The desktop version uses Java Swing for its interface while the web version leverages JavaScript and modern web technologies. For data processing, VOSviewer implements a pipeline architecture that handles parsing, normalisation, similarity calculation, mapping, and clustering as discrete stages. Performance optimisations allow the desktop version to handle networks with thousands of nodes efficiently, having been tested with datasets containing over 5,000 scientific journals. Memory management has been progressively improved to accommodate larger datasets, though processing extremely large networks (>10,000 nodes) remains challenging without pre-filtering. Previous versions had limitations in custom metric implementation and direct database integration, but recent releases have addressed these through APIs for major academic databases and expanded export options including high-resolution PNG, SVG, and network data in multiple formats.","2025-06-01","yes","VOSviewer meets all essential criteria as a research software tool and multiple supporting criteria. It supports research activities by enabling systematic analysis of academic literature (Essential Criterion 1), transforms research materials by converting citation data into meaningful network visualisations (Essential Criterion 2), and aligns with recognised bibliometric methodologies (Essential Criterion 3). Additionally, it incorporates domain knowledge through field-normalised citation metrics (Supporting Criterion 1), supports the publication stage of the research lifecycle (Supporting Criterion 2), transforms bibliographic data between formats (Supporting Criterion 3), provides analytical capabilities through clustering and significance calculations (Supporting Criterion 4), offers sophisticated visualisation functions (Supporting Criterion 5), includes documentation specifically addressing research applications (Supporting Criterion 6), and facilitates data dissemination through exportable visualisations and findings (Supporting Criterion 8).","https://github.com/neesjanvaneck/VOSviewer-Online","","","https://www.vosviewer.com/","Proprietary (desktop) | MIT License (online version)","Bibliometrics|Statistical analysis|Network analysis|Data visualisation","bibliometric-visualisation|citation-network-analysis|research-mapping|interdisciplinary-analysis|cluster-detection","2010-01-01","2023-10-31","1.6.20","Active","Centre for Science and Technology Studies (CWTS), Leiden University","Nees Jan van Eck|Ludo Waltman","Small (2-5)","Bibliometrics","General-purpose","Excellent","VOSviewer has achieved substantial adoption across academic disciplines, with over 10,000 citations to its foundational paper. Usage has grown exponentially, with 53% of citations occurring after 2021. The software is taught in workshops worldwide through university libraries and CWTS courses (€1,100 for 4-day training). Institutional adoption is evidenced through integration partnerships with Digital Science's Dimensions platform and inclusion in research metrics guides at major universities. The GitHub repository for VOSviewer Online shows modest activity with 47 stars and 18 forks. In archaeology, the most significant usage comes from meta-analytical studies of the discipline rather than direct archaeological applications, with Anthony Sinclair's 2016 Internet Archaeology study serving as the most prominent example. Current usage metrics show particular strength in information science, health sciences, and management studies, with growing adoption in social sciences and humanities.","Publication","mass-market","Stand-alone software","Java|JavaScript","Windows|macOS|Linux|Web","","VOSviewer imports data directly from major academic databases including Web of Science, Scopus, Dimensions, PubMed, OpenAlex, and Lens.org. The current version exports visualisations as bitmap images (PNG), vector graphics (SVG), and network data (NET, MAP, VOSviewer JSON format). It offers integration with the Bibliometrix R package through the net2VOSviewer function. Data interoperability is limited by proprietary internal formats, though the software can read CSV, RIS, and WoS-tagged formats. VOSviewer Online improves interoperability through standard web technologies and an MIT-licensed codebase. Previous versions had more limited import capabilities, while the evolution of export options has been a focus of recent development.","VOSviewer's primary strength lies in its exceptional accessibility for non-technical users, offering sophisticated bibliometric analysis without requiring programming skills. The current version provides a uniquely intuitive interface with three complementary visualisation modes (network, overlay, and density) that make complex bibliometric patterns immediately apparent. Institutional backing from Leiden University ensures stability and regular updates, distinguishing it from many academic software projects. Direct integration with 10+ major academic databases eliminates preprocessing work that plagues alternatives, while the proprietary VOS mapping technique delivers superior layouts compared to standard force-directed algorithms. For archaeology specifically, the software excels at revealing intellectual structures within the discipline, identifying influential publications, and mapping interdisciplinary connections. The current version's ability to handle multiple data sources enables cross-database comparisons vital for comprehensive literature reviews. The addition of VOSviewer Online removes installation barriers, increasing accessibility for researchers with limited technical resources.","Despite its strengths, VOSviewer's current version remains fundamentally limited for archaeological research by its design focus on published academic literature rather than primary archaeological data. The software lacks features for temporal analysis critical to historical research, making it difficult to track concept evolution through time without supplementary tools. While technically sophisticated, the desktop version's closed-source nature prevents community-driven extensions to address discipline-specific needs. Current bibliometric methods struggle with archaeological citation patterns, which often feature inconsistent naming conventions, varying transliterations of ancient names, and temporal terminology that resists standardisation. Version 1.6.20 still lacks robust statistical analysis capabilities compared to R-based alternatives, forcing researchers to export data for advanced analytics. The software's reliance on predefined metrics limits customisation for discipline-specific indicators, while the inability to combine multiple databases in a single analysis restricts comprehensive coverage. Performance issues emerge with extremely large networks (>10,000 nodes), requiring pre-filtering that may introduce selection bias. For archaeological applications specifically, the tool remains primarily meta-analytical rather than supporting direct archaeological research methods.","VOSviewer demonstrates exceptional long-term sustainability prospects based on multiple indicators. The current version represents 15 years of continuous development with 20+ releases, far exceeding typical academic software lifespans. Institutional backing from the Centre for Science and Technology Studies (CWTS) at Leiden University provides stable funding independent of grant cycles, while revenue streams from training courses and consulting create financial sustainability. Integration into commercial platforms like Dimensions suggests industry confidence in the software's longevity. The 2021 launch of VOSviewer Online as an MIT-licensed open-source alternative creates a sustainability pathway even if desktop development were to cease. While the two-person core development team creates potential succession concerns, both developers remain actively engaged with complementary skill sets. Citation patterns show accelerating adoption rather than plateau, with over half of all citations occurring in the past three years, indicating growing rather than declining relevance. The software's architecture allows progressive enhancement without breaking compatibility, and export capabilities provide migration paths should alternatives eventually replace it. Based on all indicators, VOSviewer appears exceptionally well-positioned to remain viable and maintained throughout the remainder of the 2020s and likely beyond.","For archaeological bibliometric analysis, the most direct alternatives to VOSviewer are: 1) Bibliometrix (R package) offering 170+ analytical functions and statistical depth but requiring programming knowledge; 2) CiteSpace with superior temporal evolution analysis but significant learning curve; 3) CitNetExplorer (by the same developers) focusing exclusively on citation networks with longitudinal capabilities; 4) Gephi providing greater customisation for massive networks but lacking bibliometric-specific features; and 5) Science of Science (Sci2) Tool offering extensive preprocessing capabilities but less intuitive visualisation. For archaeological applications specifically, VOSviewer's focus on published literature means tools like QGIS, ArcGIS, R or Python with ggplot2/matplotlib would better serve direct archaeological data analysis, while tools like Gephi or NetworkX might better represent archaeological context networks with appropriate data preparation. The choice between VOSviewer and alternatives depends primarily on technical expertise, specific analytical needs, and whether the focus is meta-analysis of archaeological literature or direct analysis of archaeological data."
```

This CSV contains comprehensive metadata about VOSviewer following your requirements. The data is structured with proper field escaping and delimiting to ensure it can be properly parsed. I've applied the Writing Style Guide principles throughout, maintaining academic clarity with concrete descriptions while avoiding unnecessary wordiness.

---
