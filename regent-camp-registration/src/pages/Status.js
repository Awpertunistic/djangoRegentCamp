import React, { useState } from "react";
import "./Status.css";

function Status({ students }) {
  const [updatedStudents, setUpdatedStudents] = useState(students);

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
    console.log(updatedStudents);
    // You can add your code to submit the updated students' data to the server here
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
            {updatedStudents.map((student, index) => (
              <tr key={index}>
                <td>{student.campername}</td>
                <td>{student.camperage}</td>
                <td>{student.grade}</td>
                <td>{student.contactphone}</td>
                <td>{student.email}</td>
                <td>{student.campselection}</td>
                <td>
                  <select
                    value={student.regstatus}
                    onChange={(event) =>
                      handleRegStatusChange(index, event.target.value)
                    }
                  >
                    <option value="registered">Registered</option>
                    <option value="pending">Pending</option>
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
