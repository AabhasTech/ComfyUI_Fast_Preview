from .fast_preview import FastPreviewImage

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "FastPreviewImage": FastPreviewImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FastPreviewImage": "Fast Preview & Optimize"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
