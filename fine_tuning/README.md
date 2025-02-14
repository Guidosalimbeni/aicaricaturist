# Fine-Tuning Pipeline for Caricature Style

This directory contains the implementation for fine-tuning SDXL using LoRA to create caricatures in a specific style.

## Setup

1. Install dependencies:

```bash
pip install -r ../requirements.txt
```

2. Set up your Replicate API token:
   - Get your API token from [replicate.com/account](https://replicate.com/account)
   - Create a `.env` file in the root directory and add:
   ```
   REPLICATE_API_TOKEN=your_token_here
   ```

## Data Preparation

1. Create a `raw` directory in the `data` folder:

```bash
mkdir -p data/raw
```

2. Place your training images in the `data/raw` directory:

   - Support formats: PNG, JPG, JPEG
   - Recommended: 20 images for style training
   - Images will be automatically processed to 1024x1024 PNG format

3. Run the data preparation script:

```bash
python data/prepare_data.py
```

This will:

- Process all images to the required format
- Create a zip file ready for training

## Configuration

Edit `configs/training_config.json` to set your training parameters:

```json
{
  "input_images_path": "path/to/training_images.zip",
  "destination": "your-username/caricature-model",
  "token_string": "CARICATURE",
  "caption_prefix": "a caricature drawing in the style of",
  "train_batch_size": 1,
  "num_train_epochs": 100,
  "learning_rate": 1e-4,
  "validation_prompt": "a caricature drawing in the style of CARICATURE, portrait"
}
```

Key parameters:

- `input_images_path`: Path to your prepared training images zip file
- `destination`: Your Replicate username and model name
- `token_string`: Token to identify your style in prompts
- `caption_prefix`: Prefix for image captions during training

## Training

1. Create your model on Replicate:

```bash
replicate model create your-username/caricature-model
```

2. Start the training:

```bash
python src/train.py
```

3. Monitor training progress:

- The script will provide a URL to monitor training on Replicate
- Training typically takes several hours

## Using the Fine-Tuned Model

After training completes:

1. Your model will be available at `replicate.com/your-username/caricature-model`
2. Use the token string in your prompts: "a caricature drawing in the style of CARICATURE, portrait of a person"

## Notes

- The training process uses SDXL with LoRA for efficient fine-tuning
- Training images should be clear examples of your caricature style
- Avoid background clutter in training images for best results
