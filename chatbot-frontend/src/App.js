import { Container, Typography } from '@mui/material';
import ChatInterface from './ChatInterface';

function App() {
  return (
    <Container>
      <Typography variant="h3" gutterBottom sx={{ mt: 3, textAlign: 'center' }}>
        Travel Assistant
      </Typography>
      <ChatInterface />
    </Container>
  );
}

export default App;