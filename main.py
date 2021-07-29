import os
from init import *
from func import *
from distance_FC import *
base_dir = '/Users/mioulin/Desktop/pybrain/DMT/data/Mins8'
corr_matrices = {}
for folder in [x for x in os.listdir(f'{base_dir}/DMT/DMT_post1') if x[0] != '.'][:2]:
    corr_matrices[folder] = {
        'FCDMT': get_corr_matrix(f'{base_dir}/DMT/DMT_post1/{folder}/DMT_post1_rdsmffms6FWHM_bd_M_V_DV_WMlocal2_modecorr.nii.gz'),
        'FCPCB': get_corr_matrix(f'{base_dir}/PCB/PCB_post1/{folder}/PCB_post1_rdsmffms6FWHM_bd_M_V_DV_WMlocal2_modecorr.nii.gz'),
    }
df = pd.DataFrame()
for indv in corr_matrices.keys():
    dist = distance_FC(corr_matrices[indv]['FCDMT'], corr_matrices[indv]['FCPCB'])
    pears = dist.pearson()
    geodes = dist.geodesic()
    df = df.append([{'Individual': indv, 'Type': 'Geodesic', 'Distance': geodes},
                    {'Individual': indv, 'Type': 'Correlation', 'Distance': pears}], ignore_index=True)
df.to_csv('FC_analysis_test.csv')