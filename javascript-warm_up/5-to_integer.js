#!/usr/bin/python3
const [, , arg] = process.argv;
const parsedArg = parseInt(arg);
if (!isNaN(parsedArg)) {
  console.log(`My number: ${parsedArg}`);
} else {
  console.log("Not a number");
}
