# Face_Recognizer

## 📌 Description

📌 Description

This project implements a facial recognition system using OpenCV:

Detection and recognition of faces in an image.

Facial data augmentation to improve model robustness.

---

## 🚀 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/AlxWrtl/IdentiFace.git
cd IdentiFace
```

### 2️⃣ Créer un environnement virtuel avec `uv`

```bash
uv venv .venv
source .venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
uv pip install -r requirements.txt
```

---

## 📂 Structure du projet

```
IdentiFace/
│── identify_face.py            # Identify faces in an image
│── FaceDataAugmentation.py     # Facial data augmentation script
│── requirements.txt            # List of dependencies
│── .venv/                      # Virtual environment (excluded from the repo)
└── README.md                   # Project documentation


---

🎯 Usage

🔍 1️⃣ Face Detection

Run the identify_face.py script with an input image and a dataset of known faces:

python3 identify_face.py -i <image_path> -p <prototxt_path> -m <model_path>

Example:

python3 identify_face.py --i Your_Photo.jpeg -p models/deploy.prototxt -m models/res10_300x300_ssd_iter_140000.caffemodel

📈 2️⃣ Facial Data Augmentation

If you want to generate image variations to improve recognition:

python3 FaceDataAugmentation.py --d <Images_Dataset_Path>

Example:

python3 FaceDataAugmentation.py --d /path/to/your/images

This will create 5 augmented variations of each image found in Images/.

🔥 Author

Alexandre Wertel
