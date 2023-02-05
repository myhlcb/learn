function ss(a, b) {
  console.log(a, 11, b);
  a = 4;
  b.push(3);
}
a = 1;
b = [1, 2, 3];
ss(a, b);

console.log(a, b);
