# Takes initial data from a csv file
def load_data_from_csv(filename):
    import csv
    
    data = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:
            value = int(row[1])  
            data.append(value)
    
    print("Data points loaded from", filename)
    return data


# Takes initial centroids from a csv file
def load_initial_centroids_from_csv(filename):
    import csv
    
    centroids = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        for row in reader:
            value = float(row[1])  # Assuming the value is in the second column
            centroids.append(value)
    
    print("Initial centroids loaded from", filename)
    return centroids