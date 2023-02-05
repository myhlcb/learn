package main

import (
	"fmt"
	"lib1"
	_ "lib2"
)

func swap(a *int, b *int) {
	temp := *a
	*a = *b
	*b = temp
}
func main() {
	lib1.Test()
	aa := 10
	bb := 20
	swap(&aa, &bb)
	fmt.Println(aa, bb)
}
