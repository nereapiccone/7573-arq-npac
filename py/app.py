from flask import Flask
import time

app = Flask(__name__)

@app.route("/quick")
def root():
  return "Hola, mundo python!"

@app.route("/slow")
def root_time():
  time.sleep( 1 )
  return "Hola, mundo python lento!"

@app.route("/delay")
def root_time():
  time.sleep( 1 )
  return "Esperamos 1 seg - delay!"



if __name__ == "__main__":
  app.run()
