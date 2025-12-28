import React, { useState } from 'react';
import {
    Box,
    Chip,
    Typography,
    Collapse,
    IconButton,
    Paper
} from '@mui/material';
import { motion, AnimatePresence } from 'framer-motion';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import HotelIcon from '@mui/icons-material/Hotel';
import HikingIcon from '@mui/icons-material/Hiking';
import InfoIcon from '@mui/icons-material/Info';
import DirectionsIcon from '@mui/icons-material/Directions';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';

const quickActions = [
    {
        label: "Park Information",
        query: "Tell me about Bale Mountains National Park",
        icon: <InfoIcon fontSize="small" />,
        color: "primary"
    },
    {
        label: "How to Get There",
        query: "How do I get to Bale Mountains?",
        icon: <DirectionsIcon fontSize="small" />,
        color: "secondary"
    },
    {
        label: "Accommodations",
        query: "What are the accommodation options?",
        icon: <HotelIcon fontSize="small" />,
        color: "success"
    },
    {
        label: "Activities",
        query: "What activities can I do in the park?",
        icon: <HikingIcon fontSize="small" />,
        color: "info"
    },
    {
        label: "Best Time to Visit",
        query: "When is the best time to visit?",
        icon: <LocationOnIcon fontSize="small" />,
        color: "warning"
    },
    {
        label: "Park Fees",
        query: "What are the park entrance fees?",
        icon: <AttachMoneyIcon fontSize="small" />,
        color: "error"
    }
];

const QuickActions = ({ onActionClick }) => {
    const [expanded, setExpanded] = useState(true);

    return (
        <Paper sx={{
            mx: 3,
            mb: 2,
            bgcolor: 'rgba(255, 255, 255, 0.9)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.2)'
        }}>
            <Box sx={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                p: 2,
                pb: expanded ? 1 : 2
            }}>
                <Typography variant="subtitle2" fontWeight="600" color="text.secondary">
                    Quick Actions
                </Typography>
                <IconButton
                    size="small"
                    onClick={() => setExpanded(!expanded)}
                    sx={{
                        transform: expanded ? 'rotate(0deg)' : 'rotate(180deg)',
                        transition: 'transform 0.3s ease'
                    }}
                >
                    <ExpandMoreIcon />
                </IconButton>
            </Box>

            <Collapse in={expanded}>
                <Box sx={{
                    px: 2,
                    pb: 2,
                    display: 'flex',
                    flexWrap: 'wrap',
                    gap: 1
                }}>
                    <AnimatePresence>
                        {quickActions.map((action, index) => (
                            <motion.div
                                key={action.label}
                                initial={{ opacity: 0, scale: 0.8 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0.8 }}
                                transition={{
                                    duration: 0.3,
                                    delay: index * 0.05
                                }}
                                whileHover={{ scale: 1.05 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <Chip
                                    icon={action.icon}
                                    label={action.label}
                                    onClick={() => {
                                        console.log('Chip clicked:', action.query);
                                        onActionClick(action.query);
                                    }}
                                    color={action.color}
                                    variant="outlined"
                                    sx={{
                                        cursor: 'pointer',
                                        transition: 'all 0.2s ease',
                                        '&:hover': {
                                            boxShadow: '0 2px 8px rgba(0,0,0,0.15)',
                                            transform: 'translateY(-1px)'
                                        },
                                        '& .MuiChip-icon': {
                                            transition: 'transform 0.2s ease'
                                        },
                                        '&:hover .MuiChip-icon': {
                                            transform: 'scale(1.1)'
                                        }
                                    }}
                                />
                            </motion.div>
                        ))}
                    </AnimatePresence>
                </Box>
            </Collapse>
        </Paper>
    );
};

export default QuickActions;