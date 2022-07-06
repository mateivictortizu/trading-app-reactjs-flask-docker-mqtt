import React from "react";
import { Webpages } from "./webpages";
import { CookiesProvider } from 'react-cookie';

function App() {
  return (
    <CookiesProvider>
      <Webpages></Webpages>
    </CookiesProvider>
  );
}

export default App;