# ComfyUI Fast Preview

A lightweight, highly optimized custom node for ComfyUI that compresses and previews images directly from the volatile `/temp` directory. This node minimizes payload size for downstream integrations (like Flow Worker APIs) while displaying the image file size in KB/MB directly on the ComfyUI node interface.

## Features
- **Fast Conversion:** Prioritizes conversion speed (e.g., WebP `method=2`).
- **Supports Multiple Formats:** WEBP, JPEG, and PNG.
- **Quality Control:** Integer slider from 1 to 100.
- **No Clutter:** Saves entirely to ComfyUI's temporary folder, preventing disk bloat. Behaves exactly like the core `Preview Image` node.
- **On-Node File Size:** Dynamically injects a UI text display on the node to show the resulting file size (KB/MB).

## Installation

### Via ComfyUI Manager (Coming Soon)
Search for `ComfyUI Fast Preview` in the ComfyUI Manager and click Install.

### Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
```bash
git clone https://github.com/AabhasTech/ComfyUI_Fast_Preview.git
```
3. Restart ComfyUI.

## Usage
Add the node via `image -> Fast Preview & Optimize`.
Connect an image output to the node, select your format and quality, and run the prompt!