import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Status.css";

function Status() {
  const [updatedStudents, setUpdatedStudents] = useState([]);

  useEffect(() => {
    fetch("/backend/register/")
      .then((response) => response.json())
      .then((data) => setUpdatedStudents(data));
  }, []);

  const handleRegStatusChange = (index, newRegStatus) => {
    const updatedStudent = {
      ...updatedStudents[index],
      regstatus: newRegStatus,
    };
    const newStudents = [...updatedStudents];
    newStudents[index] = updatedStudent;
    setUpdatedStudents(newStudents);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const studentsToDelete = updatedStudents?.filter(
      (student) => student.regstatus === "cancelled"
    );

    if (studentsToDelete?.length > 0) {
      axios
        .delete("/backend/delete/", {
          data: { students: studentsToDelete },
        })
        .then((response) => {
          console.log(response.data);
          alert("Successfully Received!");
        })
        .catch((error) => {
          console.log(error);
          alert("Unable to Submit Request.");
        });
    }

    const studentsToUpdate = updatedStudents?.filter(
      (student) => student.regstatus !== student.originalRegstatus
    );

    if (studentsToUpdate?.length > 0) {
      axios
        .post("/backend/update_reg_status/", { students: studentsToUpdate })
        .then((response) => {
          console.log(response.data);
          alert("Successfully updated!");
        })
        .catch((error) => {
          console.log(error);
          alert("Unable to update status.");
        });
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <table>
          <thead>
            <tr>
              <th>Camper Name</th>
              <th>Age</th>
              <th>Grade</th>
              <th>Contact Phone</th>
              <th>Email</th>
              <th>Camp Selection</th>
              <th>Registration Status</th>
            </tr>
          </thead>
          <tbody>
            {updatedStudents?.map((student, index) => (
              <tr key={index}>
                <td>{student.CamperName}</td>
                <td>{student.CamperAge}</td>
                <td>{student.CamperGrade}</td>
                <td>{student.PhoneNumber}</td>
                <td>{student.Email}</td>
                <td>{student.Program}</td>
                <td>
                  <select
                    value={student.regstatus}
                    onChange={(event) =>
                      handleRegStatusChange(index, event.target.value)
                    }
                  >
                    <option value="Registered">Registered</option>
                    <option value="Paid">Paid</option>
                    <option value="Waiting List">Waiting List</option>
                    <option value="cancelled">Cancelled</option>
                  </select>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="submit-button" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
}

export default Status;
