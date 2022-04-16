import React from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import HomeNavigation from './Utils/HomeNavigation/HomeNavigation';
import { Grid } from '@mui/material';
import StockNavigation from './Utils/StockNavigation/StockNavigation';


const HomeLogged = () => {

    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');
    const [buttonHomeClicked, setButtonHomeClicked] = React.useState('mywatchlist');
    const [buttonStockClicked, setButtonStockClicked] = React.useState('mywatchlist');

    return (
        <div className='mainDivLogged'>
            <Header />
            <div className="firstDivLogged">
                <Grid container spacing={1}>
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
                            </Grid>
                        </div>
                    }
                    {(buttonClicked === 'home') && (buttonHomeClicked === 'mywatchlist') &&
                        <div>
                            <Grid item>
                                <StockNavigation
                                    buttonStockClicked={buttonStockClicked}
                                    setButtonStockClicked={setButtonStockClicked} 
                                />
                            </Grid>
                        </div>
                    }
                    {(buttonClicked === 'home') && (buttonHomeClicked === 'popular') &&
                        <div>
                            <Grid item>
                                <StockNavigation
                                    buttonStockClicked={buttonStockClicked}
                                    setButtonStockClicked={setButtonStockClicked} 
                                />
                            </Grid>
                        </div>
                    }
                    {(buttonClicked === 'home') && (buttonHomeClicked === 'us_stocks') &&
                        <div>
                            <Grid item>
                                <StockNavigation
                                    buttonStockClicked={buttonStockClicked}
                                    setButtonStockClicked={setButtonStockClicked} 
                                />
                            </Grid>
                        </div>
                    }
                    {(buttonClicked === 'home') && (buttonHomeClicked === 'new_on_platform') &&
                    <div>
                        <Grid item>
                            <StockNavigation 
                                buttonStockClicked={buttonStockClicked}
                                setButtonStockClicked={setButtonStockClicked} 
                            />
                        </Grid>
                        </div>
                    }
                </Grid>
            </div>
        </div>
    );
}

export default HomeLogged;