import pandas as pd
import csv

df = pd.read_csv('/Users/tuannguyen/Downloads/Project-1---COMP4010/data/owid-energy.csv')

vietnam_data = df[(df['country'] == 'Vietnam') & (df['year'].between(1985, 2021))][['year', 'fossil_electricity', 'renewables_electricity']]
vietnam_data = vietnam_data.fillna('---').replace(0, '---')

# Calculate global averages excluding Vietnam from 1985 onwards
global_data = df[(df['country'] != 'Vietnam') & (df['year'] >= 1985)]
global_averages = global_data.groupby('year')[['fossil_electricity', 'renewables_electricity']].mean().reset_index()

# Merge and calculate total electricity
merged_data = vietnam_data.merge(global_averages, on='year', suffixes=('_vietnam', '_global'))
merged_data['total_electricity'] = merged_data[['fossil_electricity_vietnam', 'renewables_electricity_vietnam', 'fossil_electricity_global', 'renewables_electricity_global']].apply(lambda x: sum([float(y) for y in x if y != '---']), axis=1)

# Format function to ensure numeric values have three decimal places
def format_value(value):
    if value == '---':
        return value
    else:
        formatted_value = f"{float(value):.3f}"
        return f'"{formatted_value}"'

# Apply formatting
for col in merged_data.columns:
    if col not in ['year', 'fossil_electricity_vietnam', 'renewables_electricity_vietnam']:
        merged_data[col] = merged_data[col].apply(format_value)

# Transpose the DataFrame for desired format
formatted_data = merged_data.set_index('year').T
formatted_data = formatted_data.loc[['total_electricity', 'fossil_electricity_vietnam', 'renewables_electricity_vietnam', 'fossil_electricity_global', 'renewables_electricity_global']]
formatted_data = formatted_data[sorted(formatted_data.columns, reverse=True)]

# Save to TSV without automatic quoting
output_path = '/path/to/save/electricity_data_vietnam_global.tsv'
formatted_data.to_csv(output_path, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\\')

print("File saved:", output_path)
