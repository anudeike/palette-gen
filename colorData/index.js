// this file gets all the color information from the pictures that I chose
var ColorThief = require('colorthief');
var fs = require("fs");

// the color thief module only needs a path to the photos
const path = "sunset_example.png"

// get the colors
ColorThief.getPalette(path, 5).then(c => {
    console.log(c);
}).catch(e => {
    console.log(e);
})
