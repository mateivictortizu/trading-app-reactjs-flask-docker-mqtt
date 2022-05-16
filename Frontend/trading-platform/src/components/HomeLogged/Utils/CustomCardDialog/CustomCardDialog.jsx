import './CustomCardDialog.css';
import React from "react";
import { Dialog, DialogTitle, TextField, Button, DialogContent } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

export function CustomCardDialog({ openCard, setOpenCard, setOpenDeposit, Transition }) {

    const [sumAdd,setSumAdd]=React.useState(0.0);

    function handleCloseCard() {
        setOpenCard(false);
    }

    function pay() {
        fetch("http://127.0.0.1:5002/add-money", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user: "matteovkt@gmail.com",
                    value: parseInt(sumAdd),
                }),
            }).then(setOpenCard(false));
    }

    function back(){
        setOpenCard(false);
        setOpenDeposit(true);
    }

    const handleChangeSumAdd = (event) => {
        setSumAdd(event.target.value);
    };


    return (
        <div>
            <Dialog
                open={openCard}
                onClose={handleCloseCard}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{ backgroundColor: '#E8E8E8', textAlign: 'center' }}> Add card
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
                            id="Card number"
                            label="Card number"
                            type="string"
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Expiry date"
                            label="Expiry date"
                            type="string"
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="CVC/CVV"
                            label="CVC/CVV"
                            type="string"
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Name on card"
                            label="Name on card"
                            type="string"
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Sum"
                            label="Sum"
                            type="string"
                            value={sumAdd}
                            onChange={handleChangeSumAdd}
                            style={{ width: '90%', marginTop: '20px' }}
                        />

                        <Button id='buttonPayCardDialog' onClick={pay}>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none" /><path fill='white' d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z" /></svg>
                            &nbsp;
                            Pay
                        </Button>
                    </div>
                </DialogContent>
            </Dialog>
        </div>
    )
}