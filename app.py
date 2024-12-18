from flask import Flask, render_template, request, jsonify
from game_logic import WordGame

app = Flask(__name__)
games = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    game_id = request.remote_addr  # Using IP as game ID for simplicity
    games[game_id] = WordGame()
    masked_word = games[game_id].start_new_game()
    return jsonify({
        "masked_word": masked_word,
        "message": "Game started! Try to guess the word."
    })

@app.route('/make_guess', methods=['POST'])
def make_guess():
    game_id = request.remote_addr
    if game_id not in games:
        return jsonify({"error": "No active game"}), 400
    
    guess = request.json.get('guess', '').strip()
    result = games[game_id].make_guess(guess)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
