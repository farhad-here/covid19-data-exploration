#library
import pandas as pd
import sqlite3
import os
import streamlit as st
import altair as alt

#function
def run_query(file_name):
       current_dir = os.path.dirname(os.path.abspath(__file__))

       file_path = os.path.join(current_dir, '..', 'queries', file_name)
       file_path = os.path.normpath(file_path)

       if not os.path.exists(file_path):
              raise FileNotFoundError(f"فایل پیدا نشد: {file_path}")
    
       with open(file_path, 'r', encoding='utf-8') as file:
              query = file.read()
       return pd.read_sql_query(query, conn)

#data set
df = pd.read_csv('data\country_wise_latest.csv')
#connect to sqlite3
conn = sqlite3.connect('covid_data.db')
df.to_sql('covid', conn, if_exists='replace', index=False)


# Total confirmed cases per country
st.title("Total confirmed cases per country")
total_confirmed_cases_per_country = run_query('../queries/Total confirmed cases per country.sql')
st.dataframe(total_confirmed_cases_per_country)
       #chart 
st.bar_chart(data=total_confirmed_cases_per_country,x='Country/Region',y='total_confirmed')
st.line_chart(data=total_confirmed_cases_per_country,x='Country/Region',y='total_confirmed')
st.divider()

# Total confirmed cases for Iran and Egypt
st.title("Total confirmed cases for Iran and Egypt")
total_confirmed_cases_for_iran = run_query('../queries/Total confirmed cases for Iran.sql')
st.dataframe(total_confirmed_cases_for_iran)
#chart total confirmed cases for Iran and Egypt
st.bar_chart(data=total_confirmed_cases_for_iran,x='Country/Region',y='total_confirmed_iran_egypt')
st.divider()

#Top 10 countries by death rate
st.title('Top 10 countries by death rate')
top_ten_countries_death_rate = run_query('../queries/Top ten countries by death rate.sql')
st.dataframe(top_ten_countries_death_rate)
#chart
st.bar_chart(data=top_ten_countries_death_rate,x='Country/Region',y='death_rate')
st.line_chart(data=top_ten_countries_death_rate,x='Country/Region',y='death_rate')
st.divider()

#all countries death rate
st.title('all countries death rate')
all_countries_death_rate = run_query('../queries/all countries death rate.sql')
st.dataframe(all_countries_death_rate)
#chart
st.bar_chart(data=all_countries_death_rate,x='Country/Region',y='death_rate')
st.line_chart(data=all_countries_death_rate,x='Country/Region',y='death_rate')

st.divider()
#Iran death by covid
st.write('# Iran death by covid')
iran_death_cov = run_query('../queries/iran death by covid.sql')
st.dataframe(iran_death_cov)

st.divider()


# Active vs. Recovered comparison

st.title('Active vs. Recovered comparison')
active_recovered_comparison = run_query('../queries/Active vs Recovered comparison.sql')
st.dataframe(active_recovered_comparison)
#chart

# Assuming active_recovered_comparison is a DataFrame
# with at least these columns: 'Country/Region', 'active_case', 'recovered'

# Step 1: Melt the DataFrame to long format for Altair
data_melted = active_recovered_comparison.melt(
    id_vars='Country/Region', 
    value_vars=['active_cases', 'recovered'],
    var_name='Case Type', 
    value_name='Count'
)

# Step 2: Create a bar chart
chart = alt.Chart(data_melted).mark_bar().encode(
    x='Country/Region:N',
    y='Count:Q',
    color='Case Type:N',
    tooltip=['Country/Region', 'Case Type', 'Count']
).properties(
    width=700,
    height=400,
    title='Active vs Recovered Cases Comparison'
)

# Step 3: Display the chart in Streamlit
st.bar_chart(data=active_recovered_comparison,x='Country/Region',y='active_cases')

st.bar_chart(data=active_recovered_comparison,x='Country/Region',y='recovered')

st.line_chart(data=active_recovered_comparison,x='Country/Region',y='active_cases')

st.line_chart(data=active_recovered_comparison,x='Country/Region',y='recovered')


st.altair_chart(chart, use_container_width=True)
