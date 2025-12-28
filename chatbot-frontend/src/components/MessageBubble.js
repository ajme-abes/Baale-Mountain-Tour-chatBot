import React from 'react';
import {
    Box,
    Paper,
    Typography,
    Avatar,
    Chip,
    List,
    ListItem,
    ListItemText,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow
} from '@mui/material';
import { motion } from 'framer-motion';
import PersonIcon from '@mui/icons-material/Person';
import SmartToyIcon from '@mui/icons-material/SmartToy';
import AccessTimeIcon from '@mui/icons-material/AccessTime';

// Enhanced ResponseRenderer component
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
            if (typeof item === 'string') {
                return (
                    <Typography key={index} paragraph sx={{ mb: 1.5 }}>
                        {item}
                    </Typography>
                );
            }

            switch (item.type) {
                case 'header':
                    return (
                        <Typography
                            key={index}
                            variant="h6"
                            gutterBottom
                            sx={{
                                color: 'primary.main',
                                fontWeight: 600,
                                mb: 2
                            }}
                        >
                            {item.content}
                        </Typography>
                    );

                case 'subheader':
                    return (
                        <Typography
                            key={index}
                            variant="subtitle1"
                            gutterBottom
                            sx={{
                                fontWeight: 500,
                                color: 'text.primary',
                                mb: 1.5
                            }}
                        >
                            {item.content}
                        </Typography>
                    );

                case 'text':
                    return (
                        <Typography key={index} paragraph sx={{ mb: 1.5 }}>
                            {item.content}
                        </Typography>
                    );

                case 'list':
                    return (
                        <List key={index} dense sx={{ mb: 2 }}>
                            {item.content?.map?.((listItem, idx) => (
                                <ListItem key={idx} sx={{ py: 0.5, pl: 2 }}>
                                    <Box sx={{
                                        width: 6,
                                        height: 6,
                                        borderRadius: '50%',
                                        bgcolor: 'primary.main',
                                        mr: 2,
                                        mt: 1
                                    }} />
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
                        <Paper key={index} sx={{ my: 2, overflow: 'hidden' }}>
                            <Table size="small">
                                <TableHead>
                                    <TableRow sx={{ bgcolor: 'primary.light' }}>
                                        {item.columns.map((col, i) => (
                                            <TableCell
                                                key={i}
                                                sx={{
                                                    fontWeight: 'bold',
                                                    color: 'white'
                                                }}
                                            >
                                                {col}
                                            </TableCell>
                                        ))}
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {item.rows.map((row, i) => (
                                        <TableRow
                                            key={i}
                                            sx={{
                                                '&:nth-of-type(odd)': {
                                                    bgcolor: 'action.hover'
                                                }
                                            }}
                                        >
                                            {row.map((cell, j) => (
                                                <TableCell key={j}>{cell}</TableCell>
                                            ))}
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Paper>
                    );

                case 'section':
                    return (
                        <Paper key={index} sx={{ p: 2, mb: 2, bgcolor: 'background.default' }}>
                            <Typography
                                variant="subtitle1"
                                gutterBottom
                                sx={{
                                    fontWeight: 'bold',
                                    color: 'primary.main',
                                    borderBottom: '2px solid',
                                    borderColor: 'primary.light',
                                    pb: 1,
                                    mb: 2
                                }}
                            >
                                {item.title}
                            </Typography>
                            {renderContent(item.content)}
                        </Paper>
                    );

                case 'timeline':
                    return (
                        <Box key={index} sx={{
                            borderLeft: '3px solid',
                            borderColor: 'primary.main',
                            pl: 3,
                            ml: 1,
                            mb: 2
                        }}>
                            {item.items.map((period, idx) => (
                                <Box key={idx} sx={{ mb: 2, position: 'relative' }}>
                                    <Box sx={{
                                        position: 'absolute',
                                        left: -9,
                                        top: 4,
                                        width: 12,
                                        height: 12,
                                        borderRadius: '50%',
                                        bgcolor: 'primary.main'
                                    }} />
                                    <Chip
                                        label={period.year}
                                        color="primary"
                                        size="small"
                                        sx={{ mb: 1 }}
                                    />
                                    <List dense>
                                        {period.events.map((event, eventIdx) => (
                                            <ListItem key={eventIdx} sx={{ py: 0, pl: 0 }}>
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
                        <List key={index} component="ol" sx={{ listStyleType: 'decimal', pl: 3, mb: 2 }}>
                            {item.items.map((dayItem, idx) => (
                                <ListItem key={idx} sx={{ display: 'list-item', p: 0, mb: 1 }}>
                                    <Typography fontWeight="500" color="primary.main">
                                        {dayItem.day}
                                    </Typography>
                                    <List component="ul" dense sx={{ mt: 0.5 }}>
                                        {dayItem.activities.map((activity, aIdx) => (
                                            <ListItem key={aIdx} sx={{ py: 0, pl: 2 }}>
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
                        <Paper key={index} sx={{
                            p: 2,
                            my: 2,
                            bgcolor: 'info.light',
                            border: '1px solid',
                            borderColor: 'info.main'
                        }}>
                            <Typography variant="subtitle2" gutterBottom sx={{ fontWeight: 600 }}>
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
                        <Paper key={index} sx={{
                            p: 2,
                            my: 2,
                            bgcolor: 'warning.light',
                            border: '1px solid',
                            borderColor: 'warning.main'
                        }}>
                            <Typography variant="body2" sx={{ fontWeight: 500 }}>
                                💡 {item.content}
                            </Typography>
                        </Paper>
                    );

                default:
                    return null;
            }
        });
    };

    return <Box sx={{ '& > *': { mb: 1 } }}>{renderContent(parts)}</Box>;
};

const MessageBubble = ({ message, index }) => {
    const formatTime = (timestamp) => {
        return new Date(timestamp).toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit'
        });
    };

    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{
                duration: 0.4,
                delay: index * 0.1,
                ease: "easeOut"
            }}
        >
            <Box sx={{
                display: 'flex',
                justifyContent: message.isBot ? 'flex-start' : 'flex-end',
                mb: 3,
                alignItems: 'flex-start',
                gap: 1
            }}>
                {message.isBot && (
                    <Avatar sx={{
                        bgcolor: 'primary.main',
                        width: 36,
                        height: 36,
                        mt: 0.5
                    }}>
                        <SmartToyIcon fontSize="small" />
                    </Avatar>
                )}

                <Box sx={{
                    maxWidth: '75%',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: message.isBot ? 'flex-start' : 'flex-end'
                }}>
                    <Paper
                        elevation={2}
                        sx={{
                            p: 2,
                            bgcolor: message.isBot
                                ? (message.isError ? 'error.light' : 'grey.100')
                                : 'primary.main',
                            color: message.isBot
                                ? (message.isError ? 'error.contrastText' : 'text.primary')
                                : 'primary.contrastText',
                            borderRadius: message.isBot
                                ? '18px 18px 18px 4px'
                                : '18px 18px 4px 18px',
                            position: 'relative',
                            boxShadow: message.isBot
                                ? '0 2px 8px rgba(0,0,0,0.1)'
                                : '0 2px 8px rgba(46, 125, 50, 0.3)',
                            border: message.isError
                                ? '1px solid'
                                : 'none',
                            borderColor: message.isError
                                ? 'error.main'
                                : 'transparent'
                        }}
                    >
                        {message.parts ? (
                            <ResponseRenderer parts={message.parts} />
                        ) : (
                            <Typography sx={{
                                lineHeight: 1.5,
                                wordBreak: 'break-word'
                            }}>
                                {message.text}
                            </Typography>
                        )}

                        {message.isBot && message.intent && (
                            <Box sx={{ mt: 1, pt: 1, borderTop: '1px solid rgba(0,0,0,0.1)' }}>
                                <Chip
                                    label={`${message.intent} (${message.confidence}%)`}
                                    size="small"
                                    variant="outlined"
                                    sx={{ fontSize: '0.7rem' }}
                                />
                            </Box>
                        )}
                    </Paper>

                    <Box sx={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 0.5,
                        mt: 0.5,
                        opacity: 0.7
                    }}>
                        <AccessTimeIcon sx={{ fontSize: 12 }} />
                        <Typography variant="caption">
                            {formatTime(message.timestamp)}
                        </Typography>
                    </Box>
                </Box>

                {!message.isBot && (
                    <Avatar sx={{
                        bgcolor: 'secondary.main',
                        width: 36,
                        height: 36,
                        mt: 0.5
                    }}>
                        <PersonIcon fontSize="small" />
                    </Avatar>
                )}
            </Box>
        </motion.div>
    );
};

export default MessageBubble;