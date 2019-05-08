#!/usr/bin/node
// Script print 3 kind messages about 3 programing languages using a loop
const lang = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let i = 0;
while (i < lang.length) {
  console.log(lang[i++]);
}
