function func372(x) {
  let total = 0;
  for (let i = 0; i < x; i++) {
    total += (i * 372) % 97;
  }
  return total;
}
function main() {
  const data = [];
  for (let i = 1; i < 200; i++) data.push(func372(i));
  console.log("rand-20260118-99247", data.reduce((a,b)=>a+b,0));
}
main();
