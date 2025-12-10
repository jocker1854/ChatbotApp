from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    else:
        return "I'm not sure how to respond to that. Try asking something else."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
