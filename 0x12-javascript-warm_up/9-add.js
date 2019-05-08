#!/usr/bin/node
// add 2 arguments
const input = process.argv.slice(2);
let nums = input.map(x => parseInt(x));

if (nums.length < 2) {
  console.log(NaN);
} else {
  let sum = nums[0] + nums[1];
  console.log(sum);
}
