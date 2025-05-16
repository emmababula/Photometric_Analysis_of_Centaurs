import sep
import numpy as np
from astropy.io import fits
from scipy.ndimage import shift
import matplotlib.pyplot as plt
import os
from matplotlib.colors import LogNorm

fits_directory = 'Fits/20241030+31/20241031/Chiron/r/red'
fits_files = sorted([os.path.join(fits_directory, f) for f in os.listdir(fits_directory) if f.endswith('.fits')])

initial_image_data = fits.getdata(fits_files[0]).astype(np.float32)

# Display first image and click to set initial object position
plt.imshow(initial_image_data, cmap='gray', origin='lower', norm=LogNorm())
plt.title("Click on the object's position")
initial_position = plt.ginput(1)  # Capture click
plt.close()

initial_position = (int(initial_position[0][1]), int(initial_position[0][0]))  # (y, x)

images = []
object_positions = [initial_position]  # Start with clicked position

for i, file in enumerate(fits_files):
    data = fits.getdata(file).astype(np.float32)
    
    # Background subtraction
    bkg = sep.Background(data)
    data_sub = data - bkg
    objects = sep.extract(data_sub, 1.5, err=bkg.globalrms)
    
    # Find object closest to the initial object position
    if i > 0:
        obj = min(objects, key=lambda obj: np.hypot(obj['y'] - initial_position[0], obj['x'] - initial_position[1]))
        object_positions.append((obj['y'], obj['x']))
    images.append(data)

# Set reference position based on the initial object position
ref_y, ref_x = object_positions[0]

# Calculate shifts
shifts = [(ref_y - y, ref_x - x) for y, x in object_positions]

# Apply shifts and stack the aligned images
aligned_images = [shift(img, shift=(dy, dx)) for img, (dy, dx) in zip(images, shifts)]

# Stack the images by taking median
stacked_image = np.median(aligned_images, axis=0)

# Rotate the image by 180 degrees
stacked_rot = np.rot90(stacked_image, 2)

# Save the rotated stacked image to a new FITS file
hdu = fits.PrimaryHDU(stacked_rot)
hdu.writeto(f'Github\star_stacked_1031_r.fits', output_verify='silentfix', overwrite=True)

plt.imshow(stacked_rot, cmap='gray', origin='lower', norm=LogNorm())
plt.colorbar()
plt.title("Stacked Image (Log Scale)")
plt.savefig(f'Github\star_stacked_1031_r.png')
plt.show()
