echo Flask_App=%cd%\microblog.py>.flaskenv

call %cd%\myvenv\Scripts\activate
flask run
cmd \k