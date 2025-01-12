from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

def determine_winner(user, computer):
    if user == computer:
        return 'It\'s a tie!'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)