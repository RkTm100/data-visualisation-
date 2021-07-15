import pandas as pd
import plotly.express as px
qw=pd.read_csv("./data.csv")
guy=px.scatter(qw,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
guy.show()