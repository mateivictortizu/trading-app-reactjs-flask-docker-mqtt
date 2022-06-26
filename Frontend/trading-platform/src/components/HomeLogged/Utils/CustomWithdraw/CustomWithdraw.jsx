import React from "react";
import { Dialog, DialogTitle, TextField, Button, DialogContent } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';

export function CustomWithdrawMoney({ openWithdraw, setOpenWithdraw, setOpenDeposit, Transition }) {

    const [suma, setSuma] = React.useState(0.0);
    const [iban, setIban] = React.useState('');
    const [bank, setBank] = React.useState('');
    const [swift, setSwift] = React.useState('');

    function handleCloseWithdraw() {
        setOpenWithdraw(false);

    };

    function withdraw() {
        fetch(GATEWAY_HOST + "//withdraw-money", {
            method: "POST",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(suma),
            }),
        }).then(handleCloseWithdraw());
    };

    function back() {
        setOpenWithdraw(false);
        setOpenDeposit(true);
    };

    const handleChangeSuma = (event) => {
        setSuma(event.target.value);
    };

    const handleChangeIban = (event) => {
        setIban(event.target.value);
    };

    const handleChangeBank = (event) => {
        setBank(event.target.value);
    };

    const handleChangeSwift = (event) => {
        setSwift(event.target.value);
    };

    return (
        <div>
            <Dialog
                open={openWithdraw}
                onClose={handleCloseWithdraw}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{ backgroundColor: '#E8E8E8', textAlign: 'center' }}> Withdraw Funds
                    <IconButton
                        aria-label="close"
                        onClick={back}
                        sx={{
                            position: 'absolute',
                            left: 8,
                            top: 10,
                            color: 'black'
                        }}>
                        <ArrowBackIcon />
                    </IconButton>
                </DialogTitle>
                <DialogContent style={{ width: '99%' }}>
                    <div style={{ textAlign: 'center', borderRadius: '10px', marginTop: '20px', backgroundColor: '#E8E8E8' }}>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="IBAN"
                            label="IBAN"
                            type="string"
                            value={iban}
                            onChange={handleChangeIban}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Bank"
                            label="Bank"
                            type="string"
                            value={bank}
                            onChange={handleChangeBank}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="SWIFT"
                            label="SWIFT"
                            type="string"
                            value={swift}
                            onChange={handleChangeSwift}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Sum"
                            label="Sum"
                            type="string"
                            value={suma}
                            onChange={handleChangeSuma}
                            style={{ width: '90%', marginTop: '20px' }}
                        />

                        <Button id='buttonPayCardDialog' onClick={withdraw}>
                            WITHDRAW
                        </Button>
                    </div>
                </DialogContent>
            </Dialog>
        </div>
    )
}