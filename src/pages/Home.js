import React from "react";
import "./Home.css";
import Forest from "./Forest.jpg";

function Home() {
  return (
    <div>
      <body>
        <div className="container">
          <img
            src={Forest}
            alt="Forest"  
          ></img>
          <div className="text">
            <h1>Welcome to the Regent Camp Registry</h1>
          </div>
        </div>
        <footer class="footer">
          <div class="container">
            <p class="footer__text">Copyright © 2023</p>
          </div>
        </footer>
      </body>
    </div>
  );
}

export default Home;
