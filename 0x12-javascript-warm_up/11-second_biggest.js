#!/usr/bin/node

const arr = [];
const argvLen = process.argv.length;

if (argvLen === 2 || argvLen === 3) {
  console.log(0);
  return;
} else {
  for (let i = 2; i < argvLen; i++) {
    arr[i - 2] = process.argv[i];
  }
}
const newArr = arr.sort();
const len = newArr.length;
console.log(newArr[len - 2]);
