import axios from 'axios';
import {
    Box,
    TextField,
    Button,
    List,
    ListItem,
    ListItemText,
    Paper,
    Typography,
    CircularProgress,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow
} from '@mui/material';
import { useEffect, useState, useRef } from 'react';
import { motion } from 'framer-motion';
const images = [
    "https://balemountains.org/wp-content/uploads/2014/01/010706_1.jpg",
    "https://balemountains.org/wp-content/uploads/2013/03/BAL0053.jpg",
    "https://balemountains.org/wp-content/uploads/2014/01/BAL00881.jpg",
    "https://balemountains.org/wp-content/uploads/2019/10/Sera_James_Irvine_Harenna_forest_Bale_Mountain_Lodge-SMALL-1-1024x713.jpg",
    "https://balemountains.org/wp-content/uploads/2013/02/delphin-ruche037-1024x685.jpg",
    "https://balemountains.org/wp-content/uploads/2014/01/040707_4_-30-1024x685.jpg"
    
];
// Left side moving image component
const MovingImage = () => {
    const [currentImageIndex, setCurrentImageIndex] = useState(0);

    // Image change effect (every 5 seconds, change to the next image)
    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 5000); // Change every 5 seconds (you can adjust this)

        return () => clearInterval(interval);
    }, []);

    return (
        <Box sx={{ height: '100%', overflow: 'hidden', borderRadius: '12px', position: 'relative' }}>
            <motion.img
                src={images[currentImageIndex]}
                alt="Slideshow Image"
                key={currentImageIndex} // This forces the animation to reset when image changes
                style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover'
                }}
                animate={{
                    y: [0, 15, 0] // Floating animation
                }}
                transition={{
                    duration: 6,
                    repeat: Infinity,
                    ease: 'easeInOut'
                }}
            />
        </Box>
    );
};

// Component to render chatbot responses
const ResponseRenderer = ({ parts }) => {
  const renderNestedList = (items, depth = 0) => {
    return items.map((item, index) => {
    if (typeof item === 'object' && item.subitems) {
    return (
    <Box key={index} sx={{ pl: depth * 2 }}>
    <Typography component="span" fontWeight="500">
    {item.text}
    </Typography>
    <List dense sx={{ pl: 2 }}>
    {renderNestedList(item.subitems, depth + 1)}
    </List>
    </Box>
    );
    }
    return (
    <ListItem key={index} sx={{ py: 0, pl: depth * 2 }}>
    <ListItemText primary={item} />
    </ListItem>
    );
    });
    };
    
    const renderContent = (content) => {
    return content.map((item, index) => {
    if (typeof item === 'string') return <Typography key={index} paragraph>{item}</Typography>;
    
    switch(item.type) {
    case 'header':
    return <Typography key={index} variant="h6" gutterBottom>{item.content}</Typography>;
    
    case 'subheader':
    return <Typography key={index} variant="subtitle1" gutterBottom>{item.content}</Typography>;
    
    case 'text':
    return <Typography key={index} paragraph>{item.content}</Typography>;
    
    case 'list':
    return (
    <List key={index} dense>
    {item.content?.map?.((listItem, idx) => (
    <ListItem key={idx} sx={{ py: 0 }}>
    <ListItemText primary={listItem} />
    </ListItem>
    ))}
    {item.items?.map?.((listItem, idx) => (
    <Box key={idx} sx={{ pl: 2 }}>
    {renderNestedList([listItem])}
    </Box>
    ))}
    </List>
    );
    
    case 'table':
    return (
    <Table key={index} size="small" sx={{ my: 2 }}>
    <TableHead>
    <TableRow>
    {item.columns.map((col, i) => (
    <TableCell key={i} sx={{ fontWeight: 'bold' }}>{col}</TableCell>
    ))}
    </TableRow>
    </TableHead>
    <TableBody>
    {item.rows.map((row, i) => (
    <TableRow key={i}>
    {row.map((cell, j) => (
    <TableCell key={j}>{cell}</TableCell>
    ))}
    </TableRow>
    ))}
    </TableBody>
    </Table>
    );
    
    case 'section':
    return (
    <Box key={index} sx={{ mb: 3 }}>
    <Typography variant="subtitle1" gutterBottom sx={{ fontWeight: 'bold' }}>
    {item.title}
    </Typography>
    {renderContent(item.content)}
    </Box>
    );
    
    case 'timeline':
    return (
    <Box key={index} sx={{ borderLeft: '3px solid', borderColor: 'primary.main', pl: 2, ml: 1 }}>
    {item.items.map((period, idx) => (
    <Box key={idx} sx={{ mb: 2 }}>
    <Typography variant="subtitle2" color="primary">
    {period.year}
    </Typography>
    <List dense>
    {period.events.map((event, eventIdx) => (
    <ListItem key={eventIdx} sx={{ py: 0 }}>
    <ListItemText primary={event} />
    </ListItem>
    ))}
    </List>
    </Box>
    ))}
    </Box>
    );
    
    case 'ordered-list':
    return (
    <List key={index} component="ol" sx={{ listStyleType: 'decimal', pl: 3 }}>
    {item.items.map((dayItem, idx) => (
    <ListItem key={idx} sx={{ display: 'list-item', p: 0 }}>
    <Typography fontWeight="500">{dayItem.day}</Typography>
    <List component="ul" dense>
    {dayItem.activities.map((activity, aIdx) => (
    <ListItem key={aIdx} sx={{ py: 0 }}>
    <ListItemText primary={activity} />
    </ListItem>
    ))}
    </List>
    </ListItem>
    ))}
    </List>
    );
    
    case 'summary':
    return (
    <Paper key={index} sx={{ p: 2, my: 2, bgcolor: 'background.default' }}>
    <Typography variant="subtitle2" gutterBottom>
    {item.content[0]}
    </Typography>
    <List component="ol" sx={{ listStyleType: 'decimal', pl: 2 }}>
    {item.content.slice(1).map((point, idx) => (
    <ListItem key={idx} sx={{ display: 'list-item', p: 0 }}>
    <Typography>{point}</Typography>
    </ListItem>
    ))}
    </List>
    </Paper>
    );
    
    case 'note':
    return (
    <Paper key={index} sx={{ p: 2, my: 2, bgcolor: 'info.light' }}>
    <Typography variant="body2">{item.content}</Typography>
    </Paper>
    );
    
    default:
    return null;
    }
    });
    };
    return <Box sx={{ '& > *': { mb: 2 } }}>{renderContent(parts)}</Box>;
};

