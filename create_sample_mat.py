import numpy as np
from scipy.io import savemat

# Create synthetic ppm axis
ppm = np.linspace(-5, 5, 1024)

# Create synthetic MRI spectrum (two peaks)
spec = (
    np.exp(-(ppm - 1) ** 2 * 5)
    + np.exp(-(ppm + 2) ** 2 * 3)
)

# Create time vector
t = np.linspace(0, 1, 1024)

# Save to MAT file
data = {
    "ppm": ppm,
    "spec": spec,
    "t": t
}

savemat("test.mat", data)

print("Synthetic test.mat created successfully!")