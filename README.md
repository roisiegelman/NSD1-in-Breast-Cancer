# Elucidating the role of NSD1  in breast cancer heterogeneity progression

###  introduction
Breast cancer is one of the world's most common types of cancer. It is an aggressive, highly heterogeneous disease caused by mammary epithelial cell changes driven by genetic and epigenetic alterations. Reversible epigenetic regulation promotes breast cancer heterogeneity between and within tumors' cells by enabling cellular plasticity. 

On a molecular level, tumors can be classified into subtypes based on a combination of histopathology of the primary tumor and the expression pattern of hormones estrogen receptor (ER), progesterone receptor (PR), and human epidermal growth factor receptor 2 (HER2). The proliferative capacity of the tumor cells, as measured by the Ki67 marker, also contributes to tumor classification. Recent technological advances also implemented genomic and transcriptomic profiling for classification6. Of the five main breast cancer subtypes, Luminal A and B express hormone receptors. Luminal A displays low Ki67 and is HER2 negative, whereas luminal B tumors express high levels of Ki67 and can be either HER2 positive or negative. Normal-like tumors express hormone receptors but not HER2 and Ki67, as well as additional genomic and transcriptomic profiling6. HER2 positive, as its name applies, expresses amplified HER2 but not hormone receptors. Finally, basal-like breast cancer (by and large overlapping with triple-negative breast cancer, TNBC) is defined by a lack of expression of hormonal receptors and HER2<sup>2</sup>.
![image](https://github.com/roisiegelman/Project/assets/166688546/e3e723d3-6f10-4aa7-87ad-461efc3558ea)

Our understanding of the relationship between histone post-translational modifications (PTMs) and the capacity of mammary tumor cells to develope is limited. In this project, relying on recent findings, I will explore the role of a specific histone modification, H3K36me2, and its central modulator, NSD1, in promoting breast cancer and the difference between the different subtypes.![image](https://github.com/roisiegelman/Project/assets/166688546/898795ce-b799-4cec-89cc-2ca37f4a3c0b)

Nuclear receptor binding SET domain (NSD) proteins consist of NSD1, NSD2, and NSD3. These proteins participate in the regulation of tumor initiation and progression. However, the biological functions of NSD family  in BC progression remain unclear. 
Here, I propose to explore the underlying mechanisms and biological functions of NSD1 in BC progression. We formulated a hypothesis that NSD1 would strengthen BC cell drug resistance and lead to poor prognosis in patients with BC.

###  main goals

1.  explore the effect of NSD1 gene expression on the overall survival of BC patients with different subtypes (Luminal A, Luminal B and Basal-like)
  
2. Investigate the cellular pathways affected by NSD1 levels within patients with different subtypes (Luminal A, Luminal B and Basal-like)   

###  Technical steps:
1.  **Export data from [cBioPrtal](https://www.cbioportal.org/)**
    * Choose a database according to the cancer type. In this project, I investigated the data from [METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric)
    * Download clinical data and expression levels of the gene of choice. I chose *NSD1*
    * Download survival and mRNA expression data for groups with different expression levels of the gene of interest for each subtype separately. One might opt to compare data using either the median or quartiles. 
      I chose to compare the *bottom and the top quartiles of the expression of NSD1 and compare Luminal A (LumA), Luminal B(LumB) and Basal-like (Basal)*
2.  **Coordinate the loading, merging, cleaning, and saving of the data by** 
   * Execute the script `data_processing.py`
    ```
python _data_processing.py
```
   * The script will yield `cleaned_clinical_nsd1_data.csv` that will be used in the next part
   * Detailed explanations and requirements can be found in [`data_processing_explained.md`](https://github.com/roisiegelman/Project/blob/main/data_processing_explained.md)
   * Testing the script:
   ```
pytest test_data_processing.py
```

```
git clone ...
git status
git add
git commit -m "some explanation"
git push
```
This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04) at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/).
