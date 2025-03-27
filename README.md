# Polar-lows-project
The repository with the models for detecting polar lows and forecasting their trajectory

The folowing repository has files for the project of detecting and forecasting the trajectories of the polar lows. There are 6 files that contain following information:
- **Polar_LOW_LSTM_approach.ipynb** file has the proposed LSTM based models for polar lows' trajectory prediction
- **Transformer_models.ipynb** includes 2 transformer based models (attention-based and convolution + attention mixup models) for polar lows' trajectory prediction
- **split_set_edit.py** has tools for splitting and labeling the manually acquired data from the "EddyClicker" framework
- **Polar_LOW_GRU.ipynb** file has the proposed GRU based model for forecasting the trajectory of the polar lows
- **labeled_data_with_splits.csv** file has coordinates of the eye of the vortex (polar low) and 3 supplementary points of the ellipsis marking th polar low area
- **** file has the DL models for classification algorithm to identify polar lows.

The models were developed as part of the final project for the ML course in Skoltech. 
Authors of the project are: Anastasia Yagnych, Bogdan Monogov, Dominique Watt, Fathma BintayIslam, Hamza Said
