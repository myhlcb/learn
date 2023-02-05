package main

import "fmt"

func fool() (r1 int) {
	c := 100
	fmt.Println(c)
	r1 = 100
	return
}

func main() {
	ss := fool()
	fmt.Println(ss)
}
