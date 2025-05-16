# Photometric_Analysis_of_Centaurs
Photometric analysis of Centaurs using ZTF and SAAO data. Includes rotation period detection, lightcurve modeling, and activity searches via PSF and shift-stack methods. Results were presented at LPSC and AAS.

## Introduction

Centaurs are small solar system bodies with orbits between Jupiter and Neptune, exhibiting both asteroidand comet-like traits. Their orbits are unstable, lasting only a few million years due to gravitational interactions with giant planets. Close encounters with Jupiter and Saturn can shrink their semi-major axes, increasing solar heating and triggering comet-like activity. Many eventually become Jupiter Family Comets (JFCs) through these orbital shifts. We present a photometric study of Centaurs using ZTF data from SNAPS (Trilling et al. 2023) and new observations from the SAAO 1.9m telescope and the TTT 0.8m telescope. Our analysis includes rotation period determinations, including one previously unreported.

## Project Overview & Steps

This project followed the workflow below:

1. **Data Collection**
   - Acquired lightcurvedata from ZTF and image data from SAAO.
   - Downloaded both photometric time-series and stacked FITS images.
2. **Lightcurve & Period Analysis**
   - Plotted lightcurves of multiple objects.
   - Applied Lomb-Scargle periodograms to search for rotational signals.
   - Identified best-fit periods and phase-folded the lightcurves.
3. **Cometary Activity Search**
   - Stacked images using shift-and-stack methods to align moving targets.
   - Performed PSF analysis to compare target profiles to field stars.
   - Visually and statistically evaluated coma/tail signatures.
4. **Results & Interpretation**
   - Summarized results in tables and plots.
   - Compared findings to known Jupiter Family Comets.
   - Prepared and presented posters at LPSC and AAS.

---

## Repository Structure 
<pre> Photometric_Analysis_of_Centaurs/
  ├── Code/
  │ ├── Flux_Contour/
  │ │ └── radial_contour.py
  │ ├── Folded_Lightcurve/
  │ │ └── folded_lightcurves.ipynb
  │ ├── Lightcurve_Generation/
  │ │ └── lightcurve.ipynb
  │ ├── Lombscargle_Periodogram/
  │ │ └── lombscargle.ipynb
  │ └── Shift_Stack/
  │ │ └── stacking_median.py
  ├── Data/
  │ ├── FITS_Files/ # Raw and stacked FITS data
  │ └── SNAPS_Data/ # Raw and processed ZTF data
  ├── plots/ 
  │ ├── lightcurves/ # Lightcurve plots per object 
  │ ├── periodograms/ # Periodogram outputs 
  │ └── activity/ # Coma detection results and stacked images 
  ├── results/ 
  │ ├── summary_table.csv # Summary of derived periods and other parameters 
  │ └── poster/ # LPSC and AAS posters (PDFs) 
  ├── LICENSE 
  ├── README.md 
  └── requirements.txt # Python package dependencies 
</pre>
