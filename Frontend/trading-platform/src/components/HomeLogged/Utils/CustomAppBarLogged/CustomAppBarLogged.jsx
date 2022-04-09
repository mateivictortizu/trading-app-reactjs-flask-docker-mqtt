import './CustomAppBarLogged.css';
import React from "react";
import { useCookies } from 'react-cookie';
import { Button, Stack, Toolbar, Box, AppBar, Typography } from '@mui/material';
import { CustomMenuStats } from '../CustomMenuStats/CustomMenuStats';
import { CustomMenuUser } from '../CustomMenuUser/CustomMenuUser';

export function CustomAppBarLogged({ handleClickOpenDeposit }) {
    const [anchorUser, setAnchorUser] = React.useState(null);
    const [anchorAccountStats, setAnchorAccountStats] = React.useState(null);
    const [cookies, setCookie, removeCookie] = useCookies(['jwt']);
    const [funds,setFunds]=React.useState(5.00);
    const [portofolio,setPortofolio]=React.useState(1);
    var data = {
        datasets: [
            {
                data: [funds, portofolio],
                backgroundColor: [
                    '#32CD32',
                    '#0066cc'
                ],
            },
        ],
    };
    

    const handleCloseUser = () => {
        setAnchorUser(null);
    };

    const handleClickUser = (event) => {
        setAnchorUser(event.currentTarget);
    };

    const handleCloseAccountStats = () => {
        setAnchorAccountStats(null);
    };

    const handleClickAccountStats = (event) => {
        setAnchorAccountStats(event.currentTarget);
    };

    function logout() {
        removeCookie('jwt');
    }

    function deposit() {
        handleCloseUser();
        handleClickOpenDeposit();
    }

    return (
        <div className="appBar">

            <Box sx={{ flexGrow: 1 }}>
                <AppBar id='appBarLogged'>
                    <Toolbar>
                        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                            <div className="svg-icon">
                                <svg width="32" height="32" viewBox="0 0 32 32"><g><path fill="#0066cc" d="M11.13 24.97L16 14.16l4.87 10.81c.25.75.75 1 1.37 1h4.62c1 0 1.37-.62 1-1.5L19.99 7c-.25-.75-.75-1-1.37-1h-5.24c-.63 0-1.12.25-1.37 1L4.14 24.47c-.37.88 0 1.5 1 1.5h4.62c.62 0 1.12-.25 1.37-1"></path></g></svg>
                            </div>
                        </Typography>
                        <Stack spacing={5} direction="row">
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                color='inherit'
                                id='appBarButtonAccountValue'
                                onClick={handleClickAccountStats}
                            >
                                Account value: ${funds+portofolio}
                            </Button>
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                variant="outlined"
                                color='inherit'
                                onClick={deposit}
                                id='appBarButtonDeposit'
                            >
                                Deposit funds
                            </Button>
                            <Button
                                aria-controls="simple-menu"
                                aria-haspopup="true"
                                color='inherit'
                                onClick={handleClickUser}
                                id='appBarButtonInvesting'
                            >
                                Investing Money
                            </Button>
                        </Stack>

                        <CustomMenuUser
                            anchorUser={anchorUser} 
                            handleCloseUser={handleCloseUser}
                            deposit={deposit}
                            logout={logout}
                        />

                        <CustomMenuStats
                            anchorAccountStats={anchorAccountStats}
                            handleCloseAccountStats={handleCloseAccountStats}
                            data={data}
                            funds={funds}
                            portofolio={portofolio}/>

                    </Toolbar>
                </AppBar>
            </Box>
        </div>
    )
}