import "./UnauthentichatedHeader.css";
import React from "react";
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';


export function CustomLogin({ openLogin,setOpenLogin, Transition}) {
    
    const handleCloseLogin = () => {
        setIdentifierLogin("");
        setPasswordLogin("");
        setOpenLogin(false);
    };

    const handleSendLogin = () => {
        fetch("https://127.0.0.1:5001/login", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                identifier: identifierLogin,
                password: passwordLogin,
            }),
        })
            .then((data) => {
                if (data.status === 200) {
                    data.json().then((message) => {
                        console.log(message);
                    });

                } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    data.json().then((message) => {
                        console.log(message)
                    });
                } else {
                    throw new Error("Internal server error");
                }
            })
            .catch((error) => {
                console.log(error);
            });
        handleCloseLogin();
    };

    const [identifierLogin, setIdentifierLogin] = React.useState("");
    const handleChangeIdentifierLogin = (event) => {
        setIdentifierLogin(event.target.value);
    };

    const [passwordLogin, setPasswordLogin] = React.useState("");
    const handleChangePasswordLogin = (event) => {
        setPasswordLogin(event.target.value);
    };

    return (
        <div>
            <Dialog
                open={openLogin}
                onClose={handleCloseLogin}
                TransitionComponent={Transition}
                keepMounted
                style={{backdropFilter: 'blur(4px)'}}
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