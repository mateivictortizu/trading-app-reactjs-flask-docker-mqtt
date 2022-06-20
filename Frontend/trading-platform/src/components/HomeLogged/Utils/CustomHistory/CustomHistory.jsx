import React from "react";
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input} from '@mui/material';

export function CustomHistory({ openHistory, setOpenHistory, Transition, stock_symbol, logo, stockName }) {

    function handleCloseHistory() {
        setOpenHistory(false);
    };

    function get_history_of_stock() {
        fetch("http://127.0.0.1:5000/history", {
            method: "POST",
            credentials:'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                stock_symbol: stock_symbol,
            }),
        }).then(setOpenHistory(false));

    };

    return (
        <div>
            <Dialog
                open={openHistory}
                onClose={handleCloseHistory}
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
                    History - {stockName}
                </DialogTitle>
                <DialogContent style={{ height: '250px' }}>
                </DialogContent>
            </Dialog>
        </div>
    )
}