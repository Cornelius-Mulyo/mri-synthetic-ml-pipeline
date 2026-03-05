import numpy as np


def shift_spectrum_frequency(spec, hzshift, t):
    """
    Shift spectrum frequency using time-domain modulation.
    """

    spec = np.asarray(spec)
    t = np.asarray(t)

    if spec.shape[0] != len(t):
        raise ValueError("Time vector length must match spectrum length")

    if np.allclose(hzshift, 0):
        return spec

    # reshape to 2D
    spec = spec.reshape(len(t), -1)

    # IFFT to time domain
    fid = np.fft.ifft(np.fft.ifftshift(spec, axes=0), axis=0)

    # Apply frequency shift
    phase = np.exp(-1j * 2 * np.pi * hzshift * t)

    for i in range(fid.shape[1]):
        fid[:, i] *= phase

    # Back to frequency domain
    spec_shifted = np.fft.fftshift(np.fft.fft(fid, axis=0), axes=0)

    return spec_shifted.squeeze()


def magnitude(spec):
    """Return magnitude spectrum."""
    return np.abs(spec)