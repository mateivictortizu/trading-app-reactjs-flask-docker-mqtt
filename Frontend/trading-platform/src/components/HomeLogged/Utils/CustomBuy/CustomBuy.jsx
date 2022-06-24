import './CustomBuy.css';
import React from "react";
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input } from '@mui/material';

export function CustomBuy({ openBuy, setOpenBuy, Transition, stockName, price, logo, stock_symbol, valueAccount }) {

    const [value, setValue] = React.useState(0.0);
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    const [errorBuy, setErrorBuy] = React.useState("");



    function handleCloseBuy() {
        setOpenBuy(false);
        setValue(0.0);
        setErrorBuy("");
    };

    const handleValueChange = (event) => {
        setValue(event.target.value);
        if (price*event.target.value <= valueAccount){
            setErrorBuy("");
        }
        else {
            setErrorBuy("Not enought money");
        }
    };

    function buy_invested() {
        if (value > 0) {
            if (price*value <= valueAccount) {
                console.log(price*value);
                console.log(valueAccount);
                fetch("http://127.0.0.1:5000/buy", {
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
                            handleCloseBuy();
                        });

                    }
                    else if (data.status === 403) {
                        setErrorBuy("Not enought money");
                        handleCloseBuy();
                        removeCookie("jwt");
                        removeCookie("session");
                        navigate('/');
                    }
                    else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then(() => {
                            setErrorBuy("Not enought money");
                        });
                    } else {
                        setErrorBuy("Not enought money");
                    }
                }
                );
            }
            else {
                setErrorBuy("Not enought money");
                console.log("Not money");
            }
        }
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
                <DialogContent style={{ height: '250px' }}>
                    <Typography id='valueBuy'>Value</Typography>
                    <Input
                        id='insertBuy'
                        disableUnderline={true}
                        error={errorBuy !== ""}
                        helpertext={errorBuy}
                        style={{color:(errorBuy !== "")?'#7F0000':'#0066cc'}}
                        autoFocus
                        fullWidth
                        onChange={handleValueChange}
                        value={value}
                    />
                    <Button id='buttonBuy' disabled={(errorBuy !== "")} onClick={buy_invested}>BUY</Button>
                </DialogContent>
            </Dialog>
        </div>
    )
}