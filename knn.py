import metrics
import pandas as pd

def knn(new_data, data, labels, k, metric="euclidean"):
    # Get distances to new data
    distances = get_distances(data, new_data, metric)
    # Make a dataframe of distances
    df_dists = pd.DataFrame(data=distances, index=data.index, columns=['dist'])
    # Add labels to the distances for further classification
    df_dists['labels'] = labels
    # Get k shortest distances
    df_nn = df_dists.sort_values(by=['dist'], axis=0)[:k]
    predictions = df_nn["labels"].mode()
    # If there are more than one option for prediction, it outputs "unknown"
    if(len(predictions)==1):
        prediction = df_nn['labels'].mode().values[0]
    else:
        prediction = "Nežinoma"
    return prediction

def get_distances(train_data, test_data, metric="euclidean"):
    distances = []

    # Calculate distances based on which metric is chosen
    # Throw an error in case the metric is input incorrectly
    # This stops the program from giving a prediction without using metrics
    if (metric == "euclidean"):
        for i in train_data.index:
            distances.append(metrics.euclidean_distance(train_data.iloc[i], test_data))
    elif (metric == "manhattan"):
        for i in train_data.index:
            distances.append(metrics.manhattan_distance(train_data.iloc[i], test_data))
    else:
        raise Exception("Nežinoma metrika\n galimos:\n- euclidean\n- manhattan")

    return distances