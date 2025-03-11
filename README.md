# IDENTIFACE

## 📌 Description

IdentiFace is a facial recognition system built with OpenCV, dlib, and the face_recognition library. This project enables:

- **Facial Data Augmentation**: Generates enhanced variations of face images to improve recognition accuracy and model generalization.
- **Face Identification & Database Management**: Stores and retrieves face encodings from an SQLite database for efficient and  fast identification.
- **Face Detection & Recognition**: Detects and identifies faces in images using deep learning-based face encodings.


---

## 🚀 Installation

### 1️⃣ Clone the project

```bash
git clone https://github.com/AlxWrtl/IdentiFace.git
cd IdentiFace
```

### 2️⃣ Create a virtual environment with `uv`

```bash
uv venv --python 3.10 .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## 📂 Project Structure

```plaintext
IdentiFace/
│── faceDataAugmentation.py                         # Facial data augmentation script
│── identify_face.py                                # Identify faces in an image
│── whoIsIt.py                                      # Main face recognition script
│── save_trained_faces.py                           # Script to save trained face encodings
│── requirements.txt                                # List of dependencies
│── db/                                             # Database-related files
│   ├── db_models.py                                # Database models for storing face encodings
│   └── save_trained_faces.py                       # Script for saving faces to the database
│── models/                                         # Pre-trained deep learning models for face detection
│   ├── deploy.prototxt                             # Model configuration file
│   └── res10_300x300_ssd_iter_140000.caffemodel    # Pre-trained face detection model
│── .venv/                                          # Virtual environment (excluded from the repo)
└── README.md                                       # Project documentation
```

---

## 🎯 Usage

### 🔍 0️⃣  Facial Data Organization

Your dataset should be structured as follows:

```plaintext
/data
│── name1/
│   └── photo.jpg
│── name2/
│   └── photo.jpg
│── name3/
│   └── photo.jpg
```

Each subfolder represents a person, and the images inside are used for facial augmentation and training the recognition system.

### 🔍 1️⃣  Facial Data Augmentation

Generate image variations to improve facial recognition accuracy.

If you don't have enough images in the Facial Data Organization step, you can run this script to expand your dataset:

```bash
python3 FaceDataAugmentation.py -d <Images_Dataset_Path>
```

Example:

```bash
python3 FaceDataAugmentation.py -d /path/to/your/dataset_images
```

This will create 20 augmented variations of each image found in `Augmented_Images/`.

### 📈 2️⃣ Import Data into Your Database

Run the save_trained_faces.py script with a dataset of known faces to import them into an SQLite database.

```bash
cd db
python3 save_trained_faces.py -d <Images_Dataset_Path>
```

Example:

```bash
cd db
python3 save_trained_faces.py -d ../Augmented_Images
```

This script scans the dataset folder, detects faces in images, extracts their encodings, and stores them in faces.db. Each encoding is linked to a name and saved as a binary object for quick retrieval during recognition.

### 📈 3️⃣ Face Detection and Recognition

Run the whoIsIt.py script with an input image of a face you want to recognize based on the dataset stored in SQLite.

```bash
cd ..
python3 whoIsIt.py -i <Path_to_Image>
```

Example:

```bash
cd ..
python3 whoIsIt.py -i sample_image.jpeg
```

This script loads known face encodings from faces.db, detects faces in the input image, and compares them to identify matches. It displays the recognized name, confidence score, and the detected emotion.

---

## 🛠 Main Dependencies

- **albumentations** → Image augmentation
- **dlib** → Face detection
- **face-recognition** → Face encoding and recognition
- **face-recognition-models** → Pre-trained models for recognition
- **imutils** → Image manipulation tools
- **numpy** → Mathematical computations
- **opencv-contrib-python** → Image processing
- **opencv-python-headless** → OpenCV without GUI support
- **pillow** → Image manipulation
- **pyyaml** → YAML file management
- **scipy** → Scientific computing
- **setuptools** → Package management tool
- **sqlalchemy** → Database management
- **deepface** → Face analysis (emotion, age, gender, race)

---

## 💡 Note

If `face-recognition-models` causes an issue, install it with:

```bash
uv pip install --force-reinstall git+https://github.com/ageitgey/face_recognition_models
```

---

## 🔥 Author

Alexandre Wertel
