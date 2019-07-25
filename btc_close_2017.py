# -*- coding: utf-8 -*-
# filename: btc_close_2017

import json
import pygal
import math

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, close = [], [], [], [], []

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotationi=20, show_minor_x_labels=False)
line_chart.title = 'close'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('Close_log', close_log)
line_chart.render_to_file('close_log.svg')
