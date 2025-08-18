import os
from PIL import Image, ImageOps

# List of directories or individual files to process
PATHS = [
    "assets/images/photography/fun",
    "assets/images/photography/travel",
    "assets/images/photography/people",
    "assets/images/portrait.jpg"  # single file
]

# Resize target
MAX_SIZE = (1600, 1600)

def optimize_image(input_path, output_path, size=MAX_SIZE):
    """Optimize a single image, preserving orientation."""
    with Image.open(input_path) as img:
        # Correct rotation using EXIF
        img = ImageOps.exif_transpose(img)

        # Only shrink if larger than target
        if img.width > size[0] or img.height > size[1]:
            img.thumbnail(size)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            img.save(output_path, optimize=True, quality=85)
            print(f"✅ Optimized {input_path} -> {output_path}")
        else:
            print(f"⚪ Skipped (already small): {input_path}")

def process_path(path):
    """Process either a directory or a single file."""
    if os.path.isfile(path):
        optimize_image(path, path)  # overwrite original
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith((".jpg", ".jpeg", ".png")):
                    file_path = os.path.join(root, file)
                    optimize_image(file_path, file_path)  # overwrite original

# Run optimization for all paths
for path in PATHS:
    process_path(path)