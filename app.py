from flask import Flask, request, render_template

app = Flask(__name__)

# Simple rule-based chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn’t understand that."

@app.route("/", methods=["GET", "POST"])
def home():
    bot_reply = ""
    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = chatbot_response(user_message)
    return render_template("index.html", reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
