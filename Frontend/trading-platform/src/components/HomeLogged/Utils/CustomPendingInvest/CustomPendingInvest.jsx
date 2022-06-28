import React from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Dialog, DialogTitle, DialogContent, Typography, Button, Input } from '@mui/material';
import RemoveCircleIcon from '@mui/icons-material/RemoveCircle';
import { GATEWAY_HOST } from '../../../../Utils/Extra/Hosts';

export function CustomPendingInvest({ openPendingInvest, setOpenPendingInvest, Transition, stock_symbol, logo, stockName, pendingInvest }) {

    function handleClosePendingInvest() {
        setOpenPendingInvest(false);
    };

    function removeFromAutobuy(id_invest){
        
        fetch(GATEWAY_HOST + "/remove-autoinvest", {
            method: "DELETE",
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id_invest:id_invest
            })
        })
            .then((data) => {
                if (data.status === 200) {
                    data.json().then((message) => {
                        console.log(message);
                    });
                }
                else if (data.status === 403) {
                    console.log('Da');
                }
            });
    };

    return (
        <div>
            <Dialog
                open={openPendingInvest}
                onClose={handleClosePendingInvest}
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
                    Pending - {stockName}
                </DialogTitle>
                <DialogContent >
                    {(pendingInvest.length !== 0) && (<TableContainer component={Paper}>
                        <Table style={{ marginTop: '20px', height: '200px' }} stickyHeader aria-label="sticky table">
                            <TableHead>
                                <TableRow>
                                    <TableCell style={{ width: '5px' }}></TableCell>
                                    <TableCell><Typography>Symbol</Typography></TableCell>
                                    <TableCell><Typography>Action</Typography></TableCell>
                                    <TableCell align="center"><Typography>Target price</Typography></TableCell>
                                    <TableCell align="center"><Typography>Quantity</Typography></TableCell>
                                    <TableCell align="center"><Typography>Date</Typography></TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody style={{ backgroundColor: "#0066cc" }}>
                                {pendingInvest.map((row) =>
                                (
                                    <TableRow key={row.stock_symbol + row.id}>
                                        <TableCell style={{ width: '5px' }}>
                                            <Button style={{ color: 'red', backgroundColor: '#0066cc', minHeight: '0px', height: '40px', minWidth: '0px', width: '40px' }} onClick={() => removeFromAutobuy(row.id)}><RemoveCircleIcon style={{ fontSize: '40px' }} /></Button>
                                        </TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.stock_symbol}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: (row.action_type === 'BUY') ? '#2AAA8A' : '#7F0000' }}>{row.action_type}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>${row.price}</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.cantitate} shares</Typography></TableCell>
                                        <TableCell align="center"><Typography style={{ color: 'white' }}>{row.date_of_autobuy}</Typography></TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>)}
                    {(pendingInvest.length === 0) && <Typography style={{ marginTop: '80px', marginBottom: '80px' }} align="center">No data available</Typography>}
                </DialogContent>
            </Dialog>
        </div>
    )
}