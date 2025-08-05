# Task Manager - Full Stack Application

A complete task management application built with Flask backend and React frontend, featuring task CRUD operations and comment management with pagination.

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask with SQLAlchemy ORM
- **Pattern**: Service-Repository pattern with Blueprints
- **Validation**: Marshmallow schemas
- **Testing**: Pytest with factory_boy
- **Database**: SQLite (development) / PostgreSQL (production ready)

### Frontend (React)
- **Framework**: React 18 with TypeScript
- **UI Library**: Chakra UI for responsive design
- **HTTP Client**: Axios for API communication
- **State Management**: Custom hooks with React Hooks
- **Build Tool**: Create React App

## 📁 Project Structure

```
├── server/                 # Flask Backend
│   ├── app/
│   │   ├── models/         # SQLAlchemy models
│   │   ├── repositories/   # Data access layer
│   │   ├── services/       # Business logic
│   │   ├── schemas/        # Marshmallow validation
│   │   └── routes/         # API endpoints
│   ├── tests/              # Pytest test suite
│   └── main.py            # Application entry point
├── client/                 # React Frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── pages/          # Page components
│   │   └── types/          # TypeScript interfaces
│   └── package.json
└── README.md
```

## 🚀 Features

### Backend Features
- ✅ **Task CRUD API**: Create, Read, Update, Delete tasks
- ✅ **Comment API**: Full CRUD with pagination
- ✅ **Validation**: Input validation with Marshmallow
- ✅ **Error Handling**: Comprehensive error responses
- ✅ **Testing**: 90%+ test coverage with Pytest
- ✅ **Database**: SQLAlchemy ORM with migrations
- ✅ **Architecture**: Clean service-repository pattern

### Frontend Features
- ✅ **Responsive Design**: Works on all device sizes
- ✅ **Task Management**: Add, edit, delete tasks
- ✅ **Real-time Updates**: Automatic refresh after actions
- ✅ **User Feedback**: Toast notifications for all actions
- ✅ **Loading States**: Proper loading indicators
- ✅ **Error Handling**: Graceful error display
- ✅ **Type Safety**: Full TypeScript implementation

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Navigate to server directory**:
   ```bash
   cd server
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**:
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

5. **Run the server**:
   ```bash
   python main.py
   ```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to client directory**:
   ```bash
   cd client
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start development server**:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

## 📚 API Documentation

### Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks with pagination |
| GET | `/api/tasks/:id` | Get specific task |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/:id` | Update existing task |
| DELETE | `/api/tasks/:id` | Delete task |

### Comment Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/comments/:task_id` | Get comments for task |
| POST | `/api/comments` | Create new comment |
| PUT | `/api/comments/:id` | Update comment |
| DELETE | `/api/comments/:id` | Delete comment |

### Request/Response Examples

**Create Task**:
```json
POST /api/tasks
{
  "title": "Complete project documentation",
  "description": "Write comprehensive README and API docs"
}
```

**Get Tasks**:
```json
GET /api/tasks?page=1&limit=10
Response:
{
  "tasks": [...],
  "page": 1,
  "limit": 10,
  "total": 25
}
```

## 🧪 Testing

### Backend Tests
```bash
cd server
pytest tests/ -v --cov=app
```

### Frontend Tests
```bash
cd client
npm test
```

## 🎯 Key Implementation Details

### Backend Architecture
- **Models**: SQLAlchemy models with relationships
- **Repositories**: Data access abstraction layer
- **Services**: Business logic and validation
- **Schemas**: Request/response serialization
- **Routes**: RESTful API endpoints

### Frontend Architecture
- **Components**: Reusable UI components (TaskCard, TaskModal)
- **Hooks**: Custom `useTasks` hook for API integration
- **Types**: TypeScript interfaces for type safety
- **State**: React hooks for local state management

### Database Design
```sql
-- Tasks table
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Comments table
CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    task_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
```

## 🔧 Development

### Adding New Features
1. **Backend**: Add model → repository → service → schema → route
2. **Frontend**: Add type → hook → component → page integration
3. **Testing**: Add unit tests for both backend and frontend

### Code Quality
- **Backend**: Follow PEP 8, use type hints, comprehensive testing
- **Frontend**: ESLint, Prettier, TypeScript strict mode
- **Both**: Consistent error handling and user feedback

## 🚀 Deployment

### Backend Deployment
- Use Gunicorn for production WSGI server
- Configure environment variables for database
- Set up proper CORS for frontend integration

### Frontend Deployment
- Build with `npm run build`
- Serve static files with nginx or similar
- Configure proxy for API calls

## 📝 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Flask and React**
