import { Button, Dialog, DialogTitle, DialogContent } from '@mui/material';
import './CustomDeposit.css';

export function CustomDeposit({ openDeposit, setOpenDeposit, Transition }) {

    const handleCloseDeposit = () => {
        setOpenDeposit(false);
    };

    return (
        <div>
            <Dialog
                open={openDeposit}
                onClose={handleCloseDeposit}
                TransitionComponent={Transition}
                keepMounted
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{backgroundColor: '#E8E8E8'}}>Deposit funds
                </DialogTitle>
                <DialogContent id='dialogContentDeposit'>
                    Select deposit method
                </DialogContent>
                <Button id='buttonBankTransferDeposit'>
                    <svg id='bankSVGDeposit' xmlns="http://www.w3.org/2000/svg" enableBackground="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24">
                        <g><rect fill="none" height="24" width="24" /></g>
                        <g>
                            <g>
                                <rect fill='white' height="7" width="3" x="4" y="10" />
                                <rect fill='white' height="7" width="3" x="10.5" y="10" /><rect fill='white' height="3" width="20" x="2" y="19" />
                                <rect fill='white' height="7" width="3" x="17" y="10" />
                                <polygon fill='white' points="12,1 2,6 2,8 22,8 22,6" />
                            </g>
                        </g>
                    </svg>
                    Bank transfer

                </Button>
                <Button id='buttonCardDeposit' >
                    <svg id='cardSVGDeposit' xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
                        <path d="M0 0h24v24H0z" fill="none" />
                        <path fill='white' d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z" />
                    </svg>
                    Credit/Debit Card
                </Button>

            </Dialog>
        </div>
    )
}