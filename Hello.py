# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():


    # Title of the dashboard
    st.title('Canadian Urban Housing Starts Dashboard')
    st.write('This dashboard presents the data on the number of housing starts throughout Canada in the year 2022. The data was obtained from Canadian Housing Mortgate Housing Corporation public datasets portal [Housing Start 2022](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/housing-market-data/housing-starts-dwelling-type). This Dashboard was created especially for the hiring managers at **Ministry of the Solicitor General**.')

    # Load data
    @st.cache_data
    def load_data():
        data = pd.read_csv('Housing_starts_2022.csv')
        return data

    housing_data = load_data()

    # Sidebar for filtering
    st.sidebar.header('Filter Data')
    province = st.sidebar.multiselect('Select Province:', housing_data['Province'].unique())
    centre = st.sidebar.multiselect('Select Centre:', housing_data['Centre'].unique())

    # Filtering data
    filtered_data = housing_data
    if province:
        filtered_data = filtered_data[filtered_data['Province'].isin(province)]
    if centre:
        filtered_data = filtered_data[filtered_data['Centre'].isin(centre)]

    # Display data
    st.write('## Housing Starts Data', filtered_data)

    # Plotting the data
    st.write('## Housing Starts by Dwelling Type')
    dwelling_types = ['Singles', 'Semis', 'Row', 'Apartment and Other']
    for dwelling in dwelling_types:
        fig = px.bar(filtered_data, x='Centre', y=dwelling, color='Province', 
                    title=f'Number of {dwelling}')
        st.plotly_chart(fig)


if __name__ == "__main__":
    run()
