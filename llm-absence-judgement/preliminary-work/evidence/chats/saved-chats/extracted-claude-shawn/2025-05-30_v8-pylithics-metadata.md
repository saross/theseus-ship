# v8-PyLithics-metadata

## Metadata
- **UUID:** `fa271a84-8a96-478e-a413-f4b610206c6e`
- **URL:** https://claude.ai/chat/fa271a84-8a96-478e-a413-f4b610206c6e
- **Date:** 2025-05-30 06:10:08

---

## Conversation

### Human (05:49:13)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (05:49:18)



I understand your requirements completely. I'll follow the detailed prompt to collect metadata about research software tools for archaeology, history, and other historical studies disciplines. I'll apply the Writing Style Guide to ensure academic tone and proper formatting, following the title convention format of "[Tool Name]: [Primary Function] for [Application Domain]".

I'll structure my response as a comprehensive report followed by the CSV output in the specified format. I won't ask follow-up questions and will handle any tool disambiguation using the guidelines provided.

I'm ready to begin researching the first tool you provide.

---

### Human (05:49:23)

PyLithics

---

### Assistant (05:49:33)



I'll research PyLithics, a tool for lithic analysis in archaeology. Since this appears to be a specialized archaeological research software tool, I'll start my research right away.
```
This block is not supported on your current device yet.
```

Your PyLithics software analysis is ready. It covers this specialized archaeological tool that automates stone tool illustration analysis, including its development by Cambridge and Alan Turing Institute researchers, technical implementation using Python and computer vision, and assessment of its strengths (1000x faster than manual analysis) and limitations (2D only, complex setup). The report evaluates its adoption, documentation quality, and long-term viability compared to emerging 3D analysis alternatives.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (06:08:27)

please also produce the requested csv

---

### Assistant (06:09:06)

I need to create a properly formatted CSV output according to the requirements in the prompt. Let me structure the CSV with all the specified columns, ensuring I use the pipe (|) separator for multiple values and proper escaping for any quotes.

The CSV should include a header row and a single data row with all the metadata I've collected about PyLithics. I'll need to ensure I follow all the formatting requirements:
- Use the controlled vocabulary lists provided where applicable
- Ensure no newlines within fields
- Use single quotes ('example') for quoted text within fields
- Make sure the number of columns in the data row matches the header row

I'll carefully create the CSV now based on all the research I've done on PyLithics.# PyLithics: Automated Analysis Software for Archaeological Stone Tool Illustrations

## Research Software Metadata Report

PyLithics is a specialized Python package that automates the analysis of stone tool illustrations in archaeological literature. Developed through a collaboration between the University of Cambridge's Department of Archaeology and the Alan Turing Institute, this software transforms traditional 2D lithic drawings into structured quantitative data using computer vision techniques. The software can identify, outline, and measure lithic artifacts from scanned illustrations approximately 1000 times faster than manual analysis methods.

The current version (v1.0) employs an 11-step automated workflow that processes lithic illustrations through pixel intensity thresholding, edge detection, contour finding, and template matching algorithms. PyLithics integrates several Python libraries including OpenCV, scikit-image, NumPy, SciPy, and Pandas to extract comprehensive measurements from 2D illustrations of stone tools.

While PyLithics represents a significant advancement in automating lithic analysis from published literature, its application is currently limited to 2D illustrations rather than 3D models or photographs. The tool primarily supports unifacial flakes and bifaces illustrated in conventional styles, which may restrict its broader adoption across archaeological subfields moving toward 3D methodologies.

Despite strong institutional backing from prestigious research organizations and a solid technical foundation, PyLithics faces sustainability challenges including a small development team and competition from emerging 3D analysis tools. However, its open-source nature, unique position in automated lithic illustration analysis, and planned future developments for 3D integration suggest potential for continued relevance in archaeological computing.

