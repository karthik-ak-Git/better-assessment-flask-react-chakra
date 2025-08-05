# Task Manager - React Client

A responsive React TypeScript application for managing tasks, built with Chakra UI.

## Features

- ✅ Display tasks in a responsive grid layout
- ✅ Add new tasks via modal
- ✅ Edit existing tasks
- ✅ Delete tasks with confirmation
- ✅ Real-time API integration with axios
- ✅ Toast notifications for user feedback
- ✅ Loading states and error handling
- ✅ Responsive design with Chakra UI

## Tech Stack

- **React 18** with TypeScript
- **Chakra UI** for components and styling
- **Axios** for API calls
- **React Hooks** for state management

## Project Structure

```
src/
├── components/
│   ├── TaskCard.tsx      # Individual task display component
│   └── TaskModal.tsx     # Modal for adding/editing tasks
├── hooks/
│   └── useTasks.ts       # Custom hook for task management
├── pages/
│   └── TaskManager.tsx   # Main page component
├── types/
│   └── index.ts          # TypeScript interfaces
├── App.tsx               # Root component with ChakraProvider
└── index.tsx             # Application entry point
```

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

3. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### API Requirements

The application expects a backend API with the following endpoints:

- `GET /api/tasks` - Fetch all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/:id` - Update an existing task
- `DELETE /api/tasks/:id` - Delete a task

Each task should have the structure:
```typescript
{
  id: number;
  title: string;
  description: string;
}
```

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (one-way operation)

## Features in Detail

### Task Management
- **Create**: Click "Add Task" button to open a modal with form inputs
- **Read**: Tasks are displayed in a responsive grid with cards
- **Update**: Click "Edit" button on any task card to modify it
- **Delete**: Click "Delete" button to remove a task

### User Experience
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Loading States**: Spinner shown while fetching data
- **Error Handling**: Toast notifications for success/error actions
- **Form Validation**: Required field validation in the modal
- **Smooth Animations**: Hover effects and transitions

### API Integration
- **Automatic Refresh**: Task list updates after every action
- **Error Recovery**: Graceful handling of API failures
- **Optimistic Updates**: UI updates immediately for better UX 