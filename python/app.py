import argparse

from lib import load_data, validate_items, compute_summary, make_report


def main() -> int:
    parser = argparse.ArgumentParser(description='Generate a project report.')
    parser.add_argument('path', nargs='?', default='data/sample.json')
    args = parser.parse_args()

    payload = load_data(args.path)
    config = load_data('config.json')
    items = payload['items']
    rules = payload['rules']

    issues = validate_items(items, rules, config['categories'])
    summary = compute_summary(items, config['categories'])
    report = make_report(config, summary, issues)
    print(report)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
