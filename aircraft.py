# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:27:56 2023

@author: dinse
"""

import pandas as pd 
df = pd.read_csv("aircraft.csv")
df.head()
df.describe()
df.info()
df.shape
df.dtypes
df.columns
"""
['Record ID', 'Incident Year', 'Incident Month', 'Incident Day',
       'Operator ID', 'Operator', 'Aircraft', 'Aircraft Type', 'Aircraft Make',
       'Aircraft Model', 'Aircraft Mass', 'Engine Make', 'Engine Model',
       'Engines', 'Engine Type', 'Engine1 Position', 'Engine2 Position',
       'Engine3 Position', 'Engine4 Position', 'Airport ID', 'Airport',
       'State', 'FAA Region', 'Warning Issued', 'Flight Phase', 'Visibility',
       'Precipitation', 'Height', 'Speed', 'Distance', 'Species ID',
       'Species Name', 'Species Quantity', 'Flight Impact', 'Fatalities',
       'Injuries', 'Aircraft Damage', 'Radome Strike', 'Radome Damage',
       'Windshield Strike', 'Windshield Damage', 'Nose Strike', 'Nose Damage',
       'Engine1 Strike', 'Engine1 Damage', 'Engine2 Strike', 'Engine2 Damage',
       'Engine3 Strike', 'Engine3 Damage', 'Engine4 Strike', 'Engine4 Damage',
       'Engine Ingested', 'Propeller Strike', 'Propeller Damage',
       'Wing or Rotor Strike', 'Wing or Rotor Damage', 'Fuselage Strike',
       'Fuselage Damage', 'Landing Gear Strike', 'Landing Gear Damage',
       'Tail Strike', 'Tail Damage', 'Lights Strike', 'Lights Damage',
       'Other Strike', 'Other Damage']
"""
df.isnull().sum().sort_values(ascending=False).head(20)
df.columns = df.columns.str.replace(' ', '_')

df.Aircraft_Type.value_counts()
df.Aircraft_Model.value_counts()
df.Engine_Model.value_counts()
df.Engine_Type.value_counts()

df.Injuries.value_counts()

filtered = (df["Aircraft_Type"]=="A") & (df["Engine_Type"]=="D")
df[filtered]

df[df["Aircraft_Type"]=="J"]["Engine_Type"]

df.Speed.sort_values(ascending = False).value_counts()
df.sort_values(by="Speed",ascending = False)[["Engine_Type","Aircraft_Type","Visibility"]].head(10)#Engine_Type=D & Aircraft_Type=A

df[df["Speed"]==2500.0][["Engine_Type","Aircraft_Type"]]
df[df["Speed"]==2500.0]

df.Visibility

df.sort_values(by="Speed",ascending = False)[["Engine1_Position","Engine2_Position","Engine3_Position","Engine4_Position"]].head(10)

df.Engine1_Strike.value_counts()
df[df.Engine1_Strike == 1]["Engine1_Position"].value_counts()#1.0 highest

df.Engine2_Strike.value_counts()
df[df.Engine2_Strike == 1]["Engine2_Position"].value_counts()#1.0

df.Engine3_Strike.value_counts()
df[df.Engine3_Strike == 1]["Engine3_Position"].value_counts()#1

df.Engine4_Strike.value_counts()
df[df.Engine4_Strike == 1]["Engine4_Position"].value_counts()#1.0 lowest

df.Wing_or_Rotor_Strike.value_counts()
df.Species_Quantity
df.Distance.sort_values(ascending = False)
df.iloc[90715]["Speed"]

df.columns
"""
df[df.Species_Name.str.contains("TURKEY")]
df.Species_Name.isnull().sum()
"""
turkey_rows = df[df['Species_Name'].notnull() & df['Species_Name'].str.contains('TURKEY')]
turkey_rows.Species_Name.value_counts()

#fuselage == GÖVDE
#propeller == pervane

df.Propeller_Strike.value_counts()#3497
df.Fuselage_Damage.value_counts()#824
df.Tail_Strike.value_counts()#1956

#içinde strike geçen sütunları barchart şeklinde göster

import matplotlib.pyplot as plt
# "strike" geçen sütunları seç
strike_columns = [col for col in df.columns if 'strike' in col.lower()]

# 1 değerlerini say ve grafikle göster
for col in strike_columns:
    counts = df[col].value_counts()
    counts.plot(kind='bar', title=f'{col} Değerleri', xlabel='Durum', ylabel='Sayı')
    plt.show()
    
"""
strike_columns
df.Other_Strike.value_counts()

