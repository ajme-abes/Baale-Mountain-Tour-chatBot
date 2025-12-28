import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
            main: '#2E7D32', // Forest green
            light: '#4CAF50',
            dark: '#1B5E20',
            contrastText: '#ffffff',
        },
        secondary: {
            main: '#FF8F00', // Warm orange
            light: '#FFB74D',
            dark: '#E65100',
            contrastText: '#ffffff',
        },
        background: {
            default: '#F1F8E9',
            paper: '#FFFFFF',
        },
        text: {
            primary: '#2E2E2E',
            secondary: '#5D5D5D',
        },
        success: {
            main: '#66BB6A',
            light: '#81C784',
            dark: '#388E3C',
        },
        info: {
            main: '#29B6F6',
            light: '#4FC3F7',
            dark: '#0277BD',
        },
        warning: {
            main: '#FFA726',
            light: '#FFB74D',
            dark: '#F57C00',
        },
        error: {
            main: '#EF5350',
            light: '#E57373',
            dark: '#C62828',
        },
    },
    typography: {
        fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
        h1: {
            fontWeight: 700,
            fontSize: '2.5rem',
            lineHeight: 1.2,
        },
        h2: {
            fontWeight: 600,
            fontSize: '2rem',
            lineHeight: 1.3,
        },
        h3: {
            fontWeight: 600,
            fontSize: '1.75rem',
            lineHeight: 1.3,
        },
        h4: {
            fontWeight: 600,
            fontSize: '1.5rem',
            lineHeight: 1.4,
        },
        h5: {
            fontWeight: 500,
            fontSize: '1.25rem',
            lineHeight: 1.4,
        },
        h6: {
            fontWeight: 500,
            fontSize: '1.1rem',
            lineHeight: 1.4,
        },
        body1: {
            fontSize: '1rem',
            lineHeight: 1.6,
        },
        body2: {
            fontSize: '0.875rem',
            lineHeight: 1.6,
        },
        button: {
            textTransform: 'none',
            fontWeight: 500,
        },
    },
    shape: {
        borderRadius: 12,
    },
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    borderRadius: 12,
                    padding: '10px 24px',
                    fontSize: '1rem',
                    fontWeight: 500,
                    textTransform: 'none',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                    transition: 'all 0.3s ease',
                    '&:hover': {
                        transform: 'translateY(-2px)',
                        boxShadow: '0 4px 16px rgba(0,0,0,0.15)',
                    },
                },
                contained: {
                    background: 'linear-gradient(45deg, #2E7D32 30%, #4CAF50 90%)',
                    '&:hover': {
                        background: 'linear-gradient(45deg, #1B5E20 30%, #2E7D32 90%)',
                    },
                },
            },
        },
        MuiTextField: {
            styleOverrides: {
                root: {
                    '& .MuiOutlinedInput-root': {
                        borderRadius: 12,
                        backgroundColor: '#ffffff',
                        transition: 'all 0.3s ease',
                        '&:hover': {
                            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                        },
                        '&.Mui-focused': {
                            boxShadow: '0 4px 16px rgba(46, 125, 50, 0.2)',
                        },
                    },
                },
            },
        },
        MuiPaper: {
            styleOverrides: {
                root: {
                    borderRadius: 16,
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                    transition: 'all 0.3s ease',
                },
            },
        },
        MuiCard: {
            styleOverrides: {
                root: {
                    borderRadius: 16,
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                    transition: 'all 0.3s ease',
                    '&:hover': {
                        transform: 'translateY(-4px)',
                        boxShadow: '0 8px 32px rgba(0,0,0,0.12)',
                    },
                },
            },
        },
    },
});

export default theme;