PH_DIFF_NOTE = 100
PH_DIFF_DOUBLENOTE = 200
PH_DIFF_SUSTAINNOTE = 150
PH_DIFF_TIME_DIFF = 100

PH_DIFF_MAX_TIME_DIFF = 500

PH_MAX_DIFF = 80000


def calculate_difficulty(chart):
    total_difficulty = 0
    for i, note in enumerate(chart.notes):
        if i >= 1:
            time_this = chart.notes[i]['time']
            time_prev = chart.notes[i - 1]['time']
            time_diff = time_this - time_prev
            total_difficulty += PH_DIFF_TIME_DIFF * (1 - max(time_diff / PH_DIFF_MAX_TIME_DIFF, 1))

        if note['type'] == "Note":
            total_difficulty += PH_DIFF_NOTE
        elif note['type'] == "DoubleNote":
            total_difficulty += PH_DIFF_DOUBLENOTE
        elif note['type'] == "SustainNote":
            total_difficulty += PH_DIFF_SUSTAINNOTE
    return (total_difficulty / PH_MAX_DIFF) * 10

