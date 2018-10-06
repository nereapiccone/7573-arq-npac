from flask import Flask
import time

app = Flask(__name__)

def fibR(n):
  if n==1 or n==2:
    return 1
  return fibR(n-1)+fibR(n-2)

 
@app.route("/")
def root():
    return "rapido como la luz\n"


@app.route("/slow")
def slow():
    return "Fibonacci de 30: " + str(fibR(30)) + "\n"


@app.route("/delay")
def delay():
    time.sleep(1)
    return "python durmio 1 seg\n"
  

if __name__ == "__main__":
    app.run()
