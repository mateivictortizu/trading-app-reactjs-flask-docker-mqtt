import React from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';
import NavigationHome from './Utils/NavigationHome/NavigationHome';
import { Grid } from '@mui/material';


const HomeLogged = () => {

    document.title = 'Your Dashbord'
    const [buttonClicked, setButtonClicked] = React.useState('home');

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

                    {(buttonClicked=='home') &&
                        <Grid item>
                            <NavigationHome />
                        </Grid>
                    }
                </Grid>
            </div>
        </div>
    );
}

export default HomeLogged;