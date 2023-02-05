package opp.interFace;

public class TestInterFace {
    public static void main(String[] args) {
        Angel a = new Angel();
        a.helpOther();
        a.def();
        Volant.stac(); // 接口调用
        GoodMan g = new GoodMan();
        g.helpOther();

    }
}
