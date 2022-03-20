import "./UnauthentichatedHeader.css";
import React from "react";
import { Slide } from '@mui/material';
import { CustomAppBar } from "./CustomAppBar";
import { CustomLogin } from "./CustomLogin";
import { CustomRegister } from "./CustomRegister";
import { CustomRegisterCompleted } from "./CustomRegisterCompleted";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});

export default function UnauthentichatedHeader() {
    
    const [openLogin, setOpenLogin] = React.useState(false);
    const handleClickOpenLogin = () => {
        setOpenLogin(true);
    };
    
    const [openRegister, setOpenRegister] = React.useState(false);
    const handleClickOpenRegister = () => {
        setOpenRegister(true);
    };

    const [openRegisterCompleted, setOpenRegisterCompleted] = React.useState(false);
    const handleClickOpenRegisterComplete = () => {
        setOpenRegisterCompleted(true);
    };

    const [messageRegister,setMessageRegister]=React.useState('');

    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <CustomAppBar
                    handleClickOpenRegister={handleClickOpenRegister}
                    handleClickOpenLogin={handleClickOpenLogin}
                />

                <CustomLogin
                    openLogin={openLogin}
                    setOpenLogin={setOpenLogin}
                    Transition={Transition}

                />

                <CustomRegister
                    openRegister={openRegister}
                    Transition={Transition}
                    setOpenRegister={setOpenRegister}
                    setMessageRegister={setMessageRegister}
                    handleClickOpenRegisterComplete={handleClickOpenRegisterComplete}
                />

                <CustomRegisterCompleted
                    openDialog={openRegisterCompleted}
                    setOpenRegisterCompleted={setOpenRegisterCompleted}
                    Transition={Transition}
                    message={messageRegister}
                />

            </div>
        </header>
    );
}