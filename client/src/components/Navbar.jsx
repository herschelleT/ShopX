import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import PropTypes from "prop-types";
import { useSelector } from "react-redux";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function TopBar({ updateTab }) {
  const userInfo = useSelector((state) => state.user.userInfo);
  const navigate = useNavigate();
  useEffect(() => {
    if(!userInfo) navigate("/auth")
    console.log(userInfo);
  
  }, [])
  return (
    <Navbar bg="dark" data-bs-theme="dark" className="w-full text-3xl">
      <Container>
        <Navbar.Brand>ShopX</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link
            onClick={() => {
              updateTab("Shop");
            }}
            value="Shop"
          >
            Shop
          </Nav.Link>
          <Nav.Link
            onClick={() => {
              updateTab("Wishlist");
            }}
            value="Wishlist"
          >
            Wishlist
          </Nav.Link>
          {userInfo?.type==="admin" && 
          <Nav.Link
            onClick={() => {
              updateTab("Admin");
            }}
            value="Admin"
          >
            Admin
          </Nav.Link>}
          <Nav.Link
            onClick={() => {
              updateTab("Settings");
            }}
            value="Settings"
          >
            Settings
          </Nav.Link>
        </Nav>
        <div className="ml-auto">
          {userInfo?.user_email }
        </div>
      </Container>
    </Navbar>
  );
}

export default TopBar;
