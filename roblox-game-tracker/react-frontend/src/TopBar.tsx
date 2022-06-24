import { useState } from "react";

interface Props {
  handleAddNewURL (data : string): null;
}

function TopBar(props : Props) {

  const [url, set_url] = useState('')

  return(
    <div className="TopBar">
      <h1>Roblox Game Tracker</h1>
      <form onSubmit={() => props.handleAddNewURL(url)}>
          <input className="game-entry-box" type="text" placeholder="ROBLOX Game URL" onChange={(text) => {set_url(text.target.value);}} />
      </form>
    </div>
  )
}

export default TopBar;