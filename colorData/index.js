// this file gets all the color information from the pictures that I chose
var ColorThief = require('colorthief');
var chroma = require('chroma-js');
var fs = require("fs");
const express = require('express');
const app = express();
const port = 5000;

// create the server
app.get('/', (req, res) => {
    res.send('Hello World')
});

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))


// // the color thief module only needs a path to the photos
// const path = "sunset_example.png"


// // get the colors
// ColorThief.getPalette(path, 5).then(c => {
    
//     // returns the colors palettes
//     console.log(c);

//     var chromas = []

//     // create the chroma objects out of each of them
//     for(var i = 0; i < c.length; i++){
//         chromas.push(chroma(c[i]))
//     }

//     console.log(chromas);
// }).catch(e => {
//     console.log(e);
// })
