import './CustomManageFunds.css';
import { Button, Dialog, DialogTitle, DialogContent } from '@mui/material';

export function CustomManageFunds({ openManageFunds, setOpenManageFunds, setOpenDeposit, setOpenWithdraw, Transition }) {
    const handleCloseManageFunds = () => {
        setOpenManageFunds(false);
    };

    function handleOpenDeposit() {
        handleCloseManageFunds();
        setOpenDeposit(true);
    };

    function handleOpenWithdraw(){
        handleCloseManageFunds();
        setOpenWithdraw(true);

    };

    return (
        <div>
            <Dialog
                open={openManageFunds}
                onClose={handleCloseManageFunds}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle> Manage funds
                </DialogTitle>
                <DialogContent dividers id='dialogContentManageFunds'>
                    <Button id='buttonDepositFundsManageFunds' onClick={handleOpenDeposit}>

                        Deposit funds

                    </Button>
                    <div id='divBetweenButtonsManageFunds'></div>
                    <Button id='buttonWithdrawFundsManageFunds' onClick={handleOpenWithdraw}>

                        Withdraw funds

                    </Button>
                </DialogContent>
            </Dialog>
        </div>
    )
}