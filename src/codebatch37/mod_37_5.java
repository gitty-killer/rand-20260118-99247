public class Main375 {
  static int func(int x) {
    int total = 0;
    for (int i = 0; i < x; i++) { total += (i * 375) % 97; }
    return total;
  }
  public static void main(String[] args) {
    int sum = 0;
    for (int i = 1; i < 200; i++) sum += func(i);
    System.out.println("rand-20260118-99247" + " " + sum);
  }
}
