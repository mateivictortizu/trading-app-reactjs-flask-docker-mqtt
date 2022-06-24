import React from "react";
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input } from '@mui/material';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';

export function CustomSell({ openSell, setOpenSell, Transition, stockName, price, logo, stock_symbol, qty_available }) {

    const [value, setValue] = React.useState(0.0);
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    const [errorSell, setErrorSell] = React.useState("");


    function handleCloseSell() {
        setOpenSell(false);
        setValue(0.0);
        setErrorSell("");
    };

    const handleValueChange = (event) => {
        setValue(event.target.value);
        if (event.target.value<=qty_available){
            setErrorSell("");
        }
        else {
            setErrorSell("Not enought shares");
        }
    };

    function sell_invested() {
        if (value > 0 && value<=qty_available) {
            fetch("http://127.0.0.1:5000/sell", {
                method: "POST",
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    stock_symbol: stock_symbol,
                    cantitate: value,
                    price: price
                }),
            }).then((data) => {
                if (data.status === 200) {
                    data.json().then(() => {
                        handleCloseSell();
                    });

                }
                else if (data.status === 403) {
                    handleCloseSell();
                    removeCookie("jwt");
                    removeCookie("session");
                    navigate('/');
                }
                else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    data.json().then(() => {
                        console.log('Error');
                    });
                } else {
                    console.log('Error');
                }
            }
            )
        }
        else {
            console.log("Bad value")
        }
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
                        style={{ color: (errorSell !== "") ? '#7F0000' : '#0066cc' }}
                        variant="standard"
                        autoFocus
                        fullWidth
                        onChange={handleValueChange}
                        value={value}
                    />
                    <Button id='buttonBuy' disabled={(errorSell !== "")} onClick={sell_invested}>SELL</Button>
                </DialogContent>
            </Dialog>
        </div>
    )
}