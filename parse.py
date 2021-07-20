import json

import chart


class Parser:
    raw_contents = ""
    raw_json = {}
    chart = chart.Chart()

    def __init__(self, path):
        with open(path, 'r') as file:
            self.raw_contents = file.read()
        self.parse_json()
        self.parse_metadata()
        self.parse_layers()

    def parse_json(self):
        self.raw_json = json.loads(self.raw_contents)

    def parse_metadata(self):
        self.chart.bpm = float(self.raw_json['editor_settings']['bpm'])

    def parse_layers(self):
        for layer in self.raw_json['layers']:
            for timing_point in layer['timing_points']:
                self.chart.notes.append(timing_point)
        self.chart.notes.sort(key=lambda note: note['time'])
        self.chart.init()
