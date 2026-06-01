from .fast_preview import FastPreviewImage
from .api_text_node import ApiTextOutputNode

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "FastPreviewImage": FastPreviewImage,
    "ApiTextOutputNode": ApiTextOutputNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FastPreviewImage": "Fast Preview & Optimize",
    "ApiTextOutputNode": "➡️ API Text Output"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
