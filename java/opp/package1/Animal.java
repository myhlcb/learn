package opp.package1;

public class Animal {
    void shut() {
        System.out.println("动物吼叫");
    }

    void cry(Animal a) {
        a.shut();
    }

    public static void main(String[] args) {
        Dog d = new Dog();
        d.cry(d);
        Cat c = new Cat();
        c.cry(c);
    }
}

class Dog extends Animal {
    @Override
    void shut() {
        // TODO Auto-generated method stub
        System.out.println("汪汪汪");

    }
}

class Cat extends Animal {
    @Override
    void shut() {
        // TODO Auto-generated method stub
        System.out.println("喵喵喵");

    }
}