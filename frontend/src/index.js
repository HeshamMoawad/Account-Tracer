import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./components/Home/Home";
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
// import Twitter from "./components/Twitter/Twitter";
import AgentsPage from "./components/Twitter/AgentsPage/AgentsPage";
import './index.css'

const root = ReactDOM.createRoot(document.getElementById("root"));

export default function App() {
  return (
    <BrowserRouter>
      <Nav />
        <div id="body">
        <Routes>
        <Route index element={<Home />} />
        {/* <Route path="/twitter" element={<Twitter />} /> */}
        <Route path="/twitter" element={<AgentsPage />} />
        </Routes>
        </div>
      <Footer />
    </BrowserRouter>
  );
}

root.render(<App />);
