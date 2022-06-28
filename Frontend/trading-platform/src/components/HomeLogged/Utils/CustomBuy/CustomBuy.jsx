import './CustomBuy.css';
import React from "react";
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input, Grid } from '@mui/material';
import Switch from '@mui/material/Switch';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

export function CustomBuy({ openBuy, setOpenBuy, Transition, stockName, price, logo, stock_symbol, valueAccount }) {

    const [value, setValue] = React.useState(0.0);
    const [priceAutobuyValue, setPriceAutobuyValue] = React.useState(0.0);
    const [qtyAutobuyValue, setQtyAutobuyValue] = React.useState(0.0);
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    const [errorBuy, setErrorBuy] = React.useState("");
    const [checked, setChecked] = React.useState(false);
    const [openAlert, setOpenAlert] = React.useState(false);
    const [messageAlert, setMessageAlert]=React.useState([]);

    const handleCloseAlert = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpenAlert(false);
    };

    const Alert = React.forwardRef(function Alert(props, ref) {
        return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
    });


    const handleChange = (event) => {
        setChecked(event.target.checked);
    };

    function handleCloseBuy() {
        setOpenBuy(false);
        setValue(0.0);
        setPriceAutobuyValue(0.0);
        setQtyAutobuyValue(0.0);
        setErrorBuy("");
    };

    const handleValueChange = (event) => {
        setValue(event.target.value);
        if (price * event.target.value <= valueAccount) {
            setErrorBuy("");
        }
        else {
            setErrorBuy("Not enought money");
        }
    };

    const handlePriceAutobuyValueChange = (event) => {
        setPriceAutobuyValue(event.target.value);
    };

    const handleQtyAutobuyValueChange = (event) => {
        setQtyAutobuyValue(event.target.value);
    };

    function autobuy_invested() {
        fetch(GATEWAY_HOST + "/autobuy", {
            method: "POST",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                stock_symbol: stock_symbol,
                cantitate: qtyAutobuyValue,
                price: priceAutobuyValue
            }),
        }).then((data) => {
            if (data.status === 200) {
                data.json().then(() => {
                    handleCloseBuy();
                    setMessageAlert(["You placed a pending buy order with "+value+" shares of "+stock_symbol,"success"])
                });

            }
            else if (data.status === 403) {
                handleCloseBuy();
                setMessageAlert(["AutoBuy failed","error"])
                removeCookie("jwt");
                removeCookie("session");
                navigate('/');
            }
            else if (data.status === 404 || data.status === 400 | data.status === 401) {
                data.json().then(() => {
                    setMessageAlert(["AutoBuy failed","error"])
                    console.log('Error');
                });
            } else {
                setMessageAlert(["AutoBuy failed","error"])
                console.log('Error');
            }
        }
        )
        handleCloseBuy();
    }

    function buy_invested() {
        if (value > 0) {
            if (price * value <= valueAccount) {
                fetch(GATEWAY_HOST + "/buy", {
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
                            setOpenAlert(true);
                            setMessageAlert(["You buy "+value+" shares of "+stock_symbol,"success"])
                        });

                    }
                    else if (data.status === 403) {
                        setErrorBuy("Not enought money");
                        setMessageAlert(["Buy fail","error"])
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
            <Snackbar open={openAlert} autoHideDuration={6000} onClose={handleCloseAlert} anchorOrigin={{
                vertical: "bottom",
                horizontal: "center"
            }}>
                <Alert onClose={handleCloseAlert} severity={messageAlert[1]} sx={{ width: '100%' }} style={{ backgroundColor: "#0066cc" }} >
                    {messageAlert[0]}
                </Alert>
            </Snackbar>
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
                <DialogContent style={{ height: '300px' }}>
                    <div style={{ textAlign: 'center', marginTop: '10px' }}>
                        Buy
                        <Switch
                            checked={checked}
                            onChange={handleChange}
                            inputProps={{ 'aria-label': 'controlled' }}
                        />
                        AutoBuy
                    </div>
                    {(checked === false) &&
                        <div>
                            <Typography id='valueBuy'>Quantity</Typography>
                            <Input
                                id='insertBuy'
                                disableUnderline={true}
                                error={errorBuy !== ""}
                                helpertext={errorBuy}
                                style={{ color: (errorBuy !== "") ? '#7F0000' : '#0066cc' }}
                                autoFocus
                                fullWidth
                                onChange={handleValueChange}
                                value={value}
                            />
                            <Button id='buttonBuy' disabled={(errorBuy !== "")} onClick={buy_invested}>BUY</Button>
                        </div>}
                    {(checked === true) &&
                        <div>
                            <Grid container spacing={2}>
                                <Grid item xs={6}>
                                    <Typography id='valueBuy'>Quantity</Typography>
                                    <Input
                                        id='insertBuy'
                                        disableUnderline={true}
                                        style={{ color: '#0066cc' }}
                                        autoFocus
                                        fullWidth
                                        onChange={handleQtyAutobuyValueChange}
                                        value={qtyAutobuyValue}
                                    />
                                </Grid>
                                <Grid item xs={6}>
                                    <Typography id='valueBuy'>Target Price</Typography>
                                    <Input
                                        id='insertBuy'
                                        disableUnderline={true}
                                        style={{ color: '#0066cc' }}
                                        autoFocus
                                        fullWidth
                                        onChange={handlePriceAutobuyValueChange}
                                        value={priceAutobuyValue}
                                    />
                                </Grid>
                            </Grid>
                            <Button id='buttonBuy' onClick={autobuy_invested}>AUTOBUY</Button>
                        </div>}
                </DialogContent>
            </Dialog>
        </div>
    )
}