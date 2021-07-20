import sys

import log
import parse
import difficulty


def parse_chart(path):
    parser = parse.Parser(path)
    chart = parser.chart
    stars = difficulty.calculate_difficulty(chart)
    print(f'Stars: {stars}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        log.err('Bad argument count')
        sys.exit(1)

    chart_path = sys.argv[1]
    parse_chart(chart_path)
