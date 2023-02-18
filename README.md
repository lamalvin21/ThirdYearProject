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

## List of SPARQL Anything queries and usage

### List DOCX samples
```
fx -q queries/list-samples.sparql
```
save list to a SPARQL Result Set file:
```
fx -q queries/list-samples.sparql -o list-samples.xml -f XML
```

### Convert DOCX samples (FX/RDF)
```
fx -q queries/convert-samples.sparql -v filename=001MIDDE.docx -o data/001MIDDE.ttl -f TTL
fx -q queries/convert-samples.sparql -v filename=002GRAVH.docx -o data/002GRAVH.ttl -f TTL
fx -q queries/convert-samples.sparql -v filename=003HAREN.docx -o data/003HAREN.ttl -f TTL
fx -q queries/convert-samples.sparql -v filename=006Lellens.docx -o data/006Lellens.ttl -f TTL
fx -q queries/convert-samples.sparql -v filename=011Vlijmen.docx -o data/011Vlijmen.ttl -f TTL
```
### Extract title and year
```
fx -q queries/nameYear.sparql -i data/list-samples.xml -p "data/?id-titleYear.ttl"
```
### Extract church
```
fx -q queries/church.sparql -i data/list-samples.xml -p "data/?id-church.ttl"
```
### Extract building description
```
fx -q queries/buildingInformation.sparql -i data/list-samples.xml -p "data/?id-building.ttl"
```
Test:
```
fx -q queries/buildingInformation.sparql -v file=001MIDDE.docx -v id=001MIDDE -p data/?id-building.ttl -f TTL
fx -q queries/buildingInformation.sparql -v file=002GRAVH.docx -v id=002GRAVH -p data/?id-building.ttl -f TTL
fx -q queries/buildingInformation.sparql -v file=003HAREN.docx -v id=003HAREN -p data/?id-building.ttl -f TTL
fx -q queries/buildingInformation.sparql -v file=006Lellens.docx -v id=006Lellens -p data/?id-building.ttl -f TTL
fx -q queries/buildingInformation.sparql -v file=011Vlijmen.docx -v id=011Vlijmen -p data/?id-building.ttl -f TTL
```

### List DOCX documents
```
fx -q queries/list-documents.sparql
```
save list to a SPARQL Result Set file:
```
fx -q queries/list-documents.sparql -o data/list-documents.xml -f XML

### Get details of an organ
Put code of any organ in the --values parameter
```
fx -q queries/organ-details.sparql --values organ=Part01_001MIDDE
```

## Database mappings

title + church -> `pipeorgan`.`instruments`.`name`
building -> ?
year -> ?
