import "./StockNavigation.css";
import React, { useEffect } from "react";
import { Button, Typography } from "@mui/material";

export default function StockNavigation({buttonStockClicked, setButtonStockClicked, buttonHomeClicked, data}) {

    function clickButton(key)
    {
        setButtonStockClicked(key);
    }

    useEffect(() => {
        if(buttonStockClicked===null)
        {
            setButtonStockClicked(data[0].symbol);
        }
      }, []);

    return (
        <div className="navigationStock">
            {data.map(item =>
            (
                    <Button key={item.symbol} onClick={() => clickButton(item.symbol)} id={(buttonStockClicked==item.symbol)?'buttonClickedNavigationStockLogged':'buttonNavigationStockLogged'}>
                        <img id='imgNavigationStockLogged' src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAAKKSURBVHhe7doxalZBGIbRuQGLIBZBSJMNpHILQnYQYlxPBBvXohKwlb8UQbdharVVyI3CtPfpvDbnVN9bD083y8/Ls3XwXxyN8fLJ7d3bOTfdfD0/jGVczMmO/rwRsEUgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQlh+XZ9fzZmePxvj8+Pbu25ybXn05fz6O1tM5AQAAAAAAAPiXlvH++4d5s7f1/s148fTTXJt+H45fL2N9Nic7+hvIOm/2dz2uTt7Ne9Ovj8eHZRkXc7IjnxUhCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQGDTGA8fayDpGQv7VgAAAABJRU5ErkJggg=="></img>
                        <Typography style={{position:'absolute', left:'80px'}}>
                            {item.name}
                        </Typography>
                        <Typography style={{position:'absolute', right:'20px', color:'green'}}>
                            250$
                        </Typography>
                        </Button>
     
                )
            )}
        </div>
    )
}