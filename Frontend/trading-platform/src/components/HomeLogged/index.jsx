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

const HomeLogged = () => {

    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    const [priceClicked, setPriceClicked] = React.useState(null);
    var stock_symbols = ['MSFT', 'AMZN', 'TSLA', 'NFLX', 'AMD', 'NVDA', 'INTC', 'FB', 'F', 'NIO', 'BABA'];
    const [datas, setDatas] = React.useState([]);
    const [valueAccount, setValueAccount] = React.useState(0.0);


    async function get_stocks() {
        setTimeout(() => {
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
                        });
        
                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then(() => {
                            console.log('Error');
                        });
                    } else {
                        console.log('Error');
                    }
                });
            get_stocks();
        }, 4000);
    };

    async function get_funds() {
        setTimeout(() => {
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
            get_funds();
        }, 2000);
    };

    if (datas.length === 0) {
        get_stocks();
        get_funds();
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
                            </div>
                        }
                        {(buttonClicked === 'home') &&
                            <div>
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
                            </div>
                        }
                        <Grid item >
                            <DataStock
                                buttonStockClicked={buttonStockClicked}
                                priceClicked={priceClicked}
                            />
                        </Grid>
                    </Grid>
                </div>
            </div>
        );
    }
}

export default HomeLogged;