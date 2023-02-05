package main

import (
	"fmt"
	"reflect"
	"time"
)

func test(a int, b int) (r1 int, r2 int) {
	r1 = 20
	r2 = 30
	return
	// return a, b
}
func test2(a int) int {
	_a := 10
	return _a
}
func test3() {
	defer fmt.Println(1)
	defer fmt.Println(2)
	defer fmt.Println(3)
}

type Hero struct {
	Name string
	Ad   int
}

func (this *Hero) Show() {
	fmt.Println(this.Name)
}

type resume struct {
	Name string `info:"name" doc:"我的名字"`
	Sex  string `info:"sex"`
}
func findTag(arg interface{}) {
	t := reflect.TypeOf(arg)
	for i := 0; i < t.NumField(); i++ {
		t := t.Field(i).Tag.Get("info")
		fmt.Println(t, 111111)
	}
}

func main() {
	c, d := test(3, 4)
	var a int = 11
	fmt.Println(&a, 1111, a)
	a = test2(a)
	fmt.Println(&a, 2222, a)
	fmt.Println("hello go", c, d)
	test3()
	var map1 = map[int]string{
		1: "one",
		2: "two",
	}
	fmt.Println(map1)

	var h Hero
	h.Name = "zhangs"
	h.Ad = 10
	h.Show()

	var r resume
	findTag(r)
	time.Sleep(1 * time.Second)
}
