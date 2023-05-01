import Navbar from "./pages/NavigationBar";
import React from "react";
import Home from "./pages/Home";
import Registration from "./pages/Registration";
import Status from "./pages/Status";
import CampManagement from "./pages/CampManagement";
import { Route, Routes } from "react-router-dom";

//Dummy data to see if the Status Page functions properly
const students = [
  {
    campername: "Alice",
    camperage: 10,
    grade: 5,
    contactphone: "555-1234",
    email: "alice@example.com",
    campselection: "Cyber Security",
    regstatus: "registered",
  },
  {
    campername: "Bob",
    camperage: 12,
    grade: 7,
    contactphone: "555-5678",
    email: "bob@example.com",
    campselection: "Robotics",
    regstatus: "pending",
  },
  {
    campername: "Charlie",
    camperage: 8,
    grade: 3,
    contactphone: "555-9012",
    email: "charlie@example.com",
    campselection: "Biophysical",
    regstatus: "cancelled",
  },
];

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Registration" element={<Registration />} />
          <Route path="/Status" element={<Status students={students} />} />
          <Route path="/CampManagement" element={<CampManagement />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
