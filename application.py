  
from flask import Flask
import jwt
app = Flask(__name__)

@app.route("/")
def home():
  encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
  return encoded_jwt
    
if __name__ == "__main__":
    app.run(debug=True)
