import "./Header.css";
import React from "react";
import { Slide } from '@mui/material';
import { CustomAppBarLogged } from "../CustomAppBarLogged/CustomAppBarLogged";
import { CustomDeposit } from "../CustomDeposit/CustomDeposit";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});


export default function Header() {
    const [openDeposit, setOpenDeposit] = React.useState(false);

    function handleClickOpenDeposit(){
        setOpenDeposit(true)
    }

    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <CustomAppBarLogged 
                    handleClickOpenDeposit={handleClickOpenDeposit}
                />
                <CustomDeposit
                    openDeposit={openDeposit}
                    setOpenDeposit={setOpenDeposit}
                    Transition={Transition}
                />

            </div>
        </header>
    );
}