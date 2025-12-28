import React, { useState, useEffect } from 'react';
import { Box, Typography, IconButton, Fade } from '@mui/material';
import { motion, AnimatePresence } from 'framer-motion';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

const images = [
    {
        url: "https://balemountains.org/wp-content/uploads/2014/01/010706_1.jpg",
        title: "Sanetti Plateau",
        description: "Breathtaking highland landscapes"
    },
    {
        url: "https://balemountains.org/wp-content/uploads/2013/03/BAL0053.jpg",
        title: "Ethiopian Wolf",
        description: "Rare endemic wildlife"
    },
    {
        url: "https://balemountains.org/wp-content/uploads/2014/01/BAL00881.jpg",
        title: "Mountain Peaks",
        description: "Dramatic mountain vistas"
    },
    {
        url: "https://balemountains.org/wp-content/uploads/2019/10/Sera_James_Irvine_Harenna_forest_Bale_Mountain_Lodge-SMALL-1-1024x713.jpg",
        title: "Harenna Forest",
        description: "Ancient cloud forest"
    },
    {
        url: "https://balemountains.org/wp-content/uploads/2013/02/delphin-ruche037-1024x685.jpg",
        title: "Wildlife Viewing",
        description: "Incredible biodiversity"
    },
    {
        url: "https://balemountains.org/wp-content/uploads/2014/01/040707_4_-30-1024x685.jpg",
        title: "Alpine Scenery",
        description: "High altitude adventures"
    }
];

const ImageCarousel = () => {
    const [currentImageIndex, setCurrentImageIndex] = useState(0);
    const [isHovered, setIsHovered] = useState(false);

    useEffect(() => {
        if (!isHovered) {
            const interval = setInterval(() => {
                setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
            }, 4000);
            return () => clearInterval(interval);
        }
    }, [isHovered]);

    const nextImage = () => {
        setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
    };

    const prevImage = () => {
        setCurrentImageIndex((prevIndex) =>
            prevIndex === 0 ? images.length - 1 : prevIndex - 1
        );
    };

    const currentImage = images[currentImageIndex];

    return (
        <Box
            sx={{
                height: '100%',
                position: 'relative',
                overflow: 'hidden',
                borderRadius: 2
            }}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            {/* Image Container */}
            <Box sx={{ height: '100%', position: 'relative' }}>
                <AnimatePresence mode="wait">
                    <motion.div
                        key={currentImageIndex}
                        initial={{ opacity: 0, scale: 1.1 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.9 }}
                        transition={{ duration: 0.8, ease: "easeInOut" }}
                        style={{ height: '100%' }}
                    >
                        <Box
                            component="img"
                            src={currentImage.url}
                            alt={currentImage.title}
                            sx={{
                                width: '100%',
                                height: '100%',
                                objectFit: 'cover',
                                filter: 'brightness(0.8)',
                                transition: 'filter 0.3s ease'
                            }}
                        />
                    </motion.div>
                </AnimatePresence>

                {/* Gradient Overlay */}
                <Box sx={{
                    position: 'absolute',
                    bottom: 0,
                    left: 0,
                    right: 0,
                    height: '50%',
                    background: 'linear-gradient(transparent, rgba(0,0,0,0.7))',
                    zIndex: 1
                }} />

                {/* Content Overlay */}
                <Box sx={{
                    position: 'absolute',
                    bottom: 0,
                    left: 0,
                    right: 0,
                    p: 3,
                    zIndex: 2,
                    color: 'white'
                }}>
                    <motion.div
                        key={`content-${currentImageIndex}`}
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6, delay: 0.3 }}
                    >
                        <Typography
                            variant="h5"
                            fontWeight="700"
                            sx={{
                                mb: 1,
                                textShadow: '2px 2px 4px rgba(0,0,0,0.5)'
                            }}
                        >
                            {currentImage.title}
                        </Typography>
                        <Typography
                            variant="body1"
                            sx={{
                                opacity: 0.9,
                                textShadow: '1px 1px 2px rgba(0,0,0,0.5)'
                            }}
                        >
                            {currentImage.description}
                        </Typography>
                    </motion.div>
                </Box>

                {/* Navigation Arrows */}
                <Fade in={isHovered}>
                    <Box>
                        <IconButton
                            onClick={prevImage}
                            sx={{
                                position: 'absolute',
                                left: 16,
                                top: '50%',
                                transform: 'translateY(-50%)',
                                bgcolor: 'rgba(255,255,255,0.2)',
                                color: 'white',
                                backdropFilter: 'blur(10px)',
                                '&:hover': {
                                    bgcolor: 'rgba(255,255,255,0.3)',
                                    transform: 'translateY(-50%) scale(1.1)',
                                },
                                transition: 'all 0.3s ease',
                                zIndex: 3
                            }}
                        >
                            <ArrowBackIosIcon />
                        </IconButton>

                        <IconButton
                            onClick={nextImage}
                            sx={{
                                position: 'absolute',
                                right: 16,
                                top: '50%',
                                transform: 'translateY(-50%)',
                                bgcolor: 'rgba(255,255,255,0.2)',
                                color: 'white',
                                backdropFilter: 'blur(10px)',
                                '&:hover': {
                                    bgcolor: 'rgba(255,255,255,0.3)',
                                    transform: 'translateY(-50%) scale(1.1)',
                                },
                                transition: 'all 0.3s ease',
                                zIndex: 3
                            }}
                        >
                            <ArrowForwardIosIcon />
                        </IconButton>
                    </Box>
                </Fade>

                {/* Dots Indicator */}
                <Box sx={{
                    position: 'absolute',
                    bottom: 16,
                    left: '50%',
                    transform: 'translateX(-50%)',
                    display: 'flex',
                    gap: 1,
                    zIndex: 3
                }}>
                    {images.map((_, index) => (
                        <Box
                            key={index}
                            onClick={() => setCurrentImageIndex(index)}
                            sx={{
                                width: 8,
                                height: 8,
                                borderRadius: '50%',
                                bgcolor: index === currentImageIndex ? 'white' : 'rgba(255,255,255,0.5)',
                                cursor: 'pointer',
                                transition: 'all 0.3s ease',
                                '&:hover': {
                                    bgcolor: 'white',
                                    transform: 'scale(1.2)'
                                }
                            }}
                        />
                    ))}
                </Box>
            </Box>

            {/* Floating Elements */}
            <Box sx={{ position: 'absolute', top: 20, right: 20, zIndex: 2 }}>
                <motion.div
                    animate={{
                        y: [0, -10, 0],
                        rotate: [0, 5, 0]
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                >
                    <Typography sx={{ fontSize: '2rem', filter: 'drop-shadow(2px 2px 4px rgba(0,0,0,0.3))' }}>
                        🏔️
                    </Typography>
                </motion.div>
            </Box>
        </Box>
    );
};

export default ImageCarousel;