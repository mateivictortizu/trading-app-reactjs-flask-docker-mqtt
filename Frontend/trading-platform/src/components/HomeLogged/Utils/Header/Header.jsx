import "./Header.css";
import React from "react";
import { Slide } from '@mui/material';
import { CustomAppBarLogged } from "../CustomAppBarLogged/CustomAppBarLogged";
import { CustomDeposit } from "../CustomDeposit/CustomDeposit";
import { CustomManageFunds } from "../CustomManageFunds/CustomManageFunds";
import { CustomCardDialog } from "../CustomCardDialog/CustomCardDialog";
import { CustomAllHistory } from "../CustomAllHistory/CustomAllHistory";
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';
import { CustomSettings } from "../CustomSettings/CustomSettings";
import { CustomWithdrawMoney } from "../CustomWithdraw/CustomWithdraw";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});


export default function Header({ accountValue, investValue }) {
    const [openDeposit, setOpenDeposit] = React.useState(false);
    const [openManageFunds, setOpenManageFunds] = React.useState(false);
    const [openHistory, setOpenHistory] = React.useState(false);
    const [openCard, setOpenCard] = React.useState(false);
    const [history, setHistory] = React.useState([]);
    const [openSettings, setOpenSettings] = React.useState(false);
    const [openWithdraw, setOpenWithdraw] = React.useState(false);

    function handleClickOpenDeposit() {
        setOpenDeposit(true)
    }

    function handleClickOpenManageFunds() {
        setOpenManageFunds(true)
    }

    function handleClickOpenSettings() {
        setOpenSettings(true)
    }

    function handleClickOpenHistory() {

        fetch(GATEWAY_HOST + "/get-all-history-user", {
            method: "POST",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then((data) => {
            if (data.status === 200) {
                data.json().then((message) => {
                    console.log(message);
                    setHistory(message['message']);

                })

            }
            else if (data.status === 403) {
                console.log('Error');
            }
            else if (data.status === 404 || data.status === 400 | data.status === 401) {
                data.json().then(() => {
                    console.log('Error');
                });
            } else {
                console.log('Error');
            }
        }
        )
        setOpenHistory(true);
    }

    return (
        <header className="headerLogged">
            <div className="header_header-container-logged">
                <CustomAppBarLogged
                    handleClickOpenDeposit={handleClickOpenDeposit}
                    handleClickOpenManageFunds={handleClickOpenManageFunds}
                    handleClickOpenHistory={handleClickOpenHistory}
                    handleClickOpenSettings={handleClickOpenSettings}
                    accountValue={accountValue}
                    investValue={investValue}
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
                    setOpenWithdraw={setOpenWithdraw}
                    Transition={Transition}
                />

                <CustomWithdrawMoney
                    openWithdraw={openWithdraw}
                    setOpenWithdraw={setOpenWithdraw}
                    setOpenDeposit={setOpenDeposit}
                    Transition={Transition}
                />

                <CustomCardDialog
                    openCard={openCard}
                    setOpenCard={setOpenCard}
                    setOpenDeposit={setOpenDeposit}
                    Transition={Transition}
                />

                <CustomSettings
                    openSettings={openSettings}
                    setOpenSettings={setOpenSettings}
                    Transition={Transition}
                />

                <CustomAllHistory
                    openHistory={openHistory}
                    setOpenHistory={setOpenHistory}
                    Transition={Transition}
                    history={history}
                ></CustomAllHistory>

            </div>
        </header>
    );
}