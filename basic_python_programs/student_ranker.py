import pandas as pd


def analyze_csv(df):
    f = df.sort_values('marks', ascending=False)
    print(f.columns)

    top_5 = f.head()['name'].to_list()
    print(top_5)

    least_5_records = f.tail()
    final_least = least_5_records.sort_values('marks', ascending=True)['name'].to_list()
    print(final_least)

    iqr_df = df[df['iqr_marks'] == True]

    has_iqr_score = iqr_df['name'].to_list()
    print(has_iqr_score)

    return top_5, final_least, has_iqr_score


if __name__ == '__main__':
    df_ = pd.read_csv('student_mark_sheets.csv')
    analyze_csv(df_)
