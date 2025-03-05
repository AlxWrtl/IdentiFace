import face_recognition
import cv2 as cv
import numpy as np
import os
import argparse
import pickle

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
ap.add_argument("-d", "--dataset", required=True,
                help="Path to dataset folder")
ap.add_argument("-c", "--confidence", type=float,
                default=0.5, help="Confidence threshold")
args = vars(ap.parse_args())


def load_faces_from_folder(dataset_path, cache_file="face_encodings.pkl"):
    if os.path.exists(cache_file):
        print("--Loading cached face encodings--")
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    encodings, names = [], []

    for name in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, name)
        if not os.path.isdir(person_path):
            continue

        print(f"--Serialize images of-- {name}")

        for filename in os.listdir(person_path):
            image_path = os.path.join(person_path, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                encodings.append(face_encodings[0])
                names.append(name)

    with open(cache_file, "wb") as f:
        pickle.dump((encodings, names), f)

    return encodings, names


print("--Loading dataset--")
known_encodings, known_names = load_faces_from_folder(args["dataset"])
print(f"{len(known_encodings)} face encodings loaded.")

print("--Processing target image--")
target_image = cv.imread(args["image"])
rgb_target = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(rgb_target, model="cnn")
face_encodings = face_recognition.face_encodings(rgb_target, face_locations)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_encodings, face_encoding, tolerance=1.05 - args["confidence"])
    name = "Unknow"

    face_distances = face_recognition.face_distance(
        known_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)

    if matches[best_match_index]:
        name = known_names[best_match_index]

    confidence = (1 - face_distances[best_match_index]) * 100
    text = f"{name}: {confidence:.2f}%"

    cv.rectangle(target_image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv.putText(target_image, text, (left, top - 10),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv.imshow("Person Found", target_image)
cv.waitKey(0)
