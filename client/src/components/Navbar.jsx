import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import PropTypes from "prop-types";

function TopBar({ updateTab }) {
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
              updateTab("Cart");
            }}
            value="Cart"
          >
            Cart
          </Nav.Link>
          <Nav.Link
            onClick={() => {
              updateTab("Settings");
            }}
            value="Settings"
          >
            Settings
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}
TopBar.propTypes = {
  updateTab: PropTypes.string,
};
export default TopBar;
