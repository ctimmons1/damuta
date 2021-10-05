# script to create clinical_ann_merged.csv
import pandas as pd

donor_clinical = pd.read_csv('data/pcawg_donor_clinical_August2016_v9.csv')
icgc_annotations = pd.read_csv('data/icgc_sample_annotations_summary_table.txt', sep = '\t')
pcawg_annotations = pd.read_csv('data/pcawg_supplement_table1.csv')

clinical_ann = icgc_annotations.rename(columns = {'tumour_aliquot_id':'tumour_specimen_aliquot_id'})
clinical_ann = clinical_ann.merge(pcawg_annotations, how = 'left', on= ['tumour_specimen_aliquot_id',
                                                                        'histology_abbreviation',
                                                                        'icgc_sample_id',
                                                                        'icgc_donor_id',
                                                                        'tumour_stage',
                                                                        'tumour_grade',
                                                                        'specimen_donor_treatment_type'
                                                                        ])

clinical_ann = clinical_ann.merge(donor_clinical, how = 'left', on  = ['icgc_donor_id', 
                                                                       'project_code', 
                                                                       'donor_wgs_included_excluded',    
                                                                       'donor_unique_id', 
                                                                       'submitted_donor_id', 
                                                                       'tcga_donor_uuid',
                                                                       'donor_survival_time',
                                                                       'donor_age_at_diagnosis',
                                                                       'first_therapy_type',
                                                                       'first_therapy_response',
                                                                       
                                                                      ])

clinical_ann.to_csv('data/clinical_ann_merged.csv')