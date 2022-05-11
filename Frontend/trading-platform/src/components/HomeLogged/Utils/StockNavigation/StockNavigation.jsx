import "./StockNavigation.css";
import React, { useEffect } from "react";
import { Button, Typography } from "@mui/material";

export default function StockNavigation({ buttonStockClicked, setButtonStockClicked, buttonHomeClicked, data }) {

    function clickButton(key) {
        setButtonStockClicked(key);
    }

    useEffect(() => {
        if (buttonStockClicked === null) {
            console.log(data[0]);
            setButtonStockClicked(data[0].stock_symbol);
        }
    }, []);

    if (data.lenght != 0) {
        return (
            <div className="navigationStock">
                {data.map(item =>
                (
                    <div key={item.symbol_stock}>
                        {console.log(item.stock_symbol)}
                        <Button key={item.symbol_stock} onClick={() => clickButton(item.stock_symbol)} id={(buttonStockClicked == item.symbol) ? 'buttonClickedNavigationStockLogged' : 'buttonNavigationStockLogged'}>
                            <img id='imgNavigationStockLogged' src={item.logo}></img>
                            <Typography id='nameStockNavigation'>
                                {item.company_name}
                            </Typography>
                            <Typography style={{ position: 'absolute', right: '20px', color: 'green',fontSize:'25px' }}>
                                {parseInt(item.price)}
                            </Typography>
                            <Typography style={{color: 'green', position:'relative',fontSize:'15px' }}>
                                .{Number((item.price-parseInt(item.price)).toFixed(2))}$
                            </Typography>
                        </Button>
                    </div>
                )
                )}
            </div>
        )
    }
}