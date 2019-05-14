#!/usr/bin/node
// This scfript will open a file and print the contents

const fs = require('fs');

const path = process.argv.slice(2);

if (path[0]) {
  fs.writeFile(path[0], path[1], (err) => {
    if (err) {
      if (err.code === 'ENOENT') {
        console.error(err);
        return;
      }
      throw err;
    }
  });
}
