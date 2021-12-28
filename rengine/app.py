from flask import Flask
from flask import render_template

app = Flask(__name__)

from business_rules import run_all
from varact import ProductVariables, ProductActions
from statistics import mean, mode
import json
from models import Alert

from kafka import KafkaConsumer

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/run')
def run():
    rules = []
    consumer = KafkaConsumer('producer_rule', bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        message = message.value
        rules.append(message['content'])

    detections = KafkaConsumer('producer', bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    c = []
    y = []
    h = []
    t = []
    v = []
    for detection in detections:
        detection = detection.value
        c.append(detection['color'])
        y.append(detection['year'])
        h.append(detection['humidity'])
        t.append(detection['temperature'])
        v.append(detection['vibration'])
    col = mode(c)
    yea = mode(y)
    hum = mean(h)
    tem = mean(t)
    vib = mean(v)
    metric = Alert(color=col, year=yea, humidity_mean=hum, temperature_mean=tem, vibration_mean=vib)
    run_all(rules, ProductVariables(metric), ProductActions(metric), False)
    return render_template('run.html', alerts=metric.alert)


if __name__ == '__main__':
    app.run()
