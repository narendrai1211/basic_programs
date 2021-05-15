import pandas as pd


def task2():
    df = pd.read_csv('~/Desktop/employee__1_.csv')
    print(df.columns)

    final_df = df[df['Emp ID'] == 499687]
    final_df['First Name'] = 'Narendra'

    df['Emp ID'].loc[499687, 'First Name'] = 'Narendra'
    print(df.head(8))

    final_df_ = pd.concat([df, final_df], ignore_index=True)
    print(final_df_.columns)

    final_df_.drop_duplicates(subset=['Emp ID'], keep='last', inplace=True)
    print(final_df_.tail(8))

    final_df_.to_csv('output_assignment.csv',
                     index=False)