df.Tail_Strike.value_counts().plot(kind="bar",title="xaxaxax",xlabel="Situation of Tail",ylabel="Counts")
plt.show()
"""
# "strike" geçen sütunları seç
strike_columns = [col for col in df.columns if 'strike' in col.lower()]

# Tüm "strike" sütunlarının toplamını al
total_strikes = df[strike_columns].sum()

# Bar grafiği oluştur
plt.figure(figsize=(10, 6))
total_strikes.plot(kind='bar', title='Toplam Strike Sayısı', xlabel='Strike', ylabel='Sayı')
plt.show()# "strike" geçen sütunları seç
strike_columns = [col for col in df.columns if 'strike' in col.lower()]

# Tüm "strike" sütunlarının toplamını al
total_strikes = df[strike_columns].sum()

# Bar grafiği oluştur
plt.figure(figsize=(10, 6))
total_strikes.plot(kind='bar', title='Toplam Strike Sayısı', xlabel='Strike', ylabel='Sayı')
plt.show()


df.Windshield_Strike.value_counts()
df.Precipitation.isnull().sum()
df.Precipitation.value_counts() 

plt.figure(figsize=(6,6))
precipitation = df["Precipitation"]
dağılım = precipitation[precipitation != 'NONE']
dağılım1 = dağılım.value_counts()
plt.pie(dağılım1,labels=dağılım1.index,autopct='%1.1f%%', startangle=120)
plt.show()

#%%
# Veri çerçevesinden sadece yağış değerlerini al
precipitation = df["Precipitation"]

# 'NONE' olmayan verileri al
distri = precipitation[precipitation != 'NONE']

# Tekrar eden değerleri say
distri1 = distri.value_counts()

# 1% altında olan değerleri topla
others_threshold = distri1.sum() * 0.01
small_categories = distri1[distri1 < others_threshold]
others_value = small_categories.sum()

# Others kategorisi oluştur
distri1 = distri1[distri1 >= others_threshold]
distri1['Others'] = others_value

# Pasta grafiği çizimi
plt.figure(figsize=(8, 8))
plt.pie(distri1, labels=distri1.index, autopct='%1.1f%%', startangle=120)

# Orta noktayı 'bulutlu' olarak işaretle
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)

# Görsel ayarları
plt.title('Precipitation Distribution')
plt.axis('equal')  

# Renkler ve açıklamaları
colors = plt.cm.tab20.colors[:len(distri1)]
legend_labels = distri1.index
plt.legend(legend_labels, loc="center left", bbox_to_anchor=(1, 0.5), title="Precipitation Type", labelspacing=1.2, facecolor='lightgrey')

plt.show()

#%%MACHINE Learning 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Veri setini yükle
data = pd.read_csv("aircraft.csv")

# 'Visibility' sütununun One-Hot Encoding işlemi
visibility_encoded = pd.get_dummies(data['Visibility'])
# Yeni One-Hot Encoding sütunlarını veri setine ekleme
data_encoded = pd.concat([data, visibility_encoded], axis=1)
# One-Hot Encoding işleminden sonra 'Visibility' sütununu kaldırma
data_encoded.drop('Visibility', axis=1, inplace=True)

# 'Precipitation' sütununun One-Hot Encoding işlemi
precipitation_encoded = pd.get_dummies(data['Precipitation'])
# Yeni One-Hot Encoding sütunlarını veri setine ekleme
data_encoded = pd.concat([data_encoded, precipitation_encoded], axis=1)
# One-Hot Encoding işleminden sonra 'Precipitation' sütununu kaldırma
data_encoded.drop('Precipitation', axis=1, inplace=True)

# Gerekli sütunları seçme ve hedef değişkeni belirleme
selected_columns = ['DAY', 'NIGHT', 'DUSK', 'DAWN', 'UNKNOWN', 'NONE', 'RAIN', 'FOG', 'SNOW', 'FOG, RAIN', 'RAIN, SNOW', 'FOG, SNOW', 'FOG, RAIN, SNOW', 'Speed', 'Injuries']
data = data_encoded[selected_columns]

# NaN değerleri ortalama ile doldurma
data.fillna(data.mean(), inplace=True)

# Özellikler ve hedef değişken seçimi
X = data.drop('Injuries', axis=1)
y = data['Injuries']

# Eğitim ve test veri setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)

# Test veri seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Model performansını değerlendirme
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

#%%
import pandas as pd

# Veri setini yükle
data = pd.read_csv("aircraft.csv")

# "strike" kelimesini içeren sütunları bul
strike_columns = [col for col in data.columns if 'strike' in col.lower()]

# Bulunan sütunları ekrana yazdır
print("Sütunlar içinde 'strike' kelimesi geçen sütunlar:")
for col in strike_columns:
    print(col)
    print(data[col].value_counts())
    print()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


