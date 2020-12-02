# Mushroom-analysis-predictive-modelling
Analyzing mushroom varieties from scraped data and building a predictive model

## Web scraping

I scraped the Czech website [Na Houbách](https://www.nahoubach.cz/atlas-hub/), due to the fact that I found descriptive variables of 141 mushrooms. 

Unfortunately I did not find a more comprehensive source of data but from a quick look, all important and often seen mushrooms are included. 

The goal is to analyze the mushrooms (mainly in regards to whether they're edible) and build a predictive model to potentially help people identifying whether a mushroom is likely to be edible or not.

Data had to be cleaned and prepped for further analysis.

## Exploratory Data Analysis

I explored what variables seem to be most connected to edibility based on simple visualization. For example, it turns out that if a mushroom has a 'vaginata', it is toxic. That is due to the mushroom belonging to the Amanita genus. 

Furthermore, I confirmed the folk knowledge that most mushrooms are growing in autumn, and that the best bet is any type of forest (though mixed forests seem to yield the most benefit).

Furthermore, it is apparent that mushroom edibility is largely determined by which genus they belong to. Likely not a surprise - though the key of this analysis was not to go further into names, but to assist the average forest-goer to pick mushrooms based on visual characteristics.

## Predictive modelling

It was quite difficult to do any predictive modelling with such a small dataset. With that said, first all categorical variables needed to be one-hot-encoded, split (one mushroom can have two colored head, for example) and then could be fit into a model.

-tbd
