import java.util.Scanner;

public class TestCon {
    public static void main(String[] args) {
        double a = (int) (Math.random() * 6) + 1;
        double b = (int) (Math.random() * 6) + 1;
        double c = (int) (Math.random() * 6) + 1;
        int result = (int) (a + b + c);
        System.out.println(result);
        if (result > 15) {
            System.out.println("手气不错");
        } else if (result > 10) {
            System.out.println("手气一般");
        } else {
            System.out.println("手气不咋地");
        }
        switch (result) {
            case 15:
                System.out.println("15了");
                break;
            case 16:
                System.out.println("16了");
                break;
            case 17:
                System.out.println("17了");
                break;
            case 18:
                System.out.println("18了");
                break;
            default:
                System.out.println(result);
                break;
        }
        int cc = 10;
        while (cc < 15) {
            System.out.println("得到cc:" + cc);
            cc++;
        }
        for (int i = 0; i < 100; i++) {
            if (i % 3 == 0) {
                System.out.println(i);
            }
        }
        Scanner s = new Scanner(System.in);
        while (true) {
            System.out.println("请输入月薪");
            int salary = s.nextInt();
            System.out.println("请输入月数");
            int mon = s.nextInt();
            int amount = salary * mon;
            if (amount > 50) {
                System.out.println("恭喜");
            } else {
                System.out.println("需要努力");
            }
            // 输入88退出，输入66继续
            System.out.println("输入88退出，输入66继续");
            int comm = s.nextInt();
            if (comm == 88) {
                System.out.println("退出");
                break;
            }
            if (comm == 66) {
                System.out.println("继续");
                continue;
            }
        }
        System.out.println("生活艰难");
    }
}