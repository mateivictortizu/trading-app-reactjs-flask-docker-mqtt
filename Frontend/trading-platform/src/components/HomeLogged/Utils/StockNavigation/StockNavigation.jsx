import "./StockNavigation.css";
import React from "react";
import { Button, Typography } from "@mui/material";

export default function StockNavigation({ buttonStockClicked, setButtonStockClicked, setPriceClicked, data }) {

    function clickButton(key, price) {
        setButtonStockClicked(key);
        setPriceClicked(price);
    }

    if (data.lenght !== 0) {
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
}