# v8-MapReader-metadata

## Metadata
- **UUID:** `3e7619f6-9911-48a5-846c-a77fa68d9c36`
- **URL:** https://claude.ai/chat/3e7619f6-9911-48a5-846c-a77fa68d9c36
- **Date:** 2025-05-23 08:17:56

---

## Conversation

### Human (08:02:05)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (08:02:09)



I understand the requirements completely. I'll follow the archaeological research software tools metadata collection process as outlined in the detailed prompt. I'll apply the Writing Style Guide to both the report and CSV output, and use the specified title conventions.

For each tool you provide, I'll conduct thorough research and produce:
1. A properly formatted title following the "[Tool Name]: [Primary Function] for [Application Domain]" template
2. A comprehensive CSV record with all the required fields
3. A formatted report that adheres to the Writing Style Guide

I'm ready to begin researching the first tool you provide. Please share the name or acronym of the tool you'd like me to investigate.

---

### Human (08:02:24)

MapReader

---

### Assistant (08:02:31)



I'll research MapReader thoroughly to create a comprehensive metadata entry following all the guidelines you've provided. I'll start the research process immediately.
```
This block is not supported on your current device yet.
```

Your MapReader analysis is ready. This report examines an open-source Python tool that uses computer vision to extract data from historical maps at scale. It covers MapReader's technical architecture, archaeological applications, development team, documentation quality, and comparisons with alternatives. The analysis evaluates its strengths in processing large map collections, potential for heritage documentation, and long-term viability under Alan Turing Institute's support.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (08:15:35)

please also produce the requested CSV

---

### Assistant (08:16:22)

I'll now create the CSV entry for MapReader based on my research. The CSV should follow the format specified in the instructions, with all the required fields. I need to make sure I'm thorough and provide accurate information for each field, formatted properly with pipe (|) separators for multiple values and no newlines within fields.

Let me organize the data for the CSV entry:

