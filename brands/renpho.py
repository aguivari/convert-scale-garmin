from datetime import datetime
from utils import get_physique_rating
import pandas as pd

def convert_to_utc_datetime(date_str, time_str):
    clean_date = date_str.strip().replace('-','/')
    dt_local = datetime.strptime(f"{clean_date} {time_str.strip()}", "%d/%m/%Y %H:%M:%S")
    return dt_local

def process_row(row,gender):
    date = convert_to_utc_datetime(row['Date'], row['Time'])
    fat = float(row['Body Fat(%)'])
    muscle_pct = float(row['Skeletal Muscle(%)'])
        
    data={
        'muscle_pct' : float(row['Skeletal Muscle(%)']),
        'timestamp': date,
        'weight': int(float(row['Weight(kg)']) * 100),
        'percent_fat': float(row['Body Fat(%)']),
        'percent_hydration': float(row['Body Water(%)']),
        'visceral_fat_rating': int(float(row['Visceral Fat'])),
        'muscle_mass': float(row['Muscle Mass(kg)']),
        'bone_mass': float(row['Bone Mass(kg)']),
        'metabolic_age': int(float(row['Metabolic Age'])),
        'bmi': float(row['BMI'])
    }
    p_rating = row['Body Type']
    if p_rating == '--' or pd.isna(p_rating):
        p_rating = get_physique_rating(fat, muscle_pct, gender)
    data['physique_rating'] = p_rating
    
    return data