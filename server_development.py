from flask import Flask
import os
from flask import render_template
app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__),"html"))


@app.route('/<page>')
def devserver(page):
    print("Page: ")
    print(page)

    if page == "":
        return render_template('sajt.html', temperatura=30, vazduh=30, pritisak=35)
    else:
        if page.endswith(".html"):
            return render_template(page, temperatura=30, vazduh=30, pritisak=35)
        else:
            return "404"


if __name__ == "__main__":
    app.run()
