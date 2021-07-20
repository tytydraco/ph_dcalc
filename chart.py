class Chart:
    bpm = 0.0
    notes = []
    start_time = 0
    end_time = 0
    duration = 0

    def init(self):
        note_times = [note['time'] for note in self.notes]
        self.start_time = min(note_times)
        self.end_time = max(note_times)
        self.duration = self.end_time - self.start_time
