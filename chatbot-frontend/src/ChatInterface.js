import axios from 'axios';
import {
    Box,
    TextField,
    Paper,
    Typography,
    CircularProgress,
    Container,
    Avatar,
    IconButton,
    Tooltip,
    Card
} from '@mui/material';
import { useEffect, useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import SendIcon from '@mui/icons-material/Send';
import SmartToyIcon from '@mui/icons-material/SmartToy';
import ImageCarousel from './components/ImageCarousel';
import MessageBubble from './components/MessageBubble';
import QuickActions from './components/QuickActions';
import WelcomeMessage from './components/WelcomeMessage';
import MobileHeader from './components/MobileHeader';

export default function ChatInterface() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const [isTyping, setIsTyping] = useState(false);
    const [showWelcome, setShowWelcome] = useState(true);
    const messagesEndRef = useRef(null);

    // API URL from environment variable or default to localhost
    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const handleSend = async (messageText = input) => {
        if (!messageText.trim() || loading) return;

        // Hide welcome message after first interaction
        if (showWelcome) {
            setShowWelcome(false);
        }

        setLoading(true);
        setIsTyping(true);
        const userMessage = messageText;
        setInput('');

        const userMsg = {
            id: Date.now(),
            text: userMessage,
            isBot: false,
            timestamp: new Date()
        };
        setMessages((prev) => [...prev, userMsg]);

        try {
            const response = await axios.post(`${API_URL}/api/chat/`, {
                message: userMessage
            });

            const botMsg = {
                id: Date.now() + 1,
                ...response.data,
                isBot: true,
                timestamp: new Date()
            };
            setMessages((prev) => [...prev, botMsg]);
        } catch (error) {
            console.error("Failed to fetch response", error);
            const errorMsg = {
                id: Date.now() + 1,
                text: "Sorry, I'm having trouble connecting right now. Please try again later.",
                isBot: true,
                timestamp: new Date(),
                isError: true
            };
            setMessages((prev) => [...prev, errorMsg]);
        } finally {
            setLoading(false);
            setIsTyping(false);
        }
    };

    const handleQuickAction = (action) => {
        console.log('Quick action clicked:', action);
        handleSend(action);
    };

    return (
        <>
            {/* Mobile Header */}
            <MobileHeader onQuickAction={handleQuickAction} />

            <Container maxWidth="xl" sx={{ py: { xs: 1, md: 2 }, position: 'relative', zIndex: 1 }}>
                <motion.div
                    initial={{ opacity: 0, y: 50 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                >
                    <Card sx={{
                        height: { xs: 'calc(100vh - 120px)', md: '75vh' },
                        background: 'rgba(255, 255, 255, 0.95)',
                        backdropFilter: 'blur(20px)',
                        border: '1px solid rgba(255, 255, 255, 0.2)',
                        overflow: 'hidden'
                    }}>
                        <Box sx={{ display: 'flex', height: '100%', flexDirection: { xs: 'column', md: 'row' } }}>
                            {/* Left Side - Image Carousel (Desktop Only) */}
                            <Box
                                sx={{
                                    width: { xs: '0%', md: '40%' },
                                    display: { xs: 'none', md: 'block' },
                                    position: 'relative',
                                    background: 'linear-gradient(135deg, #E8F5E9, #C8E6C9)',
                                    borderRight: '1px solid rgba(255, 255, 255, 0.2)'
                                }}
                            >
                                <ImageCarousel />
                            </Box>

                            {/* Right Side - Chat Interface */}
                            <Box
                                sx={{
                                    flex: 1,
                                    display: 'flex',
                                    flexDirection: 'column',
                                    height: '100%'
                                }}
                            >
                                {/* Chat Header (Desktop Only) */}
                                <Box sx={{
                                    p: 3,
                                    borderBottom: '1px solid rgba(0,0,0,0.1)',
                                    background: 'linear-gradient(90deg, #2E7D32, #4CAF50)',
                                    color: 'white',
                                    display: { xs: 'none', md: 'block' }
                                }}>
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                                        <Avatar sx={{ bgcolor: 'rgba(255,255,255,0.2)' }}>
                                            <SmartToyIcon />
                                        </Avatar>
                                        <Box>
                                            <Typography variant="h6" fontWeight="600">
                                                Bale Mountains AI Guide
                                            </Typography>
                                            <Typography variant="body2" sx={{ opacity: 0.9 }}>
                                                {isTyping ? 'Typing...' : 'Online • Ready to help'}
                                            </Typography>
                                        </Box>
                                    </Box>
                                </Box>

                                {/* Messages Area */}
                                <Box sx={{
                                    flex: 1,
                                    overflowY: 'auto',
                                    p: { xs: 1, md: 2 },
                                    background: 'linear-gradient(180deg, #fafafa 0%, #f5f5f5 100%)'
                                }}>
                                    {/* Welcome Message */}
                                    <AnimatePresence>
                                        {showWelcome && messages.length === 0 && (
                                            <WelcomeMessage />
                                        )}
                                    </AnimatePresence>

                                    {/* Chat Messages */}
                                    <AnimatePresence>
                                        {messages.map((msg, index) => (
                                            <MessageBubble
                                                key={msg.id}
                                                message={msg}
                                                index={index}
                                            />
                                        ))}
                                    </AnimatePresence>

                                    {isTyping && (
                                        <motion.div
                                            initial={{ opacity: 0, y: 20 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            exit={{ opacity: 0, y: -20 }}
                                        >
                                            <Box sx={{
                                                display: 'flex',
                                                justifyContent: 'flex-start',
                                                mb: 2
                                            }}>
                                                <Paper sx={{
                                                    p: 2,
                                                    bgcolor: 'grey.100',
                                                    borderRadius: '18px 18px 18px 4px',
                                                    maxWidth: '70%'
                                                }}>
                                                    <Box sx={{ display: 'flex', gap: 0.5 }}>
                                                        {[0, 1, 2].map((dot) => (
                                                            <motion.div
                                                                key={dot}
                                                                style={{
                                                                    width: 8,
                                                                    height: 8,
                                                                    borderRadius: '50%',
                                                                    backgroundColor: '#666'
                                                                }}
                                                                animate={{ opacity: [0.3, 1, 0.3] }}
                                                                transition={{
                                                                    duration: 1.5,
                                                                    repeat: Infinity,
                                                                    delay: dot * 0.2
                                                                }}
                                                            />
                                                        ))}
                                                    </Box>
                                                </Paper>
                                            </Box>
                                        </motion.div>
                                    )}
                                    <div ref={messagesEndRef} />
                                </Box>

                                {/* Quick Actions (Desktop Only) */}
                                {messages.length === 0 && (
                                    <Box sx={{ display: { xs: 'none', md: 'block' } }}>
                                        <QuickActions onActionClick={handleQuickAction} />
                                    </Box>
                                )}

                                {/* Input Area */}
                                <Box sx={{
                                    p: { xs: 2, md: 3 },
                                    borderTop: '1px solid rgba(0,0,0,0.1)',
                                    background: 'rgba(255, 255, 255, 0.9)',
                                    backdropFilter: 'blur(10px)'
                                }}>
                                    <Box
                                        component="form"
                                        onSubmit={(e) => {
                                            e.preventDefault();
                                            handleSend();
                                        }}
                                        sx={{ display: 'flex', gap: { xs: 1, md: 2 }, alignItems: 'flex-end' }}
                                    >
                                        <TextField
                                            fullWidth
                                            multiline
                                            maxRows={3}
                                            placeholder="Ask me anything about Bale Mountains..."
                                            value={input}
                                            onChange={(e) => setInput(e.target.value)}
                                            disabled={loading}
                                            variant="outlined"
                                            sx={{
                                                '& .MuiOutlinedInput-root': {
                                                    borderRadius: 3,
                                                    backgroundColor: 'white',
                                                    '&:hover': {
                                                        boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                                                    },
                                                    '&.Mui-focused': {
                                                        boxShadow: '0 4px 16px rgba(46, 125, 50, 0.2)',
                                                    }
                                                }
                                            }}
                                        />
                                        <Tooltip title="Send message">
                                            <span>
                                                <IconButton
                                                    type="submit"
                                                    disabled={loading || !input.trim()}
                                                    sx={{
                                                        bgcolor: 'primary.main',
                                                        color: 'white',
                                                        width: { xs: 40, md: 48 },
                                                        height: { xs: 40, md: 48 },
                                                        '&:hover': {
                                                            bgcolor: 'primary.dark',
                                                            transform: 'scale(1.05)',
                                                        },
                                                        '&:disabled': {
                                                            bgcolor: 'grey.300',
                                                            color: 'grey.500',
                                                        },
                                                        transition: 'all 0.2s ease'
                                                    }}
                                                >
                                                    {loading ? (
                                                        <CircularProgress size={20} color="inherit" />
                                                    ) : (
                                                        <SendIcon fontSize="small" />
                                                    )}
                                                </IconButton>
                                            </span>
                                        </Tooltip>
                                    </Box>
                                </Box>
                            </Box>
                        </Box>
                    </Card>
                </motion.div>
            </Container>
        </>
    );
}