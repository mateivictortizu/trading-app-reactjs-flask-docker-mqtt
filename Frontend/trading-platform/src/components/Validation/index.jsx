import React from "react";
import UnauthentichatedHeader from "../../Utils/UnauthentichatedHeader/UnauthentichatedHeader"
import Footer from "../../Utils/Footer/Footer"
import Typography from '@mui/material/Typography';
import { Button } from "@mui/material";
import "./Validation.css"
import { useParams } from 'react-router-dom';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';

const Validation = () => {
    document.title = "Confirm your account"
    let { id } = useParams();
    return (
        <div className="main-div">
            <UnauthentichatedHeader></UnauthentichatedHeader>
            <div id="firstDivValidation">
                <br/><br/>
                <Typography
                    component="h1"
                    variant="h2"
                    align="center"
                    gutterBottom
                    style={{ fontWeight: "300" }}
                    id="typographyValidation"
                >

                    <CheckCircleOutlineIcon id="iconCheck"></CheckCircleOutlineIcon>
                    <br></br>
                    Your account was succesfully validated!

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
                <Button id="buttonValidation">Continue</Button>
            </div>
            <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
            <div id="footerDivValidation">
                <Footer id='footerValidation'></Footer>
            </div>
        </div>
    )
}

export default Validation;

