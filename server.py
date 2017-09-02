from flask import Flask, render_template, request
from typograph import typograph
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_text = request.form.get('text')
        original_text = input_text
        if not input_text:
            input_text = None
        return render_template(
            'form.html',
            text_after_typograph=typograph(input_text),
            text_before_typograph=original_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
