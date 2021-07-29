import pandas as pd
from init import *
from nilearn.connectome import ConnectivityMeasure

def get_corr_matrix(file_name):
    time_series = pd.DataFrame(masker.fit_transform(file_name), columns=labels)
    correlation_measure = ConnectivityMeasure(kind='correlation')
    correlation_matrix = correlation_measure.fit_transform([time_series.values])[0]
    return pd.DataFrame(correlation_matrix, index=labels, columns=labels)