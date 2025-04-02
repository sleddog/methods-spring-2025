use std::env;

fn main() {
    // get arguments
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("No argument found, please provide an integer.");
        std::process::exit(1);
    }

    // assign the argument given to a integer ("bound")
    let bound: i32 = args[1].parse().expect("Failed to parse arguement as integer");
    
    // increment from 1 to the bound
    for current in 1..(bound + 1) {
        // check if current number is a multiple of 3 and 5
        if current % 3 == 0 && current % 5 == 0{
            println!("BobCat");
        // check if current number is a multiple of 3
        } else if current % 3 == 0 {
            println!("Bob");
        // check if current number is a multiple of 5
        } else if current % 5 == 0 {
            println!("Cat");
        // otherwise, print the current number
        } else {
            println!("{}", current);
        }
    }
}