from flask import Flask
import os
from flask import render_template
app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__),"html"))


@app.route('/<page>')
def devserver(page):
    print("Page: ")
    print(page)
    entries = [{temperatura_1:50, temperatura_2:49, pritisak:500, vlaznost:48},
               {temperatura_1: 47, temperatura_2: 46, pritisak: 501, vlaznost: 45},
               {temperatura_1: 44, temperatura_2: 43, pritisak: 502, vlaznost: 42},
               {temperatura_1: 41, temperatura_2: 40, pritisak: 503, vlaznost: 39}]

    if page == "":
        return render_template('sajt.html', temperatura=30, vazduh=30, pritisak=35, entries=entries)
    else:
        if page.endswith(".html"):
            return render_template(page, temperatura=30, vazduh=30, pritisak=35, entries=entries)
        else:
            return "404"


if __name__ == "__main__":
    app.run()
