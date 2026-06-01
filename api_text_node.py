class ApiTextOutputNode:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    # Tells ComfyUI's API wrapper that this node yields valid execution data
    OUTPUT_NODE = True
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "send_text_to_api"
    CATEGORY = "Fast Preview"

    def send_text_to_api(self, text):
        text_value = str(text)
        print(f"[Fast Preview] Sending text string to API payload: {text_value}")
        return {"ui": {"text": [text_value]}, "result": (text_value,)}
