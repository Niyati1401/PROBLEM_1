import csv

def read_spec(spec_file):
    
    offsets = []
    with open(spec_file, 'r', encoding='utf-8') as file:
        for line in file:
            offsets.append(int(line.strip()))
    return offsets

def parse_fixed_width_file(input_file, offsets):
   
    records = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.rstrip('\n')
            start = 0
            record = []
            for offset in offsets:
                record.append(line[start:start+offset].strip())
                start += offset
            records.append(record)
    return records

def write_csv_file(records, output_file):
    
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for record in records:
            writer.writerow(record)

def write_fixed_width_file(records, output_file, offsets):
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for record in records:
            line = ""
            for i, field in enumerate(record):
                line += field.ljust(offsets[i])
            outfile.write(line + '\n')

if __name__ == "__main__":
    # Example usage
    spec_file = r'Users\niyatibhagavatam\Downloads\problem_1\spec.txt'       # Update with the actual path
    input_file = r'Users\niyatibhagavatam\Downloads\problem_1\input.txt'     # Update with the actual path
    csv_output_file = r'Users\niyatibhagavatam\Downloads\problem_1\output.csv'   # Update with the actual path
    fixed_width_output_file = r'Users\niyatibhagavatam\Downloads\problem_1\output_fixed_width.txt'   

    offsets = read_spec(spec_file)
    records = parse_fixed_width_file(input_file, offsets)
    write_csv_file(records, csv_output_file)
    write_fixed_width_file(records, fixed_width_output_file, offsets)
