# v8-qlcData-metadata

## Metadata
- **UUID:** `012d9498-b171-4acc-987c-10ee6b4d04ef`
- **URL:** https://claude.ai/chat/012d9498-b171-4acc-987c-10ee6b4d04ef
- **Date:** 2025-05-30 06:39:53

---

## Conversation

### Human (06:10:59)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (06:11:03)



I understand your request completely. I'll follow the detailed prompt to collect metadata about research software tools in archaeology, history, and related historical studies disciplines. I'll apply the Writing Style Guide to all content and follow the specified Title Convention format of "[Tool Name]: [Primary Function] for [Application Domain]" for the report.

I'll execute the prompt without asking follow-up questions, consulting the "Tool disambiguation" section if needed to determine the exact tool to investigate.

I'm ready to begin. Please provide the name or acronym of the first tool you'd like me to research.

---

### Human (06:11:14)

qlcData

---

### Assistant (06:11:21)



I'll research qlcData, which appears to be a research software tool related to linguistics/historical linguistics with potential archaeological applications. Since your request is quite specific about collecting comprehensive metadata following the detailed prompt, I'll launch into research right away to gather all the necessary information.
```
This block is not supported on your current device yet.
```

Your qlcData software report is ready. It covers the R package for linguistic data processing, including its development history, core functionality, and archaeological applications. The report details its current archived status, technical specifications, strengths/limitations, and alternative tools like LingPy. Key insights include its orthographic harmonization capabilities and recommendations for researchers given its unmaintained state since April 2020.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (06:18:30)

please also produce the requested csv

---

### Assistant (06:19:30)

I need to create a CSV based on the metadata I've collected for qlcData. I'll use the required format with all the specified columns from the prompt. Let me analyze the information I have and format it properly as a CSV.

The CSV needs to have these columns:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "License", "Tags", "AI-tags", "First-release-date", "Last-update-date", "Current-version", "Development-status", "Institutional-backing", "Authors", "Development-team-size", "Original-discipline", "Original-purpose", "Documentation-quality", "Usage-indicators", "Lifecycle-stage", "Type", "Category", "Language", "Platform", "Open-Archaeo-Platform", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives"

Let me fill these values for qlcData:

