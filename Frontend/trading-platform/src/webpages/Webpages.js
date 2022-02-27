import React from "react"
import { HashRouter as Router, Route, Routes} from "react-router-dom"
import Home from "../components/Home";

const Webpages = () =>
{
    return(
        <Router>
            <Routes>
            <Route path="/" element={<Home />}></Route> 
             </Routes>
        </Router>
    );
};

export default Webpages;