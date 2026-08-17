import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv",skipinitialspace=True)

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()
print("=" * 60)
print("SMA QUANTITATIVE ANALYSIS")
print("=" * 60)

# ------------------------------------------------------------
# 1. BASIC INFORMATION
# ------------------------------------------------------------

print("\nNumber of observations:", len(df))

# ------------------------------------------------------------
# 2. GROUP MEANS
# ------------------------------------------------------------

summary = df.groupby("prestrain_percent")[
    ["recovered_strain_percent", "residual_strain_percent"]
].mean()

print("\nMean strain by prestrain:")
print(summary.round(3))

# ------------------------------------------------------------
# 3. PERCENTAGE CHANGE
# ------------------------------------------------------------

first_recovered = summary["recovered_strain_percent"].iloc[0]
last_recovered = summary["recovered_strain_percent"].iloc[-1]

first_residual = summary["residual_strain_percent"].iloc[0]
last_residual = summary["residual_strain_percent"].iloc[-1]

recovered_change = (
    (last_recovered - first_recovered)
    / first_recovered
) * 100

residual_change = (
    (last_residual - first_residual)
    / first_residual
) * 100

print("\nRecovered strain percentage increase:")
print(round(recovered_change, 2), "%")

print("\nResidual strain percentage increase:")
print(round(residual_change, 2), "%")

# ------------------------------------------------------------
# 4. CORRELATION
# ------------------------------------------------------------

recovered_corr = df[
    ["prestrain_percent", "recovered_strain_percent"]
].corr().iloc[0, 1]

residual_corr = df[
    ["prestrain_percent", "residual_strain_percent"]
].corr().iloc[0, 1]

print("\nCorrelation between prestrain and recovered strain:")
print(round(recovered_corr, 4))

print("\nCorrelation between prestrain and residual strain:")
print(round(residual_corr, 4))

# ------------------------------------------------------------
# 5. VISUALIZATION
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["prestrain_percent"],
    df["recovered_strain_percent"],
    label="Recovered strain"
)

plt.scatter(
    df["prestrain_percent"],
    df["residual_strain_percent"],
    label="Residual strain"
)

plt.xlabel("Prestrain (%)")
plt.ylabel("Strain (%)")
plt.title("Effect of Prestrain on Recovered and Residual Strain")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "sma_prestrain_quantitative_analysis.png",
    dpi=300
)

plt.show()

print("\nAnalysis completed.")