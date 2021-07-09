import pandas as pd
import plotly.express as px

#bar
#df = pd.read_csv('csv files\data.csv')
#fig=px.bar(df,x='Country',y='InternetUsers', title='internet users per country')
#fig.show()

#line
#ab = pd.read_csv('csv files\line_chart.csv')
#fig1 = px.line(ab,x ='Year',y='Per capita income',color ='Country', title ='Per Capita Income Of Some Countries')


# scatter
df = pd.read_csv('C:\whiteHat\pythonProgram\Copy+of+data+-+data.csv')
fig2 = px.scatter(df,x ='date', y= 'cases',color ='country',title='Covid Cases Around the World')
fig2.show()