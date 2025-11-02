"""
Module: analysis.py
Description: Contains analytical functions for ECG feature extraction and signal quality evaluation.
"""

import numpy as np
from scipy.signal import welch


def compute_rr_intervals(annotations, fs):
    """
    Computes RR intervals from annotation data.

    Parameters:
        annotations (wfdb.Annotation): Annotations containing R-peak sample indices.
        fs (float): Sampling frequency.

    Returns:
        rr_intervals (array): Time intervals between successive R-peaks (seconds).
    """
    return np.diff(annotations.sample) / fs


def compute_hr(rr_intervals):
    """
    Calculates heart rate (HR) in beats per minute from RR intervals.

    Parameters:
        rr_intervals (array): Time differences between R-peaks.

    Returns:
        hr_intervals (array): Heart rate (BPM) derived from RR intervals.
    """
    return 60 / rr_intervals


def band_power(f, Pxx, f_low, f_high):
    """
    Computes power within a specified frequency band.

    Parameters:
        f (array): Frequency axis.
        Pxx (array): Power spectral density (PSD).
        f_low (float): Lower bound of frequency band.
        f_high (float): Upper bound of frequency band.

    Returns:
        power (float): Integrated power in the given band.
    """
    mask = (f >= f_low) & (f <= f_high)
    return np.trapz(Pxx[mask], f[mask])


def compute_snr(signal, filtered_signal, fs, band=(0.5, 40.0)):
    """
    Estimates Signal-to-Noise Ratio (SNR) improvement after filtering.

    Parameters:
        signal (array): Original ECG signal.
        filtered_signal (array): Filtered ECG signal.
        fs (float): Sampling frequency.
        band (tuple): Frequency range for signal band.

    Returns:
        snr_before (float): SNR before filtering (dB).
        snr_after (float): SNR after filtering (dB).
        snr_gain (float): SNR improvement (dB).
        noise_reduction (float): Percentage reduction in out-of-band noise.
    """
    # Compute Power Spectral Density (PSD) before and after filtering
    f_before, Pxx_before = welch(signal, fs=fs, nperseg=4096)
    f_after,  Pxx_after = welch(filtered_signal, fs=fs, nperseg=4096)

    # Calculate in-band and out-of-band power components
    power_sigband_before = band_power(f_before, Pxx_before, *band)
    power_outband_before = band_power(
        f_before, Pxx_before, 0, band[0]) + band_power(f_before, Pxx_before, band[1], fs/2)
    power_sigband_after = band_power(f_after, Pxx_after, *band)
    power_outband_after = band_power(
        f_after, Pxx_after, 0, band[0]) + band_power(f_after, Pxx_after, band[1], fs/2)

    # Compute SNR and noise reduction
    snr_before = 10 * np.log10(power_sigband_before /
                               (power_outband_before + 1e-12))
    snr_after = 10 * np.log10(power_sigband_after /
                              (power_outband_after + 1e-12))
    snr_gain = snr_after - snr_before
    noise_reduction = 100.0 * \
        (1 - (power_outband_after / (power_outband_before + 1e-12)))

    return snr_before, snr_after, snr_gain, noise_reduction
