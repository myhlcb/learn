// 普通属性和方法对象使用;
// static属性和方法供类使用
// static不能调用普通对象和方法
public class TestStatic {
    int a, b;
    static String company = "company";

    TestStatic(int a, int b) {
        this.a = a;
        this.b = b;
    }

    void eat() {
        System.out.println(this.a + "eat");
    }

    static void eat(String b) {
        // eat(); // 报错，static不能使用非static方法
        // this.eat() // 报错， static不能使用this
        System.out.println(company);// company是static属性，可以直接使用
    }

    public static void main(String[] args) {
        System.out.println("main");
        TestStatic s = new TestStatic(1, 2);
        s.eat();
        s.eat("b"); // 对象可以使用，追溯到父类的static的eat
        TestStatic.eat("c"); // 可以直接使用
    }
}
