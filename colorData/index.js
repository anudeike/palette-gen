// this file gets all the color information from the pictures that I chose
var ColorThief = require('colorthief');
var chroma = require('chroma-js');
var fs = require("fs");
const express = require('express');
const app = express();
const port = 5000;
const cors = require('cors');

// use cors
app.use(cors());

// create the server
app.get('/', (req, res) => {
    res.sendFile(process.cwd() + '/static/index.html')
});

// create another endpoint
app.get('/getPalette', (req, res) => {
    path = process.cwd() + '/photo_data/sunset/sunset1.jfif'

    ColorThief.getPalette(path, 5).then(c => {
    
        var chromas = []
    
        // create the chroma objects out of each of them
        for(var i = 0; i < c.length; i++){
            chromas.push(chroma(c[i]).hex())
        }

        console.log(chromas);
        res.send(chromas);
    }).catch(e => {
        console.log(e);
    })
})

// essentially we create an endpoint here and then call it in vuejs
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))


