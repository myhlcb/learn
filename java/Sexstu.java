public class Sexstu {
    int age;
    String name;

    // static引用需要再定义this
    public void study(Sexstu self) {
        System.out.println(this.name + ":在学习");
    }

    public static void main(String[] args) {
        Sexstu s = new Sexstu();
        s.age = 10;
        s.name = "zhangs";
        s.study(s);
    }
}
