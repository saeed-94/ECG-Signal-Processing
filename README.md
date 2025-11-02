
# 🫀 ECG Signal Processing and Noise Reduction (MIT-BIH Database)

This project focuses on **processing and analyzing real ECG signals** from the MIT-BIH Arrhythmia Database using **Python**.  
The main goal is to **remove motion and powerline noise**, improve the **signal-to-noise ratio (SNR)**, and compute **heart rate (HR)** variations accurately.

---

## ⚙️ Project Overview

In biomedical signal processing, ECG signals often contain unwanted components such as:
- Baseline wander (motion artifacts)
- Powerline interference (50/60 Hz)
  
To address these, a **4th-order Butterworth bandpass filter (0.5–40 Hz)** was designed and applied to remove these noise sources.  
After filtering, **R-peaks were detected**, **RR-intervals were computed**, and **Heart Rate (HR)** trends were visualized.

---

## 🧩 Tools and Libraries

| Library | Purpose |
|----------|----------|
| `NumPy` | Signal manipulation and numerical computation |
| `SciPy` | Filtering (Butterworth) and spectral analysis (Welch PSD) |
| `Matplotlib` | Visualization of ECG and HR trends |
| `WFDB` | Reading ECG data and annotations from MIT-BIH database |
| `Pandas` | Data handling and calculations |

---

## 🧠 Processing Pipeline

1. **Load ECG Record**  
   Load signal and annotations using the `wfdb` library.

2. **Bandpass Filtering**  
   Apply a 4th-order Butterworth bandpass filter (0.5–40 Hz).

3. **Noise and Power Analysis**  
   Use Welch’s Power Spectral Density (PSD) to estimate in-band and out-band power before and after filtering.

4. **Feature Extraction**  
   Compute RR intervals and convert to HR (beats per minute).

5. **Visualization and Comparison**  
   Plot the original vs. filtered ECG and HR trends.

---

## 📊 Results

### 🎧 Filtered ECG Signal
The following plot shows the original (noisy) and filtered ECG signal with improved clarity of R-peaks.

![Filtered ECG](/results/ecg_filtered_plot.png)

---

### ⏱️ RR-Interval Analysis
The RR-intervals were computed using annotated R-peaks.

![RR Intervals](/results/rr_intervals_plot.png)

---

### ❤️ Heart Rate (HR) Trend
Heart rate variations (BPM) calculated from RR intervals.

![HR Plot](/results/hr_plot.png)

---

## 📈 Quantitative Performance

| Metric | Before Filtering | After Filtering | Improvement |
|:--|:--:|:--:|:--:|
| Signal-band Power (0.5–40 Hz) | 3.41e-02 | 3.35e-02 | – |
| Out-band Power | 2.30e-03 | 4.13e-05 | ↓ 98.2% |
| SNR (dB) | 11.72 | 29.09 | +17.36 dB |

> ✅ The bandpass filter effectively **removed ~98% of out-band noise**,  
> leading to a **17.3 dB increase in SNR** and **significantly improved ECG clarity**.

---

## 📁 Project Structure

```bash
ECG-Signal-Processing/
│
├── src/                          # Source code directory
│   ├── load_data.py              # Load ECG record and annotations (MIT-BIH)
│   ├── filter_signal.py          # Butterworth bandpass filter (0.5–40 Hz)
│   ├── analyze_hr.py             # Compute RR and HR intervals
│   ├── analyze_psd.py            # PSD & SNR analysis using Welch method
│   └── main.py                   # Main execution pipeline
│
├── results/                      # Output plots and analysis results
│   ├── filtered_signal.png       # ECG before & after filtering
│   ├── RR_intervals.png          # RR interval variation plot
│   └── HR_plot.png               # Heart rate (BPM) variation plot
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation


## 🧩 Key Takeaways

- Designed and implemented a **biomedical-grade bandpass filter**  
- Achieved **98% noise suppression** and **17 dB SNR improvement**  
- Accurately computed **RR intervals and heart rate variability (HRV)**  
- Created reproducible visualizations and metrics for clinical signal quality

---

## 📜 License
This project is released under the **MIT License** — feel free to use, modify, and share with attribution.

---

## 👨‍💻 Author
**[Saeed Ghorbani]**  
Biomedical Engineer | Signal Processing & AI Enthusiast  
📧 sa_ghorbani95@yahoo.com  
🌐 GitHub: [github.com/saeed-94](https://github.com/saeed-94)
