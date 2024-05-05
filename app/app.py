from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    category = ["ストロベリー", "チョコレート","プレーン"]
    return render_template("index.html", name=name, category=category)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)