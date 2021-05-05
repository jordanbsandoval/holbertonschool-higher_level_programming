#!/usr/bin/node
'use strict';
// importando el modulo fs
let fs = require("fs");

// obteniendo el path del archivo
let dato = process.argv[2];


fs.readFile(dato, 'utf8', function (err, data)
{
    if (err) 
    {
        console.error(err);
        return;
    }
    console.log(data);
});
