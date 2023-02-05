package main

import "fmt"

type Book struct {
	name string
	auth string
}

func changeBook(book Book) {
	book.name = "ccc"
}
func change(book *Book) {
	book.name = "sccc"
}

func main() {
	var book Book
	book.name = "ssss"
	book.auth = "zhangs"
	fmt.Println(book)
	changeBook(book)
	fmt.Println(book)
	change(&book)
	fmt.Println(book)
}
