# ORGANS Knowledge Graph
**6CCS3PRJ Final Year Project**

**Author**: Alvin Lam

**Supervisor**: Dr Alberto Meroño-Peñuela

## Abstract
This knowledge graph focuses on a specific organ, which is passed in through command line. The graph contains entities related to the organ such as, but not limited to, its parthood, historical background and relevant external information. Data in the knowledge graph was obtained from an organ dataset located in the output folder. This dataset was constructed based on a Dutch organ encyclopedia. The goal of the knowledge graph was to provide extensive information about an organ, leveraging linked data from different sources such as [Wikidata](https://www.wikidata.org/wiki/Q1444) and [MusicBrainz](https://musicbrainz.org/instrument/55a37f4f-39a4-45a7-851d-586569985519) to provide a comprehensive solution. The knowledge graph serves as a valuable resource for those involved in the Polifonia project as well as anyone interested in organs.

## User Instructions
Execution of this software requires installation of [java](https://www.oracle.com/java/technologies/downloads/) and [SPARQL Anything v0.8.1](https://github.com/SPARQL-Anything/sparql.anything/releases).
1. Navigate to project directory and add SPARQL Anything .jar file.
2. Execute query in appropriate directory:
```
java -jar sparql-anything-0.8.1.jar -q queries/organ-details.sparql --values organ=Part01_001MIDDE --output output/output.ttl
```
(can select any organ from output/organids.json and replace organ in --values parameter)

3. View resulting knowledge graph in output.ttl in output folder. 

## SPARQL Anything query

### Get details of an organ
Put code of any organ in the --values parameter
```
fx -q queries/organ-details.sparql --values organ=Part01_001MIDDE
```

## Others 

Resources [ontology](https://github.com/polifonia-project/organs-ontology) and [dataset](https://github.com/polifonia-project/organs-dataset) (also in output folder) are from the [Polifonia project](https://github.com/polifonia-project). 

Credit for the provided resources include: [Enrico Daga](https://github.com/enridaga), [Peter van Kranenburg](https://github.com/pvankranenburg), [Eline Duijsens](https://github.com/ElineDuijsens), [Eoin Kearns](https://github.com/EoinKearns), [Fiorela Ciroku](https://github.com/FiorelaCiroku) and [roccotrip](https://github.com/roccotrip).

Contributions and use of repository are welcome. 