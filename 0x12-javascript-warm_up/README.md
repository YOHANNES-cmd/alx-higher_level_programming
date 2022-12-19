# JavaScript Warm Up

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

This project contains some tasks for learning the basics of **JavaScript**.

## Tasks To Complete

+ [x] 0. First constant, first print<br/>_**[0-javascript_is_amazing.js](0-javascript_is_amazing.js)**_ contains a script that prints "JavaScript is amazing":
  + You must create a constant variable called `myVar` with the value "JavaScript is amazing".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 1. 3 languages<br/>_**[1-multi_languages.js](1-multi_languages.js)**_ contains a script that prints 3 lines:
  + The first line: "C is fun".
  + The second line: "Python is cool".
  + The third line: "JavaScript is amazing".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 2. Arguments<br/>_**[2-arguments.js](2-arguments.js)**_ contains a script that prints a message depending on the number of arguments passed:
  + If no arguments are passed to the script, print "No argument".
  + If only one argument is passed to the script, print "Argument found".
  + Otherwise, print "Arguments found".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 3. Value of my argument<br/>_**[3-value_argument.js](3-value_argument.js)**_ contains a script that prints the first argument passed to it:
  + If no arguments are passed to the script, print "No argument".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.
  + You are not allowed to use `length`.

+ [x] 4. Create a sentence<br/>_**[4-concat.js](4-concat.js)**_ contains a script that prints the two arguments passed to it in the following format: `<first argument> is <second argument>`
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 5. An Integer<br/>_**[5-to_integer.js](5-to_integer.js)**_ contains a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer.
  + If the argument can’t be converted to an integer, print "Not a number".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.
  + You are not allowed to use `try/catch`.

+ [x] 6. Loop to languages<br/>_**[6-multi_languages_loop.js](6-multi_languages_loop.js)**_ contains a script that prints 3 lines: (like [1-multi_languages.js](1-multi_languages.js)) but by using an array of strings and a loop.
  + The first line: "C is fun".
  + The second line: "Python is cool".
  + The third line: "JavaScript is amazing".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.
  + You are not allowed to use any `if/else` statement.
  + You can use only one `console.log`.
  + You must use a loop (`while`, `for`, etc.).

+ [x] 7. I love C<br/>_**[7-multi_c.js](7-multi_c.js)**_ contains a script that prints "C is fun" `x` times.
  + Where`x` is the first argument of the script.
  + If the first argument can’t be converted to an integer, print "Missing number of occurrences".
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.
  + You can use only two `console.log`.
  + You must use a loop (`while`, `for`, etc.).

+ [x] 8. Square<br/>_**[8-square.js](8-square.js)**_ contains a script that prints a square.
  + The first argument is the size of the square.
  + If the first argument can’t be converted to an integer, print "Missing size".
  + You must use the character `X` to print the square.
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.
  + You must use a loop (`while`, `for`, etc.).

+ [x] 9. Add<br/>_**[9-add.js](9-add.js)**_ contains a script that prints the addition of 2 integers.
  + The first argument is the first integer.
  + The second argument is the second integer.
  + You have to define a function with this prototype: `function add(a, b)`.
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 10. Factorial<br/>_**[10-factorial.js](10-factorial.js)**_ contains a script that computes and prints a factorial.
  + The first argument is integer (argument can be cast as integer) used for computing the factorial
  + Factorial of `NaN` is `1`.
  + You must do it recursively.
  + You must use a function.
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 11. Second biggest!<br/>_**[11-second_biggest.js](11-second_biggest.js)**_ contains a scrpt that searches the second biggest integer in the list of arguments.
  + You can assume all arguments can be converted to integer.
  + If no argument passed, print `0`.
  + If the number of arguments is 1, print `0`.
  + You must use `console.log(...)` to print all output.
  + You are not allowed to use `var`.

+ [x] 12. Object<br/>_**[12-object.js](12-object.js)**_ updates a script to replace the value `12` with `89`:
  + You are not allowed to use `var`.
  + The script to update:
  ```js
  #!/usr/bin/node
  const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
  /*
  YOUR CODE HERE
  */
  console.log(myObject);
  ```

+ [x] 13. Add file<br/>_**[13-add.js](13-add.js)**_ contains a function that returns the addition of 2 integers.
  + The function must be visible from outside.
  + The name of the function must be `add`.
  + You are not allowed to use `var`.

+ [x] 14. Const or not const<br/>_**[100-let_me_const.js](100-let_me_const.js)**_ contains a file that modifies the value of `myVar` to `333`.

+ [x] 15. Call me Moby<br/>_**[101-call_me_moby.js](101-call_me_moby.js)**_ contains a function that executes a function `x` times.
  + The function must be visible from outside.
  + Prototype: `function (x, theFunction)`.
  + You are not allowed to use `var`.

+ [x] 16. Add me maybe<br/>_**[102-add_me_maybe.js](102-add_me_maybe.js)**_ contains a function that increments a number and calls a function with the number as its argument.
  + The function must be visible from outside.
  + Prototype: `function (number, theFunction)`.
  + You are not allowed to use `var`.

+ [x] 17. Increment object<br/>_**[103-object_fct.js](103-object_fct.js)**_ updates a script by adding a new function `incr` that increments the integer `value`.
  + You are not allowed to use `var`.
  + The script to update:
  ```js
  #!/usr/bin/node
  const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
  /*
  YOUR CODE HERE
  */
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  ```
