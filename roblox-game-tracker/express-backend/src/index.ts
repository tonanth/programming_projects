import express = require('express');

const app = express();
const port = 4321;

app.get('/', (req, res) => {
  res.send('Hello, World!')
})

app.listen(port, () => {
  console.log(`example app listening on port ${port}`)
})