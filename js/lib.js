const fs = require('fs');

function loadData(path) {
  return JSON.parse(fs.readFileSync(path, 'utf8'));
}

function validateItems(items, rules, categories) {
  const issues = [];
  const allowedStatuses = new Set(rules.allowed_statuses || []);
  for (const item of items) {
    if (item.amount < rules.min_amount || item.amount > rules.max_amount) {
      issues.push(`amount_out_of_range:${item.id}`);
    }
    if (item.score < 0 || item.score > 100) {
      issues.push(`score_out_of_range:${item.id}`);
    }
    if (!categories.includes(item.category)) {
      issues.push(`unknown_category:${item.id}`);
    }
    if (!allowedStatuses.has(item.status)) {
      issues.push(`unknown_status:${item.id}`);
    }
  }
  return issues;
}

function computeSummary(items, categories) {
  const totalAmount = items.reduce((sum, item) => sum + item.amount, 0);
  const avgScore = Math.round((items.reduce((sum, item) => sum + item.score, 0) / items.length) * 100) / 100;
  const topItem = items.reduce((best, item) => (item.score > best.score ? item : best), items[0]).id;
  const categoryTotals = {};
  for (const category of categories) {
    categoryTotals[category] = 0;
  }
  for (const item of items) {
    if (categoryTotals[item.category] !== undefined) {
      categoryTotals[item.category] += item.amount;
    }
  }
  return { totalAmount, avgScore, topItem, categoryTotals };
}

function makeReport(config, summary, issues) {
  const lines = [];
  lines.push(config.project_title);
  lines.push(`Goal: ${config.goal}`);
  lines.push('Metrics');
  lines.push(`- Total ${config.amount_label}: ${summary.totalAmount}`);
  lines.push(`- Avg ${config.score_label}: ${summary.avgScore}`);
  lines.push(`- Top ${config.entity_name}: ${summary.topItem}`);
  lines.push('Category totals');
  for (const [key, value] of Object.entries(summary.categoryTotals)) {
    lines.push(`- ${key}: ${value}`);
  }
  lines.push(`Issues: ${issues.length}`);
  return lines.join('
');
}

module.exports = { loadData, validateItems, computeSummary, makeReport };
