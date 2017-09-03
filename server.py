from flask import Flask, render_template, request
from typograph import typograph
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_text = request.form.get('text')
        if not input_text:
            output_text = "Введена пустая строка"
        else:
            output_text = typograph(input_text)
        return render_template(
            'form.html',
            text_after_typograph=output_text,
            text_before_typograph=input_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
