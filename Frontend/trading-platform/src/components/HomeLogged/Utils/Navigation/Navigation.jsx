import "./Navigation.css";
import React from "react";
import { Button } from "@mui/material";
import HomeIcon from '@mui/icons-material/Home';
import PieChartIcon from '@mui/icons-material/PieChart';
import SearchIcon from '@mui/icons-material/Search';
import NotificationsIcon from '@mui/icons-material/Notifications';

export default function Navigation({buttonClicked,setButtonClicked}) {

    function clickHome() {
        setButtonClicked('home');
    }

    function clickPie() {
        setButtonClicked('pie');
    }

    function clickSearch() {
        setButtonClicked('search');
    }

    function clickNotification() {
        setButtonClicked('notification');
    }

    return (
        <div class="sidebar">
            {(buttonClicked==='home') ? (
                <Button title='Home' id='buttonClickedSidebarLogged'>
                    <HomeIcon />
                </Button>
            ) : (
                <Button title='Home' id='buttonSidebarLogged' onClick={clickHome}>
                    <HomeIcon />
                </Button>
            )}

            {(buttonClicked==='pie') ? (
                <Button title='Portofolio' id='buttonClickedSidebarLogged'>
                    <PieChartIcon />
                </Button>
            ) : (
                <Button title='Portofolio' id='buttonSidebarLogged' onClick={clickPie}>
                    <PieChartIcon />
                </Button>
            )}

            {(buttonClicked==='search') ? (
                <Button title='Search' id='buttonClickedSidebarLogged'>
                    <SearchIcon />
                </Button>
            ) : (
                <Button title='Search' id='buttonSidebarLogged' onClick={clickSearch}>
                    <SearchIcon />
                </Button>
            )}

            {(buttonClicked==='notification') ? (
                <Button title='Notification' id='buttonClickedSidebarLogged'>
                    <NotificationsIcon />
                </Button>
            ) : (
                <Button title='Notification' id='buttonSidebarLogged' onClick={clickNotification}>
                    <NotificationsIcon />
                </Button>
            )}

        </div>
    );
}