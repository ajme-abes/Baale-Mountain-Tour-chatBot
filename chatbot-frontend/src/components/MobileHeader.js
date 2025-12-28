import React from 'react';
import { Box, Typography, IconButton, Drawer, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { useState } from 'react';
import { motion } from 'framer-motion';
import MenuIcon from '@mui/icons-material/Menu';
import InfoIcon from '@mui/icons-material/Info';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import HotelIcon from '@mui/icons-material/Hotel';
import HikingIcon from '@mui/icons-material/Hiking';

const MobileHeader = ({ onQuickAction }) => {
    const [drawerOpen, setDrawerOpen] = useState(false);

    const menuItems = [
        { icon: <InfoIcon />, text: "Park Information", action: "Tell me about Bale Mountains National Park" },
        { icon: <LocationOnIcon />, text: "How to Get There", action: "How do I get to Bale Mountains?" },
        { icon: <HotelIcon />, text: "Accommodations", action: "What are the accommodation options?" },
        { icon: <HikingIcon />, text: "Activities", action: "What activities can I do in the park?" }
    ];

    return (
        <>
            <Box sx={{
                display: { xs: 'flex', md: 'none' },
                alignItems: 'center',
                justifyContent: 'space-between',
                p: 2,
                background: 'linear-gradient(90deg, #2E7D32, #4CAF50)',
                color: 'white'
            }}>
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.5 }}
                >
                    <Typography variant="h6" fontWeight="600">
                        🏔️ Bale Mountains
                    </Typography>
                </motion.div>

                <IconButton
                    color="inherit"
                    onClick={() => setDrawerOpen(true)}
                    sx={{
                        bgcolor: 'rgba(255,255,255,0.1)',
                        '&:hover': { bgcolor: 'rgba(255,255,255,0.2)' }
                    }}
                >
                    <MenuIcon />
                </IconButton>
            </Box>

            <Drawer
                anchor="right"
                open={drawerOpen}
                onClose={() => setDrawerOpen(false)}
                PaperProps={{
                    sx: {
                        width: 280,
                        background: 'linear-gradient(135deg, #E8F5E9, #C8E6C9)',
                    }
                }}
            >
                <Box sx={{ p: 2 }}>
                    <Typography variant="h6" color="primary.main" gutterBottom>
                        Quick Actions
                    </Typography>
                    <List>
                        {menuItems.map((item, index) => (
                            <ListItem
                                key={item.text}
                                onClick={() => {
                                    onQuickAction(item.action);
                                    setDrawerOpen(false);
                                }}
                                sx={{
                                    borderRadius: 2,
                                    mb: 1,
                                    cursor: 'pointer',
                                    '&:hover': {
                                        bgcolor: 'rgba(46, 125, 50, 0.1)'
                                    }
                                }}
                            >
                                <ListItemIcon sx={{ color: 'primary.main' }}>
                                    {item.icon}
                                </ListItemIcon>
                                <ListItemText primary={item.text} />
                            </ListItem>
                        ))}
                    </List>
                </Box>
            </Drawer>
        </>
    );
};

export default MobileHeader;