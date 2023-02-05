package main

import (
	"fmt"
	"time"
)

func main() {
	const (
		a = 30 * iota
		b
		c
		d
	)
	// c := make(chan int)
	cc := make(chan int)

	fmt.Printf("len cc:%d\n", len(cc))
	go func() {
		defer fmt.Println("goroutine结束")
		fmt.Println("goroutine正在运行")
		// c <- 666
		for i := 0; i < 4; i++ {
			cc <- i
			fmt.Println("发送元素", i)
		}
	}()
	// num := <-c
	time.Sleep(time.Second * 2)
	for i := 0; i < 3; i++ {
		num := <-cc
		fmt.Println(num, 11111)

	}
	// fmt.Println(cc, 1111111)
	fmt.Println("结束")
}
