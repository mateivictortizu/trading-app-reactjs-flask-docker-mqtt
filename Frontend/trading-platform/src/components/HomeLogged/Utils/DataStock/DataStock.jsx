import './DataStock.css';
import React, { useEffect } from "react";
import { Typography } from '@mui/material';
import { Button } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';
import HistoryIcon from '@mui/icons-material/History';
import { CustomBuy } from '../CustomBuy/CustomBuy';

export default function DataStock({ buttonStockClicked, priceClicked, Transition }) {
    const [stockInfo, setStockInfo] = React.useState(null);
    const [period, setPeriod] = React.useState('1D');
    const [openBuy, setOpenBuy] = React.useState(false);
    var graphics = null;
    var change = null;
    var stock = null;
    var first_value = null;
    var last_value = null;
    var difference = null;
    var procent = null;


    var shares = 1.5;
    var avg_price = 400;

    function handleOpenBuy() {
        setOpenBuy(true);
    };

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
        if (period === '1D') {
            stock = JSON.parse(stockInfo.one_day);
            first_value = stock[0];
            last_value = stock[stock.length - 1];
            difference = last_value['y'] - first_value['y'];
            procent = ((difference / first_value['y']) * 100).toFixed(2);
            difference = difference.toFixed(2);
            if (procent >= 0)
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#2AAA8A'} />;
            else
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#7F0000'} />;
            if (procent >= 0)
                change = <Typography id='changeDataStock'> <span style={{ color: '#2AAA8A', fontWeight: 'bold' }}>{difference} ({procent}%) </span> TODAY</Typography>
            else
                change = <Typography id='changeDataStock'> <span style={{ color: '#7F0000', fontWeight: 'bold' }}>{difference} ({procent}%) </span> TODAY</Typography>
        }
        else if (period === '1M') {
            stock = JSON.parse(stockInfo.one_month);
            first_value = stock[0];
            last_value = stock[stock.length - 1];
            difference = last_value['y'] - first_value['y'];
            procent = ((difference / first_value['y']) * 100).toFixed(2);
            difference = difference.toFixed(2);
            if (procent >= 0)
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#2AAA8A'} />;
            else
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#7F0000'} />;
            if (procent >= 0)
                change = <Typography id='changeDataStock'> <span style={{ color: '#2AAA8A', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST MONTH</Typography>
            else
                change = <Typography id='changeDataStock'> <span style={{ color: '#7F0000', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST MONTH</Typography>
        }
        else if (period === '3M') {
            stock = JSON.parse(stockInfo.three_month);
            first_value = stock[0];
            last_value = stock[stock.length - 1];
            difference = last_value['y'] - first_value['y'];
            procent = ((difference / first_value['y']) * 100).toFixed(2);
            difference = difference.toFixed(2);
            if (procent >= 0)
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#2AAA8A'} />;
            else
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#7F0000'} />;
            if (procent >= 0)
                change = <Typography id='changeDataStock'> <span style={{ color: '#2AAA8A', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST 3 MONTHS</Typography>
            else
                change = <Typography id='changeDataStock'> <span style={{ color: '#7F0000', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST 3 MONTHS</Typography>
        }
        else if (period === '6M') {
            stock = JSON.parse(stockInfo.six_month);
            first_value = stock[0];
            last_value = stock[stock.length - 1];
            difference = last_value['y'] - first_value['y'];
            procent = ((difference / first_value['y']) * 100).toFixed(2);
            difference = difference.toFixed(2);
            if (procent >= 0)
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#2AAA8A'} />;
            else
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#7F0000'} />;
            if (procent >= 0)
                change = <Typography id='changeDataStock'> <span style={{ color: '#2AAA8A', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST 6 MONTHS</Typography>
            else
                change = <Typography id='changeDataStock'> <span style={{ color: '#7F0000', fontWeight: 'bold' }}>{difference} ({procent}%) </span> LAST 6 MONTHS</Typography>

        }
        else if (period === 'max') {
            stock = JSON.parse(stockInfo.maxim);
            first_value = stock[0];
            last_value = stock[stock.length - 1];
            difference = last_value['y'] - first_value['y'];
            procent = ((difference / first_value['y']) * 100).toFixed(2);
            difference = difference.toFixed(2);
            if (procent >= 0)
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#2AAA8A'} />;
            else
                graphics = <CustomGraphics name={stockInfo.stock_symbol} margin={'200px'} datas={stock} setPeriod={setPeriod} period={period} color={'#7F0000'} />;
            if (procent >= 0)
                change = <Typography id='changeDataStock'> <span style={{ color: '#2AAA8A', fontWeight: 'bold' }}>{difference} ({procent}%) </span> SINCE START</Typography>
            else
                change = <Typography id='changeDataStock'> <span style={{ color: '#7F0000', fontWeight: 'bold' }}>{difference} ({procent}%) </span> SINCE START</Typography>
        }

        return (
            <div className="dataStock">
                <CustomBuy openBuy={openBuy} setOpenBuy={setOpenBuy} Transition={Transition} stockName={stockInfo.company_name} price={priceClicked.toFixed(2)} logo={stockInfo.logo}></CustomBuy>
                <div id="firstDivDataStock">
                    <img id='imgDataStock' src={stockInfo.logo} alt={stockInfo.company_name}></img>
                    <Typography id='stockName'>{stockInfo.company_name}</Typography>
                    <Typography id='stockDetails'>{stockInfo.stock_symbol} · STOCK · US  </Typography>
                    <div id='buttonsDivDataStock'>
                        <Button id='buttonDataStock'>Sell</Button>
                        <Button id='buttonDataStock' onClick={handleOpenBuy}>Buy</Button>
                    </div>
                    <Typography id='priceDataStock'>${priceClicked.toFixed(2)}</Typography>
                    {change}
                    {graphics}
                </div>
                <div id='brDivDataStock'></div>
                <div id='otherDivDataStock'>
                    <Typography id='titleDivDataStock'>Your investment</Typography>
                    <br />
                    <Typography style={{ fontSize: '18px', fontWeight: 'bold', color: 'black', position: 'relative' }}> <span style={{ marginLeft: '40px' }}>{shares} shares</span> <span style={{ fontSize: '18px', color: 'black', fontWeight: 'bold', marginRight: '30px', right: '30px', position: 'absolute' }}>${priceClicked * shares}</span></Typography>
                    <br />
                    <hr style={{ backgroundColor: '#E8E8E8', height: 1, width: '95%', margin: 'auto' }} />
                    <br />
                    <Typography style={{ fontSize: '12px', color: 'gray', fontWeight: 'bold' }}><span style={{ marginLeft: '40px' }}>AVERAGE PRICE</span> <span id='instrumentInvestmentsRightDataStock'>SELL PRICE</span> <span id='instrumentDetailsRightDataStock'>RETURN</span></Typography>
                    <Typography style={{ color: 'black', fontWeight: 'bold' }}><span style={{ marginLeft: '40px' }}>${avg_price}</span> <span id='instrumentInvestmentsRightDataStock'>${priceClicked.toFixed(2)}</span> <span id='instrumentDetailsRightDataStock'>{(priceClicked * shares - avg_price * shares).toFixed(2)}</span></Typography>
                    <br />
                </div>
                <div id='brDivDataStock'></div>
                <div id="otherDivDataStock">
                    <Typography id='titleDivDataStock'>Company details</Typography>
                    <Typography style={{ fontSize: '15px', color: '#4E4F50', margin: '40px', position: 'relative' }}>{stockInfo.longBusinessSummary}</Typography>
                </div>
                <div id='brDivDataStock'></div>
                <div id="otherDivDataStock">
                    <Typography id='titleDivDataStock'>Instrument details</Typography>
                    <hr style={{ backgroundColor: '#E8E8E8', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography id='detailsDataStock'><span style={{ marginLeft: '20px' }}>Name</span> <span id='instrumentDetailsRightDataStock'>{stockInfo.company_name}</span></Typography>
                    <hr style={{ backgroundColor: '#E8E8E8', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography id='detailsDataStock'><span style={{ marginLeft: '20px' }}>Market name</span> <span id='instrumentDetailsRightDataStock'>NYSE</span></Typography>
                    <hr style={{ backgroundColor: '#E8E8E8', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography id='detailsDataStock'><span style={{ marginLeft: '20px' }}>Currency</span> <span id='instrumentDetailsRightDataStock'>USD</span></Typography>
                    <hr style={{ backgroundColor: '#E8E8E8', height: 1, width: '95%', margin: 'auto' }} />
                    <Typography id='detailsDataStock'><span style={{ marginLeft: '20px' }}>ISIN</span> <span id='instrumentDetailsRightDataStock'>{stockInfo.isin}</span></Typography>
                </div>
                <div id='brDivDataStock'></div>
                <div>
                    <Button variant="outlined" id='buttonHistory'><HistoryIcon style={{ color: '#4E4F50' }}></HistoryIcon>&nbsp;History</Button>
                </div>
            </div>
        )
    }
}