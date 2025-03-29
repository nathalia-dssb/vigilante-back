from PIL import Image
import requests
import dicti
import re

from transformers import CLIPProcessor, CLIPModel

def analyze(img_url, classes):

    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    url = img_url
    image = Image.open(requests.get(url, stream=True).raw)

    inputs = processor(text=classes, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

    numbers = re.findall(r"[-+]?\d*\.\d+e[-+]?\d+", str(probs))
    cleaned_numbers = [float(num) for num in numbers]

    results= dict(zip(classes, cleaned_numbers))
    return results

analyze("https://storage.googleapis.com/violence_images_bucket/violence_dataset/noviolence/NV_992.mp4_frame115.jpg", dicti.siniestro)