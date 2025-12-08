# v8-ArchaeoPhases-metadata

## Metadata
- **UUID:** `e7e67938-e612-4751-a14e-e83e55ef608b`
- **URL:** https://claude.ai/chat/e7e67938-e612-4751-a14e-e83e55ef608b
- **Date:** 2025-05-05 15:52:34

---

## Conversation

### Human (13:01:48)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
Note that a 'Writing Style Guide' is attached to this Project, please apply it to your report and the CSV.

---

### Assistant (13:02:18)



I understand your request! You'd like me to help collect metadata about research software tools specifically for archaeology, history, and related disciplines following the detailed framework provided in the "Archaeological Research Software Tools Metadata Collection" document.

The guidelines are comprehensive and include:
- Research approach requirements (accuracy, thoroughness, recency focus)
- Version clarity expectations
- Tool disambiguation principles
- Content guidelines for different fields
- Output format specifications with CSV structure
- Column specifications for all metadata fields
- Tool evaluation framework with specific criteria
- Controlled vocabulary lists

I'll apply the Australian spelling and punctuation preferences from your Writing Style Guide as well, focusing on:
- Academic clarity with direct assertions
- Active voice with strategic variation
- Concise transitions and logical progression
- Technical precision with accessibility

I'm ready to begin researching the first tool you'd like me to investigate. Please provide the name or acronym of the tool, and I'll apply the methodology outlined to collect comprehensive metadata about it.

---

### Human (13:02:23)

ArchaeoPhases

---

### Assistant (13:02:30)



Thank you for providing the tool name. I'll research ArchaeoPhases comprehensively following the metadata collection framework and apply the writing style guidelines you've shared.

Before I begin my in-depth research, I'd like to clarify a few things to ensure I provide the most accurate and useful information:

1. Do you have any specific aspects of ArchaeoPhases you're particularly interested in (e.g., its application in Bayesian chronological modelling, integration with R, specific versions)?

2. Are you aware of any institutional connections for this tool that might help focus my research (e.g., connections to specific research groups or archaeological projects)?

3. Are there specific alternative tools you'd like me to compare ArchaeoPhases with in the "Alternatives" section (e.g., OxCal, BCal, ChronoModel)?

These clarifications will help me tailor my research to best meet your needs while maintaining the comprehensive approach outlined in your guidelines.

---

### Human (13:41:51)

I need to ensure consistency across many runs of this prompt, so please just follow the provided instructions. If you have suggestions for how the prompt might be improved, remember them and I will ask after you have produced the requested output.

---

### Assistant (13:41:58)



I'll follow the instructions and research ArchaeoPhases comprehensively according to the provided framework. Starting my research now.
```
This block is not supported on your current device yet.
```

Your ArchaeoPhases software report is ready. It analyzes this R package for archaeological chronology, covering its statistical post-processing capabilities, development history, technical implementation, and applications. The report details how it complements primary dating software like OxCal, its unique tempo plot feature for visualizing patterns of change, and its position within the archaeological software ecosystem.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (15:51:46)

can you please also produce the requested csv?

---

### Assistant (15:52:34)



