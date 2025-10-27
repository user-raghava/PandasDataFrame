import pandas as pd
my_data = {
    'cars': ['XC90', 'Mustang'],
    'types': ['SUV', 'Sedan']
}
cars_df = pd.DataFrame(my_data)
cars_df.to_csv('cars.csv', index=False)
print(cars_df)

# Reading the CSV file back into a DataFrame
cars_df_from_file = pd.read_csv('cars.csv')
print(cars_df_from_file)

# Accessing the 'cars' column
print(cars_df_from_file['cars'])


