import React, { useEffect } from "react";
import { TextField, DialogTitle, Button } from '@mui/material';
import { checkIsEmpty } from "../../Utils/Extra/Validator";
import { CustomAppBar } from "./Utils/CustomAppBar/CustomAppBar";
import './ChangePass.css';
import Footer from "../../Utils/Footer/Footer";
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';


const ChangePass = () => {

    document.title = "Invest - Reset Password"
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    const [errorPasswordLogin, setErrorPasswordLogin] = React.useState(false);

    const [identifierChangePass, setIdentifierChangePass] = React.useState("");
    const handleChangeIdentifierChangePass = (event) => {
        setIdentifierChangePass(event.target.value);
    };

    const [newPassword, setNewPassword] = React.useState("");
    const handleChangeNewPassword = (event) => {
        setNewPassword(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorPasswordLogin(false);
        }
    };

    useEffect(() => {
        if (cookies.jwt) {
            navigate('/home');
        }
        else {
            fetch("http://127.0.0.1:5000" + window.location.pathname, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            setIdentifierChangePass(message['message']);

                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then((message) => {
                            navigate('/');
                        });
                    } else {
                        throw new Error("Internal server error");
                    }
                });
        }
    });

    function clickCancel() {
        navigate('/');
    };

    function clickReset() {
        fetch("http://127.0.0.1:5000/set-new-pass", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                change_pass_token: window.location.pathname.split('/')[2],
                password: newPassword,
            }),
        })
            .then((data) => {
                if (data.status === 200) {
                    data.json().then((message) => {
                        setIdentifierChangePass(message['message']);
                    });

                } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    data.json().then((message) => {
                        navigate('/');
                    });
                } else {
                    throw new Error("Internal server error");
                }
            });
    };

    return (
        <div className="main-div">
            <CustomAppBar />
            <div id="textDivChangePass">
                <div id="textFieldChangePass">
                    <DialogTitle>Reset Password</DialogTitle>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="outlined-disabled"
                        label="Email Address"
                        type="string"
                        value={identifierChangePass}
                        onChange={handleChangeIdentifierChangePass}
                        style={{ width: '450px' }}
                        disabled
                    />
                    <br />
                    <TextField
                        autoFocus
                        margin="dense"
                        error={errorPasswordLogin}
                        helperText={errorPasswordLogin ? "Fill password" : ""}
                        label="New Password"
                        type="password"
                        value={newPassword}
                        onChange={handleChangeNewPassword}
                        style={{ width: '450px' }}
                    />
                    <br />
                    <TextField
                        autoFocus
                        margin="dense"
                        error={errorPasswordLogin}
                        helperText={errorPasswordLogin ? "Fill password" : ""}
                        label="Repeat New Password"
                        type="password"
                        value={newPassword}
                        onChange={handleChangeNewPassword}
                        style={{ width: '450px' }}
                    />
                    <br /><br />
                    <Button
                        id="buttonResetChangePass"
                        onClick={clickReset}
                    >Reset</Button>
                    &nbsp;
                    &nbsp;
                    <Button
                        id="buttonCancelChangePass"
                        onClick={clickCancel}
                    >Cancel</Button>
                </div>
            </div>
            <div className="footerChangePass">
                <Footer className='footer'></Footer>
            </div>
        </div>
    );
}

export default ChangePass;