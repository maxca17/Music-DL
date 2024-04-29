import React from 'react';
import axios from 'axios';
import { Button, Form, Container, Row, Col, Alert, FormGroup, FormControl, FormLabel } from 'react-bootstrap';
import Header from './header';
import Footer from './footer';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: '',
      errorMessage: '',
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ url: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();

    axios
      .post('/api/download', {
        url: this.state.url,
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

    this.setState({ url: '' });
  }

  render() {
    return (
      <div>
        <Header />
        <Container>
          <Row className="justify-content-md-center">
            <Col md="auto">
              <Form onSubmit={this.handleSubmit}>
                <FormGroup controlId="url">
                  <FormLabel>URL</FormLabel>
                  <FormControl
                    type="url"
                    placeholder="Enter SoundCloud track URL"
                    value={this.state.url}
                    onChange={this.handleChange}
                  />
                  <Button variant="primary" type="submit" className="mt-3">
                    Download
                  </Button>
                </FormGroup>
              </Form>
              {this.state.errorMessage && (
                <Alert variant="danger" className="mt-3">
                  {this.state.errorMessage}
                </Alert>
              )}
            </Col>
          </Row>
        </Container>
        <Footer />
      </div>
    );
  }
}

export default App;