- Tool: "MapReader"
- Description: A comprehensive summary of what MapReader does, focusing on the current version
- History: Chronological development account of MapReader
- Technical-discussion: Technical implementation details
- Access-date: Today's date (2025-05-23)
- Tool-status: Based on evaluation, this should be "yes" since it meets all essential criteria and multiple supporting criteria
- Tool-status-reasoning: Detailed explanation of why it qualifies as research software
- DVCS-repo: "https://github.com/maps-as-data/MapReader"
- CRAN: "" (empty since it's not a R package)
- PyPi: "https://pypi.org/project/mapreader/"
- Other-URL: "https://mapreader.readthedocs.io/en/latest/"
- License: "MIT"
- Tags: Select from controlled vocabulary
- AI-tags: Five tags I generate to characterize the tool
- First-release-date: Based on the research
- Last-update-date: Based on the research
- Current-version: "1.1.2" (the most recent stable version)
- Development-status: "Active"
- Institutional-backing: The organizations supporting MapReader
- Authors: The key contributors
- Development-team-size: "Medium (6-20)" based on the research
- Original-discipline: "Digital Humanities"
- Original-purpose: "Project-specific" (it was developed for the Living with Machines project)
- Documentation-quality: Based on the research, seems "Comprehensive"
- Usage-indicators: Summary of usage metrics

And continuing with the technical and assessment fields:

- Lifecycle-stage: Which research stages it supports
- Type: "research-specific"
- Category: "Stand-alone software"
- Language: "Python"
- Platform: Operating systems it supports
- Open-Archaeo-Platform: Not applicable for standalone software
- Interoperability: Data formats and exchange capabilities
- Strengths: Evidence-based assessment of advantages
- Weaknesses: Evidence-based assessment of limitations
- Survivability: Long-term viability assessment
- Alternatives: Similar tools comparison

Now I'll compile all this information into a properly formatted CSV entry.Based on my comprehensive research of MapReader, I've prepared the CSV metadata entry as requested. This captures the tool's functionality, technical details, development history, and applicability to archaeological research.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"MapReader","MapReader is an open-source Python library that uses computer vision to extract, process, and analyse data from digital maps at scale. The current version offers two main pipelines: a classification pipeline for identifying visual features and a text spotting pipeline for extracting textual information. Originally developed to analyse Victorian-era Ordnance Survey maps, the tool enables researchers to process thousands of map images simultaneously through a 'patchwork' approach that divides maps into manageable grid squares. While primarily used in digital humanities for historical research, MapReader offers significant potential for archaeological applications including site detection, landscape analysis, and heritage documentation from historical cartography.","MapReader was developed as part of the Living with Machines project (2018-2023), a £9.2 million collaboration between The Alan Turing Institute and the British Library funded by UK Research and Innovation. Early development began in 2018, with concept papers published in 2021 and the first public release in 2022. The software emerged from the need to analyse thousands of historical maps for patterns of industrialisation across 19th-century Britain. It underwent substantial refinement based on user feedback from historians and archaeologists before receiving the 2023 Roy Rosenweig Prize for Innovation in Digital History from the American Historical Association. Following the conclusion of the Living with Machines project in July 2023, development transitioned to the Data/Culture initiative at The Alan Turing Institute, where it continues to be actively maintained under AHRC grant AH/Y00745X/1.","MapReader implements a modular pipeline architecture built on PyTorch that processes images through distinct stages. The current version 1.1.2 requires Python ≥3.9 and integrates with the scientific Python ecosystem through dependencies including NumPy, Pandas, scikit-learn, and matplotlib. For geospatial functionality, optional dependencies include rasterio, geopandas, and cartopy. The software's core innovation is the 'patchwork method' that divides large map sheets into manageable grid squares (typically 100m x 100m) for classification, an approach adapted from biomedical imaging that makes computer vision analysis computationally feasible for large collections. The classification pipeline employs a convolutional neural network architecture based on ResNet models, pre-trained on ImageNet and fine-tuned using transfer learning. This pipeline achieved a 96.74% F1-macro score in identifying railway infrastructure in Victorian maps. The text spotting pipeline combines optical character recognition with a region proposal network to locate and extract map annotations. Installation presents platform-specific challenges, particularly on Windows systems requiring Visual Studio Build Tools and M1 Macs needing specific package versions. The development team addresses this through comprehensive documentation and custom conda packages. Processing performance varies by hardware configuration, but benchmark tests showed the ability to handle 30.5 million map patches from 16,000 historical maps during the Living with Machines project. Data outputs include classified patch datasets, feature probability scores, and extracted text with geographic coordinates, all exportable to standard formats (CSV, GeoJSON, GeoTIFF) for integration with GIS software. The modular architecture facilitates customisation, allowing researchers to train models on specific feature types relevant to their research questions.","2025-05-23","yes","MapReader qualifies as research software by meeting all essential criteria and multiple supporting criteria. It directly supports scholarly inquiry through data extraction from maps (Essential Criterion 1), transforms cartographic materials into structured datasets (Essential Criterion 2), and aligns with established methodologies in digital humanities and geospatial analysis (Essential Criterion 3). Among supporting criteria, MapReader incorporates domain knowledge through specialised map processing workflows (Supporting Criterion 1), supports multiple research lifecycle stages from data acquisition to analysis (Supporting Criterion 2), transforms maps into machine-readable formats (Supporting Criterion 3), performs complex pattern recognition and feature classification (Supporting Criterion 4), visualises spatial data distributions (Supporting Criterion 5), includes documentation specifically addressing research applications (Supporting Criterion 6), and facilitates data dissemination through standardised export formats (Supporting Criterion 8).","https://github.com/maps-as-data/MapReader","","https://pypi.org/project/mapreader/","https://mapreader.readthedocs.io/en/latest/","MIT","Spatial analysis|Site mapping|Aerial and satellite imagery|Data management|Machine learning","computer vision|historical maps|feature extraction|deep learning|geospatial analysis","2021-11-30","2024-02-15","1.1.2","Active","The Alan Turing Institute|British Library|Arts and Humanities Research Council (AHRC)","Katherine McDonough|Daniel C.S. Wilson|Kasra Hosseini|Kaspar Beelen|Rosie Wood|Kalle Westerling|Andrew Smith","Medium (6-20)","Digital Humanities","Project-specific","Comprehensive","MapReader has moderate adoption metrics compared to mainstream tools but strong indicators of specialised research impact. GitHub statistics show 96 stars and 15 forks as of May 2025. The software received the 2023 Roy Rosenweig Prize for Innovation in Digital History, validating its research contribution. Academic adoption continues growing with citations in computer vision, digital humanities, and plant phenotype research literature. The Alan Turing Institute hosts regular workshops dedicated to the tool, indicating institutional commitment to user growth. The project maintains active community engagement through dedicated Slack workspaces and conference presentations. While total download statistics are not published, the software has been used to process over 30.5 million map patches from 16,000 historical maps during the Living with Machines project, demonstrating its capacity for large-scale analysis.","Data Acquisition|Processing|Analysis|Interpretation","research-specific","Stand-alone software","Python","Windows|macOS|Linux","","MapReader works with standard geospatial formats including GeoTIFF and GeoJSON for input and output. The current version includes importers for map tiles from several providers and can export analysis results to formats compatible with major GIS software including QGIS and ArcGIS. Input formats include PNG, JPEG, and TIFF images with or without geographic referencing. Output formats include CSV tables of classification results, GeoJSON feature collections for spatial analysis, and visualisation-ready figures. The modular architecture facilitates integration with other Python libraries in the scientific ecosystem, particularly through pandas DataFrames as the primary internal data structure. While MapReader lacks formal API documentation for programmatic integration, its Python package design enables importing components into other applications. The software does not currently offer web service interfaces or standardised OGC-compliant services.","MapReader's key strengths include its specialisation for historical map analysis with purpose-built workflows that lower the technical barrier for humanities researchers. The software demonstrates excellent scalability, having processed collections of thousands of maps systematically while maintaining consistent quality. Its patch-based approach provides computational efficiency while preserving spatial context, addressing challenges that general-purpose computer vision tools struggle with for cartographic materials. The interactive annotation interface enables domain experts to create training datasets without extensive computer vision expertise. The software benefits from strong academic credibility through peer-reviewed publications and institutional support from the Alan Turing Institute, ensuring methodological rigour. The extensive documentation includes conceptual explanations, practical tutorials, and example repositories that support users at different technical levels. The MIT license and open-source development model encourage transparency and community contributions while allowing both academic and commercial applications. For archaeological research specifically, the classification pipeline offers potential for systematic detection of site features across large map collections that would be impractical to analyse manually.","The primary weaknesses of MapReader include installation complexity, particularly on Windows systems requiring additional build tools and macOS M1 machines needing specific dependency versions. The software has a relatively steep learning curve for users without Python experience, limiting accessibility for some potential archaeological users. The current implementation requires substantial computational resources for training models, potentially restricting use in resource-limited settings. Documentation, while comprehensive, sometimes assumes technical knowledge that archaeology students may lack. The user interface remains primarily code-based rather than graphical, making adoption more challenging for humanities researchers. The specialisation for map analysis means MapReader has limited utility for other archaeological data types like field surveys or excavation records. The relatively small user community compared to mainstream tools means fewer examples, tutorials, and troubleshooting resources are available. Detection accuracy varies significantly based on map quality and feature distinctiveness, potentially limiting effectiveness for degraded historical maps with archaeological annotations. While the tool shows potential for archaeological applications, concrete case studies and specialised archaeological feature detection models remain underdeveloped.","MapReader demonstrates strong foundations for long-term sustainability through institutional backing, open-source development practices, and growing academic adoption. The transition from project funding to ongoing Data/Culture support, combined with Alan Turing Institute's continued involvement, provides medium-term stability. The software's modular architecture and comprehensive documentation facilitate community contributions, while the MIT license encourages widespread adoption. The establishment of the Computer Vision for Digital Heritage Special Interest Group at The Alan Turing Institute indicates institutional commitment to the research area. Maintenance continuity is evidenced by regular updates to both the codebase and documentation, with 12 active repositories now maintained under the maps-as-data GitHub organization. Potential vulnerabilities include dependence on continued academic funding, relatively small user community compared to mainstream tools, and the specialized focus that may limit broader adoption. Critical success factors for continued viability include expanding the user base through targeted archaeological case studies, simplifying installation procedures to reduce technical barriers, developing partnerships with heritage organizations for sustainable funding, and creating discipline-specific training materials to accelerate adoption. Overall, the software shows good prospects for medium-term sustainability (3-5 years) with potential for longer-term viability if the user community continues to grow.","Transkribus offers superior text recognition from historical documents but lacks MapReader's visual feature classification capabilities. Commercial alternatives like Bunting Labs provide high accuracy for utility mapping but require expensive subscriptions and lack research-oriented flexibility. General image processing libraries like OpenCV offer lower-level functionality but require extensive programming expertise to implement map-specific workflows. Professional GIS software including ArcGIS offers some raster analysis tools, but the deprecated ArcScan module and licensing costs limit accessibility for academic researchers. QGIS with machine learning plugins (QGIS SCP, dzetsaka) provides some similar capabilities but requires greater manual configuration. For archaeological applications specifically, eCognition offers object-based image analysis but at high commercial cost. The main advantage MapReader offers over these alternatives is its specialization for cartographic materials with accessible workflows designed for humanities researchers rather than computer vision experts."
```

---
