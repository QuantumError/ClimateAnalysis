import os
import requests
import zipfile
import io

# Define the folder relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, "..", "data")
os.makedirs(data_folder, exist_ok=True)  # create folder if it doesn't exist

# Public Jena Climate ZIP URL
zip_url = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip"

print("Downloading dataset…")
r = requests.get(zip_url)
r.raise_for_status()

print("Extracting CSV to /data…")
with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    for file_info in z.infolist():
        if file_info.filename.lower().endswith(".csv"):
            # Build full path for extraction
            extracted_path = os.path.join(data_folder, os.path.basename(file_info.filename))
            with open(extracted_path, "wb") as f:
                f.write(z.read(file_info.filename))
            print("Extracted:", extracted_path)

print("Done!")
