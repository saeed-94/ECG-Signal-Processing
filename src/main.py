"""
Main script for ECG signal processing pipeline.
Integrates data loading, filtering, analysis, and visualization.
"""

from load_data import load_ecg_record
from filtering import bandpass_filter
from analysis import compute_rr_intervals, compute_hr, compute_snr
from visualization import plot_ecg, plot_rr, plot_hr

# === Step 1: Load ECG Record ===
print("=== ECG Signal Processing Started ===")
record, ann = load_ecg_record("data/100")
signal = record.p_signal[:, 0]  # Select channel 1
fs = record.fs                 # Sampling frequency

# === Step 2: Apply Bandpass Filter ===
filtered_signal = bandpass_filter(signal, fs)

# === Step 3: Visualization of Filtering Effect ===
plot_ecg(signal, filtered_signal, ann)

# === Step 4: Compute RR and HR Intervals ===
rr_intervals = compute_rr_intervals(ann, fs)
plot_rr(rr_intervals)
hr_intervals = compute_hr(rr_intervals)
plot_hr(hr_intervals)

# === Step 5: Compute SNR and Noise Reduction ===
snr_before, snr_after, snr_gain, noise_reduction = compute_snr(
    signal, filtered_signal, fs)

# === Step 6: Print Final Metrics ===
print("\n=== Results Summary ===")
print(f"SNR Before Filtering: {snr_before:.2f} dB")
print(f"SNR After Filtering:  {snr_after:.2f} dB")
print(f"SNR Gain:             {snr_gain:.2f} dB")
print(f"Noise Reduction:      {noise_reduction:.2f}%")
