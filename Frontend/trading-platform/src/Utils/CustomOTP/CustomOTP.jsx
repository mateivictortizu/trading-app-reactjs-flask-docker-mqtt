import React from "react";
import './CustomOTP.css';
import { Dialog, DialogTitle, TextField, DialogContent, Grid, Button, DialogActions, Link } from "@mui/material";
import { useCookies } from 'react-cookie';

export function CustomOTP({ openOTP, setOpenOTP, Transition }) {

    const [OTP, setOTP] = React.useState("");
    const [cookies, setCookie] = useCookies(['jwt_otp']);

    function resendOTP() {
        fetch("http://127.0.0.1:5000/resend-otp", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': cookies.jwt_otp,
            },
        })
            .then((data) => {
                if (data.status == 200) {
                    data.json().then((message) => {
                        console.log(message);
                    })
                }
            })
    };

    function handleCloseOTP() {
        setOpenOTP(false);
    };

    function validateOTP() {
        fetch("http://127.0.0.1:5000/validate-otp", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': cookies.jwt_otp,
            },
            body: JSON.stringify({
                code: parseInt(OTP)
            }),
        })
            .then((data) => {
                data.json().then((message) => {
                    console.log(message);
                })

            })
    };

    const handleChangeOTP = (event) => {
        setOTP(event.target.value);
    };

    return (
        <div>
            <Dialog
                open={openOTP}
                onClose={handleCloseOTP}
                TransitionComponent={Transition}
                keepMounted
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle>One-time password</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="OTP"
                        label="OTP"
                        type="string"
                        value={OTP}
                        onChange={handleChangeOTP}
                        fullWidth
                    />

                    <Grid container spacing={25}
                        direction="row">
                        <Grid item><Link id="linkOTP" onClick={resendOTP}>Resend OTP</Link></Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button id="buttonOTP" fullWidth onClick={validateOTP}>Send OTP</Button>
                </DialogActions>
            </Dialog>
        </div>);
}