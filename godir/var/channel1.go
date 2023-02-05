package main

import "fmt"

func main() {
	c := make(chan int)
	go func() {
		c <- 1
		fmt.Println("aaaa")
	}()

	// for {
	// 	if data, ok := <-c; ok {
	// 		fmt.Println(data, ok)
	// 	} else {
	// 		break
	// 	}
	// }
	num := <-c
	fmt.Println(c, 11, num)
}
