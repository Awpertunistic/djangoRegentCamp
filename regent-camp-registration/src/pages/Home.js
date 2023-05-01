import React from "react";
import "./Home.css";
import Forest from "./Forest.jpg";
import Hammock from "./Hammock.jpeg";

function Home() {
  return (
    <body>
      <div class="wrapper">
        <section class="section-opening">
          <img src={Forest} alt="Forest" class="section-opening-img"></img>
          <div class="section-opening-text">
            <h1>Welcome to the Regent Camp Registry</h1>
          </div>
        </section>
        <section class="section-content">
          <div class="section-content-text">
            <h2>A Place to Reset</h2>
            <p>
              "Remember not the former things, nor consider the things of old.
              Behold, I am doing a new thing; now it springs forth, do you not
              perceive it? I will make a way in the wilderness and rivers in the
              desert." -Isaiah 43:18-19
            </p>
          </div>
          <img src={Hammock} alt="Hammock" class="section-content-img"></img>
        </section>
        <footer class="footer">
          <div class="container">
            <ul class="footer__links">
              <li>
                <a href="https://www.instagram.com/regentuniversity/">
                  Instagram
                </a>
              </li>
              <li>
                <a href="https://www.facebook.com/regentuniversity/">
                  Facebook
                </a>
              </li>
              <li>
                <a href="https://www.linkedin.com/school/regent-university/">
                  LinkedIn
                </a>
              </li>
            </ul>
            <p class="footer__text">Copyright © 2023</p>
          </div>
        </footer>
      </div>
    </body>
  );
}

export default Home;
