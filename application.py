  
from flask import Flask
import jwt
app = Flask(__name__)

@app.route("/")
def home():
  instance = JWT()
  return "Hello, new.. "
    
if __name__ == "__main__":
    app.run(debug=True)
