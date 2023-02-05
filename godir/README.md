### 安装及配置
* GOROOT表示源码包所在路径;
* GOPATH表示开发者目录;
* go env -w GOPATH=$PWD 实时配置环境变量
* go version、go env、go help
* go build、go run *.go
### 基本语法
```
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("hello go")
	time.Sleep(1 * time.Second)
}
```
### 数据类型
* 数字类型 int + float + byte
* boolean类型 true + false
* 字符串 string
* 派生类型 interface + struct + Pointer + Array + Slice + Map + Chan + 函数
#### 派生类型
* Pointer &表示地址指针 *表示实际值,如果更改内存地址,需要传入指针。
* Array [2]int ={1,2}
* Slice 声明
```
slice1 []int = {1,2}
slice2:=[]int {1,2}
slice3:= make([]int,3,4) //表示内存空间为3，步长为4

```
* map(参照js object和py dict)
``` 
	var map1 = make(map[int]string)
	map1[1] = "one"
	map1[2] = "two"
// 第二种
var map1 = map[int]string{
		1: "one",
		2: "two",
	}
// map 不要使用map[int]string声明,因为没有分配空间,会报'panic: assignment to entry in nil map'错误
var map1 map[int]string
map1[0]="one"
map2[1]="two"
```
### 面向对象编程
* 继承和多态
### 反射reflect
### goroutine 
### channel 
## go mod
* go mod init
* go mod download
* 

### 变量
* 四种声明方式,其中:=不能用于全局
```
	var a int
	var b int = 19
	var c = 20
	d := 21
```
* 多变量声明
```
	var a, b int = 100, 200
	var (
		c = 30
		d = 40
	)
```
### 常量
* 使用const声明,const可以使用iota表示每行自动加1,初始为0;
```
const (
		a = 30 * iota
		b
		c
		d
	)
```
### 函数
```
func test(a int, b int) (r1 int, r2 int) {
	r1 = 20
	r2 = 30
	return  //有返回值的函数
	// return a, b //无返回值的函数
}
```
### import包使用
* 配置GOPATH, $GOPATH/$PWD, import包的时候$PWD/package
```
import _ "fmt" //匿名，暂时不用的package
import aa "fmt" // 别名 aa.test 代替fmt.test
import . "fmt" // 直接使用test
```
* defer使用堆栈,先进后出;而且在return函数之后执行
```
//依次打印3,2,1
func test3() {
	defer fmt.Println(1)
	defer fmt.Println(2)
	defer fmt.Println(3)
}
```