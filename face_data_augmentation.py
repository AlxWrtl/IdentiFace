import os
import cv2 as cv
import albumentations as A
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to dataset folder")
ap.add_argument("-p", "--profile_rate", type=float, default=0.3,
                help="Percentage of images that will undergo profile transformation")
args = vars(ap.parse_args())

transform = A.Sequential([
    A.Resize(height=300, width=300, p=1.0),
    A.OneOf([
        A.RandomBrightnessContrast(
            brightness_limit=0.2, contrast_limit=0.2, p=0.5),
        A.ToGray(p=0.2),
        A.GaussianBlur(p=0.3),
        A.GaussNoise(var_limit=(10, 50), p=0.3),
        A.MotionBlur(blur_limit=3, p=0.2),
        A.CLAHE(clip_limit=2.0, tile_grid_size=(8, 8), p=0.3),
    ], p=0.5),
    A.HorizontalFlip(p=0.5),
    A.OneOf([
        A.Rotate(limit=15, p=0.5),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1,
                           rotate_limit=10, p=0.5),
        A.Affine(shear=(-10, 10), rotate=(-5, 5), p=0.5),
    ], p=0.7),
    A.Perspective(scale=(0.05, 0.15), p=0.3),
])


def augment_face(image_path, output_dir, num_variations=5):
    image = cv.imread(image_path)
    if image is None:
        print(f"Not charging {image_path}")
        return
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    for i in range(num_variations):
        augmented = transform(image=image)['image']

        augmented = cv.cvtColor(augmented, cv.COLOR_RGB2BGR)
        output_file = os.path.join(output_dir, f"{base_name}_aug_{i}.jpg")
        cv.imwrite(output_file, augmented)


def augment_dataset(dataset_path, output_path="augmented_faces", num_variations=5):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for person in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person)
        output_person_path = os.path.join(output_path, person)
        if os.path.isdir(person_path):
            if not os.path.exists(output_person_path):
                os.makedirs(output_person_path)
            for filename in os.listdir(person_path):
                image_path = os.path.join(person_path, filename)
                augment_face(image_path, output_person_path, num_variations)


dataset_dir = (args["dataset"])
augmented_dir = "Augmented_Images"
augment_dataset(dataset_dir, augmented_dir, num_variations=20)
print("Finish !")
