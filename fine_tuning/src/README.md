# Fine-Tuning Scripts

This directory contains scripts for preparing and running Flux LoRA fine-tuning on Replicate.

## Scripts Overview

### 1. create_training_zip.py

Creates a training data zip file that follows Replicate's requirements for Flux fine-tuning:

- Takes images from `../data/ballerina/`
- Uses captions from `../data/template_ballerina.json`
- Creates a zip file containing both images and their corresponding caption text files
- Each image's caption is saved in a .txt file with the same name (e.g., 001.png → 001.txt)
- Output: `../data/training_data.zip`

### 2. train_flux_lora.py

Handles the Flux LoRA training process on Replicate:

- Uses the Replicate API to initiate and monitor training
- Configures optimal training parameters
- Supports integration with Weights & Biases for monitoring
- Can automatically upload the trained model to HuggingFace

## Configuration

### config.json

A configuration file (gitignored) that stores API tokens:

```json
{
  "replicate_api_token": "your-replicate-token-here",
  "huggingface_token": "your-huggingface-token-here",
  "wandb_api_key": "your-wandb-key-here"
}
```

## Training Parameters

The training script uses the following optimized parameters:

- Trigger word: "SMKRINA" (unique word unlikely to appear in training data)
- Steps: 1000
- LoRA rank: 16
- Learning rate: 0.0004
- Batch size: 1
- Resolution: "512,768,1024"
- Autocaption: Disabled (using our own captions)
- Caption dropout rate: 0.05
- Optimizer: adamw8bit

## Usage

1. First, prepare the training data:

```bash
python create_training_zip.py
```

2. Update config.json with your API tokens

3. Run the training:

```bash
python train_flux_lora.py
```

The training script will:

- Use the training data directly from GitHub (https://raw.githubusercontent.com/Guidosalimbeni/aicaricaturist/main/fine_tuning/data/training_data.zip)
- Start the training process on Replicate's servers
- Provide a web URL where you can monitor the training progress
- Display the key training parameters being used

The training will continue on Replicate's servers after the script completes. The script will provide a web URL (https://replicate.com/p/[id]) where you can:

- Monitor the training progress
- View training logs
- Get the final model once training is complete
- Access the model on HuggingFace (if configured)

## Using the Trained Model

Once training is complete, you can use the trained model in your prompts by including the trigger word "SMKRINA". This will activate the learned style in your generations.

Example prompt:

```
A SMKRINA dancing in a garden
```

Note: We use "SMKRINA" as the trigger word instead of "BALLERINA" because it's important to use a unique word that doesn't appear in the training data captions. This helps the model better associate the trigger word with the specific style being learned.

## Requirements

Required packages are listed in the root requirements.txt:

- replicate
- python-dotenv
- Pillow
- numpy
- tqdm

### prediction

import Replicate from "replicate";

const replicate = new Replicate({
auth: process.env.REPLICATE_API_TOKEN,
});

const output = await replicate.run(
"guidosalimbeni/cartoon-flux-2:1fe063aab167758c14fab9bdef9f4f67a1721e30718caa31429b6ff7f4aed666",
{
input: {
prompt: "..."
}
}
);
