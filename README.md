# IDENTIFACE

## 📌 Description

**IdentiFace** is a facial recognition system built with **OpenCV, dlib, and face_recognition** for the backend and **React Router, TypeScript, and Tailwind CSS** for the frontend.

This project provides:

- 🎭 **Facial Data Augmentation**: Generates enhanced variations of face images to improve model accuracy and generalization.
- 🔍 **Face Identification & Database Management**: Stores and retrieves face encodings using an SQLite database.
- 🧠 **Face Detection & Recognition**: Identifies faces using deep learning-based encodings.

The project is divided into two parts:

- **Backend**: Handles face recognition models, data storage, and image processing.
- **Frontend**: Web interface to interact with the recognition system.

---

## 🚀 Global Installation

### 1️⃣ Clone the project

```bash
git clone https://github.com/AlxWrtl/IdentiFace.git
cd IdentiFace
```

### 2️⃣ Install the Backend

```bash
cd backend
uv venv --python 3.10 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 3️⃣ Install the Frontend

```bash
cd ../frontend
pnpm install
```

If `pnpm` is not installed, install it globally:

```bash
npm install -g pnpm
```

### 4️⃣ Run the Project in Development Mode

#### 🌍 Start the Backend

```bash
cd backend
source .venv/bin/activate
python3 whoIsIt.py
```

#### 🎨 Start the Frontend

```bash
cd frontend
pnpm dev
```

The interface will be available at `http://localhost:5173`.

---

## 📂 Project Structure

```plaintext
IdentiFace/
│── backend/                        # Backend (Python, OpenCV, SQLite)
│   ├── db/                         # Database files
│   ├── models/                     # Pre-trained models
│   ├── face_data_augmentation.py   # Data augmentation
│   ├── who_is_it.py                # Detection & recognition
│   ├── README.md                   # Backend documentation
│── frontend/                       # Frontend (React, TypeScript, TailwindCSS)
│   ├── app/                        # Source code
│   ├── public/                     # Static assets
│   ├── package.json                # Dependencies
│   ├── README.md                   # Frontend documentation
└── README.md                       # Global documentation (this file)
```

---

## 🚀 Deployment

### 🐳 Docker Deployment

Both the backend and frontend can be containerized and deployed on cloud platforms supporting Docker.

#### 🔹 Build and Run the Backend

```bash
cd backend
docker build -t identiface-backend .
docker run -p 5000:5000 identiface-backend
```

#### 🔹 Build and Run the Frontend

```bash
cd frontend
docker build -t identiface-frontend .
docker run -p 3000:3000 identiface-frontend
```

These containers can be deployed on AWS, Google Cloud Run, Azure, DigitalOcean, Fly.io, Railway, etc.

---

## 🛠 Technologies Used

### 📌 Backend

- **Python 3.10**
- **OpenCV** → Image processing
- **Dlib** → Face detection
- **Face Recognition** → Face encoding & recognition
- **SQLite** → Lightweight database

### 📌 Frontend

- **React Router** → Client-side navigation
- **TypeScript** → Static typing
- **Vite** → Fast development
- **TailwindCSS** → Modern styling
- **ShadCN** → UI components
- **ESLint** → Code quality enforcement

---

## 🔥 Author

Developed by **Alexandre Wertel**.

Built with ❤️ using Python, OpenCV, and React.
