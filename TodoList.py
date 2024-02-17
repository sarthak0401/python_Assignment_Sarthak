from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder="Template")

todo_list = [{"task":"Sample todo", "done":False}]

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add",methods=["POST"])
def Add():
    todo = request.form['todo']
    todo_list.append({"task":todo, "done":False})
    return redirect(url_for("index"))


@app.route("/check/<int:index>")
def check(index):
    todo_list[index]['done'] = not todo_list[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todo_list[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)