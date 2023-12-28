import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./components/Home/Home";
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
import AgentsPage from "./components/Twitter/AgentsPage/AgentsPage";
import AccountsPage from "./components/Twitter/AccountsPage/AccountsPage";
import "./index.css";
import Twitter from "./components/Twitter/Twitter";
import AnalyticsPage from "./components/Twitter/AnalyticsPage/AnalyticsPage";

const root = ReactDOM.createRoot(document.getElementById("root"));

export default function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div id="body">
        <Routes>
          <Route index element={<Home />} />
          <Route path="twitter" element={<Twitter />}>
            <Route index element={<AgentsPage />} />
            <Route path="agents" element={<AgentsPage />} />
            <Route path=":project/:agentName" element={<AccountsPage />} />
            <Route path="analytics/:handle" element={<AnalyticsPage />} />
          </Route>
        </Routes>
      </div>
      <Footer />
    </BrowserRouter>
  );
}

root.render(<App />);
