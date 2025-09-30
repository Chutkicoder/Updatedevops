#Inside monitoring-demo/app.py:
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, path="/metrics")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from monitored app!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



#docker compose up -d --build
"""
Python app → http://localhost:5000/hello
 Metrics → http://localhost:5000/metrics
 Prometheus UI → http://localhost:9090
 Grafana → http://localhost:3000 (login: admin/admin)
1. Go to Grafana → Add Prometheus as data source (http://prometheus:9090).
(in add connections in left heirarchy)
2. Create a new dashboard.
3. Add panels for:
o API request rate
4. sum(rate(flask_http_request_total[5m]))
o API latency (p95)
5. histogram_quantile(0.95,
sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))
o CPU usage (process)
6. rate(process_cpu_seconds_total[1m])
o Memory (RSS MB)
7. process_resident_memory_bytes / 1024 / 1024
"""