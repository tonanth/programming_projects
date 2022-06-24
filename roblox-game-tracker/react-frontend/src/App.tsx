import React from 'react';
import logo from './logo.svg';
import TopBar from './TopBar';
import './App.css';

fetch('http://localhost:4321/').then(response => console.log(response))

function App() {

  return (
    <div className="App">
      <TopBar handleAddNewURL={() => null}/>

    </div>
  );
}

export default App;
