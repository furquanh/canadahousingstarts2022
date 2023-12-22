## Canadian Urban Housing Starts Dashboard
### Overview
This Streamlit dashboard provides an interactive way to explore and analyze the annual number of housing starts in Canadian urban centers with at least 10,000 people. The data is organized by type of dwelling, offering industry professionals and analysts a comprehensive overview of housing trends across the country.

### Features
* Data Overview: Interactive table displaying the housing starts data, with options to sort and filter based on different columns.
* Geographical Breakdown: Visualization of housing starts by location (province and urban center).
Type of Dwelling Analysis: Bar charts to analyze the distribution of different types of dwellings across regions.
* Dynamic Filtering: Users can filter data based on provinces and urban centers using a sidebar.
Interactive Visualizations: Utilizing Plotly for dynamic and interactive charts.

### Installation
install Streamlit and Plotly, which are used for creating the dashboard and visualizations, respectively. You can install these packages using pip:

```python
pip install streamlit plotly
```

### Running the Dashboard
To run the dashboard, navigate to the directory containing the streamlit_housing_dashboard.py file and the data file Housing_starts_2022.csv. Run the following command in your terminal:

```python
streamlit run Hello.py
```

### Data
The dashboard uses a CSV file named Housing_starts_2022.csv, containing the following columns:

* Province: The province where the housing starts occurred.
* Centre: The name of the urban center.
* Census Subdivision: The specific subdivision within the urban center.
* Singles: The number of single-family homes.
* Semis: The number of semi-detached homes.
* Row: The number of row houses.
* Apartment and Other: The number of apartment units and other types of dwellings.
* Total: The total number of housing starts.

### Customization
You can customize the dashboard by modifying the streamlit_housing_dashboard.py script. This includes adding new visualizations, enhancing filtering options, or modifying the layout and styling of the dashboard.

### Contributions
Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

