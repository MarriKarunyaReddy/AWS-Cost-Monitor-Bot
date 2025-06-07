import os
from flask import Flask, render_template
from utils.cost_explorer import get_cost_data

app = Flask(__name__)

@app.route('/')
def index():
    cost_info = get_cost_data()
    return render_template(
        'dashboard.html',
        data=cost_info['data'],
        total_cost=cost_info['total_cost'],
        start_date=cost_info['start_date'],
        end_date=cost_info['end_date'],
        account_id=cost_info['account_id']
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Required by Render
    app.run(host='0.0.0.0', port=port)
