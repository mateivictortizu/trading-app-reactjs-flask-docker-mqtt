import { DialogContent, Dialog,DialogActions,DialogTitle } from "@mui/material";
import DoneIcon from '@mui/icons-material/Done';
import ThumbDownAltIcon from '@mui/icons-material/ThumbDownAlt';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';

export function CustomRegisterCompleted({openDialog, handleClose, Transition, message}) {
    return (
        <div>
            <Dialog
                open={openDialog}
                onClose={handleClose}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                style={{backdropFilter: 'blur(4px)'}}
            >
                <DialogContent style={{backgroundColor: '#e8fbe8'}}>
                    <div style={{textAlign:'center'}}><DoneIcon style = {{ color: "green",  fontSize: '4em'}}></DoneIcon></div>
                    <div style={{textAlign:'center'}}>{message}</div>

                </DialogContent>
            </Dialog>
        </div>
    )

}