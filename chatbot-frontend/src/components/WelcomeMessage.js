import React from 'react';
import { Box, Typography, Card, CardContent, Grid, Avatar } from '@mui/material';
import { motion } from 'framer-motion';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import NatureIcon from '@mui/icons-material/Nature';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import HikingIcon from '@mui/icons-material/Hiking';

const features = [
    {
        icon: <LocationOnIcon />,
        title: "Explore Locations",
        description: "Discover hidden gems and popular attractions"
    },
    {
        icon: <NatureIcon />,
        title: "Wildlife & Nature",
        description: "Learn about endemic species and ecosystems"
    },
    {
        icon: <CameraAltIcon />,
        title: "Photography Tips",
        description: "Get the best shots of your adventure"
    },
    {
        icon: <HikingIcon />,
        title: "Activities",
        description: "Find exciting activities and adventures"
    }
];

const WelcomeMessage = () => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
        >
            <Card sx={{
                mb: 3,
                background: 'linear-gradient(135deg, #E8F5E9, #C8E6C9)',
                border: '1px solid rgba(255, 255, 255, 0.2)'
            }}>
                <CardContent sx={{ p: 3 }}>
                    <Box sx={{ textAlign: 'center', mb: 3 }}>
                        <Typography variant="h5" fontWeight="600" color="primary.main" gutterBottom>
                            🏔️ Welcome to Bale Mountains Explorer!
                        </Typography>
                        <Typography variant="body1" color="text.secondary">
                            I'm your AI guide to Ethiopia's natural wonder. Ask me anything about the park!
                        </Typography>
                    </Box>

                    <Grid container spacing={2}>
                        {features.map((feature, index) => (
                            <Grid item xs={12} sm={6} key={feature.title}>
                                <motion.div
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ duration: 0.4, delay: index * 0.1 }}
                                >
                                    <Box sx={{
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: 2,
                                        p: 1.5,
                                        borderRadius: 2,
                                        bgcolor: 'rgba(255, 255, 255, 0.5)',
                                        transition: 'all 0.3s ease',
                                        '&:hover': {
                                            bgcolor: 'rgba(255, 255, 255, 0.8)',
                                            transform: 'translateY(-2px)',
                                            boxShadow: '0 4px 12px rgba(0,0,0,0.1)'
                                        }
                                    }}>
                                        <Avatar sx={{
                                            bgcolor: 'primary.main',
                                            width: 40,
                                            height: 40
                                        }}>
                                            {feature.icon}
                                        </Avatar>
                                        <Box>
                                            <Typography variant="subtitle2" fontWeight="600">
                                                {feature.title}
                                            </Typography>
                                            <Typography variant="caption" color="text.secondary">
                                                {feature.description}
                                            </Typography>
                                        </Box>
                                    </Box>
                                </motion.div>
                            </Grid>
                        ))}
                    </Grid>
                </CardContent>
            </Card>
        </motion.div>
    );
};

export default WelcomeMessage;