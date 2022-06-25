import "./CustomInvested.css";
import React from "react";
import { Button, Typography } from "@mui/material";
import CustomSummary from "../CustomSummary/CustomSummary";

export default function CustomInvested({ buttonStockClicked, setButtonStockClicked, setPriceClicked, data, investValue }) {

    function clickButton(key, price) {
        setButtonStockClicked(key);
        setPriceClicked(price);
    }

    var share=1;
    var average=100;

    if (data.lenght !== 0) {
        return (
            <div>
                <div id='customInvested'>
                    <CustomSummary average={investValue} current_value={90}> </CustomSummary>


                    <div id="firstDivNavigationInvested">
                        {data.map(item =>
                        (
                            <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationInvestedLogged' : 'buttonNavigationInvestedLogged'}>
                                <img id='imgNavigationInvestedLogged' src={item.logo} alt={item.stock_symbol} ></img>
                                <Typography id='nameInvestedNavigation'>
                                    {item.company_name}
                                </Typography >
                                <Typography id='shareInvestedNavigation'>
                                    {share} shares
                                </Typography>
                                <Typography style={{color: '#555', fontWeight: 'bold', position: 'absolute', fontSize: '15px', right: '20px', top: '15px'}}>${Number(share*item.price).toFixed(2)}</Typography>
                                <Typography style={{color: '#2AAA8A', position: 'absolute', fontSize: '13px', right: '20px', top: '35px'}}>{Number(share*item.price-share*average).toFixed(2)} ({Number((share*item.price-share*average)/(share*average)*100).toFixed(2)}%)</Typography>
                            </Button>
                        )
                        )}
                    </div>
                </div>
            </div>
        )
    }
}