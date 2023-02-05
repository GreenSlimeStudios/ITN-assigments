use std::io;

fn main() {
    println!("Hello, world!");

    let mut input: String = String::new();
    while io::stdin().read_line(&mut input).ok() == Some(v) {
        println!("{input}");
    }
}
