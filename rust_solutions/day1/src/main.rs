use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

pub fn naive(file_path: String) -> Result<u32, Box<dyn std::error::Error>>{
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    let mut max_cal: u32 = 0;
    let mut running_cal: u32 = 0;

    for line in reader.lines() {
        let parsed_int: u32 = line.unwrap().parse::<u32>().unwrap_or(0);
        if parsed_int == 0 {
            max_cal = (running_cal > max_cal).then_some(running_cal).unwrap_or(max_cal);
            running_cal = 0;
        } else {
            running_cal += parsed_int;
        }
   }
   Ok(max_cal)
}

fn main() -> () {
    let result: u32 = naive(String::from("input.txt")).unwrap();
    println!("{}", result);
    ()
}
