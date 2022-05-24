import "./CustomStockSummary.css";
import React from "react";
import { Typography } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';

export default function CustomStockSummary({data}) {

    if (data.lenght !== 0) {
        return (
            <div className="navigationCustomStockSummary">
                <div id="firstDivCustomStockSummary">
                    <Typography id='priceCustomStockSummary'>$500</Typography>
                    <CustomGraphics margin={'50px'}></CustomGraphics>
                </div>
            </div>
        )
    }
}