package opp.interFace;

public interface Volant {
    int FLY_HIGHT = 100;

    void fly();

    default void def() {
        System.out.println("默认方法");
    }

    public static void stac() {
        System.out.println("静态方法");
    }
}

interface Honest {
    void helpOther();
}

class GoodMan implements Honest {
    @Override
    public void helpOther() {
        System.out.println("goofman helpOther");

    }
}

class Angel implements Volant, Honest {
    @Override
    public void fly() {
        System.out.println("angel fly");

    }

    @Override
    public void helpOther() {
        System.out.println("angel helpOther");

    }

    // @Override
    // public void def() {
    // System.out.println("angel默认方法");
    // }
}