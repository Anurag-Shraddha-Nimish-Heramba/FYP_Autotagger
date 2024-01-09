## About data
The dataset initially had 200,000 rows, but many had 'Product' set to NaN. After removing such rows, 65,737 remained. 
Post combining similar 'Product' categories, 13 distinct values existed. The concatenated issue corpus was tokenized, removing problematic tokens. 
The top 25,000 tokens were chosen, and the model trained on 15,000 issues.
