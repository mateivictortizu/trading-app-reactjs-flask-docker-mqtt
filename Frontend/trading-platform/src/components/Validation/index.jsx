import React, { useEffect } from "react";
import UnauthentichatedHeader from "../Home/Utils/UnauthentichatedHeader/UnauthentichatedHeader"
import Footer from "../../Utils/Footer/Footer"
import Typography from '@mui/material/Typography';
import { Button } from "@mui/material";
import "./Validation.css"
import { useParams } from 'react-router-dom';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';
import { USER_HOST } from "../../Utils/Extra/Hosts";

function ConditionalRenderingValidation({ responseCode, messageResponse }) {
    function ResendValidateAccountFuncton(){
        fetch("http://" + USER_HOST + "/resend-validate-account", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                identifier:"matteovkt@gmail.com"
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
            .catch((error) => {
                console.log(error);

            });
    }

    if (responseCode === 201) {
        return (
            <div className="main-div">
                <div id="firstDivValidation">
                    <br /><br />
                    <Typography
                        component="h1"
                        variant="h2"
                        align="center"
                        gutterBottom
                        style={{ fontWeight: "300" }}
                        id="typographyValidation"
                    >

                        <CheckCircleOutlineIcon id="iconCheck" style={{color:"green"}}></CheckCircleOutlineIcon>
                        <br></br>
                        {messageResponse}

                    </Typography>
                    <br></br>
                </div>
                <div id="secondDivValidation">
                    <Typography
                        component="h2"
                        variant="h5"
                        align="center"
                        color="#000"
                        gutterBottom
                        style={{ fontWeight: "50" }}
                        id="typographySecondaryValidation"
                    >
                        Thank you for creating your account and confirming your email address. Your account has now been succesfully created.
                        <br></br>
                        We are very happy you have decided to join us - we will work together to build a partenership.
                        <br></br>
                        Please tell your friend about the our platform - we are always looking to attract new members.

                    </Typography>
                </div>
                <div id="thirdDivValidation">
                    <Button id="buttonValidation" onClick={ResendValidateAccountFuncton}>Continue</Button>
                </div>
            </div>);

    }
    else {
        return (
            <div className="main-div">

                <div id="firstDivValidation">
                    <br /><br />
                    <Typography
                        component="h1"
                        variant="h2"
                        align="center"
                        gutterBottom
                        style={{ fontWeight: "300" }}
                        id="typographyValidation"
                    >

                        <ErrorOutlineIcon id="iconCheck" style={{color:"orange"}}></ErrorOutlineIcon>
                        <br></br>
                        {messageResponse}

                    </Typography>
                    <br></br>
                </div>
                <div id="secondDivValidation">
                </div>
                <div id="thirdDivValidation">
                    <Button id="buttonValidation">Continue</Button>
                </div>
            </div>);
    }
};



const Validation = () => {
    
    function ValidateAccountFuncton(){
        fetch("http://" + USER_HOST + "/validate-account/" + id, {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then((data) => {
                if (data.status === 200) {
                    setCodeResponse(data.status);
                    data.json().then((message) => {
                        console.log(message);
                        setMessageResponse(message['message']);
                    });

                } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                    setCodeResponse(data.status);
                    data.json().then((message) => {
                        setMessageResponse(message.error);
                    });
                } else {
                    throw new Error("Internal server error");
                }
            })
            .catch((error) => {
                console.log(error);

            });
    }

    document.title = "Confirm your account";
    let { id } = useParams();
    const [messageResponse, setMessageResponse] = React.useState("");
    const [codeResponse, setCodeResponse] = React.useState("");
    if (messageResponse == "" && codeResponse === "")
    {
        ValidateAccountFuncton();
    }
    return (
        <div className="main-div-validation">
            <div className="content">
                <UnauthentichatedHeader></UnauthentichatedHeader>
                <ConditionalRenderingValidation responseCode={codeResponse} messageResponse={messageResponse}></ConditionalRenderingValidation>
            </div>
            <div id="footerDivValidation">
                <Footer id='footerValidation'></Footer>
            </div>
        </div >

    )
}

export default Validation;

