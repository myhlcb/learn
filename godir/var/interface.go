package main

import "fmt"

func myFunc(arg interface{}) {
	fmt.Println(arg)
	val, ok := arg.(string)
	fmt.Println(val, 111, ok)
}

type Book struct {
	name string
	auth string
}

func main() {
	book := Book{"zhang3", "lisi4"}
	myFunc(book)
	myFunc(100)
	myFunc("100")
}
