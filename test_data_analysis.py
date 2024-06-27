import pytest
import pandas as pd
from data_analysis import (
    load_data, ensure_columns_present, convert_os_status,
    create_expression_groups, run_gsea, plot_kaplan_meier
)

def test_load_data():
    data = load_data('cleaned_clinical_nsd1_data.csv')
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_ensure_columns_present():
    data = pd.DataFrame({
        'OS_MONTHS': [1, 2, 3],
        'OS_STATUS': ['1:DECEASED', '0:LIVING', '1:DECEASED'],
        'CLAUDIN_SUBTYPE': ['LumA', 'LumB', 'Basal'],
        'NSD1': [0.5, 0.3, 0.8]
    })
    required_columns = ['OS_MONTHS', 'OS_STATUS', 'CLAUDIN_SUBTYPE', 'NSD1']
    ensure_columns_present(data, required_columns)

def test_convert_os_status():
    data = pd.DataFrame({
        'OS_MONTHS': [1, 2, 3],
        'OS_STATUS': ['1:DECEASED', '0:LIVING', '1:DECEASED']
    })
    data = convert_os_status(data)
    assert 'event' in data.columns
    assert data['event'].tolist() == [1, 0, 1]

def test_create_expression_groups():
    data = pd.DataFrame({
        'NSD1': [0.1, 0.5, 0.8, 0.3, 0.7, 0.6]
    })
    data = create_expression_groups(data, 'NSD1')
    assert 'high_expression' in data.columns
    assert 'low_expression' in data.columns
    assert data['high_expression'].sum() == 2
    assert data['low_expression'].sum() == 2

def test_run_gsea():
    data = pd.DataFrame({
        'Gene': ['GeneA', 'GeneB', 'GeneC'],
        'Log2 Ratio': [1.5, -1.0, 0.5]
    })
    gsea_filepath = '_NSD1_high_vs_low_quartiles.xlsx'
    gene_set_filepath = 'h.all.v2023.2.Hs.symbols.gmt'
    gsea_results = run_gsea(data, gsea_filepath, gene_set_filepath, 'LumA')
    assert gsea_results is not None
    assert hasattr(gsea_results, 'res2d')
    assert 'Term' in gsea_results.res2d.columns

def test_plot_kaplan_meier():
    data = pd.DataFrame({
        'OS_MONTHS': [10, 20, 30, 40, 50, 60],
        'OS_STATUS': ['1:DECEASED', '0:LIVING', '1:DECEASED', '0:LIVING', '1:DECEASED', '0:LIVING'],
        'CLAUDIN_SUBTYPE': ['LumA', 'LumA', 'LumA', 'LumA', 'LumA', 'LumA'],
        'NSD1': [0.1, 0.5, 0.8, 0.3, 0.7, 0.6]
    })
    data = convert_os_status(data)
    data = create_expression_groups(data, 'NSD1')
    data = data[data['CLAUDIN_SUBTYPE'] == 'LumA']
    gsea_filepath = '_NSD1_high_vs_low_quartiles.xlsx'
    gene_set_filepath = 'h.all.v2023.2.Hs.symbols.gmt'
    
    import matplotlib
    matplotlib.use('Agg')  # Use a non-interactive backend to avoid displaying the plot during tests
    
    plot_kaplan_meier(data, 'NSD1', gsea_filepath, gene_set_filepath, 'LumA')

if __name__ == '__main__':
    pytest.main()
