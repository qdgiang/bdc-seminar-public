import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [message, setMessage] = useState(null);
  const [textEncoded, setTextEncoded] = useState(null);

  const handleInput = (event) => {
    setTextEncoded(event.target.value);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await fetch(`/api/base64decoder/${textEncoded}`);
      let resJson = await res.json();
      if (res.status === 200) {
        console.log(res, resJson);
        setMessage(resJson.message);
      } else {
        setMessage("Message can not encode");
      }
    } catch (err) {
      console.log(err);
    }
  }

  // TODO: Input is text -> decoded to base65 format
  // TODO: upload image -> returned image dectected
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <h4>
          Welcome to Seminar 5
        </h4>
        Input your text that you want to decode...
        <input onChange={handleInput}/>
        <p>The secret message is: {message}</p>
        <button onClick={handleSubmit}>Decode</button>
      </header>
    </div>
  );
}

export default App;
