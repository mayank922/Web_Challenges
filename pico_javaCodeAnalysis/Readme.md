## Challenge

BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!

## Initial Analysis

Upon exploring the application, I discovered that:

- The 'Flag' book is restricted to admin users only
- The application uses JWT (JSON Web Tokens) for authentication
- Reading the Flag book requires privilege escalation from a regular user to admin

## Solution

### What I tried first

I tested the usual JWT tricks:
- Removing the signature 
- Changing algorithm to `none` 
- Algorithm confusion attacks 

Everything was properly validated by the backend.

### The actual solution

- Looking at the source code, I found the vulnerability in the `SecretGenerator` class which had the secret key harcoded
- Since I can see algo HS256 is used and I knew the secret key, I could sign my own tokens using the Burp JWT editor extenstion.
- Modified the JWT payload to change the role and userID to admin, signed it with new signature 
- Sent the modified request and got the flag!

## Refernces

- https://portswigger.net/burp/documentation/desktop/testing-workflow/vulnerabilities/session-management/jwts
- https://portswigger.net/web-security/jwt