import React from "react";
import { Button, Stack, Toolbar, Box, AppBar, Typography } from '@mui/material';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import './CustomAppBar.css';

export function CustomAppBar() {
    const [anchorEl, setAnchorEl] = React.useState(null);

    const handleClose = () => {
        setAnchorEl(null);
    };

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    return (
        <div className="appBar">

            <Box sx={{ flexGrow: 1 }}>
                <AppBar style={{ backgroundColor: 'white', color: 'black' }} position="static">
                    <Toolbar>
                        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                            <div className="svg-icon">
                                <svg width="32" height="32" viewBox="0 0 32 32"><g><path fill="#0066cc" d="M11.13 24.97L16 14.16l4.87 10.81c.25.75.75 1 1.37 1h4.62c1 0 1.37-.62 1-1.5L19.99 7c-.25-.75-.75-1-1.37-1h-5.24c-.63 0-1.12.25-1.37 1L4.14 24.47c-.37.88 0 1.5 1 1.5h4.62c.62 0 1.12-.25 1.37-1"></path></g></svg>
                            </div>
                        </Typography>
                        <Stack spacing={10} direction="row">
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                color='inherit'
                                style={{ color: "#0066cc" }}
                            >
                                Account value: $
                            </Button>
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                variant="outlined"
                                color='inherit'
                                style={{ backgroundColor: "#0066cc", color: "white" }}
                            >
                                Deposit funds
                            </Button>
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                color='inherit'
                                onClick={handleClick}
                                style={{ color: "#0066cc", width: "350px" }}
                            >
                                Investing Money
                            </Button>
                        </Stack>
                        <Menu
                            keepMounted
                            anchorEl={anchorEl}
                            onClose={handleClose}
                            open={Boolean(anchorEl)}
                            style={{
                                "aria-labelledby": "basic-button",
                                sx: { width: anchorEl && anchorEl.offsetWidth },
                            }}
                        >
                            <MenuItem onClick={handleClose}>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none" /><path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z" fill='grey' /></svg>
                                &nbsp;
                                History
                            </MenuItem>
                            <MenuItem onClick={handleClose}>
                                <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24" /></g><g><g><rect fill='grey' height="7" width="3" x="4" y="10" /><rect fill='grey' height="7" width="3" x="10.5" y="10" /><rect fill='grey' height="3" width="20" x="2" y="19" /><rect fill='grey' height="7" width="3" x="17" y="10" /><polygon fill='grey' points="12,1 2,6 2,8 22,8 22,6" /></g></g></svg>
                                &nbsp;
                                Manage funds
                            </MenuItem>
                            <div style={{ textAlign: "center", margin: '20px' }}>
                                <Button
                                    aria-controls="simple-menu"
                                    aria-haspopup="true"
                                    color='inherit'
                                    style={{ backgroundColor: "#0066cc", color: "white", width: '90%' }}
                                >
                                    Deposit funds
                                </Button>
                            </div>
                            <div style={{ textAlign: "center", margin: '20px' }}>
                                <Stack spacing={10} direction="row" >
                                    <Button
                                        aria-controls="simple-menu"
                                        aria-haspopup="true"
                                        color='inherit'
                                        style={{ color: "#0066cc" }}
                                    >
                                        <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><path d="M0,0h24v24H0V0z" fill="none"/><path fill="grey" d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.07-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.74,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.07,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.47-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></g></svg>
                                        &nbsp;
                                        Settings
                                    </Button>
                                    <Button
                                        aria-controls="simple-menu"
                                        aria-haspopup="true"
                                        color='inherit'
                                        style={{ color: "#0066cc" }}
                                    >
                                        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><path fill="grey" d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"/></svg>
                                        &nbsp;
                                        Logout
                                    </Button>
                                </Stack>
                            </div>
                        </Menu>
                    </Toolbar>
                </AppBar>
            </Box>
        </div>
    )
}