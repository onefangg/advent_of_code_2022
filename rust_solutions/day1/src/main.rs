pub fn naive(file_path: String) -> Result<u32, Box<dyn std::error::Error>> {
    use std::fs::File;
    use std::io::BufRead;
    use std::io::BufReader;

    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    let mut max_cal: u32 = 0;
    let mut running_cal: u32 = 0;

    for line in reader.lines() {
        let parsed_int: u32 = line.unwrap().parse::<u32>().unwrap_or(0);
        if parsed_int == 0 {
            max_cal = (running_cal > max_cal)
                .then_some(running_cal)
                .unwrap_or(max_cal);
            running_cal = 0;
        } else {
            running_cal += parsed_int;
        }
    }
    Ok(max_cal)
}

pub fn alternate(file_path: String) -> u32 {
    // referenced from: https://nickymeuleman.netlify.app/garden/aoc2022-day01
    use std::fs::read_to_string;

    let read_lines: String = read_to_string(file_path).unwrap();
    let max_cal: u32 = read_lines
        .split("\n\n")
        .map(|x| x.lines().filter_map(|y| y.parse::<u32>().ok()).sum::<u32>())
        .max()
        .unwrap();

    max_cal
}

fn main() -> () {
    let result: u32 = naive(String::from("input.txt")).unwrap();
    let alt_result: u32 = alternate(String::from("input.txt"));

    println!("Naive Result: {}", result);
    println!("Alt Result: {}", alt_result);
    ()
}
