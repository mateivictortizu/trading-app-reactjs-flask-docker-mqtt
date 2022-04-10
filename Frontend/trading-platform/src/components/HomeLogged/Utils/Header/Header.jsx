import "./Header.css";
import React from "react";
import { Slide } from '@mui/material';
import { CustomAppBarLogged } from "../CustomAppBarLogged/CustomAppBarLogged";
import { CustomDeposit } from "../CustomDeposit/CustomDeposit";
import { CustomManageFunds } from "../CustomManageFunds/CustomManageFunds";
import { CustomCardDialog } from "../CustomCardDialog/CustomCardDialog";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});


export default function Header() {
    const [openDeposit, setOpenDeposit] = React.useState(false);
    const [openManageFunds, setOpenManageFunds] = React.useState(false);
    const [openHistory, setOpenHistory] = React.useState(false);
    const [openCard, setOpenCard] = React.useState(false);

    function handleClickOpenDeposit(){
        setOpenDeposit(true)
    }

    function handleClickOpenManageFunds(){
        setOpenManageFunds(true)
    }

    function handleClickOpenHistory(){
        setOpenHistory(true)
    }

    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <CustomAppBarLogged 
                    handleClickOpenDeposit={handleClickOpenDeposit}
                    handleClickOpenManageFunds={handleClickOpenManageFunds}
                    handleClickOpenHistory={handleClickOpenHistory}
                />
                <CustomDeposit
                    openDeposit={openDeposit}
                    setOpenDeposit={setOpenDeposit}
                    setOpenCard={setOpenCard}
                    Transition={Transition}
                />

                <CustomManageFunds
                    openManageFunds={openManageFunds}
                    setOpenManageFunds={setOpenManageFunds}
                    setOpenDeposit={setOpenDeposit}
                    Transition={Transition}
                />

                <CustomCardDialog
                    openCard={openCard} 
                    setOpenCard={setOpenCard}
                    Transition={Transition}
                />

            </div>
        </header>
    );
}