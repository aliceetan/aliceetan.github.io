import os
import json

# Path to your photography folder
PHOTO_DIR = "assets/images/photography"

# Initialize dictionary
photos_dict = {}

# Loop through subdirectories
for category in os.listdir(PHOTO_DIR):
    category_path = os.path.join(PHOTO_DIR, category)
    if os.path.isdir(category_path):
        # List all files (images) in the category
        images = [f"{category}/{img}" for img in os.listdir(category_path)
                  if img.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))]
        photos_dict[category] = images

# Output JSON file
with open(os.path.join(PHOTO_DIR, "photos.json"), "w") as f:
    json.dump(photos_dict, f, indent=2)

print("photos.json generated successfully!")
