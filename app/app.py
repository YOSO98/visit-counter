from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def index():
    count = r.incr("visits")
    return render_template("index.html", count=count)

@app.route("/reset")
def reset():
    r.set("visits", 0)
    return render_template("index.html", count=0, reset=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