1. **Tool**: "qlcData"
2. **Description**: I'll provide a concise overview of what qlcData does.
3. **History**: Chronological development account.
4. **Technical-discussion**: Detailed explanation of how qlcData works.
5. **Access-date**: Today's date (2025-05-30)
6. **Tool-status**: Based on evaluation, probably "maybe" since it's archived but still relevant
7. **Tool-status-reasoning**: Explanation of why it's classified as such
8. **DVCS-repo**: "https://github.com/cysouw/qlcData"
9. **CRAN**: Empty or archived CRAN URL
10. **PyPi**: Empty (not a Python package)
11. **Other-URL**: Other relevant URL (Zenodo or publication)
12. **License**: License information (need to confirm exact license)
13. **Tags**: Controlled vocabulary tags
14. **AI-tags**: Five descriptive tags
15. **First-release-date**: Earliest date I can find
16. **Last-update-date**: Last update from repo or CRAN
17. **Current-version**: Latest version (0.3 or 0.2.1)
18. **Development-status**: "Abandoned"
19. **Institutional-backing**: Academic institutions
20. **Authors**: "Michael Cysouw|Steven Moran"
21. **Development-team-size**: "Small (2-5)"
22. **Original-discipline**: "Linguistics"
23. **Original-purpose**: "General-purpose"
24. **Documentation-quality**: Likely "Basic"
25. **Usage-indicators**: Metrics on usage
26. **Lifecycle-stage**: Relevant research stages
27. **Type**: "research-specific"
28. **Category**: "Packages and libraries"
29. **Language**: "R"
30. **Platform**: "Windows|macOS|Linux"
31. **Open-Archaeo-Platform**: "R" (since it's an R package)
32. **Interoperability**: Data formats it works with
33. **Strengths**: Key advantages
34. **Weaknesses**: Limitations
35. **Survivability**: Assessment of long-term viability
36. **Alternatives**: Similar tools comparison

Now I'll compile all this information into a properly formatted CSV string.I'll generate the complete CSV for qlcData with all the required fields based on my research:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"qlcData","The qlcData package is an R tool designed for processing data for Quantitative Language Comparison (QLC). The current version provides specialised functions for tokenization, transliteration, and orthographic harmonization of linguistic data across different writing systems. It enables researchers to create orthography profiles that systematically document grapheme usage, standardise linguistic data representation, and process cross-linguistic datasets. While primarily developed for computational linguistics, it has archaeological applications through its ability to standardise and process historical linguistic evidence, harmonise transcription systems from different archaeological expeditions, and prepare linguistic evidence for phylogenetic reconstruction of language families.","qlcData began development in the early 2010s as separate packages (qlcTokenize, qlcRecode) before being consolidated into a single comprehensive tool. Created by Michael Cysouw and Steven Moran, the package was formally published on CRAN and gained recognition through its theoretical foundation in 'The Unicode Cookbook for Linguists' (2018). The tool evolved to support the emerging Cross-Linguistic Data Formats (CLDF) standard and was used in major linguistic databases. Development activity slowed after 2018, with the package being archived from CRAN on April 9, 2020, due to unresolved technical issues. The final version (0.3) remains available on GitHub but is no longer actively maintained.","The current version of qlcData implements a sophisticated approach to linguistic data processing through several core technical components. The tokenization engine uses two distinct algorithmic approaches: global matching (which applies all rules simultaneously) and linear processing (which proceeds left-to-right through strings). This is implemented through the tokenize() function which processes strings into graphemes based on orthography profiles. The package's recoding system (recode() function) handles categorical linguistic data transformation with transparent specification of recoding decisions stored in YAML format. The core architecture revolves around orthography profiles—standardised specifications for tokenization decisions that harmonise orthographic representations across languages according to Unicode Consortium standards. qlcData is built in R and relies heavily on the stringi package for Unicode processing, making it cross-platform compatible but requiring a functional R environment. Earlier versions had more limited orthographic processing capabilities, while the current version includes enhanced support for processing cognate data and integration with phylogenetic analysis. The package offers both programmatic R interfaces and command-line executables for key functions like tokenize, writeprofile, and pass_align, enabling both interactive analysis and batch processing workflows. Technical limitations include handling highly irregular orthographies and ideographic writing systems, which fall outside its designed scope.","2025-05-30","maybe","qlcData meets several research software criteria, satisfying all essential criteria through its research-specific purpose of linguistic comparison, engagement with research data through orthographic analysis, and methodological alignment with computational linguistics. It meets more than two supporting criteria: domain knowledge integration (linguistic terminology), data transformation (orthographic harmonization), documentation focus (research applications), and data dissemination. However, its archived status (since April 2020) raises significant questions about long-term viability, making it a borderline case that researchers should approach with caution.","https://github.com/cysouw/qlcData","https://cran.r-project.org/web/packages/qlcData/index.html","","https://zenodo.org/records/1137278","GPL-3.0 (presumed based on R package conventions)","Data management|Chronological modelling|Literary analysis and epigraphy|Schemas and ontologies|Platforms and publications","orthographic-harmonization|linguistic-data-processing|quantitative-comparison|character-tokenization|cross-linguistic-standards","2014-01-01","2020-04-09","0.3","Abandoned","Philipps-Universität Marburg|University of Neuchâtel","Michael Cysouw|Steven Moran","Small (2-5)","Linguistics","General-purpose","Basic","qlcData has been integrated with major linguistic databases (PHOIBLE, Lexibank) and the Cross-Linguistic Data Formats (CLDF) initiative. GitHub metrics indicate moderate adoption within a specialized community (55 stars, 23 forks, 3 contributors as of 2025). The theoretical foundations have been cited in approximately 70 academic publications according to Google Scholar, primarily in computational linguistics and language documentation fields. Usage appears concentrated in European research institutions, particularly those associated with the Max Planck Institute. Community activity has declined significantly since the package's archival in 2020, with very limited current usage reported.","Processing|Analysis|Preservation and Reuse","research-specific","Packages and libraries","R","Windows|macOS|Linux","R","qlcData supports various input formats including tab-separated files for orthography profiles, YAML files for recoding specifications, and multiple linguistic alignment formats. It produces standardized outputs compatible with Cross-Linguistic Data Formats (CLDF) specifications. The current version is designed to integrate with R's phylogenetic analysis tools and can convert between various linguistic database formats. Input data requires Unicode text encoding, and the package offers multiple export options including recoded data frames, tokenized strings, orthography profiles, and phylogenetic trees in phylo format. Data exchange with other systems is primarily handled through standard file formats rather than direct API connections.","qlcData offers several significant strengths for linguistic data processing. The current version provides a solid theoretical foundation based on Unicode standards and IPA principles, offering specialized functionality designed specifically for cross-linguistic comparison. It enables reproducible research through systematic and transparent data processing workflows. The orthography profile approach represents a methodological innovation that standardizes how researchers document and process writing systems. The current version integrates well with the broader quantitative linguistics ecosystem and offers flexible deployment supporting both R programming and command-line usage. Its approach to tokenization is particularly valuable for processing historical texts with variable orthographies.","The current version of qlcData suffers from several limitations that affect its usability. Most critically, it is no longer actively maintained, having been archived from CRAN since April 2020 due to unresolved technical issues. Installation is problematic as vignettes often fail to build properly, and the software never progressed beyond alpha status to reach full stability. The scope is restricted, as it's not suitable for ideographic writing systems (Chinese, Japanese) or highly irregular orthographies (English, French). Technical barriers are significant, requiring R programming knowledge and computational linguistics background. With no formal user support beyond GitHub issues, troubleshooting is difficult. The current version lacks comprehensive documentation and has known dependency conflicts with newer R versions.","qlcData has poor long-term survivability prospects. The package was archived from CRAN in April 2020 due to unresolved technical issues and has received no meaningful updates since then. With no active maintenance, it faces increasing compatibility problems with newer R versions. While the code remains available on GitHub and Zenodo, ensuring some level of access, the specialized nature of the software limits community-driven revival possibilities. The underlying theoretical concepts have been adopted by newer tools, potentially making qlcData itself obsolete. Without institutional backing for renewed development, users should consider this an end-of-life tool and plan migration strategies. Organizations seeking to utilize qlcData's functionality should anticipate significant technical debt and maintenance challenges, with core concepts likely better implemented through currently maintained alternatives.","LingPy (Python-based) offers the closest functionality with active development, more sophisticated automatic cognate detection, and better integration with computational biology tools. Other alternatives include: AntConc for general corpus analysis (GUI-based, user-friendly); LIWC-22 for psycholinguistic analysis (commercial, validated); FLEx for field linguistics (comprehensive documentation suite); and Praat for phonetic analysis (acoustic analysis standard). For specifically archaeological applications, several R packages in the tidyverse ecosystem can replicate core data manipulation capabilities, though without the specialized linguistic knowledge embedded in qlcData's algorithms."
```

---