## CSV Output

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"PyLithics","PyLithics is an open-source Python software package designed to automatically process lithic artifact illustrations scanned from archaeological literature. Using computer vision and image processing techniques, it accurately identifies, outlines, and computes comprehensive shape and linear measurements from 2D stone tool drawings, returning structured data ready for quantitative analysis. The software enables researchers to transform the vast corpus of published lithic illustrations into machine-readable datasets, facilitating large-scale comparative analyses across time and space.","PyLithics emerged from the Palaeoanalytics project, a collaboration between The Alan Turing Institute and the University of Cambridge Department of Archaeology. The project aimed to develop machine learning and data science methodologies for non-genomic data in human evolution research. Development began as part of efforts to bridge the gap between traditional archaeological documentation and modern computational analysis methods. The software was officially published in the Journal of Open Source Software (JOSS) on January 29, 2022 as version 1.0, following peer review of both the code and accompanying paper. Future development plans include version 1.0.2 with expanded capabilities for 3D model support.","The current version of PyLithics implements an 11-step automated workflow for processing lithic illustrations. The technical architecture begins with image preprocessing using pixel intensity thresholding to isolate lithic drawings from backgrounds. Edge detection algorithms and contour finding functions then identify artifact boundaries with sub-pixel precision. The software employs custom template matching to distinguish between artifact surfaces (ventral, dorsal, platform) and recognizes characteristic features such as bulbs of percussion, ripple marks, and flake scars. Built on Python's scientific computing stack, PyLithics integrates OpenCV and scikit-image for computer vision operations, NumPy and SciPy for numerical processing, and Pandas for data structuring. The package uses a modular design with separate components for image processing, feature detection, measurement, and data output. Processing parameters are controlled via YAML configuration files, allowing customization for different illustration styles and artifact types. PyLithics maintains continuous integration through Travis CI with automated testing via pytest. Output data is structured hierarchically in JSON format, organizing measurements by lithic surfaces and including validation images with contour overlays for verification.","2023-05-30","yes","PyLithics fulfills all essential criteria as research software: (1) It serves a research-specific purpose in automating lithic analysis; (2) It transforms research materials (lithic illustrations) into structured data; (3) It aligns with established methodologies in lithic technology studies. Additionally, it meets multiple supporting criteria: it incorporates domain knowledge (lithic terminology and classification), supports data transformation (illustrations to measurements), provides analytical capabilities (morphometric analysis), includes research-oriented documentation, and enables data dissemination in structured formats.","https://github.com/alan-turing-institute/Palaeoanalytics","","","https://www.arch.cam.ac.uk/news/pylithics-new-software-stone-tool-analysis","GNU General Public License v3.0","Lithic analysis|Artefact morphology|API interfaces and web scrapers|Data management","computer vision|archaeological computing|lithic technology|automated measurement|image processing","2022-01-29","2022-01-29","v1.0","Active","The Alan Turing Institute|University of Cambridge Department of Archaeology|Leverhulme Centre for Human Evolutionary Studies","Dr. Jason J. Gellis|Dr. Camila Rangel Smith|Prof. Robert A. Foley","Small (2-5)","Archaeological computing","Project-specific","Comprehensive","Limited publicly available usage metrics. No significant community discussions, user testimonials, or case studies identified in archaeological forums or social media. The specialized nature and technical requirements may limit broader adoption.","Processing|Analysis","research-specific","Packages and libraries","Python","Linux|macOS|Windows","Python","PyLithics accepts PNG format lithic illustrations (1:1 scale preferred), PNG scale images, CSV metadata files mapping images to scales, and YAML configuration files. It outputs hierarchical JSON files containing measurements organized by lithic surfaces (ventral, dorsal, platform) and processed validation images with contour overlays. The software integrates with the Python scientific computing ecosystem and provides a command-line interface for workflow integration, with JSON output enabling further analysis in statistical tools.","Performance: ~1000x faster than manual analysis (minutes vs. seconds per artifact). Consistency: Eliminates human subjectivity in measurements. Comprehensiveness: Captures detailed surface metrics, scar measurements, flaking patterns. Open Source: Freely available with potential for community contributions. First-of-its-kind: No comparable software for automated lithic illustration analysis. Strong institutional backing: Supported by prestigious research institutions. Rigorous development: Peer-reviewed code, automated testing, professional software practices.","Limited scope: Only processes 2D illustrations, not 3D models or photographs. Artifact specificity: Optimized only for unifacial flakes and bifaces. Technical barriers: Complex installation and command-line interface may deter non-technical users. Drawing style dependency: Requires conventional lithic illustration styles. Small development team: Only 3 core developers raises sustainability concerns. Limited evidence of adoption: No visible user community or testimonials.","Moderate risk. While the software has strong institutional backing and solid technical foundation, several factors threaten long-term viability: Archaeological field rapidly moving toward 3D analysis methods; Limited evidence of active user community; Narrow application scope in an already specialized field; Competition from emerging 3D tools offering broader capabilities. Positive factors include open-source nature allowing community takeover, first-mover advantage in the niche, and stated plans for 3D integration in future versions.","3D Analysis Tools: Artifact3-D, AGMT3-D (Artifact Geomorph Toolbox 3D), 3D-EdgeAngle, photogrammetry software. Traditional Methods: Manual analysis (still widely used), R packages for morphometric analysis, CAD software with STIVA method. General Archaeological Software: CloudCompare for 3D analysis, various database management systems."
```

---
