from flask import Flask, render_template, request, jsonify
import re, random

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/process", methods=['POST'])
def process():
    if request.method == 'POST':
        testQuestions = request.form['test_questions']

        # split list by question #
        splitQuestions = re.split(r'[0-9]{1,}[.]', testQuestions)

        # remove any leading text in test document
        splitQuestions.pop(0)

        # shuffle questions
        random.shuffle(splitQuestions)

        questionNumber = 1
        shuffledQuestions = ""

        for question in splitQuestions:
            shuffledQuestions += '{}.{}'.format(questionNumber, question)
            questionNumber += 1

        return jsonify({'questions': shuffledQuestions})

    return jsonify({'error': 'Please enter some test questions in the left text-field.'})


if __name__ == "__main__":
    app.run(debug=True)
