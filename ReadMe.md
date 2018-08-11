How To Run hi.py
==================

Setup Environment variables:<br>
set FLASK\_APP=hi.py  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             # filename affected here.<br>
set FLASK\_ENV=development<br>

Depending on how you run Python on the Command Line, one option is to use the Anaconda Navigator


Method 1:
---------
cd <directory containing hi.py> <br>
Method 1: -m = run library module as a script

    `python.exe -m flask run`

Method 2:
----------
    cd <directory containing hi.py> <br>
    flask.exe run

 * Serving Flask app "hi.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 253-619-803
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [24/Jun/2018 14:41:13] "GET / HTTP/1.1" 200 -

Method 3:
----------
Run the python file directly. This initiates the program as a server:

`python.exe  hi.py`
    
Then open web page as usual: http://127.0.0.1:5000/