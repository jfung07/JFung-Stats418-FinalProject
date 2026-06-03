# JFung-Stats418-FinalProject

## Methodology
The project uses a random forest and a convolutional neural network to predict a person's color analysis.  The random forest explores six different parameter configurations, and selects the best parameter set based on the model's F1 score and accuracy.  The first configuration is a baseline configuration.  The second experiment investigates a wider search for better generalizability, while the third checks a deeper and more complex search.  The fourth set considers balancing, while the last two experiments look at the tree quantity effect.  

The convolutional neural network(CNN) consists of four blocks with a 3x3 kernel, a stride of two, one pixel padding, and ReLU activation.  The flattened output then flows through a fully connected layer before softmax prediction.  The CNN requires better hardware, so the project does not investigate parameter combinations.  The settings are 15 initial training epochs, a 0.001 learning rate, an Adamoptimizer, and cross entropy loss, but the loss and accuracy plots recommend early stoping at 8.

I split the data into training, validation, and testing sets in a 70/15/15 split.  Therefore, I train the random forest on the training set, select the parameters with the validation set, and evaluate on the testing set.  Because I do not explore parameters for the CNN, I train the data on both the training and validation images and evaluate the model on the testing set.  



## Exploratory Data Analysis
Exploratory data analysis focuses on the season color associations because the models do not address the best and worst colors.
![Figure1](visualizations/seasons_dist) shows the most common season in the data is cool winter, while the least common season is soft summer. 
![Figure2](visualizations/season_colors_table.png) shows the two best and worst colors for each color palette.  Black is the worst color for every eason except for winter and cool summer, where the worst color for the four seasons is a yellow shade.  The best colors tend to be pastel colors, however, the winter palettes tend to favor darker colors and discourage yellows and oranges.  Additionally, white is not a compimentary color for seven out of the twelve seasons, clear spring, light summer, soft summer, warm spring, and the autumn seasons.  The most unusual palettes appear to be the winter seasons recommending darker colors and discouraging bright colors.  


## Results
The best random forest model has a 0.3618 F1-score and a 45.83% accuracy.  The model uses 100 decision trees, where each tree has a maximum 10 level depth.  Additionally, the trees require at least five samples to split and each leaf requires at least two samples.  The main factor is that the model balances class weights based on frequency to account for the data's class imbalance.  Within the best model, ![Figure 3](visualizations/rf_varImp.png) shows the most influential variables are contrast and skin tone, while eye and hair collor are less influential.  The ordering is logical as eyes and hair are smaller body features compared to skin.  

The convolutional neural network did not perform as well as the random forest even though the structure was more complex with 12,974,688 parameters and had more training data.  The model has a 0.01 F1-score on the testing set, a 14.58% accuracy, and 2.729 loss.  

