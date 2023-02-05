package main

import "fmt"

// :=只能在函数内部使用
func main() {
	var a int
	fmt.Println("a=", a)
	fmt.Printf("typeof a:%T\n", a)
	e := "100"
	fmt.Printf("typeof %T\n", e)
	var b, c = 1, "ss"
	var f = 100
	a = 10
	fmt.Println(b, c, f, a)
	const aa = 10
	fmt.Println(aa)
	//    可以在const里面使用iota;iota只能配合const使用
	const (
		BEIJING = iota
		SHANGHAI
		SHENZHEN
		A, B = iota + 1, iota + 2
	)
	fmt.Println(BEIJING, SHANGHAI, SHENZHEN, A, B)
}
