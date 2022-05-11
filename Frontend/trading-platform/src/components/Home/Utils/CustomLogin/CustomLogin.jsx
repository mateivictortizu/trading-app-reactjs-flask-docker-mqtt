import React from "react";
import './CustomLogin.css';
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle, Link, Grid } from '@mui/material';
import { checkIsEmpty } from "../../../../Utils/Extra/Validator";
import { useNavigate } from "react-router-dom";
import { CustomSnackbarAlert } from "../CustomSnackbarAlert/CustomSnackbarAlert";
import { Oval } from 'react-loader-spinner';
import { CustomForgotPassword } from "../CustomForgotPassword/CustomForgotPassword";
import { CustomOTP} from "../CustomOTP/CustomOTP";
import { useCookies } from 'react-cookie';

export function CustomLogin({ openLogin, setOpenLogin, Transition, handleOpenRegister }) {

    let history = useNavigate();
    const [errorIdentifierLogin, setErrorIdentifierLogin] = React.useState(false);
    const [errorPasswordLogin, setErrorPasswordLogin] = React.useState(false);
    const [loginState, setLoginState] = React.useState(true);
    const [openAlert, setOpenAlert] = React.useState(false);
    const [severityType, setSeverityType] = React.useState('');
    const [messageAlert, setMessageAlert] = React.useState('');
    const [openForgotPassword, setOpenForgotPassword] = React.useState(false);
    const [openOTP, setOpenOTP] = React.useState(false);
    const [cookies, setCookie] = useCookies(['jwt']);
    const [ok,setOk]=React.useState(0);
    const navigate = useNavigate();
    const sleep = (milliseconds) => {
        return new Promise(resolve => setTimeout(resolve, milliseconds))
    }

    function handleCloseLoginOpenRegister(){
        handleCloseLogin();
        handleOpenRegister();


    }

    const handleSendLogin = () => {
        setAllErrorsLoginFalse();
        if (checkFields(identifierLogin, passwordLogin)) {
            setLoginState(false);
            fetch("http://127.0.0.1:5000/login", {
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
                            if (message.message=="OTP send")
                            {
                                setCookie("jwt_otp",data.headers.get("Authorization"));
                                setOpenOTP(true);
                            }
                            else
                            {
                                setCookie("jwt",data.headers.get("Authorization"));
                                setOk(1);
                            }
                            setLoginState(true);
                            handleCloseLogin();
                            if(ok===1)
                            {
                                navigate('/home'); 
                            }
                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then((message) => {
                            setLoginState(true);
                            configAlert(message.message, 'error');
                        });
                    } else {
                        throw new Error("Internal server error");
                    }
                })
                .catch(() => {
                    configAlert('Server is down', 'error')
                });
        }
    };

    const handleCloseLogin = () => {
        setIdentifierLogin("");
        setPasswordLogin("");
        setAllErrorsLoginFalse();
        handleCloseAlert();
        setOpenLogin(false);
    };

    const handleClickAlert = () => {
        setOpenAlert(true);
    };

    const handleCloseAlert = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOpenAlert(false);
    };

    const handleOpenForgotPassword = () => {
        handleCloseLogin();
        setOpenForgotPassword(true);
    };

    async function configAlert(message, severityType) {
        setSeverityType(severityType);
        setMessageAlert(message);
        handleClickAlert();
        if (severityType === 'success') {
            await sleep(3000);
            handleCloseLogin();
            await sleep(1000);
            history('/blogs');
        }
    }

    const [identifierLogin, setIdentifierLogin] = React.useState("");
    const handleChangeIdentifierLogin = (event) => {
        setIdentifierLogin(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorIdentifierLogin(false);
        }
    };

    const [passwordLogin, setPasswordLogin] = React.useState("");
    const handleChangePasswordLogin = (event) => {
        setPasswordLogin(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorPasswordLogin(false);
        }
    };

    function checkFields(identifierLogin, passwordLogin) {
        var result = true

        if (!checkIsEmpty(identifierLogin)) {
            setErrorIdentifierLogin(true);
            result = false;
        }

        if (!checkIsEmpty(passwordLogin)) {
            setErrorPasswordLogin(true);
            result = false;
        }

        return result;
    };

    function setAllErrorsLoginFalse() {
        setErrorIdentifierLogin(false);
        setErrorPasswordLogin(false);
    };

    return (
        <div>
            <Dialog
                open={openLogin}
                onClose={handleCloseLogin}
                TransitionComponent={Transition}
                keepMounted
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle>Login</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="identifierLogin"
                        error={errorIdentifierLogin}
                        helperText={errorIdentifierLogin ? "Fill identifier" : ""}
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
                        error={errorPasswordLogin}
                        helperText={errorPasswordLogin ? "Fill password" : ""}
                        label="Password"
                        type="password"
                        value={passwordLogin}
                        onChange={handleChangePasswordLogin}
                        fullWidth
                    />
                    <Grid container spacing={25}
                        direction="row">
                        <Grid item><Link id="linkLogin" onClick={handleOpenForgotPassword} >Forgot your password?</Link></Grid>
                        <Grid item><Link id="linkLogin" onClick={handleCloseLoginOpenRegister} >Open account</Link></Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button id="buttonLogin" fullWidth onClick={handleSendLogin}>{loginState ? "Login" :
                        <Oval
                            secondaryColor='#ffcc00'
                            height="20"
                            width="30"
                            color='#ffcc00'
                            ariaLabel='loading'
                        />}</Button>
                </DialogActions>
                <CustomSnackbarAlert open={openAlert} handleClose={handleCloseAlert} message={messageAlert} severityType={severityType} />
            </Dialog>

            <CustomForgotPassword
                openForgotPassword={openForgotPassword}
                setOpenForgotPassword={setOpenForgotPassword}
                Transition={Transition}>
            </CustomForgotPassword>

            <CustomOTP
                openOTP={openOTP}
                setOpenOTP={setOpenOTP}
                Transition={Transition}>
            </CustomOTP>
        </div>
    )
}