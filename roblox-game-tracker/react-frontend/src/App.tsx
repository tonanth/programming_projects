import React, {useState} from 'react';
import logo from './logo.svg';
import TopBar from './TopBar';
import './App.css';

fetch('http://localhost:4321/').then(response => console.log("response"))



function App() {

  const [updatedGames, setUpdatedGames] = useState([])

  function handleRefresh() {
    return null;
  }
  
  function handleAddNewURL(url : string) {
    handleRefresh()
    return null;
  }

  return (
    <div className="App">
      <TopBar handleAddNewURL={handleAddNewURL} handleRefresh={handleRefresh}/>

    </div>
  );
}

export default App;
