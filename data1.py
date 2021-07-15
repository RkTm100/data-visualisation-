import pandas as pd
import plotly.express as px
qw=pd.read_csv("./data.csv")
guy=px.bar(qw,x="Country",y="InternetUsers")
guy.show()