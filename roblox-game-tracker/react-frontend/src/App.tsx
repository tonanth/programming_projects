import React, {useState} from 'react';
import logo from './logo.svg';
import TopBar from './TopBar';
import './App.css';

// fetch('http://localhost:4321/').then(response => response.text()).then(data => console.log(data))



function serverIsActive(callback : Function) : void {
    fetch('http://localhost:4321/').then(response => response.text()).then(text =>{callback(text === 'roblox-game-tracker')}).catch((error) => callback(false));
}

function App() {


  const [updatedGames, setUpdatedGames] = useState<string[]>([])
  const [serverStatus, setServerStatus] = useState<boolean>(false)

  serverIsActive(setServerStatus);

  function handleRefresh() {
    return null;
  }
  
  function handleAddNewURL(url : string) {
    handleRefresh()
    return null;
  }
  
  return (
    <div className="App">
      <h1>{serverStatus.toString()}</h1>
      <TopBar handleAddNewURL={handleAddNewURL} handleRefresh={handleRefresh} />
    </div>
  );
}

export default App;
