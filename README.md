# Language_Assignment_1: Collocate tool
## This is the repository for assignment 1 in Language Analytics. 

### Project Description 
This script provides a collocation tool which produces a result of a dataframe containing the name of each collocate within a user-defined window-range of a user-defined target word in a user defined text. The dataframe shows how many times each collocate appears in the text (B), number of times each word inside the window occors with the target word (AB) and the MI (information score). The dataframe will be saved as a .csv in the "out" folder.

### Method

## Repository Structure 

The repository includes three folders: 
- in: this folder should contain the data that the code is run on
- out: this folder will contain the results after the code has been run
- src: this folder contains the script of code that has to be run to achieve the results

### Usage 
In order to reproduce the results I have gotten (and which can be found in the "out" folder), a few steps has to be followed:

1) Install the relevant packages - relevant packages for both scripts can be found in the "requirements.txt" file.
2) Make sure to place the script in the "src" folder and the data in the "in" folder. The data used for this project can is placed in the in folder.
3) Run the script from the terminal and remember to pass the required arguments (-fn (filename) -tt (targetterm) and -sp (span) -> Make sure to navigate to the main folder before executing the script - then you just have to type the following in the terminal: 
"python src/collocates.py -fn {name of the desired filename} -tt {name of the desired target term} -sp {span of words to look for collocates in}" 

This should give you the same results as I have gotten in the "out" folder.

### Results 
As adressed my results are placed in the "out", and I find this tool very useful as it allowed for a quick and easy way to compare the usage of different words across a corpus of texts. This gave an idea of the themes in each text which was very interesting for a distant analysis and could give an insight into which texts that might be interesting to analyse further. 

