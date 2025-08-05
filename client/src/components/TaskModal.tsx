import React, { useState, useEffect } from 'react';
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  FormControl,
  FormLabel,
  Input,
  Textarea,
  VStack,
  useToast
} from '@chakra-ui/react';
import { Task, CreateTaskData } from '../types';

interface TaskModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSave: (data: CreateTaskData) => Promise<Task | null>;
  task?: Task | null;
  isEditing: boolean;
}

export const TaskModal: React.FC<TaskModalProps> = ({
  isOpen,
  onClose,
  onSave,
  task,
  isEditing
}) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  useEffect(() => {
    if (isOpen) {
      if (isEditing && task) {
        setTitle(task.title);
        setDescription(task.description);
      } else {
        setTitle('');
        setDescription('');
      }
    }
  }, [isOpen, isEditing, task]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title.trim() || !description.trim()) {
      toast({
        title: 'Validation Error',
        description: 'Please fill in all fields.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    setIsSubmitting(true);
    
    try {
      const taskData = isEditing && task
        ? { title: title.trim(), description: description.trim() }
        : { title: title.trim(), description: description.trim() };

      const result = await onSave(taskData);
      
      if (result) {
        toast({
          title: isEditing ? 'Task updated' : 'Task created',
          description: isEditing 
            ? 'Task has been successfully updated.'
            : 'Task has been successfully created.',
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
        onClose();
      } else {
        toast({
          title: 'Error',
          description: isEditing 
            ? 'Failed to update task. Please try again.'
            : 'Failed to create task. Please try again.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } catch (error) {
      toast({
        title: 'Error',
        description: 'An unexpected error occurred.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleClose = () => {
    if (!isSubmitting) {
      onClose();
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={handleClose} isCentered>
      <ModalOverlay />
      <ModalContent>
        <form onSubmit={handleSubmit}>
          <ModalHeader>
            {isEditing ? 'Edit Task' : 'Add New Task'}
          </ModalHeader>
          <ModalCloseButton />
          
          <ModalBody>
            <VStack spacing={4}>
              <FormControl isRequired>
                <FormLabel>Title</FormLabel>
                <Input
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  placeholder="Enter task title"
                  disabled={isSubmitting}
                />
              </FormControl>
              
              <FormControl isRequired>
                <FormLabel>Description</FormLabel>
                <Textarea
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  placeholder="Enter task description"
                  rows={4}
                  disabled={isSubmitting}
                />
              </FormControl>
            </VStack>
          </ModalBody>

          <ModalFooter>
            <Button
              variant="ghost"
              mr={3}
              onClick={handleClose}
              disabled={isSubmitting}
            >
              Cancel
            </Button>
            <Button
              colorScheme="blue"
              type="submit"
              isLoading={isSubmitting}
              loadingText={isEditing ? 'Updating...' : 'Creating...'}
            >
              {isEditing ? 'Update Task' : 'Create Task'}
            </Button>
          </ModalFooter>
        </form>
      </ModalContent>
    </Modal>
  );
}; 