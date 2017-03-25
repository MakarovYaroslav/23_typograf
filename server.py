from flask import Flask, render_template, request
from typograph import typograph
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_text = request.form.getlist('text')[0]
        return render_template(
            'form.html',
            text_after_typograph=typograph(input_text),
            original_text=input_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
