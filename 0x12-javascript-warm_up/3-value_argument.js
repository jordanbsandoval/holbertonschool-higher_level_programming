#!/usr/bin/node
const descriptor = process.argv[2];
if (descriptor !== undefined)
{
    console.log(descriptor);
}else
{
    console.log("No argument");
}
