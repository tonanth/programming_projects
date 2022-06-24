"use strict";
exports.__esModule = true;
var express = require("express");
var app = express();
var port = 4321;
app.get('/', function (req, res) {
    res.send('Hello, World!');
});
app.listen(port, function () {
    console.log("example app listening on port ".concat(port));
});
