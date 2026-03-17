# Activity 
# 
# Create a code in Python that creates a random list of 300 integers
# between 1 and 100,000 and create five (5) clusters using k-means
# clustering using 5 random centroids. Stop the clustering process
# when no changes in the clustering happened for 2 consecutive
# iterations, or after 40 iterations whichever comes first.

# Import functions from functions file

import functions
import functions2

# Step 1: Generate the data (300 random integers between 1 and 100,000)
data = functions2.load_data_from_csv("data/data_points.csv")

# Step 2: Initialize the centroids randomly
centroids = functions2.load_initial_centroids_from_csv("data/initial_centroids.csv")

functions.save_data_to_csv(data, "results/data_points.csv")
functions.save_initial_centroids_to_csv(centroids, "results/initial_centroids.csv")

# for testing
# print ("Data points loaded from CSV:", data[:10])  # Print first 10 data points
# print ("Initial centroids loaded from CSV:", centroids)  # Print initial centroids




# Step 3: Assign each point to the nearest centroid for the first time
current_assignments = functions.assign_clusters(data, centroids)

no_change_count = 0
max_iterations = 40
previous_assignments = []
centroids_history = []

print("Starting K-Means Clustering...")
print("Initial Centroids:", centroids)
print()

# Step 4: Iteratively recompute centroids and reassign clusters until convergence or max iterations
for iteration in range(1, max_iterations + 1):
    
    print("Iteration:", iteration)
    centroids = functions.recompute_centroids(data, current_assignments, 5)
    centroids_history.append(centroids)
    
    
    print("Updated Centroids:", centroids)
    
    previous_assignments = current_assignments
    
    current_assignments = functions.assign_clusters(data, centroids)
    
    is_same = functions.check_convergence(previous_assignments, current_assignments)
    
    if is_same:
        no_change_count = no_change_count + 1
        print("No change detected. Consecutive no-change count:", no_change_count)
    else:
        no_change_count = 0
        print("Change detected. Resetting no-change count to 0")
    
    print()
    
    if no_change_count == 2:
        print("Stopped early: No changes for 2 consecutive iterations at iteration", iteration)
        break

else:
    print("Stopped: Reached maximum iterations of", max_iterations)

print()
print("Final Centroids:", centroids)



functions.save_centroids_per_iteration_to_csv(centroids_history, "results/centroids_per_iteration.csv")
functions.save_final_results_to_csv(data, current_assignments, centroids, "results/final_results.csv")
functions.plot_points_per_cluster(current_assignments, 5)