# Image Generator

## Overview

Image Generator is a Django application that leverages the Stability AI Text-to-Image API to generate and display images based on user prompts. It uses Celery for asynchronous task processing and stores generated images in a Django model.

## Features

- Asynchronous image generation using Celery
- Integration with Stability AI Text-to-Image API
- Storage of generated images and metadata in Django model
- User interface to view the latest generated images


### Prerequisites

- Python
- Django
- Celery
- Redis (for Celery)
- Requests library

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sunilbaratam/image_generator.git
   cd image_generator

2. **Run the below command in terminal**
    ```
    python manage.py runserver


### Generate Images

    Visit http://127.0.0.1:8000/generate-images/ to generate new images.

### View Images

    Visit http://127.0.0.1:8000/images/ to view the latest generated images.