from flask import Flask
import redis
import os
import time

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

while True:
    try:
        r = redis.Redis(
            host=redis_host,
            port=6379,
            decode_responses=True
        )
        r.ping()
        break
    except redis.exceptions.ConnectionError:
        print("Waiting for Redis...")
        time.sleep(2)


@app.route("/")
def home():
    visits = r.incr("visits")

    return f"""
    <html>
    <head>
        <title>Docker Compose Application</title>
    </head>
    <body>
        <h1>Docker Compose Multi-Container Application</h1>
        <p>Flask Web Application is running successfully!</p>
        <p>Redis is connected successfully!</p>
        <h2>Page Visits: {visits}</h2>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
