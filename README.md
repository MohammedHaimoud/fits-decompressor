# fits-decompressor
A simple Python script to decompress .fits.fz files into standard FITS format using Astropy.


How to Use decompress_fits.py

Step 1: Install Python

Make sure you have Python 3.8 or newer installed. You can download it from python.org.

Check installation by opening a terminal (Command Prompt) and typing:

python --version



Step 2: Install Required Packages

Open a terminal and install the Python libraries your script needs:

pip install astropy numpy matplotlib


These libraries allow the script to read FITS files, handle arrays, and display images.



Step 3: Prepare Your Files

Create a folder where your compressed .fits.fz files are located.
Example: C:\Users\admin\Desktop\my_data

Create an output folder where the decompressed FITS files will be saved.
Example: C:\Users\admin\Desktop\YOUR FITS



Step 4: Configure the Script

Open decompress_fits.py in a text editor and make sure the folder paths match your setup:

input_folder = r"C:\Users\admin\Desktop\my_data"
output_folder = r"C:\Users\admin\Desktop\YOUR FITS"


Step 5: Run the Script

In the terminal, navigate to the folder containing decompress_fits.py:

cd "C:\Users\admin\Desktop\fits-decompressor"


Then run the script:

python decompress_fits.py



Step 6: Check the Output

After running, all .fits.fz files from input_folder will be decompressed into .fits files in output_folder.

If the FITS files contain numeric image data, the script will display them using Matplotlib. Non-numeric FITS files will be skipped for display.




You now have decompressed FITS files ready for analysis, stacking, or processing with any astronomy software.
