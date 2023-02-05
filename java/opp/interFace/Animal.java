package opp.interFace;

public abstract class Animal {
    int age;

    protected abstract void rest(); // 使用abstract定义抽象类，抽象类不需要实现一个方法
}

class Dog extends Animal {
    // 抽象类方法必须重写
    @Override
    public void rest() {
        // TODO Auto-generated method stub

    }
}

class Cat extends Animal {
    // private->friendly->protected->public
    @Override
    protected void rest() {}
}