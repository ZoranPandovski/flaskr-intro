# Flaskr

Flaskr is a mini blog application that you are building following the official [Flask tutorial](http://flask.pocoo.org/docs/0.12/tutorial/introduction/). The app essentially, will do the following things:

* Let the user sign in and out with credentials specified in the configuration. Only one user is supported.
* When the user is logged in, they can add new entries to the page consisting of a text-only title and some HTML for the text.   This HTML is not sanitized because we trust the user here.
* The index page shows all entries so far in reverse chronological order (newest on top) and the user can add new ones from       there if logged in.

There is another great tutorial for flask and tdd at https://realpython.com/

## How to configure Python Flask in window?

Flask is the web development light weighted framework.  In order to do this it needs to do some configuration to your machine that is I am going to tell you in this post.

First of all you need to download Python 2.7 from its official website. And install it to your system.


Now you will get the folder named Python 27 in your C drive. Now open it and copy the path and go to your desktop and right click on My computer icon and click on properties.

After that a small window appears and in right bottom you get a button named Environment Variable, click on it.

Now you will get two boxes of System and User respectively. Under the System box click on path variable and Paste then path that you copied it in bigining.

Now open your CMD and go to your Python 27 and Scripts directly by CMD. and follow the steps
``` 
   C:\>cd Python27
   C:\>cd Scripts
   C:\>cd Python27>Scripts
   
   ```
   
 When you are inside it just type the command : pip install flask

And hit enter , it may take 2 or 3 mins depending upon your INTERNET speed.

Now make your project folder in any directory in your system. In my case let say I have created it in E drive and inside it create another folder named app and again inside it make two folder named templates and static respectively.

Now open any text editor any type then simple hello world ! Application code.
```Python

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
   ```
Now open again CMD and run the code like this it in same directory as I told above

```

E>: CD flask

E:>flask > CD app

E:flask>app python  __init__.py

Http://127.0.0.1:5000/ is running on…
```
Something like this will be shown if everything done file till now. Now open browser and type the same URL and see the result.

Since Python is case sensitive language so make sure you have typed the same code as  above.

If you face any problem regarding configuration or running the code  then you can watch this video.
https://youtu.be/hnyy5HmjqU8
Happy coding !!!!! :)

