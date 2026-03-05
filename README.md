# MRI Synthetic ML Pipeline

A lightweight machine learning pipeline that simulates MRI/MRS spectroscopy data processing. This project demonstrates signal preprocessing, frequency shifting using FFT-based techniques, and visualization of spectral transformations.

The repository is designed to mimic a simplified MRI spectroscopy workflow without relying on real patient data. Synthetic spectra are generated so that the pipeline can run anywhere while still illustrating signal processing concepts used in medical imaging research.

---

## Project Overview

Magnetic Resonance Spectroscopy (MRS) analyzes chemical signals captured during MRI scans. These signals appear as spectral peaks representing metabolite concentrations.

Before meaningful analysis can occur, spectra often require preprocessing steps such as frequency correction.

This project demonstrates that workflow by:

- Generating synthetic spectroscopy data
- Applying frequency-domain preprocessing
- Visualizing spectral transformations
- Structuring the code as a reusable ML-style pipeline

The goal is to provide a simple, reproducible example of signal processing techniques used in MRI spectroscopy analysis.

---

## Features

- Synthetic MRI/MRS spectrum generation
- FFT-based spectrum frequency shifting
- Signal preprocessing utilities
- Spectrum visualization with Matplotlib
- Modular Python code structure
- Fully reproducible pipeline without medical datasets

---

## Tech Stack

- Python
- NumPy
- SciPy
- Matplotlib
- MATLAB `.mat` file handling

---

### File Descriptions

create_sample_mat.py  
Generates synthetic MRI spectroscopy data and saves it as a `.mat` file.

preprocessing.py  
Contains signal processing functions including FFT-based frequency shifting.

shift_and_plot.py  
Loads spectroscopy data, applies frequency shifts, and visualizes the results.

train_model.py  
Reserved for machine learning experiments and model development using extracted spectral features.

---

## Running the Project

Step 1 — Generate Synthetic Data

python create_sample_mat.py

This will generate a sample spectroscopy dataset

test.mat

---

Step 2 — Run Spectrum Processing

python shift_and_plot.py --file test.mat --hzshift 10

This command will:

- Load the spectrum from the `.mat` file
- Apply a frequency shift
- Display a visualization comparing the original and shifted spectra

---

## Example Output

The script generates a plot showing two curves:

Original Spectrum  
Shifted Spectrum  

The shifted spectrum demonstrates how frequency correction alters spectral peak positions.


<img width="1920" height="1019" alt="mri-spectrum2" src="https://github.com/user-attachments/assets/845b0e07-2923-44ee-9997-c7b3900f48f6" />
<img width="1920" height="1001" alt="mri-spectrum1" src="https://github.com/user-attachments/assets/ea028ec6-0d79-4ed9-a9df-9e36a8d924b0" />


---

## Why Synthetic Data?

Real MRI spectroscopy datasets are typically restricted due to privacy regulations and data governance policies.

To ensure the project remains reproducible and accessible, synthetic spectra are generated that mimic real metabolite peak structures while avoiding the use of protected medical data.

This allows anyone to run and experiment with the pipeline without requiring access to clinical datasets.

---

