A minimal project showcasing password based authentication in Python. Utilizes flask-login session management, and werkzeug password hashing. Day 68 course in [100 days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code).

![Screenshot of login page](/static/images/login.png)

Default werkzeug hashing algorithm at this time of writing (2026) is scrypt - see screenshot below, which also includes 8 salt characters.

![Screenshot of password hashes in a database](/static/images/db.png)