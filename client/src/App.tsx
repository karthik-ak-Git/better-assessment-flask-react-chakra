import React from 'react';
import { ChakraProvider, Box } from '@chakra-ui/react';
import { TaskManager } from './pages/TaskManager';

function App() {
  return (
    <ChakraProvider>
      <Box minH="100vh" bg="gray.50">
        <TaskManager />
      </Box>
    </ChakraProvider>
  );
}

export default App; 