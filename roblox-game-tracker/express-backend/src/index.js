"use strict";
exports.__esModule = true;
var express = require("express");
var cors = require("cors");
var app = express();
var port = 4321;
app.use(cors());
app.get('/', function (req, res) {
    res.send('roblox-game-tracker');
});
app.listen(port, function () {
    console.log("example app listening on port ".concat(port));
});
