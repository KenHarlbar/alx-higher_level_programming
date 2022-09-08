#!/usr/bin/node

const number = process.argv[2];
if (!isNaN(number)) {
  for (let i = 0; i < number; i++) {
    let s = '';
    for (let j = 0; j < number; j++) {
      s += 'X';
    }
    console.log(s);
  }
} else {
  console.log('Missing size');
}
