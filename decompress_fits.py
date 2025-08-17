from astropy.io import fits
import matplotlib.pyplot as plt
import os
import numpy as np

# Folder containing your .fits.fz files
input_folder = r"C:\Users\COSMAN\Desktop\my_data"

# Folder to save uncompressed FITS files
output_folder = r"C:\Users\COSMAN\Desktop\YOUR FITS"
os.makedirs(output_folder, exist_ok=True)

# Loop over all .fits.fz files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".fits.fz"):
        input_path = os.path.join(input_folder, filename)
        
        # Open compressed FITS
        with fits.open(input_path) as hdul:
            # Save as normal .fits in the new folder
            fits_filename = filename.replace(".fits.fz", ".fits")
            output_path = os.path.join(output_folder, fits_filename)
            hdul.writeto(output_path, overwrite=True)
            
            print(f"Decompressed: {fits_filename} -> {output_folder}")
            
            # Optional: display the image if numeric
            data = hdul[0].data
            if isinstance(data, np.ndarray) and np.issubdtype(data.dtype, np.number):
                plt.imshow(data, cmap='gray', origin='lower')
                plt.colorbar()
                plt.title(fits_filename)
                plt.show()
            else:
                print(f"Skipping display for {fits_filename} (data not numeric)")
