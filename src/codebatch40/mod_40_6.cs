using System;
class Program406 {
  static int Func(int x) {
    int total = 0;
    for (int i = 0; i < x; i++) { total += (i * 406) % 97; }
    return total;
  }
  static void Main() {
    int sum = 0;
    for (int i = 1; i < 200; i++) sum += Func(i);
    Console.WriteLine("rand-20260118-99247" + " " + sum);
  }
}
