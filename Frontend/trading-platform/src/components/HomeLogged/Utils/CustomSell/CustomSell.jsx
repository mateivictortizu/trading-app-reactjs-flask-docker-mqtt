import React from "react";
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input} from '@mui/material';

export function CustomSell({ openSell, setOpenSell, Transition, stockName, price, logo, stock_symbol }) {

    const [value, setValue] = React.useState(0.0);


    function handleCloseSell() {
        setOpenSell(false);
        setValue(0.0);
    };

    const handleValueChange = (event) => {
        setValue(event.target.value);
    };

    function sell_invested() {
        fetch("http://127.0.0.1:5000/sell", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user: "matteovkt@gmail.com",
                stock_symbol: stock_symbol,
                cantitate: value,
                price: price
            }),
        }).then(setOpenSell(false)).then(setValue(0.0));

    };

    return (
        <div>
            <Dialog
                open={openSell}
                onClose={handleCloseSell}
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
                    Sell {stockName}
                    <Typography id='priceCustomBuy'>${price}</Typography>
                </DialogTitle>
                <DialogContent style={{ height: '250px' }}>
                    <Typography id='valueBuy'>Value</Typography>
                    <Input
                        id='insertBuy'
                        disableUnderline={true}
                        variant="standard"
                        autoFocus
                        fullWidth
                        onChange={handleValueChange}
                        value={value}
                    />
                    <Button id='buttonBuy' onClick={sell_invested}>SELL</Button>
                </DialogContent>
            </Dialog>
        </div>
    )
}