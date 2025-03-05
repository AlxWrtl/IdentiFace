import argparse
import cv2 as cv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
ap.add_argument("-p", "--prototxt", required=True,
                help="Path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
                help="Path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
                help="Minimum confidence threshold")
args = vars(ap.parse_args())

net = cv.dnn.readNetFromCaffe(args["prototxt"], args["model"])

image = cv.imread(args["image"])
(h, w) = image.shape[:2]
blob = cv.dnn.blobFromImage(
    cv.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

net.setInput(blob)
detections = net.forward()

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > args["confidence"]:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        text = f"{confidence * 100:.2f}%"
        y = max(startY - 10, 10)
        cv.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv.putText(image, text, (startX, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

cv.imshow("found", image)
cv.waitKey(0)
