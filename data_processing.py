import pandas as pd

def load_and_rename_clinical_data(filepath='brca_metabric_clinical_data.csv'):
    clinical_data = pd.read_csv(filepath)
    clinical_data.rename(columns={
        'Overall Survival (Months)': 'OS_MONTHS',
        'Overall Survival Status': 'OS_STATUS',
        'Pam50 + Claudin-low subtype': 'CLAUDIN_SUBTYPE'
    }, inplace=True)
    return clinical_data

def load_and_rename_nsd1_data(filepath='NSD1_mRNA_expression.csv'):
    nsd1_data = pd.read_csv(filepath)
    nsd1_data.rename(columns={
        'Sample ID': 'Sample_ID',
        'NSD1: mRNA expression z-scores relative to all samples (log microarray)': 'NSD1'
    }, inplace=True)
    return nsd1_data

def merge_data(clinical_data, nsd1_data):
    merged_data = pd.merge(clinical_data, nsd1_data, left_on='Sample ID', right_on='Sample_ID')
    return merged_data

def save_data(data, filepath='merged_clinical_nsd1_data.csv'):
    data.to_csv(filepath, index=False)

def clean_data(data):
    cleaned_data = data.dropna(subset=['OS_MONTHS', 'OS_STATUS', 'CLAUDIN_SUBTYPE', 'NSD1'])
    return cleaned_data

# Main function to process the data
def main():
    clinical_data = load_and_rename_clinical_data()
    nsd1_data = load_and_rename_nsd1_data()
    merged_data = merge_data(clinical_data, nsd1_data)
    cleaned_data = clean_data(merged_data)
    save_data(cleaned_data, 'cleaned_clinical_nsd1_data.csv')
    print("Cleaned data saved to 'cleaned_clinical_nsd1_data.csv'")

if __name__ == "__main__":
    main()
