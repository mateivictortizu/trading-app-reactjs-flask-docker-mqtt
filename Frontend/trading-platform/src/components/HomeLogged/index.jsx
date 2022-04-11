import React from 'react';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';
import Navigation from './Utils/Navigation/Navigation';


const HomeLogged = () => {
    document.title = 'Your Dashbord'
    return (
        <div className='mainDivLogged'>
            <Header />
            <div className="firstDivLogged">
                <Navigation />
            </div>
            <div id='footer'>
                footer
            </div>
        </div>
    );
}

export default HomeLogged;