import React from 'react';
import { Box, CircularProgress, Typography } from '@mui/material';
import { motion } from 'framer-motion';

const LoadingSpinner = ({ message = "Loading..." }) => {
    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
        >
            <Box sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                p: 4
            }}>
                <motion.div
                    animate={{ rotate: 360 }}
                    transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                >
                    <CircularProgress
                        size={40}
                        thickness={4}
                        sx={{
                            color: 'primary.main',
                            mb: 2
                        }}
                    />
                </motion.div>
                <Typography variant="body2" color="text.secondary">
                    {message}
                </Typography>
            </Box>
        </motion.div>
    );
};

export default LoadingSpinner;