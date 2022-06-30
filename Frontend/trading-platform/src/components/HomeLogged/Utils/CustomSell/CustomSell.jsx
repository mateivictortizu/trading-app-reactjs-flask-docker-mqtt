import React from "react";
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input, Grid } from '@mui/material';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import Switch from '@mui/material/Switch';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

export function CustomSell({ openSell, setOpenSell, Transition, stockName, price, logo, stock_symbol, qty_available }) {

    const [value, setValue] = React.useState(0.0);
    const [priceAutosellValue, setPriceAutosellValue] = React.useState(0.0);
    const [qtyAutosellValue, setQtyAutosellValue] = React.useState(0.0);
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    const [errorSell, setErrorSell] = React.useState("");
    const [checked, setChecked] = React.useState(false);
    const [openAlert, setOpenAlert] = React.useState(false);
    const [messageAlert, setMessageAlert] = React.useState([]);


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


    function handleCloseSell() {
        setOpenSell(false);
        setValue(0.0);
        setPriceAutosellValue(0.0);
        setQtyAutosellValue(0.0);
        setErrorSell("");
    };

    const handleValueChange = (event) => {
        setValue(event.target.value);
        if (event.target.value <= qty_available) {
            setErrorSell("");
        }
        else {
            setErrorSell("Not enought shares");
        }
    };

    const handlePriceAutosellValueChange = (event) => {
        setPriceAutosellValue(event.target.value);
    };

    const handleQtyAutosellValueChange = (event) => {
        setQtyAutosellValue(event.target.value);
    };

    function sell_invested() {
        if (value > 0 && value <= qty_available) {
            fetch(GATEWAY_HOST + "/sell", {
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
                        var no_shares = value;
                        handleCloseSell();
                        setOpenAlert(true);
                        setMessageAlert(["You sell " + no_shares + " shares of " + stock_symbol, "success"])
                    });

                }
                else if (data.status === 403) {
                    handleCloseSell();
                    setOpenAlert(true);
                    setMessageAlert(["Sell failed", "error"])
                    removeCookie("jwt");
                    removeCookie("session");
                    navigate('/');
                }
                else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    data.json().then(() => {
                        setOpenAlert(true);
                        setMessageAlert(["Sell failed", "error"])
                        console.log('Error');
                    });
                } else {
                    setOpenAlert(true);
                    setMessageAlert(["Sell failed", "error"])
                    console.log('Error');
                }
            }
            )
        }
        else {
            setOpenAlert(true);
            setMessageAlert(["Quantity is wrong", "error"])
        }
    };

    function autosell_invested() {
        fetch(GATEWAY_HOST + "/autosell", {
            method: "POST",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                stock_symbol: stock_symbol,
                cantitate: qtyAutosellValue,
                price: priceAutosellValue
            }),
        }).then((data) => {
            if (data.status === 200) {
                data.json().then(() => {
                    handleCloseSell();
                    setOpenAlert(true);
                    setMessageAlert(["You placed a pending sell order with " + qtyAutosellValue + " shares of " + stock_symbol, "success"])
                });

            }
            else if (data.status === 403) {
                handleCloseSell();
                setOpenAlert(true);
                setMessageAlert(["AutoSell failed", "error"])
                removeCookie("jwt");
                removeCookie("session");
                navigate('/');
            }
            else if (data.status === 404 || data.status === 400 | data.status === 401) {
                data.json().then(() => {
                    setOpenAlert(true);
                    setMessageAlert(["AutoSell failed", "error"])
                    console.log('Error');
                });
            } else {
                setOpenAlert(true);
                setMessageAlert(["Sell failed", "error"])
                console.log('Error');
            }
        }
        )
        handleCloseSell();
    }

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
                <DialogContent style={{ height: '300px' }}>
                    <div style={{ textAlign: 'center', marginTop: '10px' }}>
                        Sell
                        <Switch
                            checked={checked}
                            onChange={handleChange}
                            inputProps={{ 'aria-label': 'controlled' }}
                        />
                        AutoSell
                    </div>
                    {(checked !== true) && <div>
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
                                        onChange={handleQtyAutosellValueChange}
                                        value={qtyAutosellValue}
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
                                        onChange={handlePriceAutosellValueChange}
                                        value={priceAutosellValue}
                                    />
                                </Grid>
                            </Grid>
                            <Button id='buttonBuy' onClick={autosell_invested}>AUTOSELL</Button>
                        </div>}
                </DialogContent>
            </Dialog>
        </div>
    )
}