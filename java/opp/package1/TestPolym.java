package opp.package1;

// javac-d.Animal.java TestPolym.java 编译相关包
// java opp.package1.TestPolym 调用
import opp.package1.Animal;

public class TestPolym {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.cry(d);
    }
}