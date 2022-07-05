import React from "react";
import { Dialog, DialogTitle, TextField, Button, DialogContent } from '@mui/material';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';
import MuiAlert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';


export function CustomSettings({ openSettings, setOpenSettings, Transition }) {
    function handleCloseSettings() {
        setOpenSettings(false);
        setOldPassword('');
        setNewPassword('');
        setRepeatNewPassword('');
    };

    const [oldPassword, setOldPassword] = React.useState('');
    const [newPassword, setNewPassword] = React.useState('');
    const [repeatNewPassword, setRepeatNewPassword] = React.useState('');
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

    const handleChangeOldPassword = (event) => {
        setOldPassword(event.target.value);
    };

    const handleChangeNewPassword = (event) => {
        setNewPassword(event.target.value);
    };

    const handleChangeRepeatNewPassword = (event) => {
        setRepeatNewPassword(event.target.value);
    };

    function change_pass() {
        fetch(GATEWAY_HOST + "/change-password", {
            method: "PUT",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                password: oldPassword,
                new_password: newPassword
            }),
        }).then((data) => {
            if (data.status === 200) {
                data.json().then(() => {
                    handleCloseSettings();
                });

            }
            else if (data.status === 403) {
                setMessageAlert(['Change password error', "error"])
                setOpenAlert(true);
            }
            else if (data.status === 404 || data.status === 400 | data.status === 401) {
                data.json().then(() => {
                    setMessageAlert(['Change password error', "error"])
                    setOpenAlert(true);
                });
            } else {
                setMessageAlert(['Change password error', "error"])
                setOpenAlert(true);
            }
        }
        );
    }

    return (
        <div>
            <Dialog
                open={openSettings}
                onClose={handleCloseSettings}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{ backgroundColor: '#E8E8E8', textAlign: 'center' }}> Settings
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
                            id="Old password"
                            label="Old password"
                            type="password"
                            value={oldPassword}
                            onChange={handleChangeOldPassword}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="New Password"
                            label="New Password"
                            type="password"
                            value={newPassword}
                            onChange={handleChangeNewPassword}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="Repeat New Password"
                            label="Repeat New Password"
                            type="password"
                            value={repeatNewPassword}
                            onChange={handleChangeRepeatNewPassword}
                            style={{ width: '90%', marginTop: '20px' }}
                        />
                        <Button id='buttonPayCardDialog' onClick={change_pass}>
                            Change Password
                        </Button>
                    </div>
                </DialogContent>
            </Dialog>
        </div>
    )
}