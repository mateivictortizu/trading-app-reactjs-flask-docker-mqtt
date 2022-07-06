import "./CustomInvested.css";
import React from "react";
import { Button, Typography } from "@mui/material";
import CustomSummary from "../CustomSummary/CustomSummary";

export default function CustomInvested({ buttonStockClicked, setButtonStockClicked, setPriceClicked, dataForInvest, dataUserInvest, investValue }) {

    function clickButton(key, price) {
        setButtonStockClicked(key);
        setPriceClicked(price);
    }
    
    var current_value = 0;

    if (dataForInvest.length !== 0) {
        for (const i in dataForInvest) {
            current_value = current_value + dataUserInvest[dataForInvest[i]['stock_symbol']]['cantitate'] * dataForInvest[i]['price'];
        }
        return (
            <div>
                <div id='customInvested'>
                    <CustomSummary average={investValue} current_value={current_value}> </CustomSummary>


                    <div id="firstDivNavigationInvested">
                        {dataForInvest.map(item =>
                            (dataUserInvest[item.stock_symbol]['cantitate'].toFixed(2) > 0) && (
                                <Button key={item.stock_symbol} onClick={() => clickButton(item.stock_symbol, item.price)} id={(buttonStockClicked === item.stock_symbol) ? 'buttonClickedNavigationInvestedLogged' : 'buttonNavigationInvestedLogged'}>
                                    <img id='imgNavigationInvestedLogged' src={item.logo} alt={item.stock_symbol} ></img>
                                    <Typography id='nameInvestedNavigation'>
                                        {item.company_name}
                                    </Typography >
                                    <Typography id='shareInvestedNavigation'>
                                        {dataUserInvest[item.stock_symbol]['cantitate'].toFixed(2)} shares
                                    </Typography>
                                    <Typography style={{ color: '#555', fontWeight: 'bold', position: 'absolute', fontSize: '15px', right: '20px', top: '15px' }}>${Number(dataUserInvest[item.stock_symbol]['cantitate'] * item.price).toFixed(2)}</Typography>
                                    <Typography style={{ color: (Number(dataUserInvest[item.stock_symbol]['cantitate'] * item.price - dataUserInvest[item.stock_symbol]['cantitate'] * dataUserInvest[item.stock_symbol]['price']).toFixed(2)>=0)?'#2AAA8A':'#7F0000', position: 'absolute', fontSize: '13px', right: '20px', top: '35px' }}>{Number(dataUserInvest[item.stock_symbol]['cantitate'] * item.price - dataUserInvest[item.stock_symbol]['cantitate'] * dataUserInvest[item.stock_symbol]['price']).toFixed(2)} ({Number((dataUserInvest[item.stock_symbol]['cantitate'] * item.price - dataUserInvest[item.stock_symbol]['cantitate'] * dataUserInvest[item.stock_symbol]['price']) / (dataUserInvest[item.stock_symbol]['cantitate'] * dataUserInvest[item.stock_symbol]['price']) * 100).toFixed(2)}%)</Typography>
                                </Button>
                            )
                        )}
                    </div>
                </div>
            </div>
        )
    }
    else
    {
        return (
            <div>
                <div id='customInvested'>
                    <CustomSummary average={investValue} current_value={current_value}> </CustomSummary>


                    <div id="firstDivNavigationInvested">
                        <Typography align="center" style={{marginTop:'40px', fontSize:'30px', marginBottom:'40px', color:'#656565'}}>No investment</Typography>
                    </div>
                </div>
            </div>
        )
    }
}