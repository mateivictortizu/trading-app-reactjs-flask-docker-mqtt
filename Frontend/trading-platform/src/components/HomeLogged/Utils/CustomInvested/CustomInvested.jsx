import "./CustomInvested.css";
import React from "react";
import { Button, Typography } from "@mui/material";
import CustomStockSummary from "../CustomStockSummary/CustomStockSummary";

export default function CustomInvested({ buttonStockClicked, setButtonStockClicked, setPriceClicked, data }) {

    function clickButton(key, price) {
        setButtonStockClicked(key);
        setPriceClicked(price);
    }

    if (data.lenght !== 0) {
        return (
            <div>
                <div id='customInvested'>
                    <CustomStockSummary data={data}></CustomStockSummary>


                    <div id="firstDivNavigationInvested">
                        {data.map(item =>
                        (
                            <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationInvestedLogged' : 'buttonNavigationInvestedLogged'}>
                                <img id='imgNavigationInvestedLogged' src={item.logo} alt={item.stock_symbol} ></img>
                                <Typography id='nameInvestedNavigation'>
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
            </div>
        )
    }
}