public class TestThis {
    double a;

    // 重载
    TestThis(double a) {
        this.a = a;
        System.out.println("first this");
    }

    TestThis(int a) {
        this(3.14);
        System.out.println("first this:" + a);
    }

    TestThis(int a, int b) {
        this(3);
        System.out.println("first this:" + a + "," + b);
    }

    public static void main(String[] args) {
        TestThis s = new TestThis(1, 2);

    }

}
