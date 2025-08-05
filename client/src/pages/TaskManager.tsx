import React, { useState } from 'react';
import {
  Box,
  Heading,
  Button,
  SimpleGrid,
  Spinner,
  Center,
  Text,
  Alert,
  AlertIcon,
  useDisclosure,
  Container,
  Flex
} from '@chakra-ui/react';
// Using a simple plus symbol instead of AddIcon to avoid dependency issues
import { TaskCard } from '../components/TaskCard';
import { TaskModal } from '../components/TaskModal';
import { useTasks } from '../hooks/useTasks';
import { Task, CreateTaskData } from '../types';

export const TaskManager: React.FC = () => {
  const { tasks, loading, error, createTask, updateTask, deleteTask } = useTasks();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [isEditing, setIsEditing] = useState(false);

  const handleAddTask = () => {
    setEditingTask(null);
    setIsEditing(false);
    onOpen();
  };

  const handleEditTask = (task: Task) => {
    setEditingTask(task);
    setIsEditing(true);
    onOpen();
  };

  const handleSaveTask = async (taskData: CreateTaskData) => {
    if (isEditing && editingTask) {
      return await updateTask(editingTask.id, taskData);
    } else {
      return await createTask(taskData);
    }
  };

  const handleDeleteTask = async (taskId: number) => {
    return await deleteTask(taskId);
  };

  if (loading) {
    return (
      <Center minH="100vh">
        <Spinner size="xl" color="blue.500" />
      </Center>
    );
  }

  return (
    <Container maxW="container.xl" py={8}>
      <Box>
        <Flex justify="space-between" align="center" mb={8}>
          <Heading size="lg" color="gray.700">
            Task Manager
          </Heading>
          <Button
            colorScheme="blue"
            onClick={handleAddTask}
            size="md"
          >
            + Add Task
          </Button>
        </Flex>

        {error && (
          <Alert status="error" mb={6} borderRadius="md">
            <AlertIcon />
            {error}
          </Alert>
        )}

        {tasks.length === 0 ? (
          <Center py={12}>
            <Box textAlign="center">
              <Text fontSize="lg" color="gray.500" mb={4}>
                No tasks found
              </Text>
              <Text color="gray.400">
                Create your first task by clicking the "Add Task" button above.
              </Text>
            </Box>
          </Center>
        ) : (
          <SimpleGrid
            columns={{ base: 1, md: 2, lg: 3 }}
            spacing={6}
            minChildWidth="300px"
          >
            {tasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onEdit={handleEditTask}
                onDelete={handleDeleteTask}
              />
            ))}
          </SimpleGrid>
        )}

        <TaskModal
          isOpen={isOpen}
          onClose={onClose}
          onSave={handleSaveTask}
          task={editingTask}
          isEditing={isEditing}
        />
      </Box>
    </Container>
  );
}; 