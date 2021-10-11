# Mushroom-analysis-predictive-modelling
Analyzing mushroom varieties from scraped data and building a predictive model

## Web scraping

I scraped the Czech website [Na Houbách](https://www.nahoubach.cz/atlas-hub/), due to the fact that I found descriptive variables of 141 mushrooms. 

Unfortunately I did not find a more comprehensive source of data but from a quick look, all important and often seen mushrooms are included. 

The goal is to analyze the mushrooms (mainly in regards to whether they're edible) and build a predictive model to potentially help people identifying whether a mushroom is likely to be edible or not.

Data had to be cleaned and prepped for further analysis.

## Exploratory Data Analysis

I explored what variables seem to be most connected to edibility based on simple visualization. For example, it turns out that if a mushroom has a 'vaginata', it is toxic. That is due to the mushroom belonging to the Amanita genus (muchomůrky). When the mushroom is a "hřib", it is most likely edible.

![Genus](https://github.com/jachymDvorak/Mushroom-analysis-predictive-modelling/blob/main/images/genus.png)

Also it is unsurprising that if you want to pick mushroom, you gotta go to the forest.

![Mista rustu hub](https://github.com/jachymDvorak/Mushroom-analysis-predictive-modelling/blob/main/images/mista_rustu.png)

Furthermore, I confirmed the folk knowledge that most mushrooms are growing in autumn, and that the best bet is any type of forest (though mixed forests seem to yield the most benefit).

![Doba rustu hub](https://github.com/jachymDvorak/Mushroom-analysis-predictive-modelling/blob/main/images/doba_rustu.png)

It is apparent that mushroom edibility is largely determined by which genus they belong to. Likely not a surprise - though the key of this analysis was not to go further into names, but to assist the average forest-goer to pick mushrooms based on visual characteristics.

## Predictive modelling

It was quite difficult to do any predictive modelling with such a small dataset. With that said, first all categorical variables needed to be one-hot-encoded, split (one mushroom can have two colored head, for example) and then could be fit into a model.

The best I could do was using a Logistic Regression model with optimized hyperparameters using grid search, when penalizing the model more for incorrectly classifying a mushroom as edible when it is, in fact, inedible (false positive). That is because eating a toxic mushroom is much worse than not eating an edible mushroom.

![Model performance](https://github.com/jachymDvorak/Mushroom-analysis-predictive-modelling/blob/main/images/results_best_model.png)
