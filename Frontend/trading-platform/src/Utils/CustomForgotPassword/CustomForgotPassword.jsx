import React from "react";
import './CustomForgotPassword.css';
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';
import { checkIsEmpty } from "../Extra/Validator";

export function CustomForgotPassword({ openForgotPassword, setOpenForgotPassword, Transition }) {

    const [openAlert, setOpenAlert] = React.useState(false);
    const [identifierLogin, setIdentifierLogin] = React.useState("");

    const handleClickAlert = () => {
        setOpenAlert(true);
    };

    const handleCloseAlert = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpenAlert(false);
    };

    const handleChangeIdentifierLogin = (event) => {
        setIdentifierLogin(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorIdentifierForgotPassword(false);
        }
    };

    const [errorIdentifierForgotPassword, setErrorIdentifierForgotPassword] = React.useState(false);

    const handleCloseForgotPassword = () => {
        setOpenForgotPassword(false);
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
                        label="Username or Email Address"
                        type="string"
                        value={identifierLogin}
                        onChange={handleChangeIdentifierLogin}
                        fullWidth
                    />
                </DialogContent>
                <DialogActions>
                    <Button id="buttonForgotPassword" fullWidth >Recover password</Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}