import React from 'react';
import Home from "../Home";
import HomeLogged from "../HomeLogged";
import Validation from '../Validation';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ChangePass from '../ChangePass';
import Test from './test';

export function Webpages() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/home" element={<HomeLogged />} />
        <Route exact path="/validate-account/:id" element={<Validation />} />
        <Route exact path="/reset-pass/:token" element={<ChangePass />} />
        <Route exact path="/test" element={<Test/>} />
      </Routes>
    </BrowserRouter>
  );
}