import pandas as pd
import plotly.express as px
qw=pd.read_csv("./covid.csv")
guy=px.scatter(qw,x="date",y="cases",color="country")
guy.show()