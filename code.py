from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file

start=datetime.datetime(2015,11,2)
end=datetime.datetime(2016,3,10)
df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

p=figure(x_axis_type='datetime',width=1000,height=300)
p.title.text="CandleStick Chart"
p.grid.grid_line_alpha=0.3
p.sizing_mode="scale_both"
hours_12=12*60*60*1000

def inc_dec(c,o):
    if c>o:
        return"Increase"
    elif c<o:
        return "Decrease"
    else:
        return "Equal"
    
df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

df["Middle"]=(df.Close+df.Open)/2
df["Height"]=abs(df.Close-df.Open)

p.segment(df.index,df.High,df.index,df.Low,color="black")
    
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,
       df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,
       df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")

output_file="CS.html"
show(p)
