import React from 'react';
import { Navbar } from 'react-bootstrap';

class Header extends React.Component {
  render() {
    return (
      <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand href="#home">My Music App!</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Navbar.Text className="ml-auto text-white">Welcome to the SoundCloud Downloader</Navbar.Text>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default Header;