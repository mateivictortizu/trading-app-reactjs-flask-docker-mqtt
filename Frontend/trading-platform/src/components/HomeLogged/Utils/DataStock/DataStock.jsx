import './DataStock.css';
import React from "react";
import { Typography } from '@mui/material';
import { Button } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';

export default function DataStock({buttonDataStockClicked, setButtonDataStockClicked}) {
    return (
        <div className="dataStock">
            <img id='imgDataStock' src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAAKKSURBVHhe7doxalZBGIbRuQGLIBZBSJMNpHILQnYQYlxPBBvXohKwlb8UQbdharVVyI3CtPfpvDbnVN9bD083y8/Ls3XwXxyN8fLJ7d3bOTfdfD0/jGVczMmO/rwRsEUgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQlh+XZ9fzZmePxvj8+Pbu25ybXn05fz6O1tM5AQAAAAAAAPiXlvH++4d5s7f1/s148fTTXJt+H45fL2N9Nic7+hvIOm/2dz2uTt7Ne9Ovj8eHZRkXc7IjnxUhCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQGDTGA8fayDpGQv7VgAAAABJRU5ErkJggg=="></img>
            <Typography id='stockName'>Microsoft</Typography>
            <Typography id='stockDetails'>MSFT · STOCK · US  </Typography>
            <div id='buttonsDivDataStock'>
                <Button id='buttonDataStock'>Sell</Button>
                <Button id='buttonDataStock'>Buy</Button>
            </div>
            <Typography id='priceDataStock'>$200.99</Typography>
            <CustomGraphics/>
        </div>
    )
}