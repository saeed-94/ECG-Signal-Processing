"""
Module: visualization.py
Description: Handles visualization of ECG signal, RR intervals, and HR trends.
"""

import matplotlib.pyplot as plt


def plot_ecg(signal, filtered_signal, annotations):
    """
    Plots raw and filtered ECG signals along with R-peaks.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(signal[:2000], label='Raw Signal')
    plt.plot(filtered_signal[:2000], label='Filtered Signal', color='orange')
    plt.scatter(annotations.sample[annotations.sample < 2000],
                filtered_signal[annotations.sample[annotations.sample < 2000]],
                color='red', marker='*', label='R-peaks')
    plt.title("ECG Signal Filtering Result")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_rr(rr_intervals):
    """
    Plots RR intervals over time.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(rr_intervals[:2000], color='blue')
    plt.title("RR Intervals")
    plt.xlabel("Samples")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.show()


def plot_hr(hr_intervals):
    """
    Plots Heart Rate (BPM) variation over time.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(hr_intervals[:2000], color='green')
    plt.title("Heart Rate (HR) Over Time")
    plt.xlabel("Samples")
    plt.ylabel("BPM")
    plt.grid(True)
    plt.show()
