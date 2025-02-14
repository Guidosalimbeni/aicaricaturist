import json
import csv
import zipfile
from pathlib import Path

# Paths
data_dir = Path("aicaricaturist/fine_tuning/data")
images_dir = data_dir / "ballerina"
json_path = data_dir / "template_ballerina.json"

# Load the JSON with captions
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create CSV file
csv_path = data_dir / "captions.csv"
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['caption', 'image_file'])
    for img in data['images']:
        if not img['caption']:
            print(f"Warning: Missing caption for {img['filename']}")
        writer.writerow([img['caption'], img['filename']])

# Create zip file
zip_path = data_dir / "training.zip"
with zipfile.ZipFile(zip_path, 'w') as zf:
    # Add images
    for img in data['images']:
        img_path = images_dir / img['filename']
        zf.write(img_path, img_path.name)
    # Add CSV
    zf.write(csv_path, csv_path.name)

print(f"Created training package at: {zip_path}")
print("The zip file contains your images and captions.csv ready for training")
