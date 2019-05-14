from flask import Flask
import os
from flask import render_template
app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__),"html"))
@app.route('/')
def devserver():
    return render_template('sajt.html', temperatura=30, vazduh=30, pritisak=35)
	
if __name__ == "__main__":
	app.run()