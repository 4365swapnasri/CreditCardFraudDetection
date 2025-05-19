As the Dataset is too big to upload into github,i have included it in this readme file

The dataset used, contains transactions carried out by European credit card holders that took place over two days in September 2013, and is available on kaggle at https://www.kaggle.com/mlg-ulb/creditcardfraud/version/3.

It is a very unbalanced data set, that is, it has 492 fraud transactions, which represents only 0.172% of the 284,807 transactions.

The input variables are numeric, the result of a PCA transformation. Due to confidentiality issues, the original data and other complementary information were not made available.

The only variables that have not been transformed with the PCA are 'Time' and 'Value'. The variable 'Time' contains the seconds between each transaction and the first transaction in the data set. The 'Amount' variable refers to the amount of the transaction.

The 'Class' variable is the response variable (Target) and has a value "1" in case of fraud and "0" otherwise.