export default function ChatInterface() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const messagesEndRef = useRef(null);

    useEffect(() => messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }), [messages]);

    const handleSend = async (e) => {
        e.preventDefault();
        if (!input.trim() || loading) return;

        setLoading(true);
        const userMessage = input;
        setInput('');

        const userMsg = { id: Date.now(), text: userMessage, isBot: false };
        setMessages((prev) => [...prev, userMsg]);

        try {
            const response = await axios.post('http://localhost:8000/api/chat/', { message: userMessage });
            const botMsg = { id: Date.now() + 1, ...response.data, isBot: true };
            setMessages((prev) => [...prev, botMsg]);
        } catch (error) {
            console.error("Failed to fetch response", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box
            sx={{
                display: 'flex',
                height: '88vh',
                backgroundColor: '#f7f7f7',
                overflow: 'hidden'
            }}
        >
            {/* Left Side - Animated Image */}
            <Box
                sx={{
                    width: '35%',
                    display: { xs: 'none', md: 'block' },
                    position: 'relative',
                    backgroundColor: '#e8f5e9',
                    p: 2
                }}
            >
                <Typography variant="h5" sx={{ mb: 2, textAlign: 'center', fontWeight: 'bold' }}>
                    Explore Baale Mountain 🌄
                </Typography>
                <Box sx={{ height: '95%', overflow: 'hidden', borderRadius: '12px' }}>
                    <MovingImage  />
                </Box>
            </Box>

            {/* Right Side - Chat Interface */}
            <Box
                component="form"
                onSubmit={handleSend}
                sx={{
                    flex: 1,
                    p: 3,
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    backgroundColor: '#e8f5e9'
                }}
            >
                <Typography variant="h4" align="center" gutterBottom fontWeight="bold" color="primary">
                    Baale Mountain Travel Chatbot
                </Typography>

                {/* Chat Messages */}
                <Paper sx={{ flex: 1, overflowY: 'auto', p: 2, mb: 2, backgroundColor: '#fafafa' }}>
                    <List>
                        {messages.map((msg) => (
                            <ListItem
                                key={msg.id}
                                sx={{ justifyContent: msg.isBot ? 'flex-start' : 'flex-end' }}
                            >
                                <Paper
                                    sx={{
                                        p: 1.5,
                                        bgcolor: msg.isBot ? 'secondary.light' : 'primary.main',
                                        color: msg.isBot ? 'black' : 'white',
                                        borderRadius: 3,
                                        maxWidth: '70%'
                                    }}
                                >
                                    {msg.parts ? (
                                        <ResponseRenderer parts={msg.parts} />
                                    ) : (
                                        <Typography>{msg.text}</Typography>
                                    )}
                                    {msg.isBot && msg.intent && (
                                        <Typography variant="caption" sx={{ mt: 0.5, opacity: 0.7 }}>
                                            Intent: {msg.intent} (Confidence: {msg.confidence}%)
                                        </Typography>
                                    )}
                                </Paper>
                            </ListItem>
                        ))}
                        <div ref={messagesEndRef} />
                    </List>
                </Paper>

                {/* Input Field */}
                <Box sx={{ display: 'flex', gap: 1 }}>
                    <TextField
                        fullWidth
                        placeholder="Ask about Baale Mountain..."
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        disabled={loading}
                        sx={{
                            backgroundColor: 'white',
                            '& .MuiOutlinedInput-root': { borderRadius: 3 }
                        }}
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        disabled={loading}
                        sx={{ minWidth: 100, borderRadius: 3 }}
                    >
                        {loading ? <CircularProgress size={24} color="inherit" /> : 'Send'}
                    </Button>
                </Box>
            </Box>
        </Box>
    );
}