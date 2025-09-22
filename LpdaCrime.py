
import pandas as pd
df = pd.read_csv(r"C:\Users\bola\Downloads\Crime_Data_from_2020_to_Present.csv")
print(df)

#Exploring the data structure
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.describe())

#clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns)

# Handling missing values 

print(df.isnull().sum())

df = df.fillna({'mocodes':0})

# Assuming negative ages are entry errors, converting to absolute values
df['vict_age'] = df['vict_age'].apply(lambda x: abs(x) if x < 0 else x)


df['vict_sex'] = df['vict_sex'].astype(str).str.strip()

df['vict_sex'] = df['vict_sex'].apply(lambda x:  'Male' if x == 'M' else 'Female' if x == 'F' else 'Unknown')
print(df['vict_sex'])


df['vict_descent'] = df['vict_descent'].apply(lambda x: 'Asian' if x == 'A' else 'Black' if x == 'B'\
else 'Chinese' if x == 'C' else 'Cambodian' if x == 'D' else 'Filipino' if x == 'F' else 'Guamanian' if x == 'G'\
else 'Hispanic' if x == 'H' else 'American Indian' if x == 'I' else 'Japanese' if x == 'J' else 'Korean' if x == 'K'\
else 'Laotian' if x == 'L' else 'Other' if x == 'O' else 'Pacific Islander' if x == 'P'\
else 'Samoan' if x == 'S' else 'Hawaiian' if x == 'U' else 'Vietnamese' if x == 'V'\
else 'White' if x == 'W' else 'Unknown' if x == 'X' else 'Asian Indian' if x == 'Z' else "Unknown")
                                              
print([df.vict_descent]) 

df['premis_cd']=df['premis_cd'].fillna(0)

df['premis_desc'] = df['premis_desc'].fillna('Not described')

df['premis_desc'] = df['premis_desc'].str.title()


df['weapon_used_cd'] = df['weapon_used_cd'].fillna(0)

df['weapon_desc'] = df['weapon_desc'].fillna('Unknown')

df['weapon_desc'] = df['weapon_desc'].str.title()

df['location'] = df['location'].str.strip().str.title()

df['cross_street'] = df['cross_street'].str.strip().str.title()

df['cross_street'] = df['cross_street'].fillna('Unknown')

df['status'] = df['status'].fillna('Unk')

df['date_rptd'] = pd.to_datetime(df['date_rptd'], errors='coerce')

df['crm_cd_1'] = df['crm_cd_1'].fillna(0)

df['crm_cd_2'] = df['crm_cd_2'].fillna(0)

df['crm_cd_3'] = df['crm_cd_3'].fillna(0)

df['crm_cd_4'] = df['crm_cd_4'].fillna(0)

# Assume 'date_rptd' is already datetime
df['date_only'] = df['date_rptd'].dt.normalize()
df['time_only'] = df['date_rptd'].dt.normalize()

df['date_occ'] = pd.to_datetime(df['date_occ'], errors='coerce')

# Assume 'date_occ' is already datetime
df['date'] = df['date_occ'].dt.normalize()
df['time'] = df['date_occ'].dt.normalize()

df['time_occ'] = pd.to_datetime(df['time_occ'], errors='coerce')

df['time1'] = df['time_occ'].dt.normalize()

df['premis_cd'] = df['premis_cd'].astype(int)

df['weapon_used_cd'] =df['weapon_used_cd'].astype(int)



df['crm_cd_1'] =df['crm_cd_1'].astype(int)

df['crm_cd_2'] =df['crm_cd_2'].astype(int)

df['crm_cd_3'] =df['crm_cd_3'].astype(int)

df['crm_cd_4'] =df['crm_cd_4'].astype(int)



df = df.rename({
    'date_only' : 'new_date_rptd',
    'time_only' : 'new_time_rptd',
    'date' : 'new_date_occ',
    'time' : 'new_time_occu'
})

print(df['vict_sex'].value_counts())

df.to_excel('cleaned_data.xlsx')

