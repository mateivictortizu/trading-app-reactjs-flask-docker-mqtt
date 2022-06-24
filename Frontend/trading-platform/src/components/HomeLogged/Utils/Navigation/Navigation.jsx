import "./Navigation.css";
import React from "react";
import { Button } from "@mui/material";
import HomeIcon from '@mui/icons-material/Home';
import PieChartIcon from '@mui/icons-material/PieChart';
import SearchIcon from '@mui/icons-material/Search';

export default function Navigation({ buttonClicked, setButtonClicked }) {

    function clickHome() {
        setButtonClicked('home');
    }

    function clickPie() {
        setButtonClicked('pie');
    }

    function clickSearch() {
        setButtonClicked('search');
    }


    return (
        <div className="sidebar">
            <Button title='Home' onClick={clickHome} id={(buttonClicked === 'home') ? 'buttonClickedSidebarLogged' : 'buttonSidebarLogged'}>
                <HomeIcon />
            </Button>

            <Button title='Portofolio' onClick={clickPie} id={(buttonClicked === 'pie') ? 'buttonClickedSidebarLogged' : 'buttonSidebarLogged'}>
                <PieChartIcon />
            </Button>

            <Button title='Search' onClick={clickSearch} id={(buttonClicked === 'search') ? 'buttonClickedSidebarLogged' : 'buttonSidebarLogged'}>
                <SearchIcon />
            </Button>
        </div>
    );
}