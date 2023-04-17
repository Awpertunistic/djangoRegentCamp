import React, { Component } from "react";
import "./Registration.css";

class Registration extends Component {
  constructor(props) {
    super(props);
    this.state = {
      parentname: "",
      campername: "",
      camperage: "",
      grade: "",
      contactphone: "",
      email: "",
      campselect: "",
      regstatus: "",
    };
  }

  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({
      [name]: value,
    });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    // perform form submission action (e.g. send data to server)
  };

  render() {
    return (
      // Regent Camp Form Information and Handling
      <form onSubmit={this.handleSubmit} className="form">
        <label className="form__label">
          Parent's Name:
          <input
            type="text"
            name="parentname"
            value={this.state.parentname}
            onChange={this.handleInputChange}
            className="form__input"
          />
        </label>
        <label className="form__label">
          Camper's Name:
          <input
            type="text"
            name="campername"
            value={this.state.campername}
            onChange={this.handleInputChange}
            className="form__input"
          />
        </label>
        <label className="form__label">
          Camper's Age:
          <input
            type="number"
            name="camperage"
            value={this.state.camperage}
            onChange={this.handleInputChange}
            className="form__input"
          />
        </label>
        <label className="form__label">
          Grade:
          <select
            name="grade"
            value={this.state.grade}
            onChange={this.handleInputChange}
            className="form__select"
          >
            <option value="9th">9th</option>
            <option value="10th">10th</option>
            <option value="11th">11th</option>
            <option value="12th">12th</option>
          </select>
        </label>
        <label className="form__label">
          Contact Number:
          <input
            type="tel"
            name="contactphone"
            value={this.state.contactphone}
            onChange={this.handleInputChange}
            className="form__input"
          />
        </label>
        <label className="form__label">
          Email:
          <input
            type="email"
            name="email"
            value={this.state.email}
            onChange={this.handleInputChange}
            className="form__input"
          />
        </label>
        <label className="form__label">
          Camp Selection:
          <select
            name="campselect"
            value={this.state.campselect}
            onChange={this.handleInputChange}
            className="form__select"
          >
            <option value="Biophysical">Biophysical</option>
            <option value="Robotics">Robotics</option>
            <option value="Cyber Security">Cyber Security</option>
            <option value="Crytography">Crytography</option>
          </select>
        </label>
        <label className="form__label">
          Status of Registration:
          <select
            name="regstatus"
            value={this.state.regstatus}
            onChange={this.handleInputChange}
            className="form__select"
          >
            <option value="Registered">Registered</option>
            <option value="Paid">Paid</option>
            <option value="Waiting List">Waiting Listed</option>
          </select>
        </label>
        <button type="submit" className="form__submit-btn">
          Submit
        </button>
      </form>
    );
  }
}

export default Registration;
