from flask import Flask, render_template, request
from rag_pipeline import create_rag_pipeline

app = Flask(__name__)

qa_chain = create_rag_pipeline()

@app.route("/", methods=["GET", "POST"])
def index():

    answer = ""

    if request.method == "POST":
        question = request.form["question"]

        result = qa_chain.invoke(question)

        answer = result["result"]

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)