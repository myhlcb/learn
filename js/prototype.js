function Foo(name) {
  this.name = name;
}
Foo.prototype.getCar = function () {
  console.log(this.name);
};
const foo = new Foo('cat');

// foo.__proto__===Foo.prototype //准则1
// Foo.__proto__===Function.prototype  // Foo是函数
// Foo.prototype.__proto__===Object.prototype //Foo.prototyp是对象
// Funtion.prototype.__proto__===Object.prototype // Funtion.prototype是对象
// Object.__proto__===Funtion.prototype // Object是函数
// Array.__proto__===Funtion.prototype // Array是函数

// Object.prototype.__proto__===null // 原型链终止
// null.prototype.__proto__===Object.prototype // null.prototype是对象

foo.getCar();
console.log(foo.__proto__===Foo.prototype,1)
console.log(Foo.__proto__===Function.prototype,2)
console.log(Foo.prototype.__proto__===Object.prototype,3)
console.log(Function.prototype.__proto__===Object.prototype,4)
console.log(Function.__proto__===Object.__proto__,Object.__proto__,4.1)
console.log(Function.__proto__===Function.prototype,Function.prototype,4.2)
console.log(Function.__proto__.__proto__===Object.prototype,4.3)

console.log(Object.__proto__===Function.prototype,5)
console.log(Array.__proto__===Function.prototype,6)
console.log(Object.prototype.__proto__===null,7)
console.log(typeof null,typeof Object, typeof undefined)






console.log(foo.__proto__===Foo.prototype,22,foo.__proto__)
console.log(Foo.__proto__===Function.prototype,44,Foo.__proto__===Function.__proto__)
console.log(foo.prototype,Foo.prototype.__proto__===Object.prototype,8,
    foo.__proto__.__proto__===Object.prototype,
    77,Foo.prototype.__proto__===foo.__proto__.__proto__)
console.log(Function.prototype.__proto__===Object.prototype)

console.log(Function.__proto__,111,Object.prototype,222)
console.log(Object.prototype.__proto__===null,Object.__proto__===Function.prototype)
console.log(Object.prototype.__proto__===null,Function.prototype.__proto__.__proto__===null,2)

console.log(Object.__proto__===Function.__proto__,Object.__proto__===Function.prototype)