package main

import (
	"encoding/json"
	"fmt"
	_ "os"
	"reflect"
)

type Reader interface {
	ReadBook()
}
type Write interface {
	WriteBook()
}
type Book struct {
}

func (this *Book) ReadBook() {
	fmt.Println("read book")
}
func (this *Book) WriteBook() {
	fmt.Println("write book")
}

type Animal struct {
	Name string
	Age  int
	Bred string
}
type User struct {
	Id   int
	Name string
	Age  int
}

func reflectNum(arg interface{}) {
	fmt.Println(reflect.TypeOf(arg))
	fmt.Println(reflect.ValueOf(arg))
}

type resume struct {
	Name string `info:"name" doc:"我的名字"`
	Sex  string `info:"sex"`
}
type Movie struct {
	Name  string `json:"title"`
	Price int    `json:"price"`
}

func findTag(arg interface{}) {
	t := reflect.TypeOf(arg)
	for i := 0; i < t.NumField(); i++ {
		t := t.Field(i).Tag.Get("info")
		fmt.Println(t, 111111)
	}
}
func main() {
	var book Reader
	book = &Book{}
	book.ReadBook()
	var w Write
	w = book.(Write)
	w.WriteBook()

	var num float64 = 1.2345
	reflectNum(num)

	u := Animal{"tom", 10, "green"}
	// u:=User{1,"sz",25}
	t := reflect.TypeOf(u)
	v := reflect.ValueOf(u)
	fmt.Println(t, 33, v)

	for i := 0; i < t.NumField(); i++ {
		// fmt.Println(i,111,t.Field(i).Name,t.Field(i).Type,333)
		// fmt.Println(v.Field(i).Interface())
		f := t.Field(i)
		fmt.Printf("%s : %v\n", f.Name, f.Type)
		// 获取字段的值信息
		// Interface()：获取字段对应的值
		val := v.Field(i).Interface()
		fmt.Println("val :", val)
	}
	var r resume
	findTag(r)
	m := Movie{"zhangs", 10}
	fmt.Println(m, 22222)

	jsonStr, _ := json.Marshal(m)
	fmt.Printf("jsonstr=%s\n", jsonStr)
	mm := Movie{}
	err := json.Unmarshal(jsonStr, &mm)
	fmt.Println(err, 1111)
	fmt.Printf("xx:%v\n", mm)
}
