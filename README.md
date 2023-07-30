# Dota 2 Data Analysis

This project is a simple attempt at fetching Dota 2 information, like match data, from Valve Software's API and analysing it using the Pandas library.

## Requirements
This project requires the following libraries and software:
- [**requests**](https://pypi.org/project/requests/) for API communtication.
- [**pandas**](https://pandas.pydata.org/) for data analysis.
- [**Jupyter Notebook**](https://jupyter.org/)

## Project Structure

```
├── dota2api.py
├── pandas.ipynb
├── .gitignore
├── README.md
├── data
|   ├──  [file].json
|   ├──  ...
├── private
|   ├── steam_data.txt
|   ├── .gitkeep
```

- **dota2api.py** contains the code for fetching data from the Steam API.
- **pandas.ipynb** is a Jupyter Notebook containing the code for data analysis using Pandas.
- **data** is the folder with all the stored data, including match data, abilities, hero IDs, item IDs, and possibly more.
- **private** is the folder that includes the private file *steam_data.txt*, which should have your Steam Web API Key.

## Further Resources
Much of the constant data, like abilities, heroes, IDs, and other game data, can be downloaded from Opendota's [Github](https://github.com/odota/dotaconstants/tree/master/build). This does not require API access.
Keep in mind that sometimes the data has to be updated and re-downloaded after a patch.

The documentation for accessing the Steam API for Dota 2 can be found on the [Team Fortress Wiki](https://wiki.teamfortress.com/wiki/WebAPI#Dota_2)(?).







