  
from flask import Flask
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
app = Flask(__name__)

@app.route("/")
def home():
  instance = JWT()
  return "Hello, new.. "
    
if __name__ == "__main__":
    app.run(debug=True)
