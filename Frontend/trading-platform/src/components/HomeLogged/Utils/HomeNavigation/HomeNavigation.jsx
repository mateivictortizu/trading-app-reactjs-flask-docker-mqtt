import "./HomeNavigation.css";
import React from "react";
import { Button } from "@mui/material";

export default function HomeNavigation({buttonHomeClicked, setButtonHomeClicked}) {

    function clickMyWatchlist()
    {
        setButtonHomeClicked('mywatchlist');
    }

    function clickPopular()
    {
        setButtonHomeClicked('popular');
    }

    function clickUSStocks()
    {
        setButtonHomeClicked('us_stocks');
    }

    function clickNewPlatform()
    {
        setButtonHomeClicked('new_on_platform');
    }


    return(
        <div className="navigationHome">
            <Button id={!(buttonHomeClicked==='mywatchlist')?'buttonNavigationHomeLogged':'buttonClickedNavigationHomeLogged'} onClick={clickMyWatchlist}>My Watchlist</Button>
            
            <Button id={!(buttonHomeClicked==='popular') ?'buttonNavigationHomeLogged':'buttonClickedNavigationHomeLogged'} onClick={clickPopular}>Popular</Button>
        
            <Button id={!(buttonHomeClicked=='us_stocks')?'buttonNavigationHomeLogged':'buttonClickedNavigationHomeLogged'} onClick={clickUSStocks}>US Stocks</Button>
          
            <Button id={!(buttonHomeClicked=='new_on_platform') ?'buttonNavigationHomeLogged':'buttonClickedNavigationHomeLogged'} onClick={clickNewPlatform}>New On Platform</Button>

        </div>
    );

}