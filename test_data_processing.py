import pytest
import pandas as pd
from io import StringIO
from unittest.mock import patch
from data_processing import load_and_rename_clinical_data, load_and_rename_nsd1_data, merge_data, save_data, clean_data

# Mock data
clinical_data_csv = """
Sample ID,Overall Survival (Months),Overall Survival Status,Pam50 + Claudin-low subtype
1,10,1:DECEASED,LumA
2,20,0:LIVING,LumB
3,30,1:DECEASED,Basal
"""

nsd1_data_csv = """
Sample ID,NSD1: mRNA expression z-scores relative to all samples (log microarray)
1,2.5
2,3.5
3,1.5
"""

@pytest.fixture
def clinical_data():
    return pd.read_csv(StringIO(clinical_data_csv))

@pytest.fixture
def nsd1_data():
    return pd.read_csv(StringIO(nsd1_data_csv))

def test_load_and_rename_clinical_data():
    with patch('pandas.read_csv', return_value=pd.read_csv(StringIO(clinical_data_csv))):
        data = load_and_rename_clinical_data()
        assert 'OS_MONTHS' in data.columns
        assert 'OS_STATUS' in data.columns
        assert 'CLAUDIN_SUBTYPE' in data.columns

def test_load_and_rename_nsd1_data():
    with patch('pandas.read_csv', return_value=pd.read_csv(StringIO(nsd1_data_csv))):
        data = load_and_rename_nsd1_data()
        assert 'Sample_ID' in data.columns
        assert 'NSD1' in data.columns

def test_merge_data(clinical_data, nsd1_data):
    # Ensure columns are renamed before merging
    clinical_data.rename(columns={
        'Overall Survival (Months)': 'OS_MONTHS',
        'Overall Survival Status': 'OS_STATUS',
        'Pam50 + Claudin-low subtype': 'CLAUDIN_SUBTYPE'
    }, inplace=True)
    nsd1_data.rename(columns={
        'Sample ID': 'Sample_ID',
        'NSD1: mRNA expression z-scores relative to all samples (log microarray)': 'NSD1'
    }, inplace=True)
    
    merged = merge_data(clinical_data, nsd1_data)
    assert 'OS_MONTHS' in merged.columns
    assert 'OS_STATUS' in merged.columns
    assert 'CLAUDIN_SUBTYPE' in merged.columns
    assert 'NSD1' in merged.columns

def test_clean_data(clinical_data, nsd1_data):
    # Ensure columns are renamed before merging and cleaning
    clinical_data.rename(columns={
        'Overall Survival (Months)': 'OS_MONTHS',
        'Overall Survival Status': 'OS_STATUS',
        'Pam50 + Claudin-low subtype': 'CLAUDIN_SUBTYPE'
    }, inplace=True)
    nsd1_data.rename(columns={
        'Sample ID': 'Sample_ID',
        'NSD1: mRNA expression z-scores relative to all samples (log microarray)': 'NSD1'
    }, inplace=True)
    
    merged = merge_data(clinical_data, nsd1_data)
    cleaned = clean_data(merged)
    assert cleaned.shape[0] == 3  # no rows should be dropped in this case

def test_save_data(monkeypatch, tmpdir):
    filepath = tmpdir.join('output.csv')
    def mock_to_csv(self, path_or_buf, index=True):
        assert path_or_buf == str(filepath)

    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)
    data = pd.read_csv(StringIO(clinical_data_csv))
    save_data(data, filepath)
