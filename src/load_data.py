"""
Module: load_data.py
Description: Handles loading of ECG signal and annotations from the MIT-BIH database using WFDB library.
"""

import wfdb


def load_ecg_record(path):
    """
    Loads an ECG record and its corresponding annotations.

    Parameters:
        path (str): Path to the ECG record (without file extension).

    Returns:
        record (wfdb.Record): ECG signal record containing sampled data and metadata.
        annotation (wfdb.Annotation): Corresponding annotation file with R-peak markers.
    """
    record = wfdb.rdrecord(path)          # Read raw ECG signal from WFDB file
    # Read annotation file (.atr) containing R-peaks
    annotation = wfdb.rdann(path, 'atr')
    return record, annotation
