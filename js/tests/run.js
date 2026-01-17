const assert = require('assert');
const { loadData, validateItems, computeSummary } = require('../lib');

const payload = loadData('data/sample.json');
const config = loadData('config.json');
const expected = payload.expected;

const issues = validateItems(payload.items, payload.rules, config.categories);
const summary = computeSummary(payload.items, config.categories);

assert.strictEqual(summary.totalAmount, expected.total_amount);
assert.strictEqual(summary.avgScore, expected.avg_score);
assert.strictEqual(summary.topItem, expected.top_item);
assert.strictEqual(issues.length, expected.issue_count);

console.log('ok');
