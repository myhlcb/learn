package main

import "fmt"

func aa(c, cc chan int) {
	x := 1
	for {
		select {
		case c <- x:
		case <-cc:
			fmt.Println("结束")
			return
		}
	}

}
func main() {
	c := make(chan int)
	cc := make(chan int)
	go func() {
		for i := 0; i < 6; i++ {
			fmt.Println(<-c, 11111, i)
		}
		cc <- 0
	}()
	aa(c, cc)
}
