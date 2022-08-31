The tripadvisor repository is part of the research 'Quality review classification for the hospitality industry'

!The ganbert_without_recent_review_git in step 3 is run with help of the Google Colab progarm!

To run the GAN-BERT model the code has to be run in the following order:

1. Run the tripadvisor scraper in the ta_scraper file
  Run scraper is shell with following command:
  - scrapy crawl tripadvisor_spider -o example.csv (in experiment the dataset is ta_10juni.csv)

2. Import the scraped csv file in the ta_clean file
  - Import example.csv (in experiment dataset ta_10juni.csv is imported)
  - Run All
  - Export to 3 datasets, a labeled, test and unlabelled dataset in last cell under the text 'Export labeled, test and unlabeled dataset'. For example labeled_example.csv, test_axample.csv and unlabeled_example.csv.
  
3. Import the cleaned dataset in the ganbert_without_recent_review_git file
  - Import the cleaned datasets in the cell where pandas is imported (under the input parameters). The labeled dataset has to be imported in the df_lab, the unlabeled dataset in the df_unlab and the test dataset in the df_test.
  - If other labels are used for quality they have to be changed in the cell with label_list
  - The following step is the connect the notebook with the Google Colab program which can be done by inserting the host location of the server behind the '!echo $XRT_TPU_CONFIG' codes.
  - Now the code is ready to run and the results can be seen in the cell with 'print(classification_report(all_labels_ids, all_preds))'.

Finshed!
