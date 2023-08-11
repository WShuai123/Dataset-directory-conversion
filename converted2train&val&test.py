import os
import shutil
import random

def split_dataset(original_dataset_dir, train_dir, val_dir, test_dir, train_ratio=0.6, val_ratio=0.2):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    class_folders = os.listdir(original_dataset_dir)

    for class_folder in class_folders:
        class_path = os.path.join(original_dataset_dir, class_folder)
        if os.path.isdir(class_path):
            class_images = os.listdir(class_path)
            num_images = len(class_images)
            num_train = int(num_images * train_ratio)
            num_val = int(num_images * val_ratio)

            random.shuffle(class_images)

            train_images = class_images[:num_train]
            val_images = class_images[num_train:num_train+num_val]
            test_images = class_images[num_train+num_val:]

            train_class_dir = os.path.join(train_dir, class_folder)
            os.makedirs(train_class_dir, exist_ok=True)

            val_class_dir = os.path.join(val_dir, class_folder)
            os.makedirs(val_class_dir, exist_ok=True)

            test_class_dir = os.path.join(test_dir, class_folder)
            os.makedirs(test_class_dir, exist_ok=True)

            for image in train_images:
                src = os.path.join(class_path, image)
                dst = os.path.join(train_class_dir, image)
                shutil.copyfile(src, dst)

            for image in val_images:
                src = os.path.join(class_path, image)
                dst = os.path.join(val_class_dir, image)
                shutil.copyfile(src, dst)

            for image in test_images:
                src = os.path.join(class_path, image)
                dst = os.path.join(test_class_dir, image)
                shutil.copyfile(src, dst)

original_dataset_dir = "/path/to/your/original/dataset"
train_dir = "/path/to/your/train/dataset"
val_dir = "/path/to/your/val/dataset"
test_dir = "/path/to/your/test/dataset"
split_dataset(original_dataset_dir, train_dir, val_dir, test_dir)

print("Dataset split and organized into train, validation, and test folders.")
