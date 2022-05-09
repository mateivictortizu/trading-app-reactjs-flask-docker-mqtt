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
    const [errorIdentifierLogin, setErrorIdentifierLogin] = React.useState(false);
    const [errorPasswordLogin, setErrorPasswordLogin] = React.useState(false);

    const [identifierLogin, setIdentifierLogin] = React.useState("");
    const handleChangeIdentifierLogin = (event) => {
        setIdentifierLogin(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorIdentifierLogin(false);
        }
    };

    const [newPassword, setNewPassword] = React.useState("");
    const handleChangeNewPassword = (event) => {
        setNewPassword(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorPasswordLogin(false);
        }
    };

    useEffect(() => {
        if(cookies.jwt)
        {
            navigate('/home');
        }
        else 
        {
            fetch("http://127.0.0.1:5000"+window.location.pathname, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            })
                .then((data) => {
                    if (data.status === 200) {
                        data.json().then((message) => {
                            
                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                        data.json().then((message) => {
                            
                        });
                    } else {
                        throw new Error("Internal server error");
                    }
                });
        }
      });

    return (
        <div className="main-div">
            <CustomAppBar />
            <div id="textDivChangePass">
                <div id="textFieldChangePass">
                    <DialogTitle>Reset Password</DialogTitle>
                    <TextField
                        autoFocus
                        margin="dense"
                        error={errorIdentifierLogin}
                        helperText={errorIdentifierLogin ? "Fill identifier" : ""}
                        label="Email Address"
                        type="string"
                        value={identifierLogin}
                        onChange={handleChangeIdentifierLogin}
                        style={{ width: '450px' }}
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
                    >Reset</Button>
                    &nbsp;
                    &nbsp;
                    <Button
                        id="buttonCancelChangePass"
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