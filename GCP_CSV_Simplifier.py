'''
Takes a CSV in the format that it is typically given to us from our Leica unit,
and strips away the data we don't typically use.
Can take single or multiple input files, will output a single file with all rows.
Discards any rows which are duplicates in every single row.
'''

import csv
import os

def press_enter_to_end():
    '''
    Allows user the chance to read the contents of the cmd window before it ends,
    when packaged as an exe.
    '''
    input("Press Enter to end...")

def filter_csv(input_folder, output_file, relevant_indices):
    '''
    Main program. Takes in all input CSV files, reads their contents,
    outputs all rows stripped down to only include relevant info.
    '''
    #grab all csv files in input
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the input folder.")
        return

    #check for output dir
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    unique_rows = set()

    #write output file (will overwrite any previous)
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        #read through each csv, take the 4 columns we want, put them on the output
        for filename in csv_files:
            input_file = os.path.join(input_folder, filename)
            with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)

                for row in reader:
                    filtered_row = tuple(row[i] for i in relevant_indices if i < len(row))
                    if filtered_row not in unique_rows:
                        unique_rows.add(filtered_row)
                        writer.writerow(filtered_row)
                        print(f'Read point {filtered_row[0]} from {input_file}')
                    else:
                        print(f'Found duplicate point, {filtered_row[0]} from {input_file}, skipping...')


INPUT_FOLDER = 'input'
OUTPUT_FILE = 'output/output.csv'
RELEVANT_COLUMNS = [0, 2, 3, 4]

filter_csv(INPUT_FOLDER, OUTPUT_FILE, RELEVANT_COLUMNS)
press_enter_to_end()
