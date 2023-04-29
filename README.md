# gephiHelper

Program that parses certain JSON file and converts into CSV, that helps to graph the Data.

To run the following program:
- ```clone``` - the following repo
- ```run``` the following command ⬇️
```py
python3 gephiHelper.py LabeledAllCalls.json
```
- ```toGraph.csv``` newely created with the conerted data

## Using Gephi to Graph

- Open the app
- Click new project
    - Data Labaratory
    - Import Spreadsheet
    - choose toGraph.cvs 
    - Separator: ```comma``` Import as: ```Adjacency List```
    - next & finish
    - Directed & ok
- Click ```Overview```
    - you can select nodes and move them around, to make graph more readable for testing 
- Click ```Preview```
    - Refresh
    - Under Node Labels choose:
        - Show Labels
        - set Outline Size to 10.0 __[for better visual]__

