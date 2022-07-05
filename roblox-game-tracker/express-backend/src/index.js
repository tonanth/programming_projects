"use strict";
exports.__esModule = true;
var express = require("express");
var cors = require("cors");
var app = express();
var port = 4321;
app.use(cors());
app.use(express.json());
app.get('/', function (req, res) {
    res.send('roblox-game-tracker');
});
app.put('/addurl', function (req, res) {
    console.log(req.body.url);
    res.end();
});
app.listen(port, function () {
    console.log("example app listening on port ".concat(port));
});
