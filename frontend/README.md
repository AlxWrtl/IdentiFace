# Identiface Frontend

## 📌 Description

IdentiFace's frontend is a modern, production-ready web interface built with **React Router, TypeScript, Vite, and Tailwind CSS**. It provides a seamless UI for interacting with the facial recognition system implemented in the backend.

## 🚀 Features

- 🌍 **React Router** for seamless navigation
- 🎨 **Tailwind CSS** for styling
- ⚡️ **Vite** for fast development and HMR (Hot Module Replacement)
- 🏗 **ShadCN** for ready-to-use UI components
- 🔍 **ESLint** for code quality and consistency
- 🐳 **Docker** for containerized deployment

---

## 🛠 Installation

### 1️⃣ Clone the project

```bash
git clone https://github.com/AlxWrtl/IdentiFace.git
cd IdentiFace/frontend
```

### 2️⃣ Install dependencies

```bash
pnpm install
```

If you don't have `pnpm`, install it globally:

```bash
npm install -g pnpm
```

### 3️⃣ Start the development server

```bash
pnpm dev
```

Your application will be available at `http://localhost:5173`.

---

## 📂 Project Structure

```plaintext
frontend/
│── app/                   # Application source code
│── public/                # Static assets
│── node_modules/          # Dependencies (excluded from repo)
│── .gitignore             # Git ignore file
│── .dockerignore          # Docker ignore file
│── Dockerfile             # Docker setup
│── package.json           # Project metadata & dependencies
│── pnpm-lock.yaml         # Dependency lockfile
│── tsconfig.json          # TypeScript configuration
│── vite.config.ts         # Vite configuration
│── react-router.config.ts # React Router configuration
└── README.md              # Project documentation
```

---

## 🚀 Deployment

### 🐳 Docker Deployment

To build and run using Docker:

```bash
docker build -t identiface-frontend .

# Run the container
docker run -p 3000:3000 identiface-frontend
```

The frontend can be deployed to any platform that supports Docker, including:

- AWS ECS
- Google Cloud Run
- Azure Container Apps
- Digital Ocean App Platform
- Fly.io
- Railway

### DIY Deployment

If you want to deploy manually, build the project first:

```bash
pnpm build
```

Then deploy the `dist/` folder to your preferred hosting service.

---

## 🎨 Styling

This project uses [Tailwind CSS](https://tailwindcss.com/) for styling. You can customize styles in `tailwind.config.ts`.

We also use [ShadCN](https://ui.shadcn.com/) for UI components. To add a new component:

```bash
pnpm dlx shadcn@latest add <component-name>
```

For example, to add a button component:

```bash
pnpm dlx shadcn@latest add button
```

---

## 🔍 Code Quality

To ensure code quality and maintainability, we use **ESLint**. Run the following command to check for linting issues:

```bash
pnpm lint
```

You can also fix issues automatically with:

```bash
pnpm lint --fix
```

---

## 📌 Author

Developed by **Alexandre Wertel** for the **IdentiFace** project.

Built with ❤️ using React Router, Tailwind CSS, and Vite.
