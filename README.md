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
  │ ├── stacking_median.py  # Shift-and-stack images using median combine for activity detection
  │ ├── folded_lightcurves.ipynb  # Plots phase-folded lightcurves using derived rotation periods
  │ ├── lightcurve.ipynb  # Generates raw lightcurves from ZTF photometric data
  │ ├── lombscargle.ipynb  # Performs Lomb-Scargle periodogram analysis to find rotation periods
  │ └── radial_contour.py  # Analyzes radial profiles and contours to assess cometary activity
  ├── Data/
  │ ├── FITS_Files/ # Raw and stacked FITS data
  │ └── SNAPS_Data/ # Raw and processed ZTF data
  ├── Plots/ 
  │ ├── Countour_and_Radial/  # Radial and contour plots for Chiron and star
  │ ├── Folded_lightcurves/  # Folded lightcurve plots for each object
  │ ├── Lightcurves/  # Lightcurve plots for each object
  │ ├── Lombscargle_Periodograms/  # Periodogram outputs 
  │ └── Stacked_Images/  # Stacked images for Chiron and star
  ├── results/ 
  │ ├── summary_table.csv # Summary of derived periods and other parameters 
  │ └── poster/ # LPSC and AAS posters (PDFs) 
  ├── LICENSE 
  ├── README.md 
  └── requirements.txt # Python package dependencies 
</pre>

---

## Key Features

- **Rotational Period Detection** using Lomb-Scargle method  
- **Activity Analysis** through stacking and PSF comparison  
- **Multi-source Observations** combining ZTF and SAAO datasets  
- **Conference-Ready**: Presented at LPSC and AAS  

---

## Requirements (Python)
- `numpy`, `pandas`, `matplotlib`
- `astropy`, `scipy`, `photutils`, `sep`, `imageio`
  
Install packages with:

```bash
pip install -r requirements.txt
```
---

## Related Presentations

- 56th Lunar and Planetary Science Conference (LPSC)
- 245th American Astronomical Society (AAS)

Posters are in Results/Posters/.

---

## Author

**Emma Babula**  
Bachelor of Arts in Astronomy, Lehigh University  
[LinkedIn](www.linkedin.com/in/emma-babula-8357211bb) | [GitHub](https://github.com/emmababula)

---

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
You may share this work with attribution but may not modify or use it commercially.
