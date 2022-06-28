import React from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Dialog, DialogTitle, DialogContent, Typography } from '@mui/material';

export function CustomAllHistory({ openHistory, setOpenHistory, Transition, history }) {

    function handleCloseHistory() {
        setOpenHistory(false);
    };

    return (
        <div>
            <Dialog
                open={openHistory}
                onClose={handleCloseHistory}
                TransitionComponent={Transition}
                keepMounted
                fullWidth
                maxWidth="sm"
                PaperProps={{
                    style: { borderRadius: 10 }
                }}
            >
                <DialogTitle style={{ backgroundColor: '#E8E8E8', textAlign: 'center' }}>
                    History
                </DialogTitle>
                <DialogContent >
                    {(history.length !== 0) && (<TableContainer component={Paper}>
                        <Table style={{ marginTop: '20px', height: '200px' }} stickyHeader aria-label="sticky table">

                            <TableBody style={{ backgroundColor: "#0066cc" }}>
                                {history.map((row) =>
                                (
                                    <TableRow key={row.stock_symbol + row.date_of_buy}>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.stock_symbol}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: (row.action_type === 'BUY') ? '#2AAA8A' : '#7F0000' }}>{row.action_type}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>${row.price}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.cantitate} shares</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.date_of_buy}</Typography></TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>)}
                    {(history.length === 0) && <Typography style={{ marginTop: '80px', marginBottom: '80px' }} align="center">No data available</Typography>}
                </DialogContent>
            </Dialog>
        </div>
    )
}