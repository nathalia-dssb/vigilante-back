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
 
    return probs.tolist()

source = analyze("https://storage.googleapis.com/violence_images_bucket/violence_dataset/dataset/NV_977.mp4_frame0.jpg", dicti.siniestro)
results= dict(zip(dicti.siniestro, source[0]))

print(results)

def first():
    peace = 0
    violence = 0
    for key, value in results.items():
        if key == 'Violenta' or key == "Hostil" or key == "Daño" or key == "Persona" or key == "Personas":
            violence += value
        
        if key == "Pacifico" or key == "Tranquilo"  or key == "Persona" or key == "Personas":
            peace += value


    if(violence > peace):
        return True
    
    return False


print(first())

def second():
    if first() == True:
        stat = analyze("https://storage.googleapis.com/violence_images_bucket/violence_dataset/dataset/NV_977.mp4_frame0.jpg", dicti.crimenes)
        results= dict(zip(dicti.crimenes, stat[0]))

        max_key = ''
        max_value = -1
        for key, value in results.items():

            if value > max_value:
                max_key = key
                max_value = value

        return "Es un " + max_key
    else:
        return "No es un siniestro"
    

print(second())