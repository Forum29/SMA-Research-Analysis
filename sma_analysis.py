import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset_final.csv")
print("Dataset:")
print(df)
print("\nNumber of experimental points:", len(df))
summary = df.groupby("prestrain_percent")[[
    "recovered_strain_percent",
    "residual_strain_percent"
]].mean()
print("\nMean recovered and residual strain by prestrain:")
print(summary)
for prestrain in sorted(df["prestrain_percent"].unique()):
    subset = df[df["prestrain_percent"] == prestrain]
    plt.plot(
        subset["prestrain_temperature_K"],
        subset["recovered_strain_percent"],
        marker="o",
        label=f"{prestrain}% prestrain"
    )
plt.xlabel("Prestrain temperature (K)")
plt.ylabel("Recovered strain (%)")
plt.title("Recovered strain vs prestrain temperature")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("recovered_strain_vs_temperature.png", dpi=300)
plt.show()
