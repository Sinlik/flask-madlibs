import logging
from flask import Flask, render_template, request, Response
from stories import Story

app = Flask(__name__, static_folder="static")

app.config['SECRET_KEY'] = 'secret'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET", "POST"])
def story ():
    placeholders = ['place', 'verb', 'noun', 'adjective', 'plural', 'about']
    if request.method == "POST":
        answers = {}
        for placeholder in placeholders:
            value = request.form.get(placeholder)
            if value:
                answers[placeholder] = value.split(', ')
        logger.debug(answers)
        story = Story(placeholders, f"Once upon a time in a long-ago {'place'}, there lived a large {'adjective'} {'noun'}. It loved to {'verb'} {'plural'}.")
        result = story.generate(answers)
        return result
    return render_template('form.html', script_file='formInfo.js', placeholders=placeholders)

if __name__ == '__main__':
    app.run()