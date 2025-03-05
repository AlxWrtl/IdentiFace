# IDENTIFACE

## 📌 Description

This project implements a facial recognition system using OpenCV, dlib, and the face_recognition library. It allows:

- Detection and recognition of faces in an image.
- Facial data augmentation to improve model robustness.
- Face identification by comparing an image with a database.

---

## 🚀 Installation

### 1️⃣ Clone the project

```bash
git clone https://github.com/AlxWrtl/IdentiFace.git
cd IdentiFace
```

### 2️⃣ Create a virtual environment with `uv`

```bash
uv venv .venv
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
│── identify_face.py            # Identify faces in an image
│── FaceDataAugmentation.py     # Facial data augmentation script
│── Augmented_Images/           # Dataset folder with all augmented images
│── whoIsIt.py                  # Main face recognition script
│── face_encodings.pkl          # Serialize the dataset file to speed up recognition
│── requirements.txt            # List of dependencies
│── .venv/                      # Virtual environment (excluded from the repo)
└── README.md                   # Project documentation
```

---

## 🎯 Usage

### 🔍 1️⃣  Facial Data Augmentation

Generate image variations to improve recognition:

```bash
python3 FaceDataAugmentation.py --d <Images_Dataset_Path>
```

Example:

```bash
python3 FaceDataAugmentation.py --d /path/to/your/images
```

This will create 5 augmented variations of each image found in `Augmented_Images/../`.

### 📈 2️⃣ Face Detection and Recognition

Run the `whoIsIt.py` script with an input image and a dataset of known faces:

```bash
python3 whoIsIt.py --i Your_Photo.jpeg --d Augmented_Images or /path/to/your/images
```

Example:

```bash
python3 whoIsIt.py --i Your_Photo.jpeg --d Augmented_Images 
```
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

---

## 💡 Note

If `face-recognition-models` causes an issue, install it with:

```bash
uv pip install --force-reinstall git+https://github.com/ageitgey/face_recognition_models
```

---

## 🔥 Author

Alexandre Wertel
