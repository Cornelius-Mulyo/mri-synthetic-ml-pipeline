import argparse
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

from preprocessing import shift_spectrum_frequency, magnitude


def load_mat_clean(file_path):
    raw = loadmat(file_path)
    return {k: v for k, v in raw.items() if not k.startswith("__")}


def main():

    parser = argparse.ArgumentParser(description="Shift MRI spectrum and plot result")

    parser.add_argument("--file", required=True, help="Path to .mat file")
    parser.add_argument("--hzshift", type=float, required=True, help="Frequency shift in Hz")

    args = parser.parse_args()

    data = load_mat_clean(args.file)

    ppm = data["ppm"].squeeze()
    spec = data["spec"].squeeze()
    t = data["t"].squeeze()

    shifted = shift_spectrum_frequency(spec, args.hzshift, t)

    plt.figure(figsize=(10, 5))

    plt.plot(ppm, magnitude(spec), label="Original Spectrum")
    plt.plot(ppm, magnitude(shifted), "--", label=f"Shifted ({args.hzshift} Hz)")

    plt.title("Original vs Shifted Spectrum")
    plt.xlabel("Chemical Shift (ppm)")
    plt.ylabel("Magnitude")

    plt.grid(True)
    plt.legend()

    plt.gca().invert_xaxis()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()