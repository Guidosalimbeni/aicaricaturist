# Fine-Tuning Stable Diffusion with Flux: A Simple Guide to Creating Your Own AI Art Style

Have you ever wanted to train an AI model on your own art style? In this guide, I'll show you how I created a custom Stable Diffusion model using Flux LoRA, trained on a series of ethereal ballerina images. The process is surprisingly straightforward and the results are impressive.

## The Goal

I wanted to create an AI model that could generate images in a specific style: ethereal, smoke-like ballerinas that blend the human form with abstract elements. The challenge was to capture this unique aesthetic in a way that could be consistently reproduced.

## Prerequisites

Before we begin, you'll need:

- A collection of images in your desired style (10+ recommended)
- A Replicate account (for training)
- A HuggingFace account (for model hosting)
- A Weights & Biases account (for monitoring)

## Step 1: Preparing Your Images and Captions

The quality of your training data is crucial. Here's how to prepare it:

1. **Image Selection**

   - Choose high-quality images that represent your style
   - Ensure consistency in style and theme
   - Aim for at least 10 images (I used 12)

2. **Writing Captions**
   - Create detailed, descriptive captions for each image
   - Focus on visual elements and style
   - Be consistent in your description format

Example caption:

```json
{
  "filename": "001.png",
  "caption": "A swirling, diaphanous cloud of white smoke faintly suggesting the silhouette of a dancer in mid-twirl, with billowing layers resembling a wispy tutu. The human form is barely discernible, requiring a careful eye to notice the graceful pose hidden within the vapor"
}
```

## Step 2: Setting Up the Training Environment

I've created a simple system that automates the entire process. You can find it on GitHub:
[https://github.com/Guidosalimbeni/aicaricaturist](https://github.com/Guidosalimbeni/aicaricaturist)

The repository includes:

1. Scripts to prepare your training data
2. A training script that interfaces with Replicate
3. Clear documentation and examples

## Step 3: Training the Model

The training process is automated and straightforward:

1. **Prepare Your Data**

   ```bash
   python create_training_zip.py
   ```

   This creates a zip file containing your images and captions in the format Replicate expects.

2. **Configure Your Settings**
   Create a config.json with your API tokens:

   ```json
   {
     "replicate_api_token": "your-token",
     "huggingface_token": "your-token",
     "wandb_api_key": "your-token"
   }
   ```

3. **Start Training**
   ```bash
   python train_flux_lora.py
   ```

The script handles everything:

- Uploads your training data
- Configures optimal training parameters
- Starts the training on Replicate's servers
- Provides a URL to monitor progress

## The Training Parameters

I used these optimized settings:

- 1000 training steps
- LoRA rank of 16
- Learning rate of 0.0004
- Custom trigger word "SMKRINA"

Note: Using a unique trigger word (like "SMKRINA" instead of "BALLERINA") helps the model better associate the word with your style.

## Monitoring Progress

The training process is transparent and easy to monitor:

1. Replicate provides a web interface to watch the training
2. Weights & Biases shows detailed training metrics
3. Once complete, the model is automatically uploaded to HuggingFace

## Using Your Trained Model

After training, you can generate images using prompts like:

```
A SMKRINA dancing in a garden
```

The trigger word ("SMKRINA" in my case) activates your trained style, which you can combine with any scene or context.

## Results and Reflections

The process was surprisingly accessible:

- No need for local GPU resources
- Simple, automated workflow
- Clear monitoring and feedback
- Professional-quality results

The entire setup took less than an hour, and training completed in a few hours on Replicate's servers.

## Conclusion

Fine-tuning AI art models has become remarkably accessible. With the right tools and preparation, anyone can create a custom model that captures their unique artistic style. The scripts and process I've shared make it even easier to get started.

Feel free to explore the repository, try it with your own images, and share your results. The world of AI art is becoming more personal and diverse, one fine-tuned model at a time.

---

_All code and documentation mentioned in this article is available on GitHub: [https://github.com/Guidosalimbeni/aicaricaturist](https://github.com/Guidosalimbeni/aicaricaturist)_
