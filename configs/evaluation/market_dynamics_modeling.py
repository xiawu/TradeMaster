task_name = "algorithmic_trading"
dataset_name = "BTC"


_base_ = [
    f"../_base_/market_dynamics_model/{task_name}/{dataset_name}/mdm.py",
]

market_dynamics_model = dict(
    type='Linear_Market_Dynamics_Model',
    data_path="data/algorithmic_trading/BTC/test.csv",
filter_strength=1,
slope_interval=[-0.15,0.15],
dynamic_number=5,
max_length_expectation=100,
OE_BTC=False,
PM='',
process_datafile_path='',
market_dynamic_labeling_visualization_paths='',
key_indicator='adjcp',
timestamp='date',
tic='tic',
labeling_method='quantile',
min_length_limit=24,
merging_metric='DTW_distance',
merging_threshold=0.005,
merging_dynamic_constraint=1
)