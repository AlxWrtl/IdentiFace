import face_recognition
import os
from db_models import session, save_encoding
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to dataset folder")
args = vars(ap.parse_args())

DATASET_PATH = args["dataset"]


def train_faces(dataset_path):
    for name in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, name)
        if not os.path.isdir(person_path):
            continue

        print(f"-- Saving encode for -- {name}")

        for filename in os.listdir(person_path):
            image_path = os.path.join(person_path, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            if not face_encodings:
                print(f"-- No faces detected -- {filename} in {person_path}")
                continue

            save_encoding(name, face_encodings[0])


print("Training done")
train_faces(DATASET_PATH)
