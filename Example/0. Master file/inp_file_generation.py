import os
import pandas as pd

os.chdir('D:/Git_projects/Abaqus_automation/Test file/')

df = pd.read_csv('data.csv', header=None)

i_values = range(5)
j = 1

# Loop through the indices and assign values to E1 and E2
for i in i_values:
    E1 = df.iloc[i, j]
    E2 = df.iloc[i, j + 1]

    print(E1, E2)
    sentence = (str(E1) + ", " + str(E2) + "\n"
    )
    print(sentence)

    with open('master_file.inp', 'r', encoding='utf-8') as file:
        data = file.readlines()

    # Search for 'Material-1' and check the following line for '*Elastic'. Note: Its case senitive
    for index, line in enumerate(data):
        if "Material-1" in line and index < len(data) - 1:
            next_line = data[index + 1]
            if "*Elastic" in next_line:
                # Replace the line after '*Elastic' with the new sentence
                data[index + 2] = sentence
                break

    # Construct the output filename based on the i_values variable
    filename = f'model_{i}.inp'

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(data)
