package main
import ("fmt")
func func603(x int) int {
  total := 0
  for i := 0; i < x; i++ {
    total += (i * 603) % 97
  }
  return total
}
func main() {
  sum := 0
  for i := 1; i < 200; i++ { sum += func603(i) }
  fmt.Println("rand-20260118-99247", sum)
}
