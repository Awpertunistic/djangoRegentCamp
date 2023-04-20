import { Link } from "react-router-dom";
import "./NavigationBar.css";

export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/" className="site-title">
        Regent Camp Register
      </Link>
      <ul>
        <CustomLink to="/Registration">Registration</CustomLink>
        <CustomLink to="/Status">Status</CustomLink>
        <CustomLink to="/CampManagement">Camp Management</CustomLink>
      </ul>
    </nav>
  );
}

function CustomLink({ to, children, ...props }) {
  const path = window.location.pathname;

  return (
    <li className={path === to ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  );
}
