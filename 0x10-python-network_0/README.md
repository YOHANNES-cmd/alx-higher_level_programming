# Python Network Part 0

This project contains some tasks for learning about network-related tasks in **cURL**.

## Tasks To Complete

+ [x] 0. cURL body size<br/>_**[0-body_size.sh](0-body_size.sh)**_ contains a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
  + The size must be displayed in bytes.
  + You have to use `curl`.

+ [x] 1. cURL to the end<br/>_**[1-body.sh](1-body.sh)**_ contains a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
  + Display only body of a `200` status code response.
  + You have to use `curl`.

+ [x] 2. cURL Method<br/>_**[2-delete.sh](2-delete.sh)**_ contains a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response.
  + You have to use `curl`.

+ [x] 3. cURL only methods<br/>_**[3-methods.sh](3-methods.sh)**_ contains a Bash script that takes in a URL and displays all HTTP methods the server will accept.
  + You have to use `curl`.

+ [x] 4. cURL headers<br/>_**[4-header.sh](4-header.sh)**_ contains a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response.
  + A header variable `X-School-User-Id` must be sent with the value `98`.
  + You have to use `curl`.

+ [x] 5. cURL POST parameters<br/>_**[5-post_params.sh](5-post_params.sh)**_ contains a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response.
  + A variable `email` must be sent with the value `test@gmail.com`.
  + A variable `subject` must be sent with the value `I will always be here for PLD`.
  + You have to use `curl`.

+ [x] 6. Find a peak<br/>_**[6-peak.py](6-peak.py)**_ contains a Python function that finds **a peak** in a list of unsorted integers.
  + Prototype: `def find_peak(list_of_integers):`.
  + You are not allowed to import any module.
  + Your algorithm must have the lowest complexity (*hint: you don’t need to go through all numbers to find a peak*).
  + [6-peak.py](6-peak.py) must contain the function.
  + [6-peak.txt](6-peak.txt) must contain the complexity of your algorithm: `O(log(n)), O(n), O(nlog(n)) or O(n2)`.
  + **Note:** there may be more than one peak in the list.

+ [x] 7. Only status code<br/>_**[100-status_code.sh](100-status_code.sh)**_ contains a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
  + You are not allowed to use any pipe, redirection, etc.
  + You are not allowed to use `;` and `&&`.
  + You have to use `curl`.

+ [x] 8. cURL a JSON file<br/>_**[101-post_json.sh](101-post_json.sh)**_ contains a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
  + Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.
  + You have to use `curl`.

+ [x] 9. Catch me if you can!<br/>_**[102-catch_me.sh](102-catch_me.sh)**_ contains a Bash script that that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
  + You have to use `curl`.
  + You are not allow to use `echo`, `cat`, etc. to display the final result.
