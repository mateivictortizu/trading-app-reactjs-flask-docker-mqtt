import React from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import HomeNavigation from './Utils/HomeNavigation/HomeNavigation';
import { Grid } from '@mui/material';
import StockNavigation from './Utils/StockNavigation/StockNavigation';
import DataStock from './Utils/DataStock/DataStock';
import Loading from '../Loading';
import CustomInvested from './Utils/CustomInvested/CustomInvested';
import CustomTable from './Utils/CustomTable/CustomTable';
import socketIOClient from "socket.io-client";
import {GATEWAY_HOST} from '../../Utils/Extra/Hosts';

const HomeLogged = () => {

    const [pendingInvest, setPendingInvest] = React.useState([]);
    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('popular');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    const [priceClicked, setPriceClicked] = React.useState(null);
    const [datas, setDatas] = React.useState([]);
    const [datasForInvest, setDatasInvest]= React.useState([]);
    const [dataUserInvest, setdataUserInvest]= React.useState([]);
    const [datasPopular, setDatasPopular] = React.useState([]);
    const [valueAccount, setValueAccount] = React.useState(0.0);
    const [stockInfo, setStockInfo] = React.useState(null);
    const [statisticData, setStatisticData]=React.useState([0,0]);
    const [rows, setRows] = React.useState([]);
    const [invest,setInvest] = React.useState([]);
    const [valueInvest, setValueInvest]=React.useState(0);
    const [recommendationValue, setRecommendationValue]=React.useState([]);
    const [showApp,setShowApp] = React.useState(true);
    var check=0;


React.useEffect(()=>{
    const socket = socketIOClient(GATEWAY_HOST,{ withCredentials: true});
    socket.on("stock_popular", (data) => {
        setDatasPopular(data['message']);
        if(buttonHomeClicked==='popular')
        {
            if(check===0)
            {   
                check=check+1;
                setButtonStockClicked(data['message'][0]['stock_symbol']);
                setPriceClicked(data['message'][0]['price']);
            }
        }
    });
    socket.on("stock_wishlist",(data) => {
        setDatas(data['message']);
        if(buttonHomeClicked==='mywatchlist')
        {
            if(check===0)
            {   
                check=check+1;
                setButtonStockClicked(data['message'][0]['stock_symbol']);
                setPriceClicked(data['message'][0]['price']);
            }
        }
    });
    socket.on("stock_invest",(data) => {
        setDatasInvest(data['message']);

    });
    socket.on("invest_on", (data)=>{
        setInvest(data);
    });
    socket.on("statisticData", (data)=>{
        setStatisticData(data);
    });
    socket.on("get_funds", (data) => {
        setValueAccount(data['value']);    
    });
    socket.on("get_investment", (data)=>{
        setStatisticData([data['medie'], data['cantitate']]);
    });

    socket.on("get_invest_value_of_account", (data)=>{
        setValueInvest(data);
    });

    socket.on("get_all_stocks",(data) => {
        setRows(data['value']);    
    });

    socket.on("detailed_user_invests",(data) => {
        setdataUserInvest(data);

    });
    socket.on("recommendation",(data) => {
        setRecommendationValue(data['message']);
    });
},[])

if (datasPopular.length === 0 || showApp === false) {
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
                investValue={valueInvest}
            />
            <div className="firstDivLogged">
                <Grid direction="row" container spacing={1}>
                    <Grid item >
                        <Navigation
                            buttonClicked={buttonClicked}
                            setButtonClicked={setButtonClicked}
                            dataForInvest={datasForInvest}
                            datasRecommendation={recommendationValue}
                            datasPopular={datasPopular}
                            datas={datas}
                            buttonHomeClicked={buttonHomeClicked}
                            setPriceClicked={setPriceClicked}
                            setButtonStockClicked={setButtonStockClicked}
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
                                    datasRecommendation={recommendationValue}
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
                                    datasRecommendation={recommendationValue}
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
                                    pendingInvest={pendingInvest} 
                                    setPendingInvest={setPendingInvest}
                                    setShowApp={setShowApp}
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
                                    dataForInvest={datasForInvest}
                                    dataUserInvest={dataUserInvest}
                                    buttonHomeClicked={buttonHomeClicked}
                                    investValue={valueInvest}
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
                                    pendingInvest={pendingInvest} 
                                    setPendingInvest={setPendingInvest}
                                    setShowApp={setShowApp}
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