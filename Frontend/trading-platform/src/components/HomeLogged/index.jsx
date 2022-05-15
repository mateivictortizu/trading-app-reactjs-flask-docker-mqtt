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
    var stock_symbols = ['MSFT', 'AMZN', 'TSLA', 'NFLX', 'AMD', 'NVDA', 'INTC', 'FB', 'F', 'NIO'];
    const [datas, setDatas] = React.useState([]);

    async function get_stocks() {
        await new Promise(r => setTimeout(r, 4000));
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
                            setButtonStockClicked(message['message'][0].stock_symbol);
                            setPriceClicked(message['message'][0].price);
                        }
                    });

                } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    data.json().then(() => {
                        console.log('Error');
                    });
                } else {
                    throw new Error("Internal server error");
                }
            });
    };

    get_stocks();

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
                <Header />
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