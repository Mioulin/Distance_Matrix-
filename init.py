import nibabel as nib
from nilearn.input_data import NiftiLabelsMasker

atlas_file = nib.load('/Users/mioulin/nilearn_data/schaefer_2018/Schaefer2018_100Parcels_7Networks_order_FSLMNI152_2mm.nii.gz')

with open('/Users/mioulin/nilearn_data/schaefer_2018/Schaefer2018_100Parcels_7Networks_order.txt', 'r') as f:
    labels = f.read().split('\n')
masker = NiftiLabelsMasker(labels_img=atlas_file, standardize=True, verbose=1,
                           memory="nilearn_cache", memory_level=2)
labels = [x.split('\t')[1][10:] for x in labels]

rest_files = ['/Users/mioulin/Desktop/pybrain/DMT/data/Mins8/DMT/DMT_post1/S01/DMT_post1_rdsmffms6FWHM_bd_M_V_DV_WMlocal2_modecorr.nii.gz']
