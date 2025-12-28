import React from 'react';
import { Box } from '@mui/material';
import { motion } from 'framer-motion';

const ParticleBackground = () => {
    const particles = Array.from({ length: 20 }, (_, i) => i);

    return (
        <Box
            sx={{
                position: 'fixed',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                zIndex: 0,
                overflow: 'hidden',
                pointerEvents: 'none'
            }}
        >
            {particles.map((particle) => (
                <motion.div
                    key={particle}
                    style={{
                        position: 'absolute',
                        width: Math.random() * 4 + 2,
                        height: Math.random() * 4 + 2,
                        backgroundColor: `rgba(76, 175, 80, ${Math.random() * 0.3 + 0.1})`,
                        borderRadius: '50%',
                        left: `${Math.random() * 100}%`,
                        top: `${Math.random() * 100}%`,
                    }}
                    animate={{
                        y: [0, -30, 0],
                        x: [0, Math.random() * 20 - 10, 0],
                        opacity: [0.1, 0.5, 0.1],
                    }}
                    transition={{
                        duration: Math.random() * 3 + 2,
                        repeat: Infinity,
                        ease: "easeInOut",
                        delay: Math.random() * 2,
                    }}
                />
            ))}

            {/* Floating mountain silhouettes */}
            {Array.from({ length: 3 }, (_, i) => (
                <motion.div
                    key={`mountain-${i}`}
                    style={{
                        position: 'absolute',
                        fontSize: '2rem',
                        color: 'rgba(46, 125, 50, 0.1)',
                        left: `${20 + i * 30}%`,
                        top: `${20 + i * 20}%`,
                    }}
                    animate={{
                        y: [0, -20, 0],
                        rotate: [0, 5, 0],
                    }}
                    transition={{
                        duration: 4 + i,
                        repeat: Infinity,
                        ease: "easeInOut",
                        delay: i * 0.5,
                    }}
                >
                    🏔️
                </motion.div>
            ))}
        </Box>
    );
};

export default ParticleBackground;