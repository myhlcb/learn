package main
import "fmt"
func slice(){
	slice1 := make([]int,3,4)
	fmt.Printf("slice1 长度是%d,容量是%d,slice=%v\n",len(slice1),cap(slice1),slice1)
	slice1 = append(slice1,1)
	fmt.Printf("slice1 长度是%d,容量是%d,slice=%v\n",len(slice1),cap(slice1),slice1)
	slice1 = append(slice1,2)
	fmt.Printf("slice1 长度是%d,容量是%d,slice=%v\n",len(slice1),cap(slice1),slice1)
	slice1 = append(slice1,3)
	fmt.Printf("slice1 长度是%d,容量是%d,slice=%v\n",len(slice1),cap(slice1),slice1)
	slice1 = append(slice1,3)
	fmt.Printf("slice1 长度是%d,容量是%d,slice=%v\n",len(slice1),cap(slice1),slice1)

	s1 :=make([]int,3)
	copy(s1,slice1)
	s :=s1[0:3]
	fmt.Println(s)
	s[0]=100
	fmt.Println(s,slice1)
}
func main(){
	slice()
	var arr []int
	arr =[]int {1,2,3} 
	fmt.Println(arr)
	for _, v := range arr {
		fmt.Println(v)
	}

}

