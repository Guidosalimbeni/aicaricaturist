import os
import json
from pathlib import Path

# Path to the ballerina folder
images_dir = Path("aicaricaturist/fine_tuning/data/cartoon")

# Get all PNG files
image_files = sorted([f.name for f in images_dir.iterdir() if f.suffix.lower() == '.png'])

# Create template structure
template = {
    "images": [
        {"filename": filename, "caption": ""} 
        for filename in image_files
    ]
}

# Save JSON template in the same directory as images
json_path = images_dir.parent / "template.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(template, f, indent=2)

print(f"Created template at: {json_path}")
print("Please add your captions to this file, then use create_training_files.py to generate the training package")
