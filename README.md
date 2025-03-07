# IDENTIFACE

## 📌 Description

IdentiFace is a facial recognition system built with OpenCV, dlib, and the face_recognition library. This project enables:

- Face Detection & Recognition: Identify and recognize faces in images.
- Facial Data Augmentation: Generate additional variations of face images to enhance model robustness.
- Face Identification: Compare an input image with stored face encodings in a database.

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

### 🔍 1️⃣  Facial Data Augmentation

Generate image variations to improve facial recognition accuracy.

If you don't have enough images, you can run this script to expand your dataset:

```bash
python3 FaceDataAugmentation.py -d <Images_Dataset_Path>
```

Example:

```bash
python3 FaceDataAugmentation.py -d /path/to/your/images
```

This will create 5 augmented variations of each image found in `Augmented_Images/../`.

### 📈 2️⃣ Import Data into Your Database

Run the `save_trained_faces.py` script with a dataset of known faces:

```bash
cd db
python3 save_trained_faces.py -d <Images_Dataset_Path>
```

Example:

```bash
cd db
python3 save_trained_faces.py -d ../Augmented_Images
```

### 📈 3️⃣ Face Detection and Recognition

Run the `whoIsIt.py` script with an input image:

```bash
cd ..
python3 whoIsIt.py -i <Path_to_Image>
```

Example:

```bash
cd ..
python3 whoIsIt.py -i sample_image.jpeg
```

The script will automatically retrieve the dataset from the database.

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
