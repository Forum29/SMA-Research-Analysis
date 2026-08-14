# Ni-Ti-Nb Shape Memory Alloy: Strain Recovery Analysis
## What Was Studied
This project investigates how prestrain and prestrain temperature are associated with recovered strain and residual strain in a Ni-Ti-Nb Shape Memory Alloy (SMA).
The project uses experimental data extracted from Fig. 9 of a published Ni-Ti-Nb SMA study and performs a preliminary quantitative analysis using Python.
## What Data Were Extracted
Nine experimental data points were extracted from Fig. 9 under three prestrain levels:
- 1%
- 3%
- 7%
and three prestrain temperatures:
- 253 K
- 263 K
- 273 K
The extracted variables are:
- Prestrain (%)
- Prestrain temperature (K)
- Recovered strain (%)
- Residual strain (%)
The dataset is stored in `Dataset_final.csv`.
The dataset preserves the source figure associated with each observation.
## What Python Analysis Was Performed
The extracted data were analyzed using Python with:
- Pandas for data processing
- Matplotlib for visualization
The analysis:
1. Loaded the extracted experimental dataset.
2. Calculated mean recovered strain for each prestrain level.
3. Calculated mean residual strain for each prestrain level.
4. Examined recovered strain as a function of prestrain temperature.
5. Generated visualizations of the observed relationships.
The main analysis script is:
`sma_analysis.py`
## What Was Found
Within the extracted experimental conditions:
- Mean recovered strain increased with increasing prestrain.
- Mean residual strain also increased with increasing prestrain.
- Recovered strain decreased with increasing prestrain temperature from 253 K to 273 K for all three investigated prestrain levels.
The extracted mean values were:
| Prestrain (%) | Mean recovered strain (%) | Mean residual strain (%) |
|---:|---:|---:|
| 1 | 0.377 | 0.030 |
| 3 | 1.973 | 0.253 |
| 7 | 5.117 | 0.867 |
For example, recovered strain decreased from:
- 0.50% → 0.21% for 1% prestrain
- 2.20% → 1.67% for 3% prestrain
- 5.50% → 4.65% for 7% prestrain
as prestrain temperature increased from 253 K to 273 K.
## Scientific Interpretation
The extracted data indicate that higher prestrain is associated with greater recovered strain, but also with greater residual strain.
This suggests that the increase in recovery with prestrain is accompanied by an increase in residual deformation within the extracted dataset.
The temperature-dependent results indicate a decrease in recovered strain with increasing prestrain temperature across the investigated range.
These findings represent trends within the extracted literature dataset and should not be generalized beyond the experimental conditions represented by the source study.
## Data Limitation
The values were extracted from a published figure rather than obtained through direct laboratory experiments.
Therefore, the dataset may contain digitization or reading uncertainty and represents only the experimental conditions available in the selected source figure.
## Project Status
**In Progress**
The current stage establishes the dataset, preliminary computational analysis, visualizations, and initial interpretation. Further work will expand the analysis and strengthen the quantitative and scientific interpretation.
