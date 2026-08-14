# Ni-Ti-Nb Shape Memory Alloy: Strain Recovery Analysis
## Overview
This project investigates the relationship between prestrain, prestrain temperature, recovered strain, and residual strain in a Ni-Ti-Nb Shape Memory Alloy (SMA).
The project uses experimental data extracted from published research literature and analyzes the extracted data using Python.
## Research Question
How do prestrain and prestrain temperature affect recovered strain and residual strain in Ni-Ti-Nb Shape Memory Alloys?
## Objectives
- Investigate the effect of prestrain on recovered strain.
- Investigate the effect of prestrain on residual strain.
- Investigate the relationship between prestrain temperature and recovered strain.
- Organize experimental data extracted from published research.
- Analyze the extracted data using Python.
- Identify trends in shape-recovery behavior within the studied experimental conditions.
## Research Background
Shape Memory Alloys (SMAs) are smart materials capable of recovering a previously deformed shape under appropriate thermomechanical conditions.
The extent of shape recovery and residual deformation can depend on the material's deformation history and temperature conditions.
This project focuses on extracted experimental data from a Ni-Ti-Nb SMA study to examine how prestrain and prestrain temperature are associated with recovered strain and residual strain.
## Dataset
The current dataset contains 9 experimental data points extracted from Fig. 9 of a published Ni-Ti-Nb SMA study.
The dataset includes:
- Prestrain (%)
- Prestrain temperature (K)
- Recovered strain (%)
- Residual strain (%)
The dataset is stored in:
`Dataset_final.csv`
Each observation is linked to its corresponding figure and experimental condition in the dataset.
## Methodology
1. Identify relevant experimental research literature.
2. Extract experimental data from published figures.
3. Organize the extracted values into a structured CSV dataset.
4. Process and analyze the dataset using Python.
5. Calculate mean recovered and residual strain for different prestrain levels.
6. Visualize the relationship between recovered strain, prestrain, and prestrain temperature.
7. Examine trends within the extracted experimental conditions.
8. Interpret the observations while considering the limitations of data extracted from published figures.
## Tools & Technologies
- Python
- Pandas
- Matplotlib
- GitHub
- Visual Studio Code
## Current Analysis
The current analysis investigates:
- Recovered strain at different prestrain levels.
- Residual strain at different prestrain levels.
- The relationship between prestrain temperature and recovered strain.
- Preliminary trends in the extracted Ni-Ti-Nb SMA data.
The extracted dataset contains three prestrain levels:
- 1%
- 3%
- 7%
and three prestrain temperatures:
- 253 K
- 263 K
- 273 K
## Preliminary Findings
The extracted data show that mean recovered strain increases with increasing prestrain.
The mean recovered strain is approximately:
| Prestrain (%) | Mean recovered strain (%) | Mean residual strain (%) |
|---:|---:|---:|
| 1 | 0.377 | 0.030 |
| 3 | 1.973 | 0.253 |
| 7 | 5.117 | 0.867 |





The extracted data also show that residual strain increases with increasing prestrain.
Within the extracted temperature range of 253–273 K, recovered strain decreases with increasing prestrain temperature for each of the three prestrain levels.
These observations describe trends within the extracted dataset and should not be generalized beyond the experimental conditions represented in the source data.
## Project Status
**In Progress**
### Completed
- Literature identification
- Experimental data extraction
- Dataset creation
- Data organization
- Preliminary Python analysis
- Initial data visualization
- Preliminary interpretation
### Next Steps
- Expand the experimental dataset
- Perform deeper quantitative analysis
- Analyze residual strain in greater detail
- Compare the effects of prestrain and prestrain temperature
- Develop additional visualizations
- Compare experimental conditions
- Develop a more detailed scientific interpretation
- Formulate final conclusions
## Limitations
The current dataset is based on experimental data extracted from published figures rather than experiments performed directly in the laboratory.
Therefore, the extracted values may contain digitization and reading uncertainty.
The current dataset contains only 9 extracted observations from one figure of a published study. The observed trends should therefore be interpreted as preliminary and should not be generalized beyond the studied conditions.
## Future Work
Future work will involve expanding the dataset using additional experimental conditions and relevant published studies, performing deeper quantitative analysis, and investigating the relationship between prestrain, temperature, shape recovery, and residual strain.
The expanded analysis may provide a stronger basis for comparing experimental conditions and identifying trends in Ni-Ti-Nb SMA behavior.
## Data Source
The experimental data used in this project were extracted from Fig. 9 of the Ni-Ti-Nb SMA study used as the primary data source.
Full bibliographic information for the source study will be provided here.
## Author
**Forum**
B.Tech — Robotics & Automation
Research interests:
- Smart Materials
- Shape Memory Alloys
- Materials Science
- Chemical Kinetics
- Chemical Thermodynamics
