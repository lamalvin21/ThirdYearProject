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
# ORGANS Dataset

## SPARQL Anything query

### Get details of an organ
Put code of any organ in the --values parameter
```
fx -q queries/organ-details.sparql --values organ=Part01_001MIDDE
```