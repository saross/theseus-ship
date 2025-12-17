# v8-glottoTrees-metadata

## Metadata
- **UUID:** `d7a4bb46-e572-49d3-961f-0c9ddc0989f8`
- **URL:** https://claude.ai/chat/d7a4bb46-e572-49d3-961f-0c9ddc0989f8
- **Date:** 2025-05-07 17:52:32

---

## Conversation

### Human (17:41:44)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (17:41:49)



I understand the task completely. You've provided detailed instructions for collecting metadata about research software tools used in archaeology, history, and related disciplines. I'll follow the process outlined in the prompt to research and document these tools according to the specified format and evaluation criteria.

I'll apply the Writing Style Guide you've shared, which emphasizes academic clarity, direct assertions with appropriate nuance, balanced authority, and technical precision with accessibility. I'll also follow the title convention format of "[Tool Name]: [Primary Function] for [Application Domain]" with an academic tone.

I'm ready to begin researching the first tool as soon as you provide its name or acronym. I'll conduct thorough research according to your specifications and present the findings in the requested CSV format within a markdown code block.

---

### Human (17:41:59)

glottoTrees

---

### Assistant (17:42:10)



I'll research glottoTrees thoroughly according to your specifications. This appears to be a software tool related to linguistics or language analysis that may have applications in archaeology and historical studies. Let me launch a comprehensive research process to gather the detailed metadata you need.
```
This block is not supported on your current device yet.
```

Your glottoTrees research analysis is ready. It evaluates this R package for phylogenetic tree manipulation in linguistic research with archaeological applications. The report covers its development by Erich Round, technical implementation, archaeological case studies, qualification as research software, key strengths in visualizing language relationships, limitations in community adoption, and long-term sustainability prospects.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (17:49:42)

please also generate the requested csv

---

### Assistant (17:50:29)



