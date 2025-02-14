import json
import replicate
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def train_flux_lora():
    # Load configuration
    config = load_config()
    
    # Set Replicate API token
    replicate.api_token = config["replicate_api_token"]
    
    # Path to the training data zip
    training_data_path = Path(__file__).parent.parent / "data/training_data.zip"
    
    if not training_data_path.exists():
        raise FileNotFoundError(f"Training data not found at {training_data_path}")
    
    # Create the training
    training = replicate.trainings.create(
        # You'll need to create a model on Replicate first and update this
        destination="guidosalimbeni/ballerina-flux",
        
        # Flux trainer model
        version="ostris/flux-dev-lora-trainer:b6af14222e6bd9be257cbc1ea4afda3cd0503e1133083b9d1de0364d8568e6ef",
        
        input={
            # Required parameters
            "input_images": str(training_data_path.resolve()),
            "trigger_word": "SMKRINA",  # Custom trigger word for the concept
            
            # Training parameters
            "steps": 1000,
            "lora_rank": 16,
            "learning_rate": 0.0004,
            "batch_size": 1,
            "resolution": "512,768,1024",
            
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
            "hf_repo_id": "guidosalimbeni/ballerina-flux-lora",
            
            # Performance settings
            "cache_latents_to_disk": False,
            "gradient_checkpointing": False,
        },
    )
    
    print(f"Training started! You can monitor it at: {training.url}")
    
    # Wait for training to complete
    training.wait()
    
    if training.status == "succeeded":
        print(f"Training completed successfully!")
        print(f"Model version: {training.output}")
    else:
        print(f"Training failed with status: {training.status}")
        if training.error:
            print(f"Error: {training.error}")

if __name__ == "__main__":
    train_flux_lora()
