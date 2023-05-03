import React, { useState } from "react";
import axios from "axios";
import "./CampManagement.css";

function CampManagement() {
  const [emailSubject, setEmailSubject] = useState("");
  const [emailMessage, setEmailMessage] = useState("");
  const [selectedCamp, setSelectedCamp] = useState("");

  const handleCampChange = (event) => {
    setSelectedCamp(event.target.value);
  };

  const handleSubjectChange = (event) => {
    setEmailSubject(event.target.value);
  };

  const handleMessageChange = (event) => {
    setEmailMessage(event.target.value);
  };

  const handleSendEmail = () => {
    axios
      .post("/backend/send-emails/", {
        camp: selectedCamp,
        subject: emailSubject,
        message: emailMessage,
      })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="camp-management-container">
      <h1 className="camp-management-heading">Camp Management</h1>
      <label className="camp-management-label" htmlFor="camp-selection">
        Select a camp:
      </label>
      <select
        className="camp-management-select"
        id="camp-selection"
        value={selectedCamp}
        onChange={handleCampChange}
      >
        <option value="">Select a camp</option>
        <option value="Biophysical">Biophysical</option>
        <option value="Robotics">Robotics</option>
        <option value="Cyber Security">Cyber Security</option>
        <option value="Cryptography">Cryptography</option>
      </select>
      <br />
      <label className="camp-management-label" htmlFor="email-subject">
        Email subject:
      </label>
      <input
        className="camp-management-input"
        type="text"
        id="email-subject"
        value={emailSubject}
        onChange={handleSubjectChange}
      />
      <br />
      <label className="camp-management-label" htmlFor="email-message">
        Email message:
      </label>
      <textarea
        className="camp-management-textarea"
        id="email-message"
        value={emailMessage}
        onChange={handleMessageChange}
      />
      <br />
      <button className="camp-management-button" onClick={handleSendEmail}>
        Send Emails
      </button>
    </div>
  );
}

export default CampManagement;
