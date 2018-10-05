from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def root():
    return "rapido como la luz\n"

@app.route("/delay")
def delay():
    time.sleep(1)
    return "python durmio 1 seg\n"

@app.route("/slow")
def root_time():
    time.sleep( 1 )
    return "calculines\n"

if __name__ == "__main__":
    app.run()
