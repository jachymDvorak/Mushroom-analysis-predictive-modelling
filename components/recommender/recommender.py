import pandas as pd
import numpy as np

df = pd.read_csv('data/mushrooms_dataset.csv', index_col=0)

class HoubovejRozpoznavac():
    
    '''
    tahle trida pripravi data, pak se zepta uzivatele na to, 
    jaka je houba co ma pred sebou,
    a pokusi se tuto houbu poznat a vratit informaci, zda je jedla
    
    '''
    
    def __init__(self, df):
    
        
        # initialize df with information about mushrooms
        self.df = df
        
        # initialize empty list to save user data
        self.user_input = []
        
        # prepare data
        self.prepare_data(df)
        
        # ask user for input
        self.ask_for_input()
        
        # print shrooms with characteristics and whether theyre edible
        self.give_shroom(self.user_input)

    def change_dash_to_nan(self, value: str) -> str:
        '''
        changes "-" in cell to "nemá"
        '''

        if value == '-':
            value = 'nemá'
        return value

    def to_list(self, value: str) -> str:
        '''
        gets a list of individual values from a string
        '''
        list_of_vals = value.split(', ')
        return list_of_vals

    def get_only_first(self, row):
        '''
        returns first attribute to simplify search
        '''

        row = row.split(',')[0]

        return row
    
    def prepare_data(self, df):
        
        '''
        function prepares data:
            - edits multiple atributes to just the first (if there are e.g. mutliple
            colors, returns just first one)
            - removes unimportant columns
            - renames columns to better reflect their content
            - re-codes numbers, add "nemá" option
        '''
        
        # re-code binary columns
        self.df['pochva'] = self.df['pochva'].map({'má': 1, 'nemá': 0}).fillna(0)
        self.df['prsten'] = self.df['prsten'].map({'má': 1, 'nemá': 0}).fillna(0)
        self.df['jedla'] = self.df['jedla'].map({'jedlá': 1, 'nejedlá': 0}).fillna(0)
        
        # re-code hymenofor
        self.df['hymenofor'] = self.df['hymenofor'].replace('jiné', '-')
        
        # change dash to nan
        self.df = self.df.applymap(self.change_dash_to_nan)
        
        # convert to list and get only first value
        self.df['vyskyt_doba'] = self.df[['vyskyt_doba']].applymap(self.to_list)
        self.df['vyskyt_misto'] = self.df[['vyskyt_misto']].applymap(self.to_list)

        self.df['tren_barva'] = self.df['tren_barva'].apply(self.get_only_first)
        self.df['klobouk_barva'] = self.df['klobouk_barva'].apply(self.get_only_first)
        self.df['klobouk_povrch'] = self.df['klobouk_povrch'].apply(self.get_only_first)

        # drop columns
        cols_to_drop = ['rod', 
                        'vyskyt_doba', 
                        'vyskyt_misto',
                        'tren_tvar',
                        'tren_konzistence',
                        'tren_povrch',
                        'klobouk_tvar']

        self.df = self.df.drop(columns = cols_to_drop)

        # rename columns
        self.df.columns = ['jedlá',
                      'barva třeně',
                      'hymenofor (spodek pod kloboukem)',
                      'barva klobouku',
                      'povrch klobouku',
                      'prsten',
                      'pochva']

        # recode values
        self.df['jedlá'] = self.df['jedlá'].map({1: 'jedlá', 0: 'nejedlá'})
        self.df['prsten'] = self.df['prsten'].map({1: 'má', 0: 'nemá'})
        self.df['pochva'] = self.df['pochva'].map({1: 'má', 0: 'nemá'})
        self.df['barva třeně'] = self.df['barva třeně'].str.replace('nemá', 'nemá třeň')
        self.df['hymenofor (spodek pod kloboukem)'] = self.df['hymenofor (spodek pod kloboukem)'].str.replace('nemá', 'nemá hymenofor')
        self.df['barva klobouku'] = self.df['barva klobouku'].str.replace('nemá', 'nemá klobouk')
        self.df['povrch klobouku'] = self.df['povrch klobouku'].str.replace('nemá', 'nemá klobouk')
                
    def ask_for_input(self) -> None:
        
        '''
        this function asks user about their shrooms. It then saves the result to the user
        input list defined above
        '''
    
        print('\nNyní se vás budeme ptát na jednotlivé charakteristiky houby, kterou jste našli.')
        print('Pokaždé do políčka napíšete jednu z nabízených možností níže.') 
        print('Pokud si nejste jistí, prosím, napište do políčka "nevím".')
        print('''\nPokud chcete vyzkoušet funkcionalitu, zkuste postupně tyto charakteristiky:
              
              -hnědá
              -rourky
              -hnědá
              -sametový
              -nemá
              -nemá\n''')

        # goes through all columns, prints options, asks for value
        for column in self.df.columns[1:]:

            print(f'\nJak byste popsali houbu co do {column}? Vyberte z těchto možností:\n')

            # writes unique possibilities
            self.temp = self.df[column].unique()

            # prints all unique possibilities
            for entry in self.temp:
                print(entry)
            
            # gets user input
            popis = input('\nVaše odpověď: ').strip()
            
            # if user does not know, marks as None
            if popis == 'nevím':
                popis = None

            # if user uses unavailable category
            elif popis.strip() not in self.temp:
                raise SyntaxError('Prosím pište jen kategorie, co jsou výše!')

            # add value to list
            self.user_input.append(popis)
            
    def give_shroom(self, user_input: list) -> None:
            
        '''
        this function outputs the shroom(s) matching the user input in the following format:
        
        user_input = ['attribute 1', 'attribute 2'] (list) from function ask_for_input
        '''
        if self.user_input[0] is not None:
            self.df = self.df[self.df['barva třeně'].eq(self.user_input[0])]
        if self.user_input[1] is not None:
            self.df = self.df[self.df['hymenofor (spodek pod kloboukem)'].eq(self.user_input[1])]
        if self.user_input[2] is not None:
            self.df = self.df[self.df['barva klobouku'].eq(self.user_input[2])]
        if self.user_input[3] is not None:
            self.df = self.df[self.df['povrch klobouku'].eq(self.user_input[3])]
        if self.user_input[4] is not None:
            self.df = self.df[self.df['prsten'].eq(self.user_input[4])]
        if self.user_input[5] is not None:
            self.df = self.df[self.df['pochva'].eq(self.user_input[5])]
        
        # if df is empty
        if len(self.df) == 0:
            print('\nTaková houba bohužel není v databázi. Omlouváme se :-(')
        
        # if just one mushroom is the result
        elif len(self.df) == 1:
            edible = self.df.iloc[0]['jedlá']
            name = self.df.index[0]
            print(f'\nVaše houba se jmenuje {name} a je {edible}!')
        
        # if more mushrooms in database, all get printed
        elif len(self.df) > 1:
            print('\nPodobných hub máme v databázi více. Mohou to být tyto houby:')

            n_of_shrooms = len(self.df)

            for i in range(0, n_of_shrooms):
                edible = self.df.iloc[i]['jedlá']
                name = self.df.index[i]
                print(f'{name} a je {edible}!')
                

HoubovejRozpoznavac(df = df)