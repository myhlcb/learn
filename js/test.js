// js分为函数对象和普通对象，每个对象都有__proto__属性，但只有函数对象才有prototype属性
// Object Function都是内置的函数,类似的还有Array Regex Date Boolean Number String
// 属性__proto__是一个对象，它有两个属性，constructor和__proto__；
// 原型对象prototype有一个默认的constructor属性，用于记录实例是由哪个构造函数创建；

function P(name, age) {
  this.name = name;
  this.age = age;
}
const p = new P('zhangs', 10);

console.log(p.__proto__ === P.prototype);
console.log(P.__proto__ === Function.prototype);
console.log(P.prototype.constructor === P);
console.log(P.prototype.__proto__ === Object.prototype); //P.prototype是普通对象
console.log(Function.prototype.__proto__ === Object.prototype); //Function.prototype是普通对象
console.log(Function.__proto__.__proto__ === Object.prototype);
console.log(Function.prototype === Function.__proto__);
console.log(Object.prototype.__proto__ === null); // 原型链终止
console.log(Object.__proto__ === Function.prototype);
console.log(Array.__proto__ === Function.prototype);