I'll create the CSV for ArchaeoPhases based on my research following your specifications.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"ArchaeoPhases","ArchaeoPhases is an R package that provides statistical tools for post-processing Markov Chain Monte Carlo (MCMC) simulations from chronological modelling software used in archaeology. The current version enables researchers to analyze outputs from primary dating programs like OxCal, ChronoModel, and BCal. Its key functionalities include creating tempo plots to visualize the rhythm of events, generating activity plots to show density of events over time, performing statistical analyses of phase transitions, and defining boundaries between successive archaeological phases. The package is particularly valuable for examining temporal patterns in archaeological chronologies, helping researchers distinguish between periods of tradition (steady patterns), innovation (abrupt changes), and fashion (rapid but temporary changes).","ArchaeoPhases emerged from statistical research at the Université de Nantes in France. The core statistical methods were under development prior to 2017, with the software formally introduced in a working paper by Anne Philippe and Marie-Anne Vibet that year. The first version (1.0) was released in 2017, followed by version 1.5 and eventually 1.8 as the last in the 1.x series. A significant update came with version 2.0 in 2023, which included comprehensive rewrites, renaming of nearly all functions for improved consistency, and implementation of the 'aion' package for internal date representation. Throughout its development, the software has maintained its focus on providing specialized statistical tools for archaeological chronology while expanding its capabilities and improving its user interface.","The current version of ArchaeoPhases is implemented in R, following standard R package conventions with a modular design. It requires R version 3.5.0 or higher and is compatible with Windows, macOS, and Linux/Unix systems. The architecture includes R source code for core functions, roxygen2 format documentation, test files, vignettes with extended documentation and examples, and example datasets (with larger datasets moved to a companion ArchaeoData package). The package has several key dependencies including 'aion' for date representation (introduced in version 2.0), 'ggplot2' for visualization, 'coda' for MCMC analysis, and 'stats' for core statistical calculations. Version 2.0 introduced significant technical changes including a complete renaming of functions for improved consistency and the adoption of the 'aion' package for standardized date representation. ArchaeoPhases implements specialized algorithms for Allen's interval algebra to reason about temporal relations, statistical methods for post-processing MCMC simulations, and visualization techniques specific to archaeological time series. The package is designed as a post-processing tool that works with outputs from primary chronological modelling software rather than performing initial modelling itself. This approach allows it to complement multiple primary tools while focusing on specialized statistical analysis of archaeological phases and transitions.","2025-05-05","yes","ArchaeoPhases meets all essential criteria for research software: (1) It has a research-specific purpose, being explicitly designed for archaeological chronological analysis; (2) It directly engages with research data by transforming MCMC outputs from chronological modelling software; (3) It aligns with methodological approaches in Bayesian chronological modelling in archaeology. It also satisfies numerous supporting criteria: it incorporates domain knowledge through specialized chronological terminology, supports the analysis stage of the research lifecycle, transforms data between formats, provides analytical capabilities for statistical inference, offers visualization functions like tempo and activity plots, includes documentation specifically addressing archaeological applications, and facilitates data dissemination through standardized outputs that can be used in publications.","https://github.com/ArchaeoStat/ArchaeoPhases","https://CRAN.R-project.org/package=ArchaeoPhases","","https://archaeostat.github.io/ArchaeoPhases/","GPL-3","Chronological modelling|Statistical analysis","archaeological chronology|statistical post-processing|MCMC simulations|temporal analysis|Bayesian modelling","2017","2023","2.0","Active","Université de Nantes|University of Hawai'i","Anne Philippe|Marie-Anne Vibet|Thomas S. Dye|Nicolas Frerebeau","Small (2-5)","Statistics|Archaeology","General-purpose","Comprehensive","ArchaeoPhases has moderate usage within specialized archaeological chronology research. It has 53 stars and 12 forks on GitHub as of May 2025, with contributions from 4 main developers. The package is cited in archaeological publications focusing on chronological modelling, with notable applications including Hawaiian social stratification studies, Rapa Nui monument construction analysis, the Canímar Abajo site in Cuba, and Paleolithic occupations at Havrincourt in France. It appears in the CRAN repository and is listed in archaeological software compilations like open-archaeo. The package has consistent but specialized usage, primarily in French and American archaeological research contexts.","Analysis","research-specific","Packages and libraries","R","Windows|macOS|Linux","R","ArchaeoPhases is designed to work with outputs from multiple chronological modelling software packages including OxCal, ChronoModel, and BCal. It reads MCMC output files from these programs and provides functions to import, process, and analyze this data within the R environment. The current version can handle various date formats through the 'aion' package implementation. Output from ArchaeoPhases can be exported as tables or visualizations suitable for publication. The package also integrates with the broader R ecosystem, allowing researchers to combine its specialized archaeological functions with other statistical and visualization packages. For larger datasets, it interfaces with the companion ArchaeoData package.","ArchaeoPhases offers several distinct strengths. First, its cross-platform integration enables working with outputs from multiple primary modelling programs (ChronoModel, OxCal, BCal), creating a flexible workflow that accommodates different software preferences. Second, the tempo plot feature provides unique visualization capabilities that reveal the pace of change over time, offering insights difficult to derive from standard chronological presentations. This helps archaeologists identify cultural patterns related to tradition, innovation, and fashion that might otherwise remain hidden. Third, as an open-source R package, it benefits from transparency, free availability, and integration with the broader R ecosystem. This allows researchers to extend analyses using additional statistical tools and customize approaches for specific archaeological problems. Finally, the software brings additional statistical rigor to archaeological phase analysis, offering more detailed probability distributions and uncertainty measures than many alternatives, enhancing confidence in chronological interpretations.","ArchaeoPhases has several notable limitations. First, it functions as a post-processing tool only, meaning users must first learn and use primary modelling software like OxCal or ChronoModel. This creates a more complex workflow requiring data management across multiple programs. Second, despite offering a graphical user interface option, getting the full benefit typically requires familiarity with R programming and statistical concepts. This learning curve can be challenging for archaeologists without computational backgrounds. Third, the software has a specialized focus on archaeological phase analysis and may not be as versatile for other types of chronological studies or broader archaeological analyses. Its strength in depth comes at the cost of breadth, making it most valuable for specific analytical questions rather than as a general archaeological tool.","ArchaeoPhases shows good prospects for long-term viability. The software has several positive indicators for continued sustainability: it is actively maintained with regular updates, the most recent major version (2.0) was released in 2023, and it has institutional backing from established academic institutions (Université de Nantes and University of Hawai'i). The development team, while small, includes both statisticians and archaeologists, providing important cross-disciplinary expertise. Being an R package hosted on CRAN ensures standardized distribution and accessibility. The software's open-source nature under the GPL-3 license allows for community contributions and forking if necessary. Its integration with widely-used primary chronological modelling tools and the broader R ecosystem enhances its long-term relevance. The main factors that could affect future viability include the specialized nature of its application, which means a relatively small user base, and potential dependence on key developers. Overall, its specialized niche, active development, institutional support, and open-source foundation suggest good prospects for continued availability and relevance.","OxCal (Oxford University's primary chronological modelling software with Chronological Query Language capabilities)|ChronoModel (CNRS-developed graphical tool for integrating multiple dating methods)|BCal (web-based Bayesian calibration tool)|ArchaeoChron (complementary R package for archaeological analyses)|BayLum (R package specializing in OSL dating within Bayesian frameworks)|ChronoLog (focusing on chronological network modelling)"
```

---
