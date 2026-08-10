import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Illustrative/Hypothetical Dataset
# This is NOT experimental SMA data.
# ---------------------------------------------------------

temperature = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

recovery_strain = np.array([
    0.5, 0.8, 1.2, 2.0, 3.1,
    4.2, 4.8, 4.5, 3.9, 3.2
])

# Calculate average recovery strain
average_strain = np.mean(recovery_strain)

# Find maximum recovery strain
maximum_strain = np.max(recovery_strain)

# Find minimum recovery strain
minimum_strain = np.min(recovery_strain)

# Display results
print("Illustrative/Hypothetical Dataset")
print("NOT experimental SMA data.")
print("-----------------------------------")

print("Temperature (°C):", temperature)
print("Recovery Strain (%):", recovery_strain)

print("\nAverage Recovery Strain: {:.2f}%".format(average_strain))
print("Maximum Recovery Strain: {:.2f}%".format(maximum_strain))
print("Minimum Recovery Strain: {:.2f}%".format(minimum_strain))

# Create graph
plt.figure(figsize=(8, 5))

plt.plot(
    temperature,
    recovery_strain,
    marker='o',
    linestyle='-'
)

plt.title("Temperature vs Recovery Strain\n"
          "Illustrative/Hypothetical Dataset")

plt.xlabel("Temperature (°C)")
plt.ylabel("Recovery Strain (%)")

plt.grid(True)

# Save graph
plt.savefig("temperature_vs_recovery_strain.png", dpi=300)

# Display graph
plt.show()