import "./HomeNavigation.css";
import React from "react";
import { Button } from "@mui/material";

export default function HomeNavigation({ buttonHomeClicked, setButtonHomeClicked, datas, datasPopular, datasRecommendation, setPriceClicked,setButtonStockClicked}) {

    function clickMyWatchlist() {
        setButtonHomeClicked('mywatchlist');
        if(datas.length!==0)
        {
            setPriceClicked(datas[0]['price']);
            setButtonStockClicked(datas[0]['stock_symbol']);
        }
        else
        {
            setPriceClicked(null);
            setButtonStockClicked(null);
        }
    }

    function clickPopular() {
        setButtonHomeClicked('popular');
        if(datasPopular.length!==0)
        {
            setPriceClicked(datasPopular[0]['price']);
            setButtonStockClicked(datasPopular[0]['stock_symbol']);
    
        }
        else
        {
            setPriceClicked(null);
            setButtonStockClicked(null);
        }
    }

    function clickRecommended() {
        setButtonHomeClicked('recommended');
        if(datasRecommendation.length !==0)
        {
            setPriceClicked(datasRecommendation[0]['price']);
            setButtonStockClicked(datasRecommendation[0]['stock_symbol']);
        }
        else
        {
            setPriceClicked(null);
            setButtonStockClicked(null);
        }
    }

    return (
        <div className="navigationHome">
            <Button id={!(buttonHomeClicked === 'mywatchlist') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickMyWatchlist}>My Watchlist</Button>

            <Button id={!(buttonHomeClicked === 'popular') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickPopular}>Popular</Button>
            <Button id={!(buttonHomeClicked === 'recommended') ? 'buttonNavigationHomeLogged' : 'buttonClickedNavigationHomeLogged'} onClick={clickRecommended}>Recommended</Button>
        </div>
    );

}