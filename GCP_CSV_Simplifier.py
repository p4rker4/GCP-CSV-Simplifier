import csv
import os

def filter_csv(input_folder, output_file, relevant_indices):
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_folder, filename)
            break
    else:
        print("No CSV file found in the input folder.")
        return

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                filtered_row = [row[i] for i in relevant_indices if i < len(row)]
                writer.writerow(filtered_row)

input_folder = 'input'
output_file = 'output/output.csv'
relevant_indices = [0, 2, 3, 4]

filter_csv(input_folder, output_file, relevant_indices)
