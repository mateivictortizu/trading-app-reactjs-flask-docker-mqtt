import React from "react";
import './CustomOTP.css';
import { Dialog, DialogTitle, TextField, DialogContent, Grid, Button, DialogActions, Link } from "@mui/material";
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';

export function CustomOTP({ openOTP, setOpenOTP, Transition }) {

    const [OTP, setOTP] = React.useState("");
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();

    function resendOTP() {
        fetch(GATEWAY_HOST+"/resend-otp", {
            method: "POST",
            credentials:'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                Authorization: cookies.jwt_otp
            }),
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
        setOTP('');
        setOpenOTP(false);
    };

    function validateOTP() {
        fetch(GATEWAY_HOST+"/validate-otp", {
            method: "POST",
            credentials:'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: parseInt(OTP),
                Authorization: cookies.jwt_otp
            }),
        })
            .then((data) => {
                if (data.status == 200) {
                    handleCloseOTP();
                    removeCookie("jwt_otp");
                    navigate('/home');

                }
                else {
                    data.json().then((message) => {
                        console.log(message);
                    })
                }

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