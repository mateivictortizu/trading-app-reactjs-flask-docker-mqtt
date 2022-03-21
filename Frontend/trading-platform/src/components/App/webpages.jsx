import React from 'react';
import Home from "../Home";
import HomeLogged from "../HomeLogged";
import { BrowserRouter, Routes, Route} from "react-router-dom";

export function Webpages() {
    return (
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/blogs" element={<HomeLogged />} />
          <Route exact path="/tests" element={<HomeLogged />} />
        </Routes>
      </BrowserRouter>
    );
  }