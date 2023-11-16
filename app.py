from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, i am vaibhav Current time is: {current_time}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
