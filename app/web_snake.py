from flask import Flask, render_template, jsonify, request
import random


app = Flask(__name__, template_folder="templates", static_folder="static")

# --- Game constants ---
WIDTH, HEIGHT = 30, 20
snake = [(5, 5)]
direction = (1, 0)
food = (10, 5)
score = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/state")
def get_state():
    return jsonify({"snake": snake, "food": food, "score": score})


@app.route("/move", methods=["POST"])
def move_snake():
    global snake, direction, food, score

    data = request.get_json()
    new_dir = data.get("dir")
    if new_dir and isinstance(new_dir, list) and len(new_dir) == 2:
        direction = tuple(new_dir)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    head = (head[0] % WIDTH, head[1] % HEIGHT)
    snake.insert(0, head)

    # Eat food
    if head == food:
        score += 1
        food = random_food()
    else:
        snake.pop()

    # Collision with self resets
    if head in snake[1:]:
        snake[:] = [(5, 5)]
        direction = (1, 0)
        score = 0

    return jsonify({"snake": snake, "food": food, "score": score})


def random_food():
    while True:
        pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if pos not in snake:
            return pos


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
