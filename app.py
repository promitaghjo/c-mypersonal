from flask import Flask, render_template_string
import csv
import os

app = Flask(__name__)

LOG_FILE = "logs/cheating_log.csv"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Exam Proctoring Dashboard</title>
    <style>
        body { font-family: Arial; background: #0f172a; color: white; text-align: center; }
        .card { background: #1e293b; padding: 20px; margin: 20px; border-radius: 10px; }
        img { width: 300px; border-radius: 10px; margin-top: 10px; }
        table { width: 90%; margin: auto; border-collapse: collapse; }
        th, td { padding: 10px; border-bottom: 1px solid #334155; }
        th { color: #38bdf8; }
    </style>
</head>
<body>
    <h1>📊 Smart Exam Cheating Detection Dashboard</h1>

    <div class="card">
        <h2>Recent Cheating Events</h2>
        <table>
            <tr>
                <th>Time</th>
                <th>Event</th>
                <th>Score</th>
                <th>Evidence</th>
            </tr>
            {% for row in logs %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}%</td>
                <td>
                    {% if row[3] %}
                        <img src="{{ row[3] }}">
                    {% else %}
                        N/A
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </table>
    </div>

    <p>🔄 Refresh page to update</p>
</body>
</html>
"""

@app.route("/")
def dashboard():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            logs = list(reader)[-5:]  # show last 5 events
    return render_template_string(HTML, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
