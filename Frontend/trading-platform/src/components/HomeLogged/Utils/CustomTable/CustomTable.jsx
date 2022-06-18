import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import './CustomTable.css';
import { Button, Typography } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import RemoveCircleIcon from '@mui/icons-material/RemoveCircle';

export default function CustomTable({rows}) {

  function addToWishlist(stock_symbol)
  {
    console.log(stock_symbol);
  }

  function removeFromWishlist(stock_symbol)
  {
    console.log(stock_symbol);
  }



  React.useEffect(() => {
  }, []);

  return (
    <TableContainer id='customTable' component={Paper}>
      <Table stickyHeader aria-label="sticky table">
        <TableHead>
          <TableRow>
            <TableCell style={{ width: '5px' }}></TableCell>
            <TableCell style={{ width: '10px' }}></TableCell>
            <TableCell><Typography>Name</Typography></TableCell>
            <TableCell align="right"><Typography>Symbol</Typography></TableCell>
            <TableCell align="right"><Typography>Price</Typography></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.stock_symbol}>
              <TableCell style={{ width: '5px' }}><Button style={{ color: '#0066cc', backgroundColor: 'white', minHeight:'0px', height:'40px', minWidth:'0px', width:'40px'}} onClick={()=>addToWishlist(row.stock_symbol)}><AddCircleIcon style={{fontSize:'40px'}}/></Button></TableCell>
              <TableCell style={{ width: '10px' }}><img id='imgCustomTable' src={row.logo} alt={row.stock_symbol} ></img></TableCell>
              <TableCell style={{ top: '10px' }}><Typography>{row.company_name}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.stock_symbol}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.price}</Typography></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}