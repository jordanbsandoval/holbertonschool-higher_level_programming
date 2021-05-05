#!/usr/bin/node
// importando el modulo request
const request = require('request');

// url a get
const url = process.argv[2];

// request
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  else if(response.statusCode === 200) {
    const info = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < info.results.length; ++i) {
      const allInfo = info.results[i].characters;
      for (let p = 0; p < allInfo.length; ++p) {
        const spt = allInfo[p].split('e/');
        if (spt[1] === '18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
