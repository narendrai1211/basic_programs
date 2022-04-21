import pandas as pd


def cell_value_check():
  # change a cell value based on another cell value
  df = pd.DataFrame({'id': [1,2,3], 'university': ['Bangalore', 'Pune', 'Punjab']})
  print(df)
  df.loc[df['id'] == 1, 'university'] = 'Bangalore University' 
  return df


if __name__ == '__main__':
  print(cell_value_check())
