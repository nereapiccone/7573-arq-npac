from flask import Flask
import time

app = Flask(__name__)

@app.route("/time")
def root():
  time.sleep( 1 )
  return "Hola, mundo python!"

if __name__ == "__main__":
  app.run()
