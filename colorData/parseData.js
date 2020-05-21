// this file gets all the color information from the pictures that I chose
var ColorThief = require('colorthief');
var chroma = require('chroma-js');
var fs = require("fs");
// const express = require('express');
// const app = express();
// const port = 5000;
// const cors = require('cors');
const path = require('path');

// get the path to the folder with all of the sunset photos
const dir = path.join(__dirname, "/photo_data/sunset")

// get paths
paths = fs.readdirSync(dir)

// compare function
function sortHSL(a, b){
    // this function goes into the sort function
    if(a[0] === b[0]){
        return 0;
    }else {
        return (a[0] < b[0]) ? -1 : 1;
    }
}

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
            // for each color in palette
            for(var i = 0; i < palette.length; i++){
                // turn into hsl
                transformedPaletteData.push(chroma(palette[i]).hsl())
            }
            
            // sort the transformed palette
            transformedPaletteData.sort(sortHSL)

            // change the id to the path of the picture
            var id = paths[j];

            palettesHex.push({id, transformedPaletteData});


        }).catch(e => {
            console.log(e);
        })
    }

    //console.log(palettesHex);
    console.log("end");
        
}

forLoop();