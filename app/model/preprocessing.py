import torch
import torchvision.transforms as transforms
from PIL import Image

from .constanst import device

def image_loader(image_name: str, size:list) -> torch.Tensor:
    image = Image.open(image_name)
    loader = transforms.Compose([
        transforms.Resize((size[1]//2, size[0]//2)),
        transforms.ToTensor()
    ])

    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)

def preprocessing(source_file:str, style_file:str, size:list):
    style_img = image_loader(f'uploaded_photos/{style_file}.jpg', size)
    source_img = image_loader(f'uploaded_photos/{source_file}.jpg', size)
    
    return source_img, style_img

if __name__ == "__main__":
    print(type(image_loader('../uploaded_photos/style_3.jpg')))