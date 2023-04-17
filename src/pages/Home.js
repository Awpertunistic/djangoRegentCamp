import React from "react";

function Home() {
  return (
    <div>
      <h1>Welcome to my React App!</h1>
      <p>
        This is the home page. Here you can find information about our app and
        what it does.
      </p>
      <form>
        <label for="fname">First Name:</label>
        <input type="text" id="fname" name="fname"></input>
      </form>
    </div>
  );
}

export default Home;
