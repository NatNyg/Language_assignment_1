# Language_Assignment_1: Collocate tool
## This is the repository for assignment 1 in Language Analytics. 

### Project Description 
This script provides a collocation tool which produces a result of a dataframe containing the name of each collocate within a user-defined window-range of a user-defined target word in a user defined text. The dataframe shows how many times each collocate appears in the text (B), number of times each word inside the window occors with the target word (AB) and the MI (information score). The dataframe will be saved as a .csv in the "out" folder. The data used for this project is 100 english novels. 

## Repository Structure 

The repository includes three folders: 
- in: this folder should contain the data that the code is run on
- out: this folder will contain the results after the code has been run
- src: this folder contains the script of code that has to be run to achieve the results

### Method
This script uses an NLP pipeline (the small english model from spacy) to prepare the text for sentiment analysis. After cleaning the text and  normalizing it by turning all words into lower and running the nlp pipeline on the doc of words, I use a function to create a nlp wordlist containing all the words from the text. 
After this a function creates list of all the collocates of the given targetword within the user-defined span (this function takes the five words before and after the targetword, so it is default set to a span of 10 - if this is changed in the arguments, this function should also be regulated in order to run properly.) b
Then the MI score is calculated by first finding A (number of times the target word appears in the text), B (how many times each collocate appears in the text) and AB how many times each collocate occors inside the window/span of the target word. I use the math library to calculate this MI-score. I have further included how to handle a ZeroDivisionError, since this occored for me when running the code. 
Lastly the function uses pandas to save the results into a dataframe containing the collocates, B, AB and MI-score. The dataframe is then saved as a .csv file to the "out" folder. 


### Usage 
In order to reproduce the results I have gotten (and which can be found in the "out" folder), a few steps has to be followed:

1) Install the relevant packages - relevant packages for both scripts can be found in the "requirements.txt" file.
2) Make sure to place the script in the "src" folder and the data in the "in" folder. The data used for this project can be accessed on the following page: https://github.com/computationalstylistics/100_english_novels 
3) Run the script from the terminal and remember to pass the required arguments (-fn (filename) -tt (targetterm) and -sp (span) -> Make sure to navigate to the main folder before executing the script - then you just have to type the following in the terminal: 
"python src/collocates.py -fn {name of the desired filename} -tt {name of the desired target term} -sp {span of words to look for collocates in}" 

This should give you the same results as I have gotten in the "out" folder.

### Results 
As adressed my results are placed in the "out" for inspection. I find this tool very useful as it allows for a quick and easy way to compare the usage of different words across a corpus of texts. This gave an idea of the themes in each text which was very interesting for a distant analysis and could give an insight into which texts that might be interesting to analyse further. 

