## Challenge:

A university's online registration portal asks students to upload their ID cards for verification. The developer put some filters in place to ensure only image files are uploaded but are they enough? Take a look at how the upload is implemented. Maybe there's a way to slip past the checks and interact with the server in ways you shouldn't.


## Solution:

- The challenge can be fully automated using a Python script, which handles the entire exploitation process from file upload to shell access.

- A standard file upload bypass (such as manipulating MIME types or file extensions) does **not** work in this challenge due to server-side validation.

- By identifying that the backend server is running **Apache**, an alternative attack vector can be used.

- The application allows uploading a `.htaccess` file, which can be leveraged to modify Apache configuration rules for the upload directory.

- The `.htaccess` file is used to:
  - Define a non-PHP file extension (e.g., `.jpg`, `.png`, or a custom extension) to be treated as PHP by the server.
  - Enable execution of PHP code in uploaded files.

- After successfully uploading the `.htaccess` file:
  - A PHP web shell is uploaded using the allowed file extension defined in the `.htaccess` configuration.

- Once the web shell is uploaded and accessed through the browser:
  - Arbitrary system commands can be executed on the server.
  - This results in full command execution and completion of the challenge.
