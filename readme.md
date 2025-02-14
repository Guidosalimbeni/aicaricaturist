# AI Caricaturist

A comprehensive implementation of a diffusion model fine-tuned to produce caricatures in a specific style from photos. This project includes fine-tuning code using Replicate's API, a ComfyUI workflow for the generation pipeline, and deployment code.

## Project Structure

```
aicaricaturist/
├── fine_tuning/           # Fine-tuning implementation
│   ├── src/              # Source code for training
│   ├── configs/          # Training configurations
│   └── data/             # Data preparation utilities
├── comfyui_workflow/     # ComfyUI pipeline (TBD)
│   ├── workflows/        # JSON workflow definitions
│   └── assets/           # Additional assets
└── replicate_deployment/ # Deployment code (TBD)
    ├── src/             # Deployment implementation
    └── tests/           # Testing utilities
```

## Components

### 1. Fine-Tuning Module

- Implementation of SDXL LoRA fine-tuning
- Data preparation utilities for training images
- Detailed instructions in [fine_tuning/README.md](fine_tuning/README.md)

### 2. ComfyUI Workflow (Coming Soon)

- Custom workflow for caricature generation
- Integration with fine-tuned model
- Pose estimation and IP-Adapter nodes

### 3. Replicate Deployment (Coming Soon)

- API endpoint implementation
- Integration tests
- Deployment configuration

## Getting Started

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Follow the setup instructions in each module's README

## Current Status

- ✅ Fine-tuning implementation complete
- 🚧 ComfyUI workflow integration (pending)
- 🚧 Replicate deployment (pending)

## License

MIT License - see LICENSE file for details
