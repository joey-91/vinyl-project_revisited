## Predicting Vinyl Record Prices

This project aims to build the best possible model for predicting record prices, given all the potential predictors I could find on Discogs.com. It started with me wanting to build something a little more interesting than the datasets available on Kaggle, and a tool I could potentially use myself for finding bargains.

## Methodology

### 1 - Scraping the data.
This was the most labour intensive part of the project. Using a combination of Selenium, Beautiful Soup and Regex (for the really stubborn problems), to extract and clean the data from it's HTML format to a structured table. Firstly scraping ~30,000 most recent records from the search pages, with settings configured to view 250 records per page. Within the scraped HTML, were the HTTP links for each record, what you'd click on to take you to the next page. On these pages were further datapoints on each record. One careful consideration I had to make while iterating through the record pages was setting a sleep time, to avoid servers blocking my IP address. Anything within a certain time frame was recognised as a bot. 
  
### 2 - Exploratory Analysis & Feature Engineering
This part involved looking at distributions, correlations between data, general insight, and figuring out which datapoints could be scaled or combined to form something more useful. Engineered Features included, a ratio of how many members of the Discog community wanted that record, squared, divided by how many have the record, which turned out to be the most useful. And a clustering to create a level in between genre & sub-genre, genre being too broad in cases of say Rock or Electronic music, and sub-genre being far too niche when it came to Ceremonial Donk Music or Easy-listening Lounge Metal. With a mixture of numeric features including age, number of tracks on the record, average rating, and categoric variables

### 3 - Regression Models
As the value i'm trying to predict is continuous, I figured this would be a regression problem. I first built a simple Linear Regression. Here i'm mainly interested in the coefficients of the model. The most predictive of price were the (Supply)^2/Demand ratio, age, rating, number of tracks, and record condition. These were all expected, but the main hidden nuggets I found interesting after this were records shipping from Greece were more expensive, and 12" records were less, probably because this is the format for singles.

The next thing to try was an ensemble model, with a simple regression score of 33%, sklearn's GradientBoostingRegressor gave me 20% uplift. Not able to say whether for positive or negative, the feature importances of this model were pretty consistent with the last model.

### 4 - Classification Models
I figured this problem could be better modelled as a price range prediction rather than exact value. Having come back to this a few times over the last couple of years with new techniques, I'm now certain I've squeezed every drop out of it. Firstly I built a Neural Network using Keras framework, with 20% drop out at each stage, and early stopping based on validation-loss. This model at it's optimum gives 55.3% accuracy (only 2% higher than my boosted regressor, which made me realise that's actually a very powerful model). 

The next and highest performing model I applied was an XGBoostClassifier, using a Bayesian method for Hyperparameter tuning, i was able to get a further 1.6% model improvement. Again the feature importances were consistent with the other models, and the supply-demand ratio is the most predictive of record price, without this I'd have a much weaker model.

### 5 - Web Tool
The next step was to pickle the model make it into a web-app. Going with a GUI approach I've just taken the 4 most important model variables, performing 15% weaker than a model trained on all variables. An improvement would be to create a tool where the user just enters the URL, and the app can request the HTML, scrape all of the data, and predict using all variables.


