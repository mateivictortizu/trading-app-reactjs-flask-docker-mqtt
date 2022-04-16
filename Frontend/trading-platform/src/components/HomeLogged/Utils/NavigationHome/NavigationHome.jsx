import "./NavigationHome.css";
import React from "react";
import { Button } from "@mui/material";

export default function NavigationHome() {
    const [buttonClicked, setButtonClicked] = React.useState('mywatchlist');

    function clickMyWatchlist()
    {
        setButtonClicked('mywatchlist');
    }

    function clickPopular()
    {
        setButtonClicked('popular');
    }

    function clickUSStocks()
    {
        setButtonClicked('us_stocks');
    }

    function clickNewPlatform()
    {
        setButtonClicked('new_on_platform');
    }


    return(
        <div className="navigationHome">
            {!(buttonClicked==='mywatchlist') ? (
                <Button id='buttonNavigationHomeLogged' onClick={clickMyWatchlist}>My Watchlist</Button>
            ) : (
                <Button id='buttonClickedNavigationHomeLogged' onClick={clickMyWatchlist}>My Watchlist</Button>
            )}

            {!(buttonClicked==='popular') ? (
                <Button id='buttonNavigationHomeLogged' onClick={clickPopular}>Popular</Button>
            ) : (
                <Button id='buttonClickedNavigationHomeLogged' onClick={clickPopular}>Popular</Button>
            )}

            {!(buttonClicked=='us_stocks') ? (
                <Button id='buttonNavigationHomeLogged' onClick={clickUSStocks}>US Stocks</Button>
            ) : (
                <Button id='buttonClickedNavigationHomeLogged' onClick={clickUSStocks}>US Stocks</Button>
            )}

            {!(buttonClicked=='new_on_platform') ? (
                <Button id='buttonNavigationHomeLogged' onClick={clickNewPlatform}>New On Platform</Button>
            ) : (
                <Button id='buttonClickedNavigationHomeLogged' onClick={clickNewPlatform}>New On Platform</Button>
            )}
        </div>
    );

}