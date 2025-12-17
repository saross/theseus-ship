# v8-KLRfome-metadata

## Metadata
- **UUID:** `3da3e93e-3658-478b-9c93-67774357e8e7`
- **URL:** https://claude.ai/chat/3da3e93e-3658-478b-9c93-67774357e8e7
- **Date:** 2025-05-09 17:34:22

---

## Conversation

### Human (18:56:26)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (18:56:31)



I understand the task completely. I'll be collecting metadata about research software tools used in archaeology, history, and related disciplines following the comprehensive guidelines provided. I'll apply the Writing Style Guide to ensure consistent, academic styling with appropriate formatting throughout.

For each tool you name, I'll conduct thorough research and provide a complete metadata entry in CSV format as specified, following the title convention: "[Tool Name]: [Primary Function] for [Application Domain]".

I'm ready to begin with the first tool or acronym whenever you're ready to provide it.

---

### Human (18:56:43)

KLRfome

---

### Assistant (18:56:56)



I'll research KLRfome as a potential archaeological research software tool and collect all the required metadata following your guidelines. Let me conduct some comprehensive research on this tool.
```
This block is not supported on your current device yet.
```

Your archaeological site predictor analysis is ready. It covers KLRfome's innovative approach to treating archaeological sites as distributions rather than points, its technical features, development history, and mathematical foundations. The report evaluates its strengths (statistical sophistication, open-source nature) and limitations (limited adoption, technical barriers), compares it with alternatives like GRASS GIS and ArcGIS, and assesses its long-term prospects in archaeological predictive modeling.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (19:07:18)

please also generate the requested csv

---

### Assistant (19:07:54)



