// function ss<T>(a:T):Array<T>{
//   return [a]
// }
// console.log(ss(1))

// 泛型约束


// function copy<T,S extends T>(target:T,source:S):T{
//   for (const key in target) {
//     target[key] = source[key]
//   }
//   return target
// }
// console.log(copy({a:1},{a:2,b:3}))

function test<T=number>(num:T):T{
  return num
}
console.log(test(1),test('str'))