import Navbar from "./pages/NavigationBar";
import React from "react";
import Home from "./pages/Home";
import Registration from "./pages/Registration";
import Status from "./pages/Status";
import CampManagement from "./pages/CampManagement";
import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Registration" element={<Registration />} />
          <Route path="/Status" element={<Status />} />
          <Route path="/CampManagement" element={<CampManagement />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
