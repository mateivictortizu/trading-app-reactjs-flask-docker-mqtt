import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import React from "react";

export function CustomSnackbarAlert({ open, handleClose,message,severityType}) {
    const Alert = React.forwardRef(function Alert(props, ref) {
        return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
    });

    return (
        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}
            anchorOrigin={{
                vertical: "bottom",
                horizontal: "center"
            }}>
            <Alert onClose={handleClose} severity={severityType} fullWidth>
                {message}
            </Alert>
        </Snackbar>
    )
}