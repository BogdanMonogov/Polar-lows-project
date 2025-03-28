# Polar-lows-project
The repository with the models for detecting polar lows and forecasting their trajectory. Following models allow the user to manually mark, identify and set coordinates of the polar lows, identify the polar low with the help of the CNNs and try to forecast the trajectory of the polar low based on the full history (LSTM, GRU) or on the part of it (Transformer based models). 

The folowing repository has files for the project of detecting and forecasting the trajectories of the polar lows. There are 6 files that contain following information:
- **Polar_LOW_LSTM_approach.ipynb** file has the proposed LSTM based models for polar lows' trajectory prediction. The main metrics for evaluating the perfomance of the model are MSE and MAE alongside the visual analysis of the restored trajectory. 
- **Transformer_models.ipynb** includes 2 transformer based models (attention-based and convolution + attention mixup models) for polar lows' trajectory prediction. The main metrics for the evaluation of the transofrmer models are MAE, MSE losses as well as introduced in the work Haversine loss alongside the visual comparison of the predicted vs real trajectories. 
- **split_set_edit.py** has tools for splitting and labeling the manually acquired data from the "EddyClicker" framework to acquire the coordinates of the polar lows as well as their labeling. 
- **Polar_LOW_GRU.ipynb** file has the proposed GRU based model for forecasting the trajectory of the polar lows. The main metrics for evaluating the perfomance of the model are MSE and MAE alongside the visual analysis of the restored trajectory. 
- **labeled_data_with_splits.csv** file has coordinates of the eye of the vortex (polar low) and 3 supplementary points of the ellipsis marking th polar low area
- **Feature_Selection_CNN** file has the CNN architecture models for binary classification of the polar lows. The performance of the CNN classifier is evaluated by the set of metrics: precision, recall, F1-score, ROC-AUC and others. 

The models were developed as part of the final project for the ML course in Skoltech. 
Authors of the project are: Anastasia Yagnych, Bogdan Monogov, Dominique Watt, Fathma BintayIslam, Hamza Said
