import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Summary:
    total_amount: int
    avg_score: float
    top_item: str
    category_totals: Dict[str, int]


def load_data(path: str) -> Dict:
    with open(path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def validate_items(items: List[Dict], rules: Dict, categories: List[str]) -> List[str]:
    issues = []
    allowed_statuses = set(rules.get('allowed_statuses', []))
    for item in items:
        if item['amount'] < rules['min_amount'] or item['amount'] > rules['max_amount']:
            issues.append(f"amount_out_of_range:{item['id']}")
        if item['score'] < 0 or item['score'] > 100:
            issues.append(f"score_out_of_range:{item['id']}")
        if item['category'] not in categories:
            issues.append(f"unknown_category:{item['id']}")
        if item['status'] not in allowed_statuses:
            issues.append(f"unknown_status:{item['id']}")
    return issues


def compute_summary(items: List[Dict], categories: List[str]) -> Summary:
    total_amount = sum(i['amount'] for i in items)
    avg_score = round(sum(i['score'] for i in items) / len(items), 2)
    top_item = max(items, key=lambda i: i['score'])['id']
    category_totals = {cat: 0 for cat in categories}
    for item in items:
        if item['category'] in category_totals:
            category_totals[item['category']] += item['amount']
    return Summary(
        total_amount=total_amount,
        avg_score=avg_score,
        top_item=top_item,
        category_totals=category_totals,
    )


def make_report(config: Dict, summary: Summary, issues: List[str]) -> str:
    lines = []
    lines.append(config['project_title'])
    lines.append(f"Goal: {config['goal']}")
    lines.append("Metrics")
    lines.append(f"- Total {config['amount_label']}: {summary.total_amount}")
    lines.append(f"- Avg {config['score_label']}: {summary.avg_score}")
    lines.append(f"- Top {config['entity_name']}: {summary.top_item}")
    lines.append("Category totals")
    for key, value in summary.category_totals.items():
        lines.append(f"- {key}: {value}")
    lines.append(f"Issues: {len(issues)}")
    return "
".join(lines)
