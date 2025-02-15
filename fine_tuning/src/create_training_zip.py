import json
import os
import zipfile
from pathlib import Path

# Get the script's directory
script_dir = Path(__file__).parent
# Load the JSON file
json_path = script_dir.parent / "data/template_carton.json"
images_dir = script_dir.parent / "data/cartoon"
output_zip = script_dir.parent / "data/training_data_cartoon.zip"

def create_training_zip():
    # Ensure we're working with absolute paths
    json_path_abs = json_path.resolve()
    images_dir_abs = images_dir.resolve()
    output_zip_abs = output_zip.resolve()
    
    # Load captions from JSON
    with open(json_path_abs, 'r') as f:
        data = json.load(f)
    
    # Create temporary directory for text files
    temp_txt_dir = script_dir.parent / "data/temp_txt"
    temp_txt_dir.mkdir(exist_ok=True)
    
    try:
        # Create text files for each image
        for image_data in data['images']:
            filename = image_data['filename']
            caption = image_data['caption']
            
            # Create text file with same name as image but .txt extension
            txt_filename = Path(filename).stem + '.txt'
            txt_path = temp_txt_dir / txt_filename
            
            with open(txt_path, 'w') as f:
                f.write(caption)
        
        # Create zip file containing both images and text files
        with zipfile.ZipFile(output_zip_abs, 'w') as zf:
            # Add images
            for image_data in data['images']:
                image_path = images_dir_abs / image_data['filename']
                if image_path.exists():
                    zf.write(image_path, image_path.name)
                else:
                    print(f"Warning: Image {image_path.name} not found")
            
            # Add text files
            for txt_file in temp_txt_dir.glob('*.txt'):
                zf.write(txt_file, txt_file.name)
        
        print(f"Created training zip file at: {output_zip_abs}")
        
    finally:
        # Clean up temporary text files
        for txt_file in temp_txt_dir.glob('*.txt'):
            txt_file.unlink()
        temp_txt_dir.rmdir()

if __name__ == "__main__":
    create_training_zip()
