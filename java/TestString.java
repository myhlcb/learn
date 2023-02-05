public class TestString {
    public static void main(String[] args) {
        String a = null;
        String b = "";
        String c = "java";
        String d = new String("");
        // System.out.println(a.length());// 报错 null
        System.out.println(null instanceof String);
        System.out.println(b.length() + "," + c.length() + "," + d.length());

    }
}
