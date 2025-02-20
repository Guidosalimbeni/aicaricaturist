# Pix2Pix Caricature Generation

This project implements a Pix2Pix model for generating caricatures from face images. The model is trained on paired face-caricature images and can generate caricature-style images from input face images.

## Setup

1. Upload the notebook to your GitHub repository
2. Open the notebook in Google Colab
3. Connect to your Google Drive (the notebook will prompt for this)
4. Ensure your face-caricature image pairs are in the correct directory: `caricature Project Diffusion/paired_caricature`
   - Face images should be named as `XXX_f.png` (e.g., `001_f.png`)
   - Corresponding caricature images should be named as `XXX_c.png` (e.g., `001_c.png`)
   - All images should be 512x512 PNG format

## Training

The notebook implements:

- Data loading and preprocessing for paired face-caricature images
- Data augmentation with:
  - Random horizontal flipping
  - Random translations (±10% of image size)
- Pix2Pix model with:
  - U-Net generator architecture
  - PatchGAN discriminator
  - L1 loss + adversarial loss
- Automatic checkpointing every 20 epochs
- Model weights saved to Google Drive

## Inference

After training, you can generate caricatures from new face images using the provided inference code:

```python
checkpoint_path = '/content/drive/MyDrive/caricature_checkpoints/ckpt_epoch_199'
generated_caricature = generate_caricature('path_to_face_image.png', checkpoint_path)
plt.imshow(generated_caricature)
plt.axis('off')
plt.show()
```

## Requirements

- TensorFlow
- TensorFlow Addons
- NumPy
- Matplotlib

The notebook will automatically install all required packages.
