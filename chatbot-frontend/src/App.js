import { ThemeProvider } from '@mui/material/styles';
import { CssBaseline, Box } from '@mui/material';
import ChatInterface from './ChatInterface';
import theme from './theme';
import Header from './components/Header';
import ParticleBackground from './components/ParticleBackground';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%)',
        position: 'relative',
        overflow: 'hidden'
      }}>
        <ParticleBackground />
        <Header />
        <ChatInterface />
      </Box>
    </ThemeProvider>
  );
}

export default App;