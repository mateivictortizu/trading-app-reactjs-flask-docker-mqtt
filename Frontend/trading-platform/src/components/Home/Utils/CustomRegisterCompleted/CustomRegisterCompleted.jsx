import React from "react";
import { DialogContent, Dialog } from "@mui/material";
import DoneIcon from '@mui/icons-material/Done';

export function CustomRegisterCompleted({ openDialog, setOpenRegisterCompleted, Transition, message }) {

    const handleClickCloseRegisterComplete = () => {
        setOpenRegisterCompleted(false);
    };


    return (
        <div>
            <Dialog
                open={openDialog}
                onClose={handleClickCloseRegisterComplete}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                style={{ backdropFilter: 'blur(4px)' }}
            >
                <DialogContent style={{ backgroundColor: '#e8fbe8' }}>
                    <div style={{ textAlign: 'center' }}><DoneIcon style={{ color: "green", fontSize: '4em' }}></DoneIcon></div>
                    <div style={{ textAlign: 'center' }}>{message}</div>

                </DialogContent>
            </Dialog>
        </div>
    )
}