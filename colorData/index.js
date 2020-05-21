// this file gets all the color information from the pictures that I chose
var ColorThief = require('colorthief');
var chroma = require('chroma-js');
var fs = require("fs");
const express = require('express');
const app = express();
const port = 5000;
const cors = require('cors');
const path = require('path');

// use cors
app.use(cors());

// create the server
app.get('/', (req, res) => {
    res.sendFile(process.cwd() + '/static/index.html')
});

// create another endpoint
app.get('/getPalette', (req, res) => {

    const dir = path.join(__dirname, "/photo_data/sunset")

    // get paths
    paths = fs.readdirSync(dir)

    // variable to hold all of the palettes
    var forLoop = async _ => {
        console.log("start: ")

        let palettesHex = []

        // for each path
        for(var j = 0; j < paths.length; j++)
        {
            // get each palette
            await ColorThief.getPalette(path.join(__dirname, "/photo_data/sunset/", paths[j]), 5).then((palette) => {

                var transformedPaletteData = []
        
                // create the chroma objects out of each of palettes
                for(var i = 0; i < palette.length; i++){
                    transformedPaletteData.push(chroma(palette[i]).hsl())
                }
    
                //console.log(transformedPaletteData);

                // get random string as id
                var id = Math.random().toString(36).substring(2, 15);

                palettesHex.push({id, transformedPaletteData});

            }).catch(e => {
                console.log(e);
            })
        }

        console.log(palettesHex);
        console.log("end");
        res.send(palettesHex);
        
    }

forLoop();


    
    

    //console.log(paletteData)


})

// essentially we create an endpoint here and then call it in vuejs
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))


