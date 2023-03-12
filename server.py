from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def chekboard():
    return render_template('index.html', num_rows=8, num_cols=8)


@app.route('/<int:num>')
def sized_chekboard(num):
    return render_template('index.html', num_rows=int(num), num_cols=int(num))


@app.route('/<int:num1>/<int:num2>')
def sized_chekboard_two_dimensions(num1, num2):
    return render_template('index.html', num_rows=int(num1), num_cols=int(num2))


@app.route('/<int:num1>/<int:num2>/<c1>/<c2>')
def sized_chekboard_two_dimensions_and_color(num1, num2, c1, c2):
    return render_template('index.html', num_rows=int(num1), num_cols=int(num2), color_one=c1, color_two=c2)


@ app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Lo siento!, no hay respuesta. Intentalo otra vez."}), 404


if __name__ == "__main__":
    app.run(debug=True)
