import os
import random
import string
import numpy as np
from PIL import Image
import folder_paths

class FastPreviewImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "image_format": (["webp", "jpeg", "png"], {"default": "webp"}),
                "quality": ("INT", {"default": 80, "min": 1, "max": 100}),
            }
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = "save_images"
    CATEGORY = "image"

    def save_images(self, images, image_format="webp", quality=80):
        results = list()
        file_sizes = list()
        temp_dir = folder_paths.get_temp_directory()

        for batch_number, image in enumerate(images):
            # Convert tensor to PIL Image
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            if image_format == "jpeg" and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Generate random 8-character string for the prefix
            prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            filename = f"fast_preview_{prefix}_{batch_number}.{image_format}"
            file_path = os.path.join(temp_dir, filename)

            # Determine compression kwargs based on format
            kwargs = {}
            if image_format == "webp":
                kwargs = {"quality": quality, "method": 2}
            elif image_format == "jpeg":
                kwargs = {"quality": quality, "optimize": True}
            elif image_format == "png":
                kwargs = {"compress_level": max(0, min(9, int((100 - quality) / 10)))}

            # Save the image
            img.save(file_path, **kwargs)

            # Calculate file size
            size_in_bytes = os.path.getsize(file_path)
            if size_in_bytes < 1024 * 1024:
                size_str = f"{size_in_bytes / 1024:.2f} KB"
            else:
                size_str = f"{size_in_bytes / (1024 * 1024):.2f} MB"

            file_sizes.append(size_str)
            results.append({
                "filename": filename,
                "subfolder": "",
                "type": "temp"
            })

        return {"ui": {"images": results, "file_sizes": file_sizes}}
