from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
from torchvision import transforms
import pytorch_lightning as pl

class FlowerDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        self.image_paths = [os.path.join(image_dir, file) for file in os.listdir(image_dir) 
                            if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image

class TrainDataModule(pl.LightningDataModule):

    def __init__(self, image_dir, batch_size=32):

        super(TrainDataModule, self).__init__()
        self.image_dir = image_dir
        self.batch_size = batch_size
        self.transform = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(degrees=15),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    def setup(self, stage=None):
        self.dataset = FlowerDataset(image_dir=self.image_dir, transform=self.transform)

    def train_dataloader(self):
        # DataLoader for training set
        return DataLoader(self.dataset, batch_size=self.batch_size, shuffle=True)

