const path = require('path');
const { loadData, validateItems, computeSummary, makeReport } = require('./lib');

function main() {
  const inputPath = process.argv[2] || path.join('data', 'sample.json');
  const payload = loadData(inputPath);
  const config = loadData('config.json');

  const issues = validateItems(payload.items, payload.rules, config.categories);
  const summary = computeSummary(payload.items, config.categories);
  const report = makeReport(config, summary, issues);
  console.log(report);
}

if (require.main === module) {
  main();
}
