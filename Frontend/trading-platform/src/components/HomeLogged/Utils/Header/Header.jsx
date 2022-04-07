import "./Header.css";
import React from "react";
import { Slide } from '@mui/material';
import { CustomAppBar } from "../CustomAppBar/CustomAppBar";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});

export default function Header() {
    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <CustomAppBar/>
            </div>
        </header>
    );
}