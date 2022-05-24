import "./HomeNavigation.css";
import React from "react";
import { Button } from "@mui/material";

export default function HomeNavigation({ buttonHomeClicked, setButtonHomeClicked }) {

    function clickMyWatchlist() {
        setButtonHomeClicked('mywatchlist');
    }

    function clickPopular() {
        setButtonHomeClicked('popular');
    }

    return (
        <div className="navigationHome">
            <Button id={!(buttonHomeClicked === 'mywatchlist') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickMyWatchlist}>My Watchlist</Button>

            <Button id={!(buttonHomeClicked === 'popular') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickPopular}>Popular</Button>
        </div>
    );

}