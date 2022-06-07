import './CustomBuy.css';
import React from "react";
import { Dialog, DialogTitle, DialogContent, Typography } from '@mui/material';

export function CustomBuy({ openBuy, setOpenBuy, Transition, stockName, price, logo }) {

    const [value, setValue] = React.useState(0.0);


    function handleCloseBuy() {
        setOpenBuy(false);
    };

    function buy_invested() {
        fetch("http://127.0.0.1:5004/buy-invested", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user: "matteovkt@gmail.com",
                stock_symbol: "MSFT",
                cantitate: parseFloat(1.6),
                price: parseFloat(180.3)
            }),
        }).then(setOpenBuy(false));

    };

    return (
        <div>
            <Dialog
                open={openBuy}
                onClose={handleCloseBuy}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{ backgroundColor: '#E8E8E8', textAlign: 'center' }}>
                <img id='imgCustomBuy' src={logo}></img>
                    Buy {stockName}
                    <Typography id='priceCustomBuy'>${price}</Typography>
                </DialogTitle>
                <DialogContent>

                </DialogContent>
            </Dialog>
        </div>
    )
}