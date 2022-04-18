import './DataStock.css';
import React from "react";
import { Typography } from '@mui/material';
import { Button } from '@mui/material';
import CustomGraphics from '../CustomGraphics/CustomGraphics';

export default function DataStock({ buttonDataStockClicked, setButtonDataStockClicked }) {
    return (
        <div className="dataStock">
            <div>
                <img id='imgDataStock' src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAAKKSURBVHhe7doxalZBGIbRuQGLIBZBSJMNpHILQnYQYlxPBBvXohKwlb8UQbdharVVyI3CtPfpvDbnVN9bD083y8/Ls3XwXxyN8fLJ7d3bOTfdfD0/jGVczMmO/rwRsEUgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQlh+XZ9fzZmePxvj8+Pbu25ybXn05fz6O1tM5AQAAAAAAAPiXlvH++4d5s7f1/s148fTTXJt+H45fL2N9Nic7+hvIOm/2dz2uTt7Ne9Ovj8eHZRkXc7IjnxUhCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQGDTGA8fayDpGQv7VgAAAABJRU5ErkJggg=="></img>
                <Typography id='stockName'>Microsoft</Typography>
                <Typography id='stockDetails'>MSFT · STOCK · US  </Typography>
                <div id='buttonsDivDataStock'>
                    <Button id='buttonDataStock'>Sell</Button>
                    <Button id='buttonDataStock'>Buy</Button>
                </div>
                <Typography id='priceDataStock'>$200.99</Typography>
                <CustomGraphics />
            </div>
            <div style={{ backgroundColor: 'rgb(240, 237, 237)', height: '20px' }}></div>
            <div>
                <Typography style={{fontSize:'30px', color:'gray', left:'40px', position:'relative', top:'10px'}}>Company details</Typography>
                <Typography style={{fontSize:'15px', color:'gray', margin:'40px', position:'relative', top:'10px'}}>Microsoft Corporation is a technology company. The Company develops and supports a range of software products, services, devices, and solutions. The Company's segments include Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. The Company's products include operating systems; cross-device productivity applications; server applications; business solution applications; desktop and server management tools; software development tools; and video games. It also designs, manufactures, and sells devices, including personal computers (PCs), tablets, gaming and entertainment consoles, other intelligent devices, and related accessories. It offers an array of services, including cloud-based solutions that provide customers with software, services, platforms, and content, and it provides solution support and consulting services. It markets and distributes its products and services through original equipment manufacturers, direct, and distributors and resellers.</Typography>
            </div>
            <div style={{ backgroundColor: 'rgb(240, 237, 237)', height: '20px' }}></div>
            <div>
                <Typography style={{fontSize:'30px', color:'gray', left:'40px', position:'relative', top:'10px',marginBottom:'20px'}}>Instrument details</Typography>
                <div>
                    <hr style={{backgroundColor:'gray', color:'gray', height: 1, width:'95%', margin: 'auto'}} />
                    <Typography style={{}}>Name</Typography>
                </div>
            </div>
        </div>
    )
}