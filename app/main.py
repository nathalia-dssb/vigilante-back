from typing import Union

from fastapi import FastAPI

from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API working"}

@app.get("/image")
def send_to_ML():
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    url = "https://media.elobservador.com.uy/p/6a17614f5f40709a696ae194c3d8337a/adjuntos/362/imagenes/100/562/0100562428/1000x0/smart/whatsapp-image-2024-11-03-at-120220-pmjpeg.jpeg"
    image = Image.open(requests.get(url, stream=True).raw)

    inputs = processor(text=["pelea de gallos", "pelea de personas", "ratas", "gatos", "conflicto", "tranquilidad", "calma", "convivencia", "destruccion de propiedad"], images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities