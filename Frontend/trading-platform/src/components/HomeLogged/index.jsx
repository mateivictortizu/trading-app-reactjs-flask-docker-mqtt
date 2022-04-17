import React from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import HomeNavigation from './Utils/HomeNavigation/HomeNavigation';
import { Grid } from '@mui/material';
import StockNavigation from './Utils/StockNavigation/StockNavigation';
import DataStock from './Utils/DataStock/DataStock';


const HomeLogged = () => {

    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState(null);
    var data = [{ 'img': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fmuslimxchange.com%2Fmsft%2F&psig=AOvVaw0cNj8kYrQP7PkFyjN_sW31&ust=1650205547974000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLig-u3kmPcCFQAAAAAdAAAAABAD', 'name': 'APPLE', 'symbol': 'APPL', 'price': 123 },
    { 'img': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fmuslimxchange.com%2Fmsft%2F&psig=AOvVaw0cNj8kYrQP7PkFyjN_sW31&ust=1650205547974000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLig-u3kmPcCFQAAAAAdAAAAABAD', 'name': 'MICROSOFT', 'symbol': 'MSFT', 'price': 124 },
    { 'img': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fmuslimxchange.com%2Fmsft%2F&psig=AOvVaw0cNj8kYrQP7PkFyjN_sW31&ust=1650205547974000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLig-u3kmPcCFQAAAAAdAAAAABAD', 'name': 'SONY', 'symbol': 'SONY', 'price': 153 }]


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
                                    data={data}
                                    buttonHomeClicked={buttonHomeClicked}
                                />
                            </Grid>
                        </div>
                    }
                    <Grid item>
                        <DataStock />
                    </Grid>
                </Grid>
            </div>
        </div>
    );
}

export default HomeLogged;