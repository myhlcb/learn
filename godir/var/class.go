package main

import "fmt"

// 属性大小写保证外部包是否能访问
type Hero struct {
	name string
	age  int
}

func (this *Hero) GetName() {
	fmt.Println("name = ", this.name)
}
func (this *Hero) SetName(name string) {
	this.name = name
}

type SuperMan struct {
	Hero
	level int
}
type Animal interface {
	Sleep()
	GetColor() string
	getType() string
}

type Cat struct {
	color string
}

func (this *Cat) Sleep() {
	fmt.Println("cat sleep")
}
func (this *Cat) GetColor() string {
	fmt.Println("name = ", this.color)
	return this.color
}
func (this *Cat) getType() string {
	fmt.Println("name = ", this.color)
	return "type"
}
func showAnimal(animal Animal) {
	fmt.Println(animal.GetColor())
}
func main() {
	// hero:=Hero{name:"zhang3",age:10}
	hero := SuperMan{Hero{"zhang3", 9}, 3}
	hero.SetName("lisi")
	fmt.Println(hero.name)
	var cat Cat
	cat.Sleep()
	var animal Animal
	animal = &Cat{"green"}
	animal.Sleep()
	showAnimal(&Cat{"yello"})
}
