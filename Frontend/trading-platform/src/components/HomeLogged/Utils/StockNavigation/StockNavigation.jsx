import "./StockNavigation.css";
import React from "react";
import { Button, Typography } from "@mui/material";

export default function StockNavigation({ buttonStockClicked, setButtonStockClicked, priceClicked, setPriceClicked, data, datasPopular, datasRecommendation, buttonHomeClicked }) {

    function clickButton(key, price) {
        setButtonStockClicked(key);
        setPriceClicked(price);
    }

    if (buttonHomeClicked === 'mywatchlist') {
        if (data.length !== 0) {
            return (
                <div className="navigationStock">
                    <div id="firstDivNavigationStock">
                        {data.map(item =>
                        (
                            <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationStockLogged' : 'buttonNavigationStockLogged'}>
                                <img id='imgNavigationStockLogged' src={item.logo} alt={item.stock_symbol} ></img>
                                <Typography id='nameStockNavigation'>
                                    {item.company_name}
                                </Typography>
                                <Typography style={{ position: 'absolute', right: '50px', color: '#2AAA8A', fontSize: '25px' }}>
                                    {parseInt(item.price)}
                                </Typography>
                                <Typography style={{ color: '#2AAA8A', position: 'absolute', fontSize: '15px', right: '20px', bottom: '20px' }}>
                                    .{Number((item.price - parseInt(item.price))).toFixed(2).toString().split(".")[1]}$
                                </Typography>
                            </Button>
                        )
                        )}
                    </div>
                </div>
            )
        }
        else {
            return (
                <div>
                    <Typography style={{ position: 'absolute', marginTop: '300px', marginLeft: '800px', fontSize: '20px', fontWeight: 'bold' }}>No stock in wishlist</Typography>
                </div>
            )
        }
    }
    else if (datasPopular.length !== 0 && buttonHomeClicked === 'popular') {
        return (
            <div className="navigationStock">
                <div id="firstDivNavigationStock">
                    {datasPopular.map(item =>
                    (
                        <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationStockLogged' : 'buttonNavigationStockLogged'}>
                            <img id='imgNavigationStockLogged' src={item.logo} alt={item.stock_symbol} ></img>
                            <Typography id='nameStockNavigation'>
                                {item.company_name}
                            </Typography>
                            <Typography style={{ position: 'absolute', right: '50px', color: '#2AAA8A', fontSize: '25px' }}>
                                {parseInt(Number(item.price).toFixed(2))}
                            </Typography>
                            <Typography style={{ color: '#2AAA8A', position: 'absolute', fontSize: '15px', right: '20px', bottom: '20px' }}>
                                .{Number((Number(item.price).toFixed(2) - parseInt(Number(item.price).toFixed(2)))).toFixed(2).toString().split(".")[1]}$
                            </Typography>
                        </Button>
                    )
                    )}
                </div>
            </div>
        )
    }
    else if (buttonHomeClicked === 'recommended') {
        if (datasRecommendation.length !== 0) {
            return (
                <div className="navigationStock">
                    <div id="firstDivNavigationStock">
                        {datasRecommendation.map(item =>
                        (
                            <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationStockLogged' : 'buttonNavigationStockLogged'}>
                                <img id='imgNavigationStockLogged' src={item.logo} alt={item.stock_symbol} ></img>
                                <Typography id='nameStockNavigation'>
                                    {item.company_name}
                                </Typography>
                                <Typography style={{ position: 'absolute', right: '50px', color: '#2AAA8A', fontSize: '25px' }}>
                                    {parseInt(item.price)}
                                </Typography>
                                <Typography style={{ color: '#2AAA8A', position: 'absolute', fontSize: '15px', right: '20px', bottom: '20px' }}>
                                    .{Number((item.price - parseInt(item.price))).toFixed(2).toString().split(".")[1]}$
                                </Typography>
                            </Button>
                        )
                        )}
                    </div>
                </div>
            )
        }
        else {
            return(
                <Typography style={{ position: 'absolute', marginTop: '300px', marginLeft: '800px', fontSize: '20px', fontWeight: 'bold' }}>No recommendation for you</Typography>

            )
        }

    }
}