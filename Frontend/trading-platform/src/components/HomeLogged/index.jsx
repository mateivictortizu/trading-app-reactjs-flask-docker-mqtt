import React from 'react';
import { Oval } from 'react-loader-spinner';
import Header from "./Utils/Header/Header"
import './HomeLogged.css';


const HomeLogged = () => {
    document.title = 'Your Dashbord'
    return (
        <div className='mainDiv'>
            <Header></Header>
        </div>
    );
}

export default HomeLogged;