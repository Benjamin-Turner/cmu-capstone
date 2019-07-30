import os
import glob

# Parent directories
model_dir = 'model'
data_dir = 'data'
output_dir = 'output'

# Child directories
data_extracted_dir = os.path.join(data_dir, 'extracted')
data_delivery_prediction_dir = os.path.join(data_dir, 'delivery_prediction')
data_benchmarking_dir = os.path.join(data_dir, 'benchmarking')

data_delivery_prediction_preprocessed_dir = os.path.join(data_delivery_prediction_dir, 'preprocessed')
data_delivery_prediction_features_dir = os.path.join(data_delivery_prediction_dir, 'features')
data_delivery_prediction_external_dir = os.path.join(data_delivery_prediction_dir, 'external')
data_delivery_prediction_data_dict_dir = os.path.join(data_delivery_prediction_dir, 'data_dict')
data_delivery_prediction_input_dir = os.path.join(data_delivery_prediction_dir, 'input')
data_benchmarking_preprocessed_dir = os.path.join(data_benchmarking_dir, 'benchmarking')
data_benchmarking_input_dir = os.path.join(data_benchmarking_dir, 'input')

output_delivery_prediction_dir = os.path.join(output_dir, 'delivery_prediction')
output_benchmarking_dir = os.path.join(output_dir, 'benchmarking')

model_scaler_dir = os.path.join(model_dir, 'scaler')

# Static file names
data_delivery_prediction_preprocessed_dir_cmu = os.path.join(data_delivery_prediction_preprocessed_dir, 'delivery_prediction_data_preprocessed_cmu.pkl.z')
data_delivery_prediction_features_dir_cmu = os.path.join(data_delivery_prediction_features_dir, 'feature_names_cmu.npz')
data_delivery_prediction_msa_dir_cmu = os.path.join(data_delivery_prediction_external_dir, 'zip_to_msa_numbers_cmu.csv')
data_delivery_prediction_data_dict_dir_cmu = os.path.join(data_delivery_prediction_data_dict_dir, 'delivery_prediction_data_dict_cmu.npz')

model_cmu = os.path.join(model_dir, 'model_cmu.pkl.z')
scaler_cmu = os.path.join(model_scaler_dir, 'scaler_cmu.pkl.z')

# Unit test cases
if __name__ == '__main__':
    print("data_delivery_prediction_data_dict_dir: ", data_delivery_prediction_data_dict_dir)
    print("data_benchmarking_preprocessed_dir: ", data_benchmarking_preprocessed_dir)
    # Test loading file
    import numpy as np
    data_dict_files = []
    for name in glob.glob(data_delivery_prediction_data_dict_dir+'/*'):
        print(name)
        data_dict_files.append(name)
    data_dict = np.load(data_dict_files[0])
    print(data_dict['y_test'].shape)