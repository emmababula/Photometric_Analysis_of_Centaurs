import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.ndimage import map_coordinates, gaussian_filter

def calculate_centroid(image, x, y, radius=5, precision=3):
    """
    Calculate the centroid of the image within a specified radius around (x, y).
    
    Parameters:
    - image (2D np.array): The image array.
    - x, y (float): Approximate center coordinates.
    - radius (int): Radius around (x, y) to calculate the centroid.
    - precision (int): Number of decimal places to round the centroid.
    
    Returns:
    - (centroid_x, centroid_y): Calculated centroid coordinates rounded to specified precision.
    """
    y_min = max(int(y) - radius, 0)
    y_max = min(int(y) + radius + 1, image.shape[0])
    x_min = max(int(x) - radius, 0)
    x_max = min(int(x) + radius + 1, image.shape[1])
    
    sub_image = image[y_min:y_max, x_min:x_max]
    y_indices, x_indices = np.indices(sub_image.shape)
    
    # Calculate intensity-weighted centroid
    total_intensity = sub_image.sum()
    centroid_x = (x_indices * sub_image).sum() / total_intensity + x_min
    centroid_y = (y_indices * sub_image).sum() / total_intensity + y_min
    
    # Round centroid to specified precision
    centroid_x = round(centroid_x, precision)
    centroid_y = round(centroid_y, precision)
    
    return centroid_x, centroid_y

def radial_profile(image, center_x, center_y, max_radius, bin_size=0.5):
    """
    Calculate the radial profile of an image from a specified subpixel center point.
    
    Parameters:
    - image (2D np.array): The image array.
    - center_x, center_y (float): Subpixel coordinates of the center point.
    - max_radius (float): The maximum radius to consider.
    - bin_size (float): The width of each radial bin in pixels.
    
    Returns:
    - radii (np.array): Array of radial distances.
    - profile (np.array): Radial profile values.
    """
    radii = np.arange(0, max_radius, bin_size)
    profile = np.zeros(len(radii) - 1)
    
    # Calculate the distance of each pixel from the center
    y, x = np.indices(image.shape)
    r = np.sqrt((x - center_x)**2 + (y - center_y)**2)

    # Calculate mean intensity in each radial bin
    for i in range(len(radii) - 1):
        annulus_mask = (r >= radii[i]) & (r < radii[i + 1])
        if np.any(annulus_mask):
            profile[i] = image[annulus_mask].mean()
    
    # Bin centers for plotting
    bin_centers = (radii[:-1] + radii[1:]) / 2
    return bin_centers, profile

def contour_plot(image, center_x, center_y, zoom_radius=20, save_path=None):
    """
    Create a contour plot of the image around a specified center point.
    
    Parameters:
    - image (2D np.array): The image array.
    - center_x, center_y (float): Coordinates of the center point.
    - zoom_radius (int): Radius of the area to zoom in on for the contour plot.
    - save_path (str, optional): File path to save the contour plot.
    """

    x_min = max(int(center_x) - zoom_radius, 0)
    x_max = min(int(center_x) + zoom_radius, image.shape[1])
    y_min = max(int(center_y) - zoom_radius, 0)
    y_max = min(int(center_y) + zoom_radius, image.shape[0])

    zoomed_image = image[y_min:y_max, x_min:x_max]
    plt.figure(figsize=(6, 6))
    plt.contour(zoomed_image, levels=15, cmap="viridis", origin="lower", 
                extent=(x_min, x_max, y_min, y_max))
    plt.colorbar(label="Flux")
    plt.scatter(center_x, center_y, color='red', marker='x', label="Calculated Center")
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.legend()
    plt.title("Contour Plot")

    if save_path:
        plt.savefig(save_path, dpi=300)
        print(f"Saved contour plot to: {save_path}")

    plt.show()

def analyze_psf(file_path, approx_center_x, approx_center_y, label='object', max_radius=20, bin_size=0.5):
    """
    Analyze the PSF of an object by creating a radial profile and contour plot.
    
    Parameters:
    - file_path (str): Path to the FITS file.
    - approx_center_x, approx_center_y (float): Approximate coordinates for the center.
    - max_radius (float): Maximum radius for the radial profile.
    - bin_size (float): Bin size for the radial profile.
    """

    with fits.open(file_path) as hdul:
        image_data = hdul[0].data
    
    # Calculate a centroid near the approximate center
    centroid_x, centroid_y = calculate_centroid(image_data, approx_center_x, approx_center_y, radius=5)
    print(f"Calculated Centroid: ({centroid_x}, {centroid_y})")
    
    radii, profile = radial_profile(image_data, centroid_x, centroid_y, max_radius, bin_size)
    plt.figure(figsize=(8, 6))
    plt.scatter(radii, profile, marker='o', color="blue")
    plt.xlabel("Radius (pixels)")
    plt.ylabel("Intensity")
    plt.title("Radial Profile")
    plt.grid(True)

    radial_plot_path = f"Github/Contour Plots/{label}_radial_profile.png"
    plt.savefig(radial_plot_path, dpi=300)
    plt.show()
    
    contour_plot(image_data, centroid_x, centroid_y, zoom_radius=max_radius, 
                 save_path=f"Github/Contour Plots/{label}_contour.png")

# Fits files
star_fits = "Image Analysis\Chiron Stacking\star_stacked_1031_r.fits"
centaur_fits = "Image Analysis\Chiron Stacking\stacked_1031_r.fits"

# Approximate coordinates from stacked images
star_coord = (194.972, 57.2407)  # Star center
centaur_coord = (161.954, 174.814)  # Centaur center

# Analyze PSF for the star
print("Star PSF Analysis")
analyze_psf(star_fits, *star_coord, label='star', max_radius=20)

# Analyze PSF for the Centaur
print("Centaur PSF Analysis")
analyze_psf(centaur_fits, *centaur_coord, label='chiron', max_radius=20)
