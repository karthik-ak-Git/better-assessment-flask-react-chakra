export interface Task {
  id: number;
  title: string;
  description: string;
}

export interface CreateTaskData {
  title: string;
  description: string;
}

// UpdateTaskData is no longer needed since we pass taskId separately 