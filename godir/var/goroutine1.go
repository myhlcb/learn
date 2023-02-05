package main

import (
	"fmt"
)

func main() {
	go func() {
		defer fmt.Println("gogogo")
		func() {
			fmt.Println("go 2 go")
		}()
		// runtime.Goexit()
		fmt.Println("go 3 go")
	}()
	i := 0
	fmt.Printf("main goroutine:i=%d\n", i)
	// time.Sleep(1 * time.Second)
}
