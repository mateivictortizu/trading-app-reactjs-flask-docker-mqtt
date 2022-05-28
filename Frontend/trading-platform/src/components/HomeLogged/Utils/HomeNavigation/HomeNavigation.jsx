import "./HomeNavigation.css";
import React from "react";
import { Button } from "@mui/material";

export default function HomeNavigation({setTime, buttonHomeClicked, setButtonHomeClicked }) {

    function clickMyWatchlist() {
        setTime(0);
        setButtonHomeClicked('mywatchlist');
    }

    function clickPopular() {
        setTime(0);
        setButtonHomeClicked('popular');
    }

    return (
        <div className="navigationHome">
            <Button id={!(buttonHomeClicked === 'mywatchlist') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickMyWatchlist}>My Watchlist</Button>

            <Button id={!(buttonHomeClicked === 'popular') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickPopular}>Popular</Button>
        </div>
    );

}