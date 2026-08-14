# Preliminary Data Analysis
## Dataset
The dataset contains 9 extracted data points from Fig. 9 of the Ni-Ti-Nb SMA study.
The data cover:
- Prestrain levels: 1%, 3%, and 7%
- Prestrain temperatures: 253 K, 263 K, and 273 K
- Recovered strain
- Residual strain
## Preliminary Analysis
The extracted Ni-Ti-Nb SMA data show that increasing prestrain from 1% to 7% is associated with an increase in both recovered strain and residual strain.
The mean recovered strain increases from approximately 0.377% at 1% prestrain to 5.117% at 7% prestrain.
The mean residual strain increases from approximately 0.030% at 1% prestrain to 0.867% at 7% prestrain.
Within the extracted prestrain temperature range of 253–273 K, recovered strain decreases with increasing prestrain temperature for all three prestrain levels.
## Numerical Summary
| Prestrain (%) | Mean recovered strain (%) | Mean residual strain (%) |
|---:|---:|---:|
| 1 | 0.377 | 0.030 |
| 3 | 1.973 | 0.253 |
| 7 | 5.117 | 0.867 |

## Temperature-Dependent Observations
For 1% prestrain, the extracted recovered strain decreases from 0.50% at 253 K to 0.21% at 273 K.
For 3% prestrain, the extracted recovered strain decreases from 2.20% at 253 K to 1.67% at 273 K.
For 7% prestrain, the extracted recovered strain decreases from 5.50% at 253 K to 4.65% at 273 K.
Therefore, within the extracted experimental conditions, recovered strain decreases with increasing prestrain temperature for all three prestrain levels.
## Interpretation
The extracted data indicate that higher prestrain is associated with higher recovered strain.
At the same time, higher prestrain is also associated with higher residual strain.
This indicates that the increase in recovered strain with prestrain is accompanied by an increase in residual deformation within the extracted dataset.
The temperature-dependent results show a decrease in recovered strain with increasing prestrain temperature across the extracted range of 253–273 K.
These observations are based on 9 extracted data points from Fig. 9 and should not be generalized beyond the experimental conditions represented by the source data.
## Python Analysis
The analysis was performed using Python with pandas and matplotlib.
The analysis script is:
`sma_analysis_final.py`
The generated visualization is:
- `effect_of_prestrain_on_strain_recovery.png`
- `recovered_strain_vs_prestrain_graph.png`
## Data Limitations
The values in the dataset were extracted from published figures rather than obtained from direct laboratory measurements.
Consequently, the extracted values may contain digitization or reading uncertainty.
The dataset is preliminary and represents only the experimental conditions available in the selected source figure.
Further analysis will require additional experimental data and comparison with other relevant studies.
