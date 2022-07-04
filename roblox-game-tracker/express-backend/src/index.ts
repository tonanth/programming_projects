import express = require('express');
import cors = require('cors')

const app = express();
const port: number = 4321;

app.use(cors())

app.get('/', (req, res) => {
  res.send('roblox-game-tracker')
})

app.get('/status', (req, res) => {
})

app.listen(port, () => {
  console.log(`example app listening on port ${port}`)
})