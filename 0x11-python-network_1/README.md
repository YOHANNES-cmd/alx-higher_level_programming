# Python Network Part 1

This project contains some tasks for learning more about network-related tasks in **Python**.

## Tasks To Complete

+ [x] 0. What's my status? #0<br/>_**[0-hbtn_header.py](0-hbtn_header.py)**_ contains a Python script that fetches `https://intranet.hbtn.io/status`.
  + You must use the package `urllib`.
  + You are not allowed to import any packages other than `urllib`.
  + The body of the response must be displayed like the following example (tabulation before `-`).
  ```powershell
  guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
  Body response:$
      - type: <class 'bytes'>$
      - content: b'OK'$
      - utf8 content: OK$
  guillaume@ubuntu:~/0x11$
  ```
  + You must use a `with` statement.

+ [x] 1. Response header value #0<br/>_**[1-hbtn_header.py](1-hbtn_header.py)**_ contains a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.
  + You must use the packages `urllib` and `sys`.
  + You are not allowed to import packages other than `urllib` and `sys`.
  + The value of this variable is different for each request.
  + You don't need to check arguments passed to the script (number or type).
  + You must use a `with` statement.

+ [x] 2. POST an email #0<br/>_**[2-post_email.py](2-post_email.py)**_ contains a Python scriptthat takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`).
  + The email must be sent in the `email` variable.
  + You must use the packages `urllib` and `sys`.
  + You are not allowed to import packages other than `urllib` and `sys`.
  + You don't need to check arguments passed to the script (number or type).
  + You must use the `with` statement.

+ [x] 3. Error code #0<br/>_**[3-error_code.py](3-error_code.py)**_ contains a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in `utf-8`).
  + You have to manage `urllib.error.HTTPError` exceptions and print: `Error code: ` followed by the HTTP status code.
  + You must use the packages `urllib` and `sys`.
  + You are not allowed to import other packages than `urllib` and `sys`.
  + You don't need to check arguments passed to the script (number or type).
  + You must use the `with` statement.

+ [x] 4. What's my status? #1<br/>_**[4-hbtn_status.py](4-hbtn_status.py)**_ contains a Python script that fetches `https://intranet.hbtn.io/status`.
  + You must use the package `requests`.
  + You are not allowed to import packages other than `requests`.
  + The body of the response must be display like the following example (tabulation before `-`).
  ```powershell
  guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
  Body response:$
      - type: <class 'str'>$
      - content: OK$
  guillaume@ubuntu:~/0x11$
  ```

+ [x] 5. Response header value #1<br/>_**[5-hbtn_header.py](5-hbtn_header.py)**_ contains a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.
  + You must use the packages `requests` and `sys`.
  + You are not allowed to import other packages than `requests` and `sys`.
  + The value of this variable is different for each request.
  + You don't need to check script arguments (number and type).

+ [x] 6. POST an email #1<br/>_**[6-post_email.py](6-post_email.py)**_ contains a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
  + The email must be sent in the variable `email`.
  + You must use the packages `requests` and `sys`.
  + You are not allowed to import packages other than `requests` and `sys`.
  + You don't need to error check arguments passed to the script (number or type).

+ [x] 7. Error code #1<br/>_**[7-error_code.py](7-error_code.py)**_ contains a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
  + If the HTTP status code is greater than or equal to 400, print: `Error code: ` followed by the value of the HTTP status code.
  + You must use the packages `requests` and `sys`.
  + You are not allowed to import packages other than `requests` and `sys`.
  + You don't need to check arguments passed to the script (number or type).

+ [x] 8. Search API<br/>_**[8-json_api.py](8-json_api.py)**_ contains a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
  + The letter must be sent in the variable `q`.
  + If no argument is given, set `q=""`.
  + If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`.
  + Otherwise:
    + Display `Not a valid JSON` if the JSON is invalid.
    + Display `No result` if the JSON is empty.
  + You must use the package `requests` and `sys`.
  + You are not allowed to import packages other than `requests` and `sys`.

+ [x] 9. My GitHub!<br/>_**[10-my_github.py](10-my_github.py)**_ contains a Python script that takes a user's GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/reference/users) to display the user's `id`.
  + You must use [Basic Authentication](https://docs.github.com/en/rest/overview/other-authentication-methods) with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to access to your information (only `read:user` permission is needed).
  + The first argument will be your `username`.
  + The second argument will be your `password` (in your case, a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)).
  + You must use the package `requests` and `sys`.
  + You are not allowed to import packages other than `requests` and `sys`.
  + You don't need to check arguments passed to the script (number or type).
  + If authenitcation fails, print `None`.

+ [x] 10. Time for an interview!<br/>_**[100-github_commits.py](100-github_commits.py)**_ contains a Python script that takes 2 arguments in order to solve this challenge.
  ```
  Please list 10 commits (from the most recent to oldest) of the repository "rails" by the user "rails"
  You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
  Print all commits by: `<sha>: <author name>` (one per line)
  ```
  + The first argument will be the `repository name`.
  + The second argument will be the `owner name`.
  + You must use the packages `requests` and `sys`.
  + You are not allowed to import packages other than `requests` and `sys`.
  + You don't need to check arguments passed to the script (number or type).
