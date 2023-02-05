package opp.package1;

public class TestClass {
    public static void main(String[] args) {
        Student s = new Student("zhangs", 20);
        s.rest();
    }
}

class Person {
    String name;
    int age;

    Person(String name, int age) {
        System.out.println("Person调用");
        this.name = name;
        this.age = age;
    }

    final public void run() {
        System.out.println("run");
    }

    public void rest() {
        System.out.println("rest");
    }
}

class Person2 {
    String name = "name";
    int age;

    // Person(String name, int age) {
    // this.name = name;
    // this.age = age;
    // }
    final public void run() {
        System.out.println("run");
    }

    public void rest() {
        System.out.println("rest");
    }
}

class Student extends Person {
    Student(String name, int age) {
        super(name, age);
        System.out.println("Student调用");
        // TODO Auto-generated constructor stub
    }

    Person2 p = new Person2();// 组合

    public void study() {
        System.out.println("学习");
    }

    @Override
    public void rest() {
        // TODO Auto-generated method stub
        System.out.println(this.p.name + ":" + this.name + "Student学习");
    }

    // final不能重写(override)，但是可以重载(overload);因为重载相当于新写的
    public void run(String s) {
        System.out.println("run");
    }
}