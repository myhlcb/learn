//形参类型 个数 顺序
public class TestOverLoad {
    public static void main(String[] args) {
        add(3.14, 5);
    }

    static double add(double a, int b) {
        return a + b;
    }

    public static int add(int a, int b) {
        return a + b;
    }
}
