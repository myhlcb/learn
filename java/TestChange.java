public class TestChange {
    public static void main(String[] args) {
        int a = 2345;
        long b = a;
        double f = a;
        float g = a;
        // int c = b; //报错 long不能转int
        int c = (int) b; // 不报错
        System.out.println(b);
        System.out.println(c);
        System.out.println((byte) 300); // 超出范围转换异常
        // 溢出问题
        int m = 1000000000; // 10亿
        int y = 20;
        int t = m * y;
        System.out.println(t);
        long tt = 1L * m * y;
        System.out.println(tt);
    }
}
