#!/usr/bin/node
// This scfript will open a file and print the contents

const fs = require('fs');

const path = process.argv.slice(2);

if (path[0]) {
  fs.readFile(path[0], 'utf8', (err, fd) => {
    if (err) {
      if (err.code === 'ENOENT') {
        console.error(err);
        return;
      }
      throw err;
    }
    console.log(fd);
  });
}
