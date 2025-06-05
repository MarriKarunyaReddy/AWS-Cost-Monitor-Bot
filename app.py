import os
from flask import Flask, render_template
from utils.cost_explorer import get_cost_data

app = Flask(__name__)

@app.route('/')
def index():
    cost_data = get_cost_data()
    return render_template('dashboard.html', data=cost_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Required by Render
    app.run(host='0.0.0.0', port=port)