Based on my research, I'll now generate the comprehensive CSV for KLRfome as requested, following the format specified in your guidelines.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"KLRfome","KLRfome (Kernel Logistic Regression on Focal Mean Embeddings) is an R package that addresses a fundamental issue in archaeological site prediction—treating archaeological sites as distributions of environmental features rather than as single points or centroids. Unlike traditional predictive models that collapse multiple measurements within a site to single values, KLRfome preserves the complex environmental relationships by modelling the distribution of measurements from within sites. It applies machine learning techniques to create predictive maps that forecast where undiscovered archaeological sites might be located based on landscape characteristics. The package implements a workflow where environmental variables are processed through kernel functions to generate similarity matrices, which then feed into a kernel logistic regression model to predict site presence probability.","KLRfome was developed by Matthew D. Harris, a researcher affiliated with the University of Pennsylvania. The development timeline includes: initial release on Zenodo in 2017, followed by presentation at Society for American Archaeology meetings in 2018-2019, and formal publication in the Journal of Open Source Software in 2019. The tool builds upon prior work by Zoltán Szabó on mean embeddings and Ji Zhu & Trevor Hastie's kernel logistic regression algorithm. Harris has acknowledged Szabó's correspondence as instrumental during the development process. The package was conceived to address methodological limitations in traditional archaeological predictive modelling, specifically the problem that archaeological sites are not points but rather distributions of environmental features across landforms.","The current version of KLRfome implements Distribution Regression using kernel methods to map distributions of environmental features to binary outcomes (site presence/absence). The technical approach involves several key components: 1) It uses Kernel Logistic Regression, specifically applying it to distribution data via the mean embedding of features. 2) The mean embedding represents a distribution of data points as a single point in a Reproducing Kernel Hilbert Space. 3) The software creates similarity matrices between distributions using the build_K function, which computes kernel similarities between all site and background areas. 4) It fits parameters using an Iterative Re-weighted Least Squares approach implemented in the KLR function. 5) Prediction is performed on new locations using focal windows of varying sizes through a roving prediction approach. This methodology preserves the spatial relationships that are lost when reducing sites to centroids or points. The package includes parallel/multi-core prediction support for processing larger datasets, which is particularly valuable when working with high-resolution environmental raster data. Technically, the package depends on several R libraries including ggplot2, NLMR, rasterVis, pROC, dplyr, and sp. The focal window prediction approach allows archaeologists to consider varying scales of environmental influence on site location, addressing a key issue in predictive modelling where the appropriate scale of analysis is often unclear. For previous versions, the initial implementation focused on the core kernel logistic regression algorithm, with later versions adding the mean embedding approach and then the focal window prediction capabilities.","2025-05-08","yes","KLRfome meets all three essential criteria for research software tools: 1) It has a research-specific purpose in archaeological site prediction; 2) It transforms archaeological site location data and environmental variables into predictive models; 3) It aligns with established archaeological methodologies for predictive modelling. It also satisfies multiple supporting criteria: it integrates domain knowledge about archaeological site formation and environmental relationships; supports the analysis stage of research; transforms data between formats; performs complex calculations and pattern recognition; includes visualization functions; has documentation focused on research applications; and facilitates data analysis for archaeological site prediction.","https://github.com/mrecos/klrfome","","","https://mrecos.github.io/klrfome/","Creative Commons Attribution 4.0 International (CC BY 4.0)","Statistical analysis|Spatial analysis|Datasets|Machine learning","archaeological prediction|site modelling|kernel methods|logistic regression|environmental analysis","2017","2019","0.1.0","Abandoned","University of Pennsylvania","Matthew D. Harris","Solo","Archaeology","Project-specific","Comprehensive","KLRfome shows limited evidence of widespread adoption in the archaeological community. The GitHub repository has fewer than 20 stars and forks, with minimal recent activity. No dedicated forums or user groups were identified. Documentation exists primarily through the developer's own examples and academic publications, with limited evidence of application in projects beyond the developer's work. The software appears to remain primarily academic rather than being widely adopted in professional archaeological practice. No notable citations in recent archaeological literature beyond the original publication were found.","Analysis","research-specific","Packages and libraries","R","Windows|macOS|Linux","R","KLRfome works with standard spatial data formats including rasters and vector data through the R spatial ecosystem. The current version can read and process common GIS formats via the sp and raster R packages. It includes functions for processing environmental raster data and for outputting prediction results in formats compatible with GIS software for visualization. Input data needs to be formatted as tables of observations with environmental variables for site and background locations, which can be derived from standard GIS operations. Output from the model can be visualized directly in R or exported for use in other GIS platforms.","KLRfome's main strength is its innovative mathematical approach that treats archaeological sites as distributions rather than points, preserving spatial relationships that influence site locations. This approach is specifically designed to address limitations in traditional archaeological predictive modelling. The software includes built-in evaluation metrics (AUC, Youden's J, Kvamme Gain) for assessing model performance. As an open-source tool with a permissive license, it allows for inspection, modification, and extension by users. The package includes comprehensive documentation with examples and theoretical explanations. Its R implementation allows integration with the broader R spatial ecosystem and reproducible research workflows. KLRfome also directly addresses uncertainty in archaeological data through its distribution-based approach, which is particularly valuable in contexts where site boundaries are unclear or environmental conditions vary within sites.","KLRfome's primary weakness is its limited adoption beyond academic contexts, with little evidence of widespread use in professional archaeological practice. The tool has a steep technical barrier, requiring R programming knowledge and familiarity with advanced statistical concepts, which may limit accessibility for many archaeologists without programming experience. It lacks a graphical user interface, being command-line only. Development appears to have stalled after 2019, with minimal recent updates to address bugs or extend functionality. The specialized mathematical approach, while theoretically sound, may be difficult for non-specialists to understand and properly implement. There are few documented case studies demonstrating successful application in real-world archaeological projects beyond the developer's own examples. The tool's dependency on a single developer raises concerns about long-term maintenance and support.","KLRfome's long-term prospects appear uncertain. Development has been minimal since 2019, suggesting the project may be inactive. Its specialised nature and limited user base may challenge sustainability without ongoing development or institutional support. The mathematical approach pioneered in KLRfome has potential value but would likely need integration into more mainstream archaeological software to achieve broader impact. Despite these challenges, the software remains functional and available through GitHub, and its open-source nature means it could be revived or incorporated into other tools. The theoretical foundation of treating sites as distributions rather than points remains relevant to archaeological predictive modelling, so the concepts may survive even if the specific implementation does not. Without evidence of an active user community or ongoing maintenance, KLRfome may remain primarily of academic interest rather than evolving into a widely-used production tool.","Archaeological predictive modelling can be performed with several alternative tools that offer different approaches and advantages: 1) GRASS GIS provides comprehensive open-source GIS capabilities with modules for predictive modelling and a large user community. 2) QGIS offers a user-friendly open-source GIS platform with plugins for spatial analysis and prediction. 3) ArcGIS includes sophisticated spatial analysis tools within a commercial GIS platform widely used in professional archaeology. 4) MaxEnt (Maximum Entropy Modelling) is frequently used for archaeological predictive modelling with a focus on presence-only data. 5) General statistical packages in R and Python provide flexibility to implement various predictive modelling approaches. While these alternatives generally have larger user communities and better support, KLRfome's unique advantage is its archaeological-specific approach that treats sites as distributions rather than points, offering a theoretically more sophisticated approach to site prediction."
```

---
