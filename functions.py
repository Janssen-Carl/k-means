# functions for k-means clustering


import random
from matplotlib import colors
import matplotlib.pyplot as plt

# function no. 1: generate random data
def generate_data(num_points, lower_bound, upper_bound):
    data = []
    for _ in range(num_points):
        random_number = random.randint(lower_bound, upper_bound)
         
        data.append(random_number)
        
    return data

# function no. 2: initialize centroids
def initialize_centroids(data, num_centroids):
    centroids = []
    data_copy = data.copy()
    
    for _ in range(num_centroids):
        random_index = random.randint(0, len(data_copy) - 1)
        candidate_centroid = data_copy[random_index]
        centroids.append(candidate_centroid)
        
        data_copy.pop(random_index)
        
    return centroids        


# function no. 3: assign clusters
def assign_clusters(data, centroids):
    assignments = []
    
    for point in data:
        closest_centroid = 0
        closest_distance = abs(point - centroids[0])
        
        for i in range(1, len(centroids)):
            distance = abs(point - centroids[i])
            
            if distance < closest_distance:
                closest_distance = distance
                closest_centroid = i
                
        assignments.append(closest_centroid)
    
    return assignments

# function no. 4: recompute centroids
def recompute_centroids(data, assignments, num_centroids):
    new_centroids = []
    
    for cluster_index in range(num_centroids):
        cluster_points = []
    
        for i in range(len(data)):
            if assignments[i] == cluster_index:
                
                cluster_points.append(data[i])
        
        cluster_sum = 0
        for point in cluster_points:
            cluster_sum = cluster_sum + point
        
        cluster_mean = cluster_sum / len(cluster_points)
        
        new_centroids.append(cluster_mean)
    
    return new_centroids


def check_convergence(previous_assignments, current_assignments):
    is_same = True
    
    for i in range(len(current_assignments)):
        if current_assignments[i] != previous_assignments[i]:
            is_same = False
            break
    
    return is_same





# function no. 6: save data to csv
import csv


def save_data_to_csv(data, filename=f"data_points.csv"):
    
    # open the file for writing
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(["index", "value"])
    
    # write each data point
    for i in range(len(data)):
        writer.writerow([i + 1, data[i]])
    
    file.close()
    print("Data points saved to", filename)


def save_initial_centroids_to_csv(centroids, filename=f"initial_centroids.csv"):
    
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(["centroid_index", "value"])
    
    # write each centroid
    for i in range(len(centroids)):
        writer.writerow([i + 1, centroids[i]])
    
    file.close()
    print("Initial centroids saved to", filename)


def save_centroids_per_iteration_to_csv(centroids_history, filename=f"centroids_per_iteration.csv"):
    
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(["iteration", "centroid_1", "centroid_2", "centroid_3", "centroid_4", "centroid_5"])
    
    # write each iteration's centroids
    for i in range(len(centroids_history)):
        row = [i + 1] + centroids_history[i]
        writer.writerow(row)
    
    file.close()
    print("Centroids per iteration saved to", filename)


def save_final_results_to_csv(data, final_assignments, final_centroids, filename=f"final_results.csv"):
    
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(["index", "value", "cluster", "final_centroid"])
    
    # write each data point with its cluster assignment and final centroid
    for i in range(len(data)):
        cluster_index = final_assignments[i]
        centroid_value = final_centroids[cluster_index]
        writer.writerow([i + 1, data[i], cluster_index + 1, centroid_value])
    
    file.close()
    print("Final results saved to", filename)
    
    

# for data vis
def plot_points_per_cluster(final_assignments, num_centroids, folder="results"):

    # count how many points are in each cluster
    cluster_counts = []

    for cluster_index in range(num_centroids):

        count = 0

        for assignment in final_assignments:
            if assignment == cluster_index:
                count = count + 1

        cluster_counts.append(count)

    # create the labels for each cluster
    cluster_labels = []
    for i in range(num_centroids):
        cluster_labels.append("Cluster " + str(i + 1))

    # create the bar graph
    plt.figure(figsize=(8, 5))
    colors = ["steelblue", "coral", "mediumseagreen", "mediumpurple", "sandybrown"]
    plt.bar(cluster_labels, cluster_counts, color=colors)

    # add labels and title
    plt.title("Number of Data Points per Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Number of Points")

    # add the count value on top of each bar
    for i in range(len(cluster_counts)):
        plt.text(i, cluster_counts[i] + 1, str(cluster_counts[i]), ha="center")

    # save the graph to the results folder
    filename = folder + "/points_per_cluster.png"
    plt.savefig(filename)
    plt.close()
    print("Graph saved to", filename)

