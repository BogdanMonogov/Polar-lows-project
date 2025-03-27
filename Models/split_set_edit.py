import pandas as pd
from sklearn.model_selection import train_test_split


polar_df = pd.read_csv(r"C:\Users\wattd\OneDrive\Desktop\EddyClicker-main\mature_events_fixed.csv.csv")
polar_df['label'] = 1 
non_df = pd.read_csv(r"C:\Users\wattd\OneDrive\Desktop\EddyClicker-main\non_events_fixed.csv.csv")
non_df['label'] = 0  
full_df = pd.concat([polar_df, non_df]).reset_index(drop=True)

polar_events = polar_df['event_id'].unique()
non_events = non_df['event_id'].unique()


polar_train_ids, polar_temp_ids = train_test_split(polar_events, test_size=0.2, random_state=42)
polar_val_ids, polar_test_ids = train_test_split(polar_temp_ids, test_size=0.5, random_state=42)

non_train_ids, non_temp_ids = train_test_split(non_events, test_size=0.2, random_state=42)
non_val_ids, non_test_ids = train_test_split(non_temp_ids, test_size=0.5, random_state=42)

def assign_split(row):
    if row['event_id'] in polar_train_ids or row['event_id'] in non_train_ids:
        return 'train'
    elif row['event_id'] in polar_val_ids or row['event_id'] in non_val_ids:
        return 'val'
    elif row['event_id'] in polar_test_ids or row['event_id'] in non_test_ids:
        return 'test'

full_df['split'] = full_df.apply(assign_split, axis=1)


print(full_df.groupby(['split', 'label']).size())


full_df.to_csv('labeled_data_with_splits.csv', index=False)
