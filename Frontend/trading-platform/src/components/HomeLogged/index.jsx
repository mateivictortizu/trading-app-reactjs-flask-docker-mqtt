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
import Cookies from 'js-cookie';

const HomeLogged = () => {

    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const [cookiesJWT, setCookieJWT, removeCookieJWT] = useCookies(['jwt']);
    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    const [priceClicked, setPriceClicked] = React.useState(null);
    const [datas, setDatas] = React.useState([]);
    const [datasInvest, setDatasInvest]= React.useState([]);
    const [datasPopular, setDatasPopular] = React.useState([]);
    const [valueAccount, setValueAccount] = React.useState(0.0);
    const [stockInfo, setStockInfo] = React.useState(null);
    const [statisticData, setStatisticData]=React.useState([0,0]);
    const [rows, setRows] = React.useState([]);
    const [invest,setInvest] = React.useState([]);

React.useEffect(()=>{
    const socket = socketIOClient('http://localhost:5000',{ withCredentials: true});
    socket.on("stock_popular", (data) => {
        setDatasPopular(data['message']);
        if(buttonHomeClicked==='popular')
        {
            setButtonStockClicked(data['message'][0]['stock_symbol']);
            setPriceClicked(data['message'][0]['price']);
        }
    });
    socket.on("stock_wishlist",(data) => {
        console.log("stock_wishlist");
        console.log(socket);
        setDatas(data['message']);
        if(buttonHomeClicked==='mywatchlist')
        {
            setButtonStockClicked(data['message'][0]['stock_symbol']);
            setPriceClicked(data['message'][0]['price']);
        }
    });
    socket.on("stock_invest",(data) => {
        console.log("stock_invest");
        console.log(socket);
        setDatasInvest(data['message']);
    });
    socket.on("invest_on", (data)=>{
        setInvest(data);
    });
    socket.on("statisticData", (data)=>{
        setStatisticData(data);
    });
    socket.on("get_funds", (data) => {
        console.log("get_funds");
        setValueAccount(data['value']);    
    });
    socket.on("get_investment", (data)=>{
        console.log('get_investment');
        console.log([data['medie'], data['cantitate']]);
        setStatisticData([data['medie'], data['cantitate']]);
    });

    socket.on("get_session", (data)=>{
        console.log(data);
    });

    socket.on("get_all_stocks",(data) => {
        console.log("get_funds");
        setRows(data['value']);    
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
                                    buttonHomeClicked={buttonHomeClicked}
                                    setButtonHomeClicked={setButtonHomeClicked}
                                    datas={datas}
                                    datasPopular={datasPopular}
                                    setPriceClicked={setPriceClicked}
                                    setButtonStockClicked={setButtonStockClicked}
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
                                    statisticData={statisticData} 
                                    setStatisticData={setStatisticData}
                                    invested = {invest}
                                    setInvested={setInvest}
                                    valueAccount={valueAccount}
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
                                    data={datasInvest}
                                    buttonHomeClicked={buttonHomeClicked}
                                />
                            </Grid>
                            <Grid item >
                                <DataStock
                                    buttonStockClicked={buttonStockClicked}
                                    priceClicked={priceClicked}
                                    statisticData={statisticData} 
                                    setStatisticData={setStatisticData}
                                    invested = {invest}
                                    setInvested={setInvest}
                                    valueAccount={valueAccount}
                                />
                            </Grid>
                        </div>
                    }

                    {(buttonClicked === 'search') &&
                        <div>
                            <CustomTable rows={rows}></CustomTable>
                        </div>
                    }

                </Grid>
            </div>
        </div>
    );
}
}

export default HomeLogged;