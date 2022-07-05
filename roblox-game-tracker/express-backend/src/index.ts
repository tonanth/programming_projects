import { Client } from 'pg';


import express = require('express');
import cors = require('cors')

const app = express();
const port: number = 4321;



app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
  res.send('roblox-game-tracker')
})

app.put('/addurl', (req, res) => {
  console.log(req.body.url)
  res.end()
})

app.listen(port, () => {
  console.log(`example app listening on port ${port}`)
})