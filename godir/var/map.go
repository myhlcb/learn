package main

import "fmt"

func s() {
	m1 := make(map[int]string, 10)
	m1[0] = "java"
	fmt.Println(m1)

}
func main() {
	s()
}
