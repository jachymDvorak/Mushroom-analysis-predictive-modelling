# import knihoven
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw = pd.read_csv('data/mushrooms_dataset.csv', index_col=0)

###############################################################################
# Helper functions
###############################################################################

def change_dash_to_nan(cell):
    '''
    zmeni "-" v bunce na nema
    '''
    
    if cell == '-':
        cell = 'nemá'
    return cell

def to_list(value):
    '''
    ziska ze seznamu mesicu a mist vyskytu jednotlive mesice/mista 
    '''
    list_of_vals = value.split(', ')
    return list_of_vals

###############################################################################
# Data processing
###############################################################################

############
# prvni graf
############
# prekodovat binarni sloupce
raw['pochva'] = raw['pochva'].map({'má': 1, 'nemá': 0}).fillna(0)
raw['prsten'] = raw['prsten'].map({'má': 1, 'nemá': 0}).fillna(0)
raw['jedla'] = raw['jedla'].map({'jedlá': 1, 'nejedlá': 0}).fillna(0)

# prekodovat hymenofor
raw['hymenofor'] = raw['hymenofor'].replace('jiné', '-')

# zmenit pomlcku na missing data
raw = raw.applymap(change_dash_to_nan)

# zkopirovat dataframe na praci
df = raw.copy()

# aplikovat pomocnou funkci
df['vyskyt_doba'] = df[['vyskyt_doba']].applymap(to_list)
df['vyskyt_misto'] = df[['vyskyt_misto']].applymap(to_list)

# binarizuje sloupce, tedy vytvori co misto, to sloupec a hodnoty 0/1
col_to_binarize1 = df['vyskyt_doba']
col_to_binarize2 = df['vyskyt_misto']

# vytvorit instanci binarizeru
mlb = MultiLabelBinarizer()

# binarizovat mesice
df_months_binarized = pd.DataFrame(mlb.fit_transform(col_to_binarize1), columns = mlb.classes_, index = df.index)
df_places_binarized = pd.DataFrame(mlb.fit_transform(col_to_binarize2), columns = mlb.classes_, index = df.index)

# odstrani puvodni sloupce s nebinarizovanymi hodnotami
df = df.drop(columns = ['vyskyt_doba', 'vyskyt_misto'])

# merge s binarizovanymi sloupci
df = df.merge(df_months_binarized, right_index = True, left_index = True, how = 'left')
df = df.merge(df_places_binarized, right_index = True, left_index = True, how = 'left')

# list ceskych mesicu
months_cz = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 
             'červenec', 'srpen', 'září', 'říjen', 'listopad', 'prosinec']

# dataframe s frekvencemi vyskytu mesicu
month_freq = pd.DataFrame(df[months_cz].apply(sum, axis = 0), columns = ['month'])
month_freq['month'] = month_freq['month'].astype(int)

############
# druhy graf
############
# list s misty vyskytu
places = ['jehličnatý les', 'kosodřevina', 'křoviny',
       'listnatý les', 'louky', 'mýtiny', 'parky', 'paseky', 'pastviny',
       'pole', 'rašeliniště', 'sady', 'smíšený les', 'stráně', 'zahrady']

# dataframe s frekvencemi vzhledem k mistu vyskytu
places_freq = pd.DataFrame(df[places].apply(sum, axis = 0), columns = ['place'])
places_freq['place'] = places_freq['place'].astype(int)
places_freq = pd.DataFrame(places_freq['place'].sort_values(ascending = False))

###############################################################################
# KDY ROSTOU HOUBY
###############################################################################

# parametry grafu
size = (16.5, 9)
fig, ax = plt.subplots(figsize=size)

# vytvoreni grafu 1
sns.set_style('white')
ax = sns.barplot(y="month", x=month_freq.index, data=month_freq, palette = 'Reds')
sns.despine()
plt.xticks(rotation= 45, fontsize = 15)
plt.yticks(fontsize = 20)
ax.set_ylabel('Počet druhů co roste', fontsize = 20)
ax.set_title('Kdy jít houbařit?', fontsize = 25)
ax.set_yticks(list(range(0,150, 10)))

plt.savefig("Doba_rustu_houbicek.png")

###############################################################################
# KDE ROSTOU HOUBY
###############################################################################

# parametry grafu
size = (16.5, 9)
fig, ax = plt.subplots(figsize=size)

# vytvoreni grafu 2
sns.set_style('white')
ax = sns.barplot(y="place", x=places_freq.index, data=places_freq, color = '#006400')
sns.despine()
plt.xticks(rotation= 45, fontsize = 15)
plt.yticks(fontsize = 20)
ax.set_ylabel('Počet druhů co roste', fontsize = 20)
ax.set_title('A kam jít houbařit?', fontsize = 25)
ax.set_yticks(list(range(0,150, 10)))

plt.savefig("Mista_rustu_houbicek.png")

###############################################################################
# JAKE SBIRAT HOUBY
###############################################################################

# parametry grafu
size = (16.5, 12)
fig, ax = plt.subplots(figsize=size)

# samotny graf
sns.set_style('white')
sns.countplot(x="hymenofor", hue="jedla", data=df, palette = 'pastel')
sns.despine()
plt.xticks(rotation= 45, fontsize = 15)
plt.yticks(fontsize = 15)
ax.set_xlabel('Hymenofor (spodek klobouku)', fontsize = 20)
ax.set_ylabel('Počet druhů co roste', fontsize = 20)
ax.set_title('A co sbírat?', fontsize = 20)
plt.legend(prop={'size': 25}, labels = ['Nejedlá', 'Jedlá'])
ax.set_yticks(list(range(0,60, 5)))

plt.savefig("Jake_sbirat_houbicky.png")

###############################################################################
# CO PRSTEN
###############################################################################

# parametry grafu
size = (16.5, 12)
fig, ax = plt.subplots(figsize=size)

# samotny graf
sns.set_style('white')
sns.countplot(x="prsten", hue="jedla", data=df, palette = 'pastel')
sns.despine()
plt.xticks(rotation= 45, fontsize = 15, labels = ['Nemá prsten', 'Má prsten'], ticks = [0, 1])
plt.yticks(fontsize = 15)
ax.set_ylabel('Počet druhů co roste', fontsize = 20)
ax.set_xlabel('')
ax.set_title('Pozor na prsteny!', fontsize = 20)
plt.legend(prop={'size': 25}, labels = ['Nejedlá', 'Jedlá'])
ax.set_yticks(list(range(0,90, 5)));

plt.savefig("Co_houbicky_s_prstenem.png")