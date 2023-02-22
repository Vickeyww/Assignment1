import pandas as pd
def clean(input_file1,input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = pd.merge(df1,df2, left_on="respondent_id", right_on="id")
    #drop
    df = df.dropna()
    df = df[~df["job"].str.contains('Insurance|insurance')]
    df = df.drop(labels='id', axis=1)
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Data file (CSV)')
    parser.add_argument('other_info_file', help='Data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file,args.other_info_file)
    print("The shape of new data: ", cleaned.shape)
    cleaned.to_csv(args.output, index=False)