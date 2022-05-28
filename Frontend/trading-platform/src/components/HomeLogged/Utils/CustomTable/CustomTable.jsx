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

export default function CustomTable() {

  const [rows,setRows]=React.useState([]);
  
  function get_all_stocks() {
    fetch("http://127.0.0.1:5001/get-all-stocks", {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then((data) => {
            if (data.status === 200) {
                data.json().then((message) => {
                    setRows(message['message']);
                });
  
            } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                data.json().then(() => {
                    console.log('Error');
                });
            } else {
                console.log('Error');
            }
        });
  }
  const [time, setTime] = React.useState(0);
  React.useEffect(() => {
    if(time === 0)
    {
      const timer = setTimeout(() => {
          setTime(time + 1);
          get_all_stocks()
      }, 1);
      return () => {
          clearTimeout(timer);
      };
    }
    else
     {
      const timer = setTimeout(() => {
          setTime(time + 1);
          get_all_stocks()
      }, 5000);
      return () => {
          clearTimeout(timer);
      };
    }
  }, [time]);

  return (
    <TableContainer id='customTable' component={Paper}>
      <Table  stickyHeader aria-label="sticky table">
        <TableHead>
          <TableRow>
            <TableCell style={{width:'5px'}}></TableCell>
            <TableCell style={{width:'10px'}}></TableCell>
            <TableCell><Typography>Name</Typography></TableCell>
            <TableCell align="right"><Typography>Symbol</Typography></TableCell>
            <TableCell align="right"><Typography>Price</Typography></TableCell>
            <TableCell align="right"><Typography>Change&nbsp;(%)</Typography></TableCell>
            <TableCell align="right"><Typography>Exchange</Typography></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow>
              <TableCell style={{width:'5px'}}><Button style={{color:'white', backgroundColor:'#0066cc', width:'5px'}}>+</Button></TableCell>
              <TableCell style={{width:'10px'}}><img id='imgCustomTable' src={row.logo} alt={row.stock_symbol} ></img></TableCell>
              <TableCell style ={{top:'10px'}}><Typography>{row.company_name}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.stock_symbol}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.price}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.change}</Typography></TableCell>
              <TableCell align="right"><Typography>{row.exchange}</Typography></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}