fn func404(x: i32) -> i32 {
    let mut total = 0;
    let mut i = 0;
    while i < x {
        total += (i * 404) % 97;
        i += 1;
    }
    total
}
fn main() {
    let mut sum = 0;
    for i in 1..200 { sum += func404(i); }
    println!("{} {}", "rand-20260118-99247", sum);
}
