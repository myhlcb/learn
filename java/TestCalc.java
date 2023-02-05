public class TestCalc {
    public static void main(String[] args) {
        int a = 3;
        long b = 6;
        long c = b / a; // long➗int结果是long
        double d = 32 / 3; // 两个整数相除，直接保留整数部分,没有四舍五入
        float f = 1.111133222211111f;
        System.out.println(c);
        System.out.println(d);
        System.out.println(f);
        int g = 10;
        int i = g++; // 先赋值，再加
        int ii = ++g; // 先加再赋值
        System.out.println(i);
        System.out.println(ii);

        // 测试逻辑运算符
        boolean aa = true;
        boolean bb = false;
        System.out.println(aa & bb);
        boolean cc = 1 > 2 && (4 < 3 / 0); // 短路与，第一个出结果就不在判断
        System.out.println(cc);
        // cc = 1 > 2 & (4 < 3 / 0); // 报错
        System.out.println(cc);

        int aaa = 7;
        int bbb = 8;
        // System.out.println(aaa && bbb); // 报错，int不能&&
        System.out.println(aaa & bbb);
        System.out.println(aaa | bbb);
        System.out.println(aaa ^ bbb);
        System.out.println(~bbb); // 取反
        // 二进制 1000
        // 计算补码(0是正数的意思) 01000
        // 取反 10111
        // 减一 10110
        // 再取反11001
        // 1是负数位，所以1001 = 9 -9
        System.out.println(aaa << 1);
        System.out.println("3" + 4);

        // char和string
        char a1 = 'a';
        char b1 = 'b';
        System.out.println(a1 + b1); // 195

        String a2 = "a";
        String b2 = "b";
        System.out.println(a2 + b2); // 195

    }
}
