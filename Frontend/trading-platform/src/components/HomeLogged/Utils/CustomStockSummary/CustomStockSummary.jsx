import "./CustomStockSummary.css";
import React from "react";
import { Typography } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';

export default function CustomStockSummary({ data }) {

    var price = 500;
    var invested = 600;
    var returned = -143;

    if (data.lenght !== 0) {
        return (
            <div className="navigationCustomStockSummary">
                <div id="firstDivCustomStockSummary">
                    <Typography id='priceCustomStockSummary'>${price}</Typography>
                    <Typography id='investedCustomStockSummary'>INVESTED</Typography>
                    <Typography id='returnCustomStockSummary'>RETURN</Typography>
                    <Typography id='valueinvestedCustomStockSummary'>${invested}</Typography>
                    <Typography id='valuereturnCustomStockSummary'>-${returned}</Typography>
                    <CustomGraphics margin={'100px'}></CustomGraphics>
                </div>
            </div>
        )
    }
}