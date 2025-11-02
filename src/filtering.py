"""
Module: filtering.py
Description: Provides signal filtering functions using Butterworth filters.
"""

import scipy.signal as scp

def bandpass_filter(signal, fs, lowcut=0.5, highcut=40.0, order=4):
    """
    Applies a 4th-order Butterworth bandpass filter to remove noise from ECG signal.

    Parameters:
        signal (array): Raw ECG signal.
        fs (float): Sampling frequency of the ECG record.
        lowcut (float): Low cutoff frequency (Hz).
        highcut (float): High cutoff frequency (Hz).
        order (int): Filter order (default=4).

    Returns:
        filtered_signal (array): Noise-reduced ECG signal.
    """
    # Design Butterworth bandpass filter
    b, a = scp.butter(order, [lowcut, highcut], btype='band', fs=fs)

    # Apply zero-phase filtering to avoid phase distortion
    filtered_signal = scp.filtfilt(b, a, signal)

    return filtered_signal
