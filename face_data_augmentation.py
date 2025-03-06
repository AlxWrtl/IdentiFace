import os
import cv2 as cv
import albumentations as A
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to dataset folder")
args = vars(ap.parse_args())

transform = A.Compose([
    A.Resize(height=300, width=300, p=1.0),
    A.RandomBrightnessContrast(
        brightness_limit=0.2, contrast_limit=0.2, p=0.5),
    A.ToGray(p=0.2),
    A.GaussianBlur(p=0.3),
    A.HorizontalFlip(p=0.5),
    A.Rotate(limit=15, p=0.5),
    A.RandomScale(scale_limit=0.1, p=0.4),
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1,
                       rotate_limit=10, p=0.5),
])

def augment_face(image_path, output_dir, num_variations=5):
    image = cv.imread(image_path)
    if image is None:
        print(f"Not charging {image_path}")
        return

    base_name = os.path.splitext(os.path.basename(image_path))[0]

    for i in range(num_variations):
        augmented = transform(image=image)['image']
        output_path = os.path.join(output_dir, f"{base_name}_aug_{i}.jpg")
        cv.imwrite(output_path, augmented)

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
augment_dataset(dataset_dir, augmented_dir, num_variations=5)
print("Finish !")