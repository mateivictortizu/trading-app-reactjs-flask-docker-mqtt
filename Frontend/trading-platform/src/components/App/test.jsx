import React from 'react';
import { io } from "socket.io-client";
import { useEffect } from 'react';
import socketIOClient from "socket.io-client";
import { Button } from '@mui/material';

function Test() {

    return (
        <div>
            Da
            <Button onClick={console.log('da')}>HTPP</Button>
            <Button onClick={console.log('da')}>WS</Button>
        </div>
    );
}

export default Test;