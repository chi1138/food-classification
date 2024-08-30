import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder 

transforms1 = transforms.Compose([
    transforms.Resize((256,256)),
    transforms.CenterCrop((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

transforms2 = transforms.Compose([  
    transforms.Resize((256,256)),
    transforms.CenterCrop((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    transforms.RandomHorizontalFlip(p=0.5)
])

full_dataset = ImageFolder('../data/raw/Taiwanese-Food-101', transform=transforms1)

# Define generator and set split size
generator1 = torch.Generator().manual_seed(38)
train_size = int(0.7 * len(full_dataset))
test_size = val_size = (len(full_dataset) - train_size)//2

# Split dataset to train, test, and validation
train_dataset, test_dataset, val_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size, val_size], generator = generator1)

train_dataset.dataset.transform = transforms2

