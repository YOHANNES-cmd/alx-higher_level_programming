# JavaScript Objects, Scopes and Closures

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

This project contains some tasks for learning about objects, scopes, and closures in **JavaScript**.

## Tasks To Complete

+ [x] 0. Rectangle #0<br/>_**[0-rectangle.js](0-rectangle.js)**_ contains an empty class `Rectangle` that defines a rectangle:
  + You must use the `class` notation for defining your class.

+ [x] 1. Rectangle #1<br/>_**[1-rectangle.js](1-rectangle.js)**_ contains a class `Rectangle` that defines a rectangle:
  + You must use the `class` notation for defining your class.
  + The constructor must take 2 arguments `w` and `h`.
  + Initialize the instance attribute `width` with the value of `w`.
  + Initialize the instance attribute `height` with the value of `h`.

+ [x] 2. Rectangle #2<br/>_**[2-rectangle.js](2-rectangle.js)**_ contains a class `Rectangle` that defines a rectangle:
  + You must use the `class` notation for defining your class.
  + The constructor must take 2 arguments `w` and `h`.
  + Initialize the instance attribute `width` with the value of `w`.
  + Initialize the instance attribute `height` with the value of `h`.
  + If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

+ [x] 3. Rectangle #3<br/>_**[3-rectangle.js](3-rectangle.js)**_ contains a class `Rectangle` that defines a rectangle:
  + You must use the `class` notation for defining your class.
  + The constructor must take 2 arguments: `w` and `h`.
  + Initialize the instance attribute `width` with the value of `w`.
  + Initialize the instance attribute `height` with the value of `h`.
  + If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
+ Create an instance method called `print()` that prints the rectangle using the character `X`.

+ [x] 4. Rectangle #4<br/>_**[4-rectangle.js](4-rectangle.js)**_ contains a class `Rectangle` that defines a rectangle:
  + You must use the `class` notation for defining your class.
  + The constructor must take 2 arguments: `w` and `h`.
  + Initialize the instance attribute `width` with the value of `w`.
  + Initialize the instance attribute `height` with the value of `h`.
  + If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
  + Create an instance method called `print()` that prints the rectangle using the character `X`.
  + Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle.
  + Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2.

+ [x] 5. Square #0<br/>_**[5-square.js](5-square.js)**_ contains a class `Square` that defines a square and inherits from `Rectangle` of [4-rectangle.js](4-rectangle.js):
  + You must use the `class` notation for defining your class and `extends`.
  + The constructor must take 1 argument: `size`.
  + The constructor of `Rectangle` must be called (by using `super()`).

+ [x] 6. Square #1<br/>_**[6-square.js](6-square.js)**_ contains a class `Square` that defines a square and inherits from `Square` of [5-square.js](5-square.js):
  + You must use the `class` notation for defining your class and `extends`.
  + Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`.
  + If `c` is `undefined`, use the character `X`.

+ [x] 7. Occurrences<br/>_**[7-occurrences.js](7-occurrences.js)**_ contains a function that returns the number of occurrences of an element in a list:
  + Prototype: `exports.nbOccurences = function (list, searchElement)`.

+ [x] 8. Esrever<br/>_**[8-esrever.js](8-esrever.js)**_ contains a function that returns the reversed version of a list:
  + Prototype: `exports.esrever = function (list)`.
  + You are not allowed to use the built-in method `reverse`.

+ [x] 9. Log me<br/>_**[9-logme.js](9-logme.js)**_ contains a function that prints the number of arguments already printed and the new argument value.
  + Prototype: `exports.logMe = function (item)`.
  + Output format: `<number arguments already printed>: <current argument value>`.

+ [x] 10. Number conversion<br/>_**[10-converter.js](10-converter.js)**_ contains a function that converts a number from base 10 to another base passed as an argument:
  + Prototype: `exports.converter = function (base)`.
  + You are not allowed to import any file.
  + You are not allowed to declare any new variable (`var`, `let`, etc..).

+ [x] 11. Factor index<br/>_**[100-map.js](100-map.js)**_ contains a script that imports an array and computes a new array.
  + Your script must import `list` from the file [100-data.js](100-data.js).
  + You must use a `map`.
  + A new list must be created with each value equal to the value of the initial list, multipled by the index in the list.
  + Print both the initial list and the new list.

+ [x] 12. Sorted occurences<br/>_**[101-sorted.js](101-sorted.js)**_ contains a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
  + Your script must import `dict` from the file [101-data.js](101-data.js).
  + In the new dictionary:
    + A key is the number of occurrences.
    + A value is the list of user ids.
  + Print the new dictionary at the end.

+ [x] 13. Concat files<br/>_**[102-concat.js](102-concat.js)**_ contains a script that concats 2 files.
  + The first argument is the file path of the first source file.
  + The second argument is the file path of the second source file.
  + The third argument is the file path of the destination.
