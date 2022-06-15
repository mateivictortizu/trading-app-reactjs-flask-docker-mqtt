import React, { useEffect } from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import HomeNavigation from './Utils/HomeNavigation/HomeNavigation';
import { Grid } from '@mui/material';
import StockNavigation from './Utils/StockNavigation/StockNavigation';
import DataStock from './Utils/DataStock/DataStock';
import { useCookies } from 'react-cookie';
import Loading from '../Loading';
import CustomInvested from './Utils/CustomInvested/CustomInvested';
import CustomTable from './Utils/CustomTable/CustomTable';
import socketIOClient from "socket.io-client";

const HomeLogged = () => {

    var popular = ['AAPL', 'TSLA', 'APPL', 'NIO', 'COIN', 'PTON', 'NFLX', 'FB', 'GOOGL', 'PLTR', 'NVDA', 'AMAZON', 'MSFT', 'RIVN'];
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    const [priceClicked, setPriceClicked] = React.useState(null);
    var stock_symbols = ['MSFT', 'AMZN', 'TSLA', 'NFLX', 'AMD', 'NVDA', 'INTC', 'FB', 'F', 'NIO', 'BABA'];
    const [datas, setDatas] = React.useState([]);
    const [datasPopular, setDatasPopular] = React.useState([]);
    const [valueAccount, setValueAccount] = React.useState(0.0);
    const [time, setTime] = React.useState(0);
    const [stockInfo, setStockInfo] = React.useState(null);


   function get_values() {
        fetch("http://127.0.0.1:5000/get-funds/matteovkt@gmail.com", {
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
    };


    function get_stocks(time) {
        if (buttonClicked === 'home') {
            if (buttonHomeClicked === 'mywatchlist') {
                fetch("http://127.0.0.1:5000/get-list-stock-price", {
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
                                console.log(message['message'][1]['stock_symbol'])
                                if (time === 0) {
                                    setButtonStockClicked(message['message'][0]['stock_symbol']);
                                    setPriceClicked(message['message'][0]['price']);
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

            if (buttonHomeClicked === 'popular') {
                fetch("http://127.0.0.1:5000/get-list-stock-price", {
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
                                if (time === 0) {
                                    setButtonStockClicked(message['message'][0]['stock_symbol']);
                                    setPriceClicked(message['message'][0]['price']);
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
        else if (buttonClicked == 'pie') {
            var invested = [];
            fetch("http://127.0.0.1:5000/get-list-stock-price", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    stock_list: ['AAPL'],
                }),
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            setDatas(message['message']);
                            if (time === 0) {
                                setButtonStockClicked(message['message'][0]['stock_symbol']);
                                setPriceClicked(message['message'][0]['price']);
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
};
/*
React.useEffect(() => {
    if (time === 0) {
        const timer = setTimeout(() => {
            setTime(time + 1);
            get_stocks(time);
            get_values();
        }, 0);
        return () => {
            clearTimeout(timer);
        };
    }
    else {
        const timer = setTimeout(() => {
            setTime(time + 1);
            get_stocks(time);
            get_values();
        }, 5000);
        return () => {
            clearTimeout(timer);
        };
    }
}, [time]);

*/

React.useEffect(()=>{

    const socket = socketIOClient('http://localhost:5000');
    socket.on("stock_popular", (data) => {
        console.log("Stock_popular");
        console.log(data['message']);
        setDatasPopular(data['message']);
        setButtonStockClicked(data['message'][0]['stock_symbol']);
        setPriceClicked(data['message'][0]['price']);
    });
    socket.on("stock_wishlist",(data) => {
        console.log("stock_wishlist");
        setDatas(data['message']);
        setButtonStockClicked(data['message'][0]['stock_symbol']);
        setPriceClicked(data['message'][0]['price']);
    });
    socket.on("get_funds", (data) => {
        console.log("get_funds")
        setValueAccount(data['value']);    
    });
},[])

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
                                    setTime={setTime}
                                    buttonHomeClicked={buttonHomeClicked}
                                    setButtonHomeClicked={setButtonHomeClicked}
                                />
                            </Grid>
                            <Grid item>
                                <StockNavigation
                                    buttonStockClicked={buttonStockClicked}
                                    setStockInfo={setStockInfo}
                                    setButtonStockClicked={setButtonStockClicked}
                                    priceClicked={priceClicked}
                                    setPriceClicked={setPriceClicked}
                                    data={datas}
                                    datasPopular={datasPopular}
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