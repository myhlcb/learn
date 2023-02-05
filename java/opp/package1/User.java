package opp.package1;

public class User {
    public String name;// 所有使用
    protected int age;// 父子，同包使用
    String address;// 同包使用
    private boolean isMan;// 只能自己使用

    public static void main() {
        System.out.println("User");
    }
}
