import pandas as pd
import knn
import save

# Read from a file
df = pd.read_csv("iris.csv", header=None)

while(True):
    # Separate dataframe to data and labels
    data = df.drop(4, axis=1)
    labels = df.iloc[:, [4]]
    # Get new input
    input_list = list()
    print("Įveskite naujus duomenis (4): \n")
    # Iterate the inputs
    for i in range(0,4):
        ele = float(input())
        input_list.append(ele)
        
    print("Įvesti duomenys: ", input_list)
    start = input("Pradėti klasifikavimą?[T/N]: ")
    if start=="T":
        k = int(input("Įveskite k: "))
        _metric = input("Pasirinkite metriką:\n" +
        "Galimos metrikos:\n"+
        "- euclidean\n- manhattan\n")
        prediction = knn.knn(input_list, data, labels, k, metric=_metric)
        input_list.append(prediction)

        print("Klasė: " + prediction)
        print(input_list)
    elif start=="N":
        continue

    save_input = input("Saugoti naujus duomenis?[T/N]: ")
    if save_input=="T":
        updated_df = save.add_new_data_to_dataframe(df, input_list)
        # To further use dataframe with saved data 
        df = updated_df
        print(df)
    elif save_input=="N":
        print("Duomenys neišsaugoti")
        continue

    save_file = input("Saugoti duomenis faile?[T/N]: ")
    if save_file=="T":
        save.save_to_file(df)
        print("Išsaugota faile")
    elif save_file=="N":
        print("Duomenys neišsaugoti faile")
        continue

    