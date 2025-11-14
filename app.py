from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

from MEDIBOT.retrieval_generation import generation, chat_with_bot
from MEDIBOT.ingest import ingestdata

app = Flask(__name__)

load_dotenv()


vstore = ingestdata("done")

# Build RAG + Memory chain
chain = generation(vstore)

@app.route("/")
def index():
    return render_template("chat.html")   # front-end template

@app.route("/get", methods=["POST"])
def chat():
    user_query = request.form["msg"]

    # Use your memory-enabled chat function
    bot_response = chat_with_bot(chain, user_query)

    print("User:", user_query)
    print("Bot:", bot_response)

    return str(bot_response)

if __name__ == "__main__":
   app.run(
    host="0.0.0.0",
    port=5000,
    debug=False,
    use_reloader=False)


