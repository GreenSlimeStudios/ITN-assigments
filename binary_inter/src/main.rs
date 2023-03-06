fn main() {
    println!("SELECT MODE\n1: decimal to binary (+/-)\n2: binary to decimal (+/-)\n");
    let mut mode: String = String::new();
    std::io::stdin().read_line(&mut mode).unwrap();
    mode = mode.trim().to_string();
    match mode.as_str() {
        "1" => to_binary(),
        "2" => to_decimal(),
        _ => (),
    }
}

fn to_binary() {
    let mut decimal_str: String = String::new();
    println!("Type in decimal value in range (-255, 255)");
    std::io::stdin().read_line(&mut decimal_str).unwrap();
    decimal_str = decimal_str.trim().to_string();
    let dec: f32 = decimal_str.parse::<f32>().unwrap();
    // println!("{dec}");
    if dec > 255. || dec < -255. {
        println!("value out of range");
        return;
    }
    let mut values: Vec<char> = Vec::new();
    let mut x: f32 = dec.abs() as f32;
    x = x.floor();

    while x >= 1.0 {
        let y: f32 = x as f32 / 2.0;
        x = y.floor();
        if y == x {
            if dec < 0. {
                values.push('1');
            } else {
                values.push('0');
            }
        } else {
            if dec < 0. {
                values.push('0');
            } else {
                values.push('1');
            }
        }
    }

    for _ in 0..8 - values.len() {
        values.push(if dec < 0. { '1' } else { '0' });
    }
    values.push(if dec < 0. { '1' } else { '0' });

    values.reverse();

    if decimal_str.contains(".") {
        values.push('.');
        let mut rem = dec.abs() - dec.abs().floor();
        for _ in 0..8 {
            rem = rem * 2.0;
            if rem >= 1.0 {
                values.push(if dec < 0.0 { '0' } else { '1' });
            } else {
                values.push(if dec < 0.0 { '1' } else { '0' });
            }
            rem = rem - rem.floor();
        }
    }
    for val in values {
        print!("{}", val);
    }
    println!();
}
fn to_decimal() {
    let mut binary_str: String = String::new();
    println!("Type in decimal value in range (-255, 255) [XXXXXXXXX.XXXXXXXX]");
    std::io::stdin().read_line(&mut binary_str).unwrap();
    binary_str = binary_str.trim().to_string();

    let mut sum: f32 = 0.;
    let mut rem_sum: f32 = 0.;
    for i in 1..9 {
        if binary_str.as_bytes()[i] as char == '1' {
            sum += 2u16.pow((8 - i) as u32) as f32;
        }
    }
    if binary_str.as_bytes()[0] as char == '1' {
        sum = -255. + sum;
    }
    if binary_str.contains(".") {
        let split: Vec<&str> = binary_str.split(".").collect();
        let rem = split[1].to_string();
        println!("{rem}");
        for i in 0..8 {
            if rem.as_bytes()[i] as char == '1' {
                rem_sum += 2f32.powi(-(i as i32 + 1));
            }
        }
        if binary_str.as_bytes()[0] as char == '1' {
            rem_sum = 1.0 - rem_sum;
        }
    }
    print!(
        "{}",
        if binary_str.as_bytes()[0] as char == '1' {
            sum - rem_sum
        } else {
            sum + rem_sum
        }
    );
}