I've prepared the CSV output with comprehensive metadata about glottoTrees. Below is the properly formatted CSV containing all the requested fields according to your specifications:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"glottoTrees","glottoTrees is an R package that facilitates the preparation, manipulation, and visualisation of phylogenetic trees specifically for linguistic research. It adapts resources from the Glottolog database, providing tools for extracting, modifying, and analysing language family trees. While primarily developed for linguistic applications, glottoTrees serves archaeological research by enabling correlations between language evolution and material culture evidence. The package allows researchers to visualise evolutionary relationships between languages, which helps integrate linguistic data with archaeological findings to reconstruct aspects of human prehistory. This bridging function is particularly valuable for calibrating language trees with archaeological evidence and identifying pre-contact cultural relationships that predate written records.","glottoTrees was developed by Erich R. Round, a Professor of Linguistics with dual affiliations at the University of Surrey (UK) and the University of Queensland (Australia). First released in 2021 as version 0.1, the software emerged from Round's research in historical linguistics and language evolution. The tool was formally documented in a 2022 paper published in Linguistic Typology by Jayden L. Macklin-Cordes and Round titled 'Challenges of sampling and how phylogenetic comparative methods help: with a case study of the Pama-Nyungan laminal contrast', which included supplementary materials with a detailed tutorial. The package has received limited updates since its initial release, with version 0.1.9 released in December 2022, but continues to be cited in academic research, particularly in studies of Australian aboriginal languages.","glottoTrees is implemented in R and functions primarily by leveraging the 'ape' (Analysis of Phylogenetics and Evolution) package along with other R dependencies. The package processes hierarchically structured language classification data from Glottolog, stored in Newick tree format, converting these text-based representations into R's native 'phylo' objects for programmatic manipulation. Its architecture is modular, organised around functional categories including tree topology manipulation, branch length adjustment, node/tip labelling, metadata extraction, and visualisation. The workflow typically involves reading Glottolog's Newick-formatted trees, parsing the linguistic metadata, and creating interactive R objects that preserve hierarchical relationships between languages. Key operations include tree grafting (combining multiple tree structures), branch rescaling (adjusting evolutionary distances), and node operations. Version 0.1.9 implements specialised tree visualisation through the plot_glotto() function, rendering downward-oriented trees in a style preferred by linguists rather than the leftward orientation common in biological phylogenetics. The package includes data from Glottolog versions 4.0 through 4.8, providing comprehensive coverage of the world's language families while maintaining version compatibility.","2025-05-07","yes","glottoTrees qualifies as a research software tool by meeting all essential criteria and exceeding the supporting criteria requirements. It creates, processes and analyses research data by manipulating phylogenetic trees for linguistic analysis; is used in academic publications with a detailed tutorial in Linguistic Typology; has adequate documentation including GitHub README, function documentation, and tutorial paper; and is publicly available on GitHub under a Creative Commons License. It satisfies 5 of 6 supporting criteria: has test files for automated testing, uses Git version control, has GitHub's issue tracking system available, is released under CC-BY-4.0 license, and shows ongoing maintenance with a release in December 2022 (v0.1.9).","https://github.com/erichround/glottoTrees","","","https://slcladal.github.io/phylo.html","CC-BY-4.0","Network analysis|Datasets|Visualizations|Templates|Statistical analysis","phylogenetics|linguistic analysis|tree visualization|comparative analysis|data transformation","2021-01-01","2022-12-15","0.1.9","Maintenance-only","University of Queensland (Australia)|University of Surrey (UK)","Erich R. Round|Jayden L. Macklin-Cordes","Solo","Linguistics","General-purpose","Basic","The tool has limited usage indicators. On GitHub, it has 5 stars and 3 forks as of May 2025. The package is referenced in at least one published paper in Linguistic Typology (2022), primarily by the original authors. It has been used in research on Australian aboriginal languages, particularly Pama-Nyungan language studies. There are no documented community discussions on Stack Overflow or similar platforms, suggesting limited adoption outside the authors' immediate academic circle. The package has seen application in specific academic contexts but lacks evidence of broader adoption across linguistics or archaeology.","Analysis","research-specific","Packages and libraries","R","R","","glottoTrees can process Newick-formatted tree files, a standard format for representing phylogenetic trees. It interoperates well with the R ecosystem, particularly with the 'ape' package for phylogenetic analysis. The current version can read tree data from Glottolog versions 4.0 through 4.8, allowing integration with this major linguistic database. It can export visualisations in standard R graphical formats (PDF, PNG, etc.). The package's interoperability is somewhat limited by its specialisation to linguistic phylogenetics and focus on Glottolog data sources, though it can potentially work with any properly formatted Newick tree regardless of origin.","glottoTrees excels at making Glottolog's genealogical data accessible and adaptable for linguistic research, allowing researchers to modify phylogenetic trees to reflect their hypotheses about language relatedness. The software provides linguistics-specific tree visualisations in a downward-running format that conforms to disciplinary conventions rather than the horizontal format common in biology. It integrates seamlessly with the broader R ecosystem, allowing researchers to leverage existing R packages for statistical analysis while maintaining focus on linguistic research questions. Its development by an active academic researcher ensures alignment with actual research needs in linguistic typology. Documentation is a notable strength, with a published tutorial in a peer-reviewed journal providing both legitimacy and accessibility.","The tool exhibits several weaknesses that limit its broader adoption. The modest community engagement metrics (5 stars, 3 forks) suggest limited usage outside the author's immediate academic circle. glottoTrees appears to be primarily maintained by a single developer, creating potential sustainability concerns if the author's priorities change. The relatively infrequent updates and commits indicate that development is not as active as comparable tools. Documentation, while present, could be more comprehensive - while there is a tutorial paper and basic GitHub documentation, the lack of extensive user guides, examples, and community-contributed documentation presents barriers to new users. The software's specificity to linguistic phylogenetics, while a strength for its target audience, limits its appeal to researchers in adjacent fields who might benefit from its functionality.","glottoTrees presents mixed long-term survivability prospects. Positively, it addresses a specific need in linguistic research that is unlikely to disappear, as phylogenetic approaches in historical linguistics continue to gain prominence. Its integration with Glottolog, a well-established linguistic resource, anchors it to a stable foundation. Implementation in R is advantageous for survivability, as R has a strong presence in academic research with robust package management infrastructure. However, several factors create sustainability concerns. Development appears primarily driven by a single researcher rather than an institutional team. The modest user community means there may not be sufficient external contributors ready to maintain the project if needed. The academic paper publications provide some insurance against complete disappearance, as the methodological approach is documented in the literature. For improved survivability prospects, the project would benefit from recruiting additional contributors, creating more comprehensive documentation, and establishing stronger institutional backing.","lingtypology: Another R package focused on linguistic data that works with Glottolog, though emphasising geographic mapping rather than phylogenetic analysis. phyloWeights: A companion package by the same author (Round) for calculating genealogically-sensitive proportions and averages. BEASTling: A tool that facilitates the application of Bayesian phylogenetic methods to linguistic data using BEAST2 framework. ape: The Analysis of Phylogenetics and Evolution package in R - more general-purpose than glottoTrees but lacks linguistics-specific functions. ggtree: An R package for visualising phylogenetic trees that offers substantial customisation options but lacks linguistic-specific defaults. Phyx: A collection of Unix/Linux command-line tools for phylogenetic analyses offering different workflow options compared to R-based approaches. D-PLACE: The Database of Places, Language, Culture and Environment provides integrated cross-cultural datasets with some phylogenetic functionalities but through a web interface rather than programmatic access."
```

---
