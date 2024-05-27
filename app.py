from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    question1 = request.form['question1']
    question2 = request.form['question2']
    question3 = request.form['question3']
    question4 = request.form['question4']

    # Сохраняем результаты опроса в файл
    with open('survey_results.txt', 'a', encoding='utf-8') as file:
        file.write(f"Name: {name}, Age: {age}\n")
        file.write(f"Question 1: {question1}\n")
        file.write(f"Question 2: {question2}\n")
        file.write(f"Question 3: {question3}\n")
        file.write(f"Question 4: {question4}\n\n")

    return 'Спасибо за участие в опросе!'

if __name__ == '__main__':
    app.run(debug=True)