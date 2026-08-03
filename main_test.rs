fn main() {
    // Hardcoded credential vulnerability in Rust file
    let api_key = "secret-rust-key-abcde12345";
    println!("Init client with API key: {}", api_key);
}