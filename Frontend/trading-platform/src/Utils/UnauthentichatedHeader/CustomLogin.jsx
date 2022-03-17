import "./UnauthentichatedHeader.css";
import React from "react";
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

export function CustomLogin({ openLogin, handleCloseLogin, Transition, identifierLogin, handleChangeIdentifierLogin, passwordLogin, handleChangePasswordLogin, handleSendLogin }) {
    return (
        <div>
            <Dialog
                open={openLogin}
                onClose={handleCloseLogin}
                TransitionComponent={Transition}
                keepMounted
            >
                <DialogTitle>Login</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="identifierLogin"
                        label="Username or Email Address"
                        type="string"
                        value={identifierLogin}
                        onChange={handleChangeIdentifierLogin}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="passwordLogin"
                        label="Password"
                        type="password"
                        value={passwordLogin}
                        onChange={handleChangePasswordLogin}
                        fullWidth
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleCloseLogin}>Cancel</Button>
                    <Button onClick={handleSendLogin}>Login</Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}