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
The knowledge graph contains information regarding a specified organ passed in through command line. Entities include the organ's parthood, history and external information. 

## SPARQL Anything query

### Get details of an organ
Put code of any organ in the --values parameter
```
fx -q queries/organ-details.sparql --values organ=Part01_001MIDDE
```