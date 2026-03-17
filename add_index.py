import csv

def add_index_to_csv(input_filename, output_filename):
    
    # read the existing csv file
    file = open(input_filename, "r")
    reader = csv.reader(file)
    
    # store all rows into a list
    rows = []
    for row in reader:
        rows.append(row)
    
    file.close()
    
    # write a new csv file with index added
    file = open(output_filename, "w", newline="")
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(["index", "value"])
    
    # write each row with an index
    for i in range(len(rows)):
        value = rows[i][0]  # get the value from the first column
        writer.writerow([i + 1, value])
    
    file.close()
    print("Indexed file saved to", output_filename)
    
add_index_to_csv("no-index-data.csv", "data_points.csv")
    