import face_recognition
import cv2 as cv
import numpy as np
import argparse
from db.db_models import load_encoding

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
ap.add_argument("-c", "--confidence", type=float,
                default=0.2, help="Confidence threshold")
args = vars(ap.parse_args())


print("-- Load known faces --")
known_encodings, known_names = load_encoding()
print(f"{len(known_encodings)} visages connus chargés.")

print("-- Processing target image --")
target_image = cv.imread(args["image"])
rgb_target = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(rgb_target, model="cnn")
face_encodings = face_recognition.face_encodings(rgb_target, face_locations)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    face_distances = face_recognition.face_distance(
        known_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    matches = face_recognition.compare_faces(
        known_encodings, face_encoding, tolerance=1.05 - args["confidence"])

    name = "Unknown"

    if any(matches):
        name = known_names[best_match_index]

    confidence = (1 - face_distances[best_match_index]) * 100
    text = f"{name}: {confidence:.2f}%" if name != "Unknown" else "Unknown"

    cv.rectangle(target_image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv.putText(target_image, text, (left, top - 10),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


cv.imshow("-- Person Found-- ", target_image)
cv.waitKey(0)
