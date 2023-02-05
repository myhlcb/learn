import java.util.Scanner;

public class TestScan {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("请输入用户名");
        String unname = s.nextLine();
        System.out.println("用户名：" + unname);
        int age = s.nextInt();
        System.out.println("年龄：" + age);
    }
}
