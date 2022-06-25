import { Typography } from "@mui/material";
import React from "react";
import './CustomSummary.css';
export default function CustomSummary({ average, current_value }) {

    return (
        <div id='divSummary'>
            <div style={{marginTop:'60px'}}>
                <Typography id='typographyTitle'>Invested:</Typography>
                <Typography id='infoSummary'>${average.toFixed(2)}</Typography>
                <Typography id='typographyTitle'>Current value:</Typography>
                <Typography id='infoSummary'>${current_value.toFixed(2)}</Typography>
                <Typography id='typographyTitle'>Change:</Typography>
                <Typography id='changeSummary' style={{color:(((current_value - average) / average * 100)>0)?'#2AAA8A':'#7F0000'}}>{((current_value - average) / average * 100).toFixed(2)}%</Typography>
            </div>
        </div>
    )
}