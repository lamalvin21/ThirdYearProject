---
id: organs-dataset
name: ORGANS Dataset
description: Data extraction pipeline for the ORGANS Pilot
type: Dataset
release-date: 
release-number: 
work-package: 
- WP1
- WP4
pilot:
- ORGANS
licence: TBD
related-component:
- sparql-anything
links:
- https://github.com/polifonia-project/organs-dataset
credits:
- https://github.com/enridaga
- https://github.com/Eline-Duijsens
---
# ORGANS Knowledge Graph
## Abstract
The knowledge graph contains information regarding a specified organ passed in through command line. Entities include the organ's parthood, history and external information. Data regarding the organ has been collected from the dataset as well as external links such as Wikidata and MusicBrainz. The dataset itself is derived from a Dutch organ encyclopedia. The goal of the knowledge graph is to display extensive amounts of data on a particular organ in the dataset. 

## User Instructions
Execution of this software requires installation of [java](https://www.oracle.com/java/technologies/downloads/) and [SPARQL Anything v0.8.1](https://github.com/SPARQL-Anything/sparql.anything/releases).
1. Navigate to project directory and add SPARQL Anything .jar
2. Execute query in appropriate directory:
```
java -jar sparql-anything-0.8.1.jar -q queries/organ-details.sparql --values organ=Part01_001MIDDE --output output/output.ttl
```
(can select any organ from output/organids.json)
3. View resulting knowledge graph in output.ttl in output folder. 

## SPARQL Anything query

### Get details of an organ
Put code of any organ in the --values parameter
```
fx -q queries/organ-details.sparql --values organ=Part01_001MIDDE
```

