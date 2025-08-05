import { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { Task, CreateTaskData } from '../types';

const API_BASE_URL = '/api/tasks';

export const useTasks = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await axios.get<{ tasks: Task[], page: number, limit: number, total: number }>(API_BASE_URL);
      setTasks(response.data.tasks);
    } catch (err) {
      setError('Failed to fetch tasks');
      console.error('Error fetching tasks:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  const createTask = useCallback(async (taskData: CreateTaskData): Promise<Task | null> => {
    try {
      setError(null);
      const response = await axios.post<Task>(API_BASE_URL, taskData);
      setTasks(prev => [...prev, response.data]);
      return response.data;
    } catch (err) {
      setError('Failed to create task');
      console.error('Error creating task:', err);
      return null;
    }
  }, []);

  const updateTask = useCallback(async (taskId: number, taskData: CreateTaskData): Promise<Task | null> => {
    try {
      setError(null);
      const response = await axios.put<Task>(`${API_BASE_URL}/${taskId}`, taskData);
      setTasks(prev => prev.map(task => 
        task.id === taskId ? response.data : task
      ));
      return response.data;
    } catch (err) {
      setError('Failed to update task');
      console.error('Error updating task:', err);
      return null;
    }
  }, []);

  const deleteTask = useCallback(async (taskId: number): Promise<boolean> => {
    try {
      setError(null);
      await axios.delete(`${API_BASE_URL}/${taskId}`);
      setTasks(prev => prev.filter(task => task.id !== taskId));
      return true;
    } catch (err) {
      setError('Failed to delete task');
      console.error('Error deleting task:', err);
      return false;
    }
  }, []);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  return {
    tasks,
    loading,
    error,
    createTask,
    updateTask,
    deleteTask,
    refetch: fetchTasks
  };
}; 