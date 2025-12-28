import React from 'react';
import { Box, Typography, Container, IconButton } from '@mui/material';
import { motion } from 'framer-motion';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import NatureIcon from '@mui/icons-material/Nature';
import CameraAltIcon from '@mui/icons-material/CameraAlt';

const Header = () => {
    return (
        <Container maxWidth="xl" sx={{ py: 3, position: 'relative', zIndex: 2 }}>
            <motion.div
                initial={{ opacity: 0, y: -50 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: "easeOut" }}
            >
                <Box sx={{
                    textAlign: 'center',
                    mb: 2,
                    background: 'rgba(255, 255, 255, 0.9)',
                    backdropFilter: 'blur(10px)',
                    borderRadius: 4,
                    p: 3,
                    boxShadow: '0 8px 32px rgba(0,0,0,0.1)',
                    border: '1px solid rgba(255, 255, 255, 0.2)'
                }}>
                    <motion.div
                        initial={{ scale: 0.8 }}
                        animate={{ scale: 1 }}
                        transition={{ duration: 0.5, delay: 0.2 }}
                    >
                        <Typography
                            variant="h2"
                            component="h1"
                            sx={{
                                background: 'linear-gradient(45deg, #2E7D32, #4CAF50, #66BB6A)',
                                backgroundClip: 'text',
                                WebkitBackgroundClip: 'text',
                                WebkitTextFillColor: 'transparent',
                                fontWeight: 700,
                                mb: 1,
                                textShadow: '0 2px 4px rgba(0,0,0,0.1)'
                            }}
                        >
                            🏔️ Bale Mountains Explorer
                        </Typography>
                    </motion.div>

                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ duration: 0.6, delay: 0.4 }}
                    >
                        <Typography
                            variant="h6"
                            sx={{
                                color: 'text.secondary',
                                mb: 2,
                                fontWeight: 400
                            }}
                        >
                            Your AI-Powered Guide to Ethiopia's Natural Wonder
                        </Typography>
                    </motion.div>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6, delay: 0.6 }}
                    >
                        <Box sx={{
                            display: 'flex',
                            justifyContent: 'center',
                            gap: 3,
                            flexWrap: 'wrap'
                        }}>
                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                <IconButton
                                    sx={{
                                        bgcolor: 'primary.main',
                                        color: 'white',
                                        '&:hover': { bgcolor: 'primary.dark' }
                                    }}
                                    size="small"
                                >
                                    <LocationOnIcon />
                                </IconButton>
                                <Typography variant="body2" color="text.secondary">
                                    Explore Locations
                                </Typography>
                            </Box>

                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                <IconButton
                                    sx={{
                                        bgcolor: 'secondary.main',
                                        color: 'white',
                                        '&:hover': { bgcolor: 'secondary.dark' }
                                    }}
                                    size="small"
                                >
                                    <NatureIcon />
                                </IconButton>
                                <Typography variant="body2" color="text.secondary">
                                    Wildlife & Nature
                                </Typography>
                            </Box>

                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                <IconButton
                                    sx={{
                                        bgcolor: 'success.main',
                                        color: 'white',
                                        '&:hover': { bgcolor: 'success.dark' }
                                    }}
                                    size="small"
                                >
                                    <CameraAltIcon />
                                </IconButton>
                                <Typography variant="body2" color="text.secondary">
                                    Photography Tips
                                </Typography>
                            </Box>
                        </Box>
                    </motion.div>
                </Box>
            </motion.div>
        </Container>
    );
};

export default Header;