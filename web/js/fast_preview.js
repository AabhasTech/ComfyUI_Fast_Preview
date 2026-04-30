import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "Comfy.FastPreviewImage",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "FastPreviewImage") {
            const onExecuted = nodeType.prototype.onExecuted;
            
            nodeType.prototype.onExecuted = function(message) {
                const r = onExecuted ? onExecuted.apply(this, arguments) : undefined;
                
                if (message?.file_sizes) {
                    let widget = this.widgets?.find((w) => w.name === "file_size_display");
                    
                    if (!widget) {
                        const widgetObj = ComfyWidgets["STRING"](this, "file_size_display", ["STRING", { multiline: false }], app);
                        widget = widgetObj.widget || widgetObj;
                        
                        if (widget && widget.inputEl) {
                            widget.inputEl.readOnly = true;
                            widget.inputEl.style.opacity = "0.8";
                            widget.inputEl.style.textAlign = "center";
                        }
                    }
                    
                    if (widget) {
                        widget.value = `Size: ${message.file_sizes.join(" | ")}`;
                    }
                }
                
                return r;
            };
        }
    }
});
