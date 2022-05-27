import React, { useEffect } from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import HomeNavigation from './Utils/HomeNavigation/HomeNavigation';
import { Grid } from '@mui/material';
import StockNavigation from './Utils/StockNavigation/StockNavigation';
import DataStock from './Utils/DataStock/DataStock';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import Loading from '../Loading';
import CustomStockSummary from './Utils/CustomStockSummary/CustomStockSummary';
import CustomInvested from './Utils/CustomInvested/CustomInvested';
import CustomTable from './Utils/CustomTable/CustomTable';

const HomeLogged = () => {

    var popular = ['TSLA', 'APPL', 'NIO', 'COIN', 'PTON', 'NFLX', 'FB', 'GOOGL', 'PLTR', 'NVDA', 'AMAZON', 'MSFT', 'RIVN'];
    var us_stocks = ['PLTR', 'NKE', 'MCD', 'KO', 'DIS', 'WMT', 'IBM', 'VZ', 'CRM', 'FDX'];
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    const [priceClicked, setPriceClicked] = React.useState(null);
    var stock_symbols = ['MSFT', 'AMZN', 'TSLA', 'NFLX', 'AMD', 'NVDA', 'INTC', 'FB', 'F', 'NIO', 'BABA'];
    const [datas, setDatas] = React.useState([]);
    const [valueAccount, setValueAccount] = React.useState(0.0);

    function get_values() {
        fetch("http://127.0.0.1:5002/get-funds/matteovkt@gmail.com", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then((data) => {
                if (data.status === 200) {
                    data.json().then((message) => {
                        setValueAccount(message['value']);
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

    function get_stocks() {
        if (buttonHomeClicked == 'mywatchlist') {
            fetch("http://127.0.0.1:5001/get-list-stock-price", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    stock_list: stock_symbols,
                }),
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            setDatas(message['message']);
                            if (buttonStockClicked === null) {
                                setButtonStockClicked('MSFT');
                                setPriceClicked(20);
                            }
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

        if (buttonHomeClicked == 'popular') {
            fetch("http://127.0.0.1:5001/get-list-stock-price", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    stock_list: popular,
                }),
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            setDatas(message['message']);
                            if (buttonStockClicked === null) {
                                setButtonStockClicked('MSFT');
                                setPriceClicked(20);
                            }
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
    }

    const [time, setTime] = React.useState(0);
    React.useEffect(() => {
        const timer = setTimeout(() => {
            setTime(time + 1);
            get_stocks();
            get_values();
        }, 100);
        return () => {
            clearTimeout(timer);
        };
    }, [time]);


    if (datas.length === 0) {
        return (
            <div>
                <Loading />
            </div>
        )
    }
    else {
        return (
            <div className='mainDivLogged'>
                <Header
                    accountValue={valueAccount}
                />
                <div className="firstDivLogged">
                    <Grid direction="row" container spacing={1}>
                        <Grid item >
                            <Navigation
                                buttonClicked={buttonClicked}
                                setButtonClicked={setButtonClicked}
                            />
                        </Grid>
                        {(buttonClicked === 'home') &&
                            <div>
                                <Grid item>
                                    <HomeNavigation
                                        buttonHomeClicked={buttonHomeClicked}
                                        setButtonHomeClicked={setButtonHomeClicked}
                                    />
                                </Grid>
                                <Grid item>
                                    <StockNavigation
                                        buttonStockClicked={buttonStockClicked}
                                        setButtonStockClicked={setButtonStockClicked}
                                        priceClicked={priceClicked}
                                        setPriceClicked={setPriceClicked}
                                        data={datas}
                                        buttonHomeClicked={buttonHomeClicked}
                                    />
                                </Grid>
                                <Grid item >
                                    <DataStock
                                        buttonStockClicked={buttonStockClicked}
                                        priceClicked={priceClicked}
                                    />
                                </Grid>
                            </div>
                        }

                        {(buttonClicked === 'pie') &&
                            <div>
                                <Grid item>
                                    <CustomStockSummary data={datas}></CustomStockSummary>
                                </Grid>
                                <Grid item>
                                <CustomInvested
                                        buttonStockClicked={buttonStockClicked}
                                        setButtonStockClicked={setButtonStockClicked}
                                        priceClicked={priceClicked}
                                        setPriceClicked={setPriceClicked}
                                        data={datas}
                                        buttonHomeClicked={buttonHomeClicked}
                                    />
                                </Grid>
                                <Grid item >
                                    <DataStock
                                        buttonStockClicked={buttonStockClicked}
                                        priceClicked={priceClicked}
                                    />
                                </Grid>
                            </div>
                        }

                        {(buttonClicked === 'search') &&
                            <div>
                                <CustomTable></CustomTable>
                            </div>
                        }

                        {(buttonClicked === 'notification') &&
                            <div>
                            </div>
                        }


                    </Grid>
                </div>
            </div>
        );
    }
}

export default HomeLogged;