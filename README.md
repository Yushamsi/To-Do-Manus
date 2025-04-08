# To-Do List Application

A modern, full-stack to-do list application built with Flask (backend) and Nuxt.js (frontend), styled with Tailwind CSS. This project was created by Manus as an experimentation using "Vibe Coding" methodology.

![To-Do List App](https://via.placeholder.com/800x400?text=To-Do+List+App)

## 🌐 Live Demo

The application is currently deployed and accessible at:

- **Frontend:** [https://sibbfies.manus.space](https://sibbfies.manus.space)
- **Backend API:** [https://8000-ibf724rj1lqoxiv9qehks-e80c6714.manus.computer](https://8000-ibf724rj1lqoxiv9qehks-e80c6714.manus.computer)

## ✨ Features

- **Task Management:**
  - View all to-do items
  - Add new tasks
  - Mark tasks as complete/incomplete
  - Delete tasks
- **Modern UI:**
  - Clean, responsive design
  - Visual feedback for user interactions
  - Tailwind CSS styling
- **Full-Stack Architecture:**
  - Flask REST API backend
  - Nuxt.js frontend with Composition API
  - API communication using Axios

## 🏗️ Architecture

### Backend (Flask)

- **RESTful API** with the following endpoints:
  - `GET /todos` – Retrieve all to-do items
  - `POST /todos` – Add a new to-do item
  - `PUT /todos/<id>` – Mark an item as complete or update it
  - `DELETE /todos/<id>` – Delete a to-do item
- **In-memory storage** (no database required)
- **CORS enabled** for frontend communication
- **Well-documented code** with comprehensive comments

### Frontend (Nuxt.js)

- **Component Structure:**
  - `AddTodo.vue` - Component for adding new tasks
  - `TodoItem.vue` - Component for displaying individual tasks
  - `index.vue` - Main page component
  - `app.vue` - Root application component
- **Styling:**
  - Tailwind CSS for modern, clean UI
  - Custom color scheme
  - Responsive design for all device sizes
- **State Management:**
  - Vue 3 Composition API
  - Reactive references for state management

## 🛠️ Technology Stack

### Backend
- Python 3.6+
- Flask 3.1.0
- Flask-CORS 5.0.1
- Gunicorn 21.2.0 (for production)

### Frontend
- Nuxt.js 3.7.0
- Vue.js 3 (with Composition API)
- Tailwind CSS 6.8.0
- Axios 1.5.0
- PostCSS 8.4.31

## 🚀 Setup Instructions

### Backend Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application in development mode:
```bash
python app.py
```

The backend will be available at http://localhost:5000

### Frontend Setup

1. Install dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

### Production Build

1. Generate a static build of the frontend:
```bash
npm run generate
```

2. For the backend, use Gunicorn as the WSGI server:
```bash
gunicorn app:app
```

## 📝 Project Structure

```
/
├── app.py                 # Flask backend application
├── app.vue                # Nuxt.js root component
├── AddTodo.vue            # Component for adding new tasks
├── TodoItem.vue           # Component for displaying tasks
├── index.vue              # Main page component
├── nuxt.config.ts         # Nuxt.js configuration
├── package.json           # Frontend dependencies
├── requirements.txt       # Backend dependencies
├── tailwind.config.js     # Tailwind CSS configuration
├── tailwind.css           # Custom CSS styles
├── Procfile               # Production web server configuration
├── PLANNING.md            # Project planning documentation
├── CHANGES.md             # Development change log
└── DEPLOYMENT.md          # Deployment documentation
```

## 📋 Development Process & 🧪 "Vibe Coding" Methodology

The development process adhered to "Vibe Coding" practices, ensuring a structured and efficient workflow. The LLM was guided to plan, execute, and document the project in a systematic manner. This approach resulted in the creation of three key files that served as the foundation for the project's direction and progress:

- **PLANNING.md** - Captures the initial project planning, structure, and objectives, ensuring a clear roadmap for development.
- **CHANGES.md** - Maintains a detailed log of all changes made during development, providing transparency and traceability.
- **DEPLOYMENT.md** - Documents the deployment process and configuration, ensuring a smooth transition to production.

By following this methodology, the project maintained clarity, focus, and alignment with its goals, leveraging the LLM's capabilities to deliver a well-organized and functional application.


## 📄 License

[MIT License](LICENSE)

## 👨‍💻 Created By

This application was created by Manus & Yushamsi as an experimental project using the "Vibe Coding" methodology.
