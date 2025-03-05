import json
import os
from pathlib import Path
import replicate

def load_config():
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def train_flux_lora():
    # Load configuration
    config = load_config()
    
    # Set Replicate API token as environment variable
    os.environ["REPLICATE_API_TOKEN"] = config["replicate_api_token"]
    
    # Use the raw GitHub URL for the training data
    training_data_url = "https://raw.githubusercontent.com/Guidosalimbeni/aicaricaturist/main/fine_tuning/data/training_data_cartoon_drawing.zip"
    print(f"Using training data from: {training_data_url}")
    
    # Create the training using the uploaded file URL
    training = replicate.trainings.create(
        # The destination should be your model on Replicate
        destination="guidosalimbeni/cartoon-drawing-flux-1",
        
        # The Flux trainer model version
        version="ostris/flux-dev-lora-trainer:b6af14222e6bd9be257cbc1ea4afda3cd0503e1133083b9d1de0364d8568e6ef",
        
        input={
            # Required parameters
            "input_images": training_data_url,
            "trigger_word": "CRTDRWFLX01",  # Custom trigger word for the concept
            
            # Training parameters
            "steps": 1000,
            "lora_rank": 12, # 16
            "learning_rate": 0.0002,
            "batch_size": 1,
            "resolution": "512,768", #1024
            
            # We have our own captions, so disable autocaption
            "autocaption": False,
            
            # Optional parameters for better training
            "caption_dropout_rate": 0.05,  # Helps prevent overfitting
            "optimizer": "adamw8bit",
            
            # Weights & Biases integration (if token provided)
            "wandb_api_key": config.get("wandb_api_key"),
            "wandb_project": "flux_train_replicate",
            "wandb_save_interval": 100,
            "wandb_sample_interval": 100,
            
            # HuggingFace integration (if token provided)
            "hf_token": config.get("huggingface_token"),
            "hf_repo_id": "Guido/cartoon-drawing-flux-1",
            
            # Performance settings
            "cache_latents_to_disk": False,
            "gradient_checkpointing": False,
        },
    )
    
    # Get the training URL and convert it to web interface URL
    api_url = training.urls['get']
    # Convert API URL to web interface URL
    # From: https://api.replicate.com/v1/predictions/[id]
    # To:   https://replicate.com/p/[id]
    training_id = api_url.split('/')[-1]
    web_url = f"https://replicate.com/p/{training_id}"
    
    print(f"Training started! You can monitor it at: {web_url}")
    print("\nIMPORTANT: The training will continue on Replicate's servers.")
    print("Visit the URL above to monitor progress and get the results.")
    print("\nTraining parameters:")
    print(f"- Model destination: guidosalimbeni/cartoon-flux-3")
    print(f"- Trigger word: CRTDRWFLX01")
    print(f"- Training steps: 1000")
    print(f"- LoRA rank: 12")

if __name__ == "__main__":
    train_flux_lora()
