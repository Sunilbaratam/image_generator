

import requests
from celery import shared_task
from django.core.files.base import ContentFile
from .models import GeneratedImage
import uuid
import os
import base64



MEDIA_ROOT = 'media/images/'  

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = 'sk-Ax6rZtnOInXdfJcUfRJhYyIKi0vg9fNLp3HPWvUwpVVEigSa'

if api_key is None:
    raise Exception("Missing Stability API key.")


@shared_task
def generate_image(prompt):
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    print(response)
    if response.status_code == 200:
        
        data = response.json()
        image_filename = f"{uuid.uuid4()}.png"  
        image_path = os.path.join(MEDIA_ROOT, image_filename)

        
        os.makedirs(MEDIA_ROOT, exist_ok=True)  
        
        for i, image in enumerate(data["artifacts"]):
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(image["base64"]))

      
        image_url = f'/media/images/{image_filename}'
        GeneratedImage.objects.create(prompt=prompt,image_url=image_url)
        return image_url
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")




