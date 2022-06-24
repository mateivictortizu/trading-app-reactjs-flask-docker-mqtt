import React from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input } from '@mui/material';

export function CustomHistory({ openHistory, setOpenHistory, Transition, stock_symbol, logo, stockName, history, setHistory }) {

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
                    <img id='imgCustomBuy' src={logo}></img>
                    History - {stockName}
                </DialogTitle>
                <DialogContent >
                    {(history.length!==0)&&(<TableContainer component={Paper}>
                        <Table style={{marginTop:'20px', height:'200px'}}  stickyHeader aria-label="sticky table">
                            <TableHead>
                                <TableRow >
                                    <TableCell align="center"><Typography>Name</Typography></TableCell>
                                    <TableCell align="center"><Typography>Action Type</Typography></TableCell>
                                    <TableCell align="center"><Typography>Price</Typography></TableCell>
                                    <TableCell align="center"><Typography>Quantity</Typography></TableCell>
                                    <TableCell align="center"><Typography>Date</Typography></TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {history.map((row) =>
                                (
                                    <TableRow key={row.stock_symbol + row.date_of_buy}>
                                        <TableCell align="center"><Typography>{row.stock_symbol}</Typography></TableCell>
                                        <TableCell align="center"><Typography>{row.action_type}</Typography></TableCell>
                                        <TableCell align="center"><Typography>{row.price}</Typography></TableCell>
                                        <TableCell align="center"><Typography>{row.cantitate}</Typography></TableCell>
                                        <TableCell align="center"><Typography>{row.date_of_buy}</Typography></TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>)}
                    {(history.length===0)&&<Typography style={{marginTop:'80px', marginBottom:'80px'}} align="center">No data available</Typography>}
                </DialogContent>
            </Dialog>
        </div>
    )
}