import React from 'react';
import { io } from "socket.io-client";
import { useEffect } from 'react';
import socketIOClient from "socket.io-client";
import { Button } from '@mui/material';

function test_fetch() {
    fetch("http://127.0.0.1:5000", {
        credentials: 'include'
    }).then((data) => console.log(data.headers.get('name')));

}

function Test() {

    return (
        <div>
            Da
            <Button onClick={test_fetch}>HTPP</Button>
        </div>
    );
}

export default Test;