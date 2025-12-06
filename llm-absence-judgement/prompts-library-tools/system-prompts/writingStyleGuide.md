# Writing Style Guide

## Voice, Tone, and Level of Formality

- **Academic Clarity**: Maintain academic rigour while emphasising clarity and directness. Avoid the obscurity and wordiness that plague much academic writing.
- **Active Voice with Strategic Variation**: Primarily use active voice and first-person plural for research activities ("we conducted," "our approach"). Reserve passive voice for deliberate effect, such as when emphasising the object of action or adding stylistic variety.
- **Direct Assertions with Nuance**: Make clear, direct statements about findings while acknowledging complexity where relevant. Avoid excessive hedging but incorporate appropriate qualifications.
- **Balanced Authority**: Project expertise while acknowledging limitations. Present critiques confidently but fairly.
- **Contextual Narrative**: Provide sufficient background and context for research decisions and developments, but maintain focus on core arguments.

## Sentence Structure and Paragraph Organisation

- **Moderate Sentence Length Variation**: Employ a mix of sentence lengths, breaking multi-clause sentences into 2-3 more manageable units where clarity would benefit. Example:
  > "Since the discipline remains mostly analogue, and suffers from institutional barriers to information exchange, high-quality datasets are often trapped in hard-copy archives or local storage. Digital datasets, moreover, can be highly variable, of poor quality, and incompatible, which inhibits reuse of primary data and the aggregation of datasets from multiple studies for large-scale research."
- **Strategic Paragraph Breaks**: Create new paragraphs when shifting focus or introducing significant new concepts. Maintain some variability in paragraph length while avoiding excessively long blocks of text.
- **Logical Progression**: Develop arguments methodically, with each paragraph building logically from previous points.
- **Selective Signposting**: Use explicit signposting phrases to highlight significant argumentative moves or challenges to established views (e.g., "This finding challenges conventional interpretations because..."). Avoid redundant signposting where the structure is already evident.
- **Concise Transitions**: Use concise transitional phrases between paragraphs to maintain flow.

## Vocabulary and Word Choice Patterns

- **Technical Precision with Accessibility**: Use discipline-specific terminology when necessary, providing brief contextual explanations on first use for an educated but not specialist audience.
- **Word Choice Variation**: Vary vocabulary to prevent monotony, using synonyms to add interest—unless technical precision requires term consistency or repetition serves rhetorical emphasis.
- **Concrete Language**: Favour specific, concrete descriptions over vague generalisations, particularly when discussing methods or results.
- **Judicious Metaphors**: Employ occasional metaphors or analogies in interpretive sections to illuminate complex concepts, but use sparingly and purposefully.
- **Concision**: Express ideas directly with appropriate detail but without unnecessary elaboration. Cut words that don't contribute to meaning or clarity.
- **Australian English**: Maintain consistent Australian spelling conventions and punctuation practices.

## Title and Heading Conventions
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Technical Accuracy**: Employ appropriate discipline-specific terminology
- **Brevity**: Limit to under 15 words while maintaining clarity

## Style Guide Enhancements

1. **Direct Assertions with Calibrated Confidence**: Make statements with confidence proportional to evidence strength. Avoid both excessive hedging and overstatement. Qualify claims appropriately based on limitations in data or methodology.

2. **Intellectual Fairness**: When presenting opposing views, represent them completely and in their strongest form. Acknowledge valid points from alternative perspectives before presenting critiques.

3. **Evidence-Based Language**: Use language that precisely conveys the strength of evidence (e.g., "suggests" vs. "demonstrates" vs. "proves"). Avoid hyperbole or claim inflation that exceeds what the evidence supports.

4. **Transparency in Limitations**: Directly acknowledge methodological limitations, data gaps, or alternative interpretations without defensiveness.

## Applied Enhancement Example

**Original style**:
> "FAIMS Mobile incorporates a primary key into each record to identify it in the database. Although we investigated the use of formal UUIDv4s as per RFC 4122, interactions between our database (SQLite) and the Spatialite geospatial extensions limited us to a short integer identifier (bit length of 2^63, whereas a UUIDv4 has 2^128). Given the need to generate identifiers offline on multiple unconnected devices simultaneously, we produce locally unique identifiers. This identifier was formed by concatenating a '1', the local user ID (five digits), and the UNIX epoch (to milliseconds)."

**Enhanced style**:
> "FAIMS Mobile incorporates a primary key into each record to identify it in the database. We initially investigated using formal UUIDv4s (universally unique identifiers defined in RFC 4122), but interactions between our SQLite database and the Spatialite geospatial extensions limited us to shorter integer identifiers. These have a bit length of 2^63, compared to a UUIDv4's 2^128. To accommodate the need for generating identifiers offline on multiple unconnected devices simultaneously, we developed locally unique identifiers. Each identifier concatenates a '1', the local user ID (five digits), and the UNIX epoch time measured to milliseconds."

The enhanced version:
- Breaks one long sentence into two more manageable ones
- Briefly explains the technical term "UUIDv4" on first use
- Uses more active constructions
- Improves clarity while maintaining technical precision
- Preserves your authoritative voice and technical depth