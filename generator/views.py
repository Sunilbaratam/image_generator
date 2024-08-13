

from django.shortcuts import render
from .tasks import generate_image
from .models import GeneratedImage

def generate_images_view(request):
    prompts = [
        "A red flying dog",
        "A piano ninja",
        "A footballer kid"
    ]

    for prompt in prompts:
        print(prompt)
        task = generate_image(prompt)
        print(task)
        
    
    return render(request, 'generator/status.html')

def images_view(request):
    
    # images = GeneratedImage.objects.all()
    images = GeneratedImage.objects.order_by('-created_at')[:3]
    return render(request, 'generator/images.html', {'images': images})

# def all_images_view(request):
    
#     all_images = GeneratedImage.objects.all()
#     # images = GeneratedImage.objects.order_by('-created_at')[:3]
#     return render(request, 'generator/images.html', {'all_images': all_images})

