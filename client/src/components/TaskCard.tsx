import React from 'react';
import {
  Heading,
  Text,
  Button,
  ButtonGroup,
  Card,
  CardBody,
  CardHeader,
  CardFooter,
  useToast
} from '@chakra-ui/react';
import { Task } from '../types';

interface TaskCardProps {
  task: Task;
  onEdit: (task: Task) => void;
  onDelete: (taskId: number) => Promise<boolean>;
}

export const TaskCard: React.FC<TaskCardProps> = ({ task, onEdit, onDelete }) => {
  const toast = useToast();

  const handleDelete = async () => {
    const success = await onDelete(task.id);
    if (success) {
      toast({
        title: 'Task deleted',
        description: 'Task has been successfully deleted.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } else {
      toast({
        title: 'Error',
        description: 'Failed to delete task. Please try again.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Card
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      shadow="md"
      _hover={{ shadow: 'lg' }}
      transition="all 0.2s"
    >
      <CardHeader pb={2}>
        <Heading size="md" color="gray.700">
          {task.title}
        </Heading>
      </CardHeader>
      
      <CardBody pt={0} pb={4}>
        <Text color="gray.600" noOfLines={3}>
          {task.description}
        </Text>
      </CardBody>
      
      <CardFooter pt={0}>
        <ButtonGroup spacing={2} size="sm" width="100%">
          <Button
            colorScheme="blue"
            variant="outline"
            flex={1}
            onClick={() => onEdit(task)}
          >
            Edit
          </Button>
          <Button
            colorScheme="red"
            variant="outline"
            flex={1}
            onClick={handleDelete}
          >
            Delete
          </Button>
        </ButtonGroup>
      </CardFooter>
    </Card>
  );
}; 