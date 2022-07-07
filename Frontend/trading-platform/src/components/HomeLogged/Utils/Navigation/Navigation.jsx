import "./Navigation.css";
import React from "react";
import { Button } from "@mui/material";
import HomeIcon from '@mui/icons-material/Home';
import PieChartIcon from '@mui/icons-material/PieChart';
import SearchIcon from '@mui/icons-material/Search';

export default function Navigation({ buttonClicked, setButtonClicked, dataForInvest, datasRecommendation,
    datasPopular, datas, buttonHomeClicked, setPriceClicked, setButtonStockClicked }) {

    function clickHome() {
        setButtonClicked('home');
        if(buttonHomeClicked==='mywatchlist')
        {
            if (datas.length !== 0) {
                setButtonStockClicked(datas[0]['stock_symbol']);
                setPriceClicked(datas[0]['price'])
            }
            else {
                setButtonStockClicked(null);
                setPriceClicked(null);
            }
        }
        if(buttonHomeClicked==='popular')
        {
            if (datasPopular.length !== 0) {
                setButtonStockClicked(datasPopular[0]['stock_symbol']);
                setPriceClicked(datasPopular[0]['price'])
            }
            else {
                setButtonStockClicked(null);
                setPriceClicked(null);
            }
        }
        if(buttonHomeClicked==='recommended')
        {
            if (datasRecommendation.length !== 0) {
                setButtonStockClicked(datasRecommendation[0]['stock_symbol']);
                setPriceClicked(datasRecommendation[0]['price'])
            }
            else {
                setButtonStockClicked(null);
                setPriceClicked(null);
            }
        }
    }

    function clickPie() {
        setButtonClicked('pie');
        if (dataForInvest.length !== 0) {
            setButtonStockClicked(dataForInvest[0]['stock_symbol']);
            setPriceClicked(dataForInvest[0]['price'])
        }
        else {
            setButtonStockClicked(null);
            setPriceClicked(null);
        }
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