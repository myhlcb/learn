public class Point {
    int x, y;

    Point(int _x, int _y) {
        this.x = _x;
        this.y = _y;
    }

    public double getDistance(Point p) {
        System.out.println(p.x);
        return Math.sqrt((p.x - x) * (p.x - x) + (p.y - y) * (p.y - y));
    }

    public static void main(String[] args) {
        Point p1 = new Point(3, 4);
        Point p = new Point(0, 0);
        double r = p.getDistance(p1);
        System.out.println(r);
    }
}
