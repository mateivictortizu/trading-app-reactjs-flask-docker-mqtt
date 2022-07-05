import React from "react";
import { Dialog, DialogTitle, TextField, Button, DialogContent } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';
import MuiAlert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';

export function CustomWithdrawMoney({ openWithdraw, setOpenWithdraw, setOpenDeposit, Transition }) {

    const [suma, setSuma] = React.useState(0.0);
    const [iban, setIban] = React.useState('');
    const [bank, setBank] = React.useState('');
    const [swift, setSwift] = React.useState('');
    const [openAlert, setOpenAlert] = React.useState(false);
    const [messageAlert, setMessageAlert] = React.useState([]);


    const handleCloseAlert = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpenAlert(false);
    };

    const Alert = React.forwardRef(function Alert(props, ref) {
        return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
    });

    function handleCloseWithdraw() {
        setSuma(0);
        setIban('');
        setBank('');
        setSwift('');
        setOpenWithdraw(false);

    };

    function withdraw() {
        if(suma>0 && iban.length>=15 && iban.length<=34 && swift.length>0)
        {
            fetch(GATEWAY_HOST + "/withdraw-money", {
                method: "POST",
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    value: parseFloat(suma),
                }),
            }).then((data) => {
                if (data.status === 200) {
                    handleCloseWithdraw();
                }
                else if (data.status === 401) {
                    setMessageAlert(['You have not enough money to withdraw this sum', "error"])
                    setOpenAlert(true);
                }
                else {
                    setMessageAlert(['Withdraw failed', "error"])
                    setOpenAlert(true);
                }
            }
            );
        }
        else
        {
            setMessageAlert(['Data errors', "error"])
            setOpenAlert(true);
        }
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
                    <Snackbar open={openAlert} autoHideDuration={6000} onClose={handleCloseAlert} anchorOrigin={{
                        vertical: "bottom",
                        horizontal: "center"
                    }}>
                        <Alert onClose={handleCloseAlert} severity={messageAlert[1]} sx={{ width: '100%' }} >
                            {messageAlert[0]}
                        </Alert>
                    </Snackbar>
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