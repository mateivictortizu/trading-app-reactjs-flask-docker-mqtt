import React from "react";
import './CustomForgotPassword.css';
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';
import { checkIsEmpty } from "../../../../Utils/Extra/Validator"

export function CustomForgotPassword({ openForgotPassword, setOpenForgotPassword, Transition }) {

    const [openAlert, setOpenAlert] = React.useState(false);
    const [identifierForgotPassword, setIdentifierForgotPassword] = React.useState("");

    const handleClickAlert = () => {
        setOpenAlert(true);
    };

    const handleCloseAlert = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpenAlert(false);
    };

    const handleChangeIdentifierForgotPassword = (event) => {
        setIdentifierForgotPassword(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorIdentifierForgotPassword(false);
        }
    };

    const [errorIdentifierForgotPassword, setErrorIdentifierForgotPassword] = React.useState(false);

    const handleCloseForgotPassword = () => {
        setIdentifierForgotPassword('');
        setOpenForgotPassword(false);
        setErrorIdentifierForgotPassword(false);
    };

    const handleSendForgotPassword = () => {
        setErrorIdentifierForgotPassword(false);
        if (checkIsEmpty(identifierForgotPassword)) {
            fetch("https://127.0.0.1:5001/forgot-password", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    identifier: identifierForgotPassword,
                }),
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            console.log(message);
                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then((message) => {
                        });
                    } else {
                        throw new Error("Internal server error");
                    }
                })
                .catch(() => {
                });
        }
        else
        {
            setErrorIdentifierForgotPassword(true);
        }
    };

    return (
        <div>
            <Dialog
                open={openForgotPassword}
                onClose={handleCloseForgotPassword}
                TransitionComponent={Transition}
                keepMounted
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle>Forgot password</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="identifierLogin"
                        error={errorIdentifierForgotPassword}
                        helperText={errorIdentifierForgotPassword ? "Fill identifier" : ""}
                        label="Username or Email"
                        type="string"
                        value={identifierForgotPassword}
                        onChange={handleChangeIdentifierForgotPassword}
                        fullWidth
                    />
                </DialogContent>
                <DialogActions>
                    <Button id="buttonForgotPassword" onClick={handleSendForgotPassword} fullWidth >Recover password</Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}