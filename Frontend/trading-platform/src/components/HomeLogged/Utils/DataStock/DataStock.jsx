import './DataStock.css';
import React, { useEffect } from "react";
import { Typography } from '@mui/material';
import { Button } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';

export default function DataStock({ buttonStockClicked, priceClicked }) {
    const [stockInfo, setStockInfo] = React.useState(null);

    useEffect(() => {
        if (buttonStockClicked !== null) {
            fetch("http://127.0.0.1:5001/get-stock-info/" + buttonStockClicked, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            setStockInfo(message);
                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then(() => {
                            console.log('Error');
                        });
                    } else {
                        console.log('Error');
                    }
                });
        }
    }, [buttonStockClicked, priceClicked]);

    if (stockInfo === null) {
        return (<div></div>)
    }
    else {
        return (
            <div className="dataStock">
                <div id="firstDivDataStock">
                    <img id='imgDataStock' src={stockInfo.logo} alt={stockInfo.company_name}></img>
                    <Typography id='stockName'>{stockInfo.company_name}</Typography>
                    <Typography id='stockDetails'>{stockInfo.stock_symbol} · STOCK · US  </Typography>
                    <div id='buttonsDivDataStock'>
                        <Button id='buttonDataStock'>Sell</Button>
                        <Button id='buttonDataStock'>Buy</Button>
                    </div>
                    <Typography id='priceDataStock'>${priceClicked.toFixed(2)}</Typography>
                    <CustomGraphics />
                </div>
                <div style={{ backgroundColor: '#ecedf1', height: '20px' }}></div>
                <div id="otherDivDataStock">
                    <Typography style={{ fontSize: '30px', color: 'gray', left: '40px', position: 'relative', top: '10px', marginBottom: '20px' }}>Company details</Typography>
                    <hr style={{ backgroundColor: 'gray', color: 'gray', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography style={{ fontSize: '15px', color: 'gray', margin: '40px', position: 'relative', top: '10px' }}>{stockInfo.longBusinessSummary}</Typography>
                </div>
                <div style={{ backgroundColor: '#ecedf1', height: '20px' }}></div>
                <div id="otherDivDataStock">
                    <Typography style={{ fontSize: '30px', color: 'gray', left: '40px', position: 'relative', top: '10px', marginBottom: '20px' }}>Instrument details</Typography>

                    <hr style={{ backgroundColor: 'gray', color: 'gray', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography style={{ fontSize: '15px', color: 'gray', margin: '40px', position: 'relative', top: '10px' }}>{stockInfo.longBusinessSummary}</Typography>

                </div>
            </div>
        )
    }
}