import streamlit as st
import requests
import pandas as pd
from pathlib import Path
st.set_page_config(
    page_title='Dashboard for advance python programming ',
    page_icon= ':snake:'
)
st.title("Illustration of data")

base_path = Path().absolute()


@st.cache_data
def read_dataframe(path:str) :
    return pd.read_parquet(path,engine='pyarrow')


st.header('Filter Movie Based On Years')

df_path = base_path/"datas/quera/movie.parquet"
st.write(base_path)
df = read_dataframe(df_path);

number1 = st.number_input('Insert a first year ',max_value=2020,step=1000)
number2 = st.number_input('Insert a second year ',min_value=number1,step=1000)
"--------"

st.dataframe(df[(df['year']>=number1)&(df['year']<=number2)])
"--------"


st.header('Filter Movie Based On Runtime')


number1 = st.number_input('Insert Time 1 ',max_value=2020,step=1)
number2 = st.number_input('Insert Time 2',min_value=number1,step=1)
"--------"

st.dataframe(df[(df['runtime']>=number1)&(df['runtime']<=number2)])
"--------"

st.header('Filter Movies Based on Actors')
dfPerson = read_dataframe(base_path/"datas/quera/person.parquet");
dfCast = read_dataframe(base_path/"datas/quera/cast.parquet");
dfMovie = read_dataframe(base_path/"datas/quera/movie.parquet");
dfGenre = read_dataframe(base_path/"datas/quera/genre_movie.parquet");
df1 = pd.merge(dfPerson,dfCast,how='inner',left_on='id',right_on='person_id');
df2 = pd.merge(dfMovie,df1,left_on='id',right_on='movie_id');

# list1=['Matthew McConaughey','Leonardo DiCaprio']

Actors = st.multiselect(
    label = "Which Actor do you want ?",
    options = [i for i in dfPerson['name']],
    default = ("Leonardo DiCaprio")
)
st.write("\n   ".join(Actors))

df2.rename(columns={'id_x':'id'},inplace=True)
st.dataframe(df2[df2['name'].isin(Actors)][dfMovie.columns])

st.header('Filter Movies Based on Genre')

st.subheader("Please select a genre")

genre = st.selectbox(
    label = "which genre do you want?",
    options = set([i.replace("'",'') for i in dfGenre['genre']]) ,
)

dfg = pd.merge(dfGenre,dfMovie , how='inner',left_on='movie_id',right_on='id');
dfg.rename(columns={'id_y':'id'},inplace=True)
st.dataframe(dfg[dfg['genre'].isin(["'"+genre+"'"])][dfMovie.columns])




st.header('Significant Charts')

st.subheader("the most 10 sold 250 top IMDB movies")
"--------"

st.bar_chart(dfMovie.sort_values('gross_us_canada',ascending=False).head(10)[['title','gross_us_canada']],x='title',y='gross_us_canada')

"-------------"


st.subheader('the most 5 repeatedly actors in  top 250 IMDB movies')
"--------------"
# top5_id = dfCast.value_counts('person_id').head(5).index.to_list()
# top5_values = dfCast.value_counts('person_id').head(5).values
# dfPerson[dfPerson['id'].isin(top5_id)]
t=pd.DataFrame(dfCast.value_counts('person_id').head(5)).reset_index()
t.rename(columns={0:'count'},inplace=True)
top5 =pd.merge(t,dfPerson , how='left' ,left_on='person_id',right_on='id')
st.bar_chart(top5[['name','count']],x='name',y='count',use_container_width=False,width=500)

"--------------"
st.subheader('the distribution of genres in top 250 IMDB movies')
"--------------------------------"

# countGenre = pd.DataFrame(dfGenre.value_counts('genre').reset_index())
# countGenre = countGenre.rename(columns={0:'count'})
# # st.pyplot(countGenre)
# st.plotly_chart(countGenre,use_container_width=False,width=500)
import matplotlib.pyplot as plt
labels = dfGenre.value_counts('genre').index.to_list()
sizes = dfGenre.value_counts('genre').values    
labels = [i.replace("'",'') for i in labels]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
legend = ['{} ({:})'.format(idx, value) for idx, value in zip(labels, sizes)]

ax1.legend(legend ,loc='center left', bbox_to_anchor=(1, 0.5))

st.pyplot(fig1)


"-------------"

st.subheader('the distribution of  age rating in top 250 IMDB movies')
"--------------------------------"


labels = dfMovie.value_counts('parental_guid').index.to_list()
sizes = dfMovie.value_counts('parental_guid').values    
# labels = [i.replace("'",'') for i in labels]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,
        shadow=False, startangle=90)
ax1.axis('equal') 
legend = ['{} ({:})'.format(idx, value) for idx, value in zip(labels, sizes)]

ax1.legend(legend ,loc='center left', bbox_to_anchor=(1, 0.5))

st.pyplot(fig1)


"-------------"


st.subheader('count of age rated in each genre in top 250 IMDB movies')

b=pd.merge(dfGenre,dfMovie ,how ='inner' ,\
           left_on='movie_id',right_on='id').groupby('genre')['parental_guid'].value_counts()
s=pd.DataFrame(b)
# st.bar_chart(s.rename(columns={'parental_guid':'count'}))

s=s.rename(columns={'parental_guid':'count'})
listIndex =s.reset_index().value_counts('genre').index.to_list()
listColumns = s.reset_index().value_counts('parental_guid').index.to_list()
final = pd.DataFrame(0,columns=listColumns,index=listIndex)
listofAll = s.rename(columns={'parental_guid':'count'}).reset_index()
for j in listofAll.value_counts('genre').index.to_list():

    for i in listofAll[listofAll['genre']==j]['parental_guid']:
        final.loc[j][i]=listofAll[listofAll['genre']==j]\
              [listofAll[listofAll['genre']==j]['parental_guid']==i]['count'].values[0]
st.bar_chart(final)

"--------------"

st.header('Interaction charts')
"--------------"
st.subheader('most soled movies in each genre')
'------------------'
mergef = pd.merge(dfGenre,dfMovie, how ='inner',left_on='movie_id',right_on='id')


test = st.selectbox(
    label = "which genree do you want?",
    options = set([i.replace("'",'') for i in dfGenre['genre']]) ,
)

h=mergef[mergef['genre']=="'"+test+"'"]\
    .sort_values('gross_us_canada',ascending=False)[['title','gross_us_canada']].head(5)

h=h[h['gross_us_canada']>0]

st.bar_chart(h,x='title',y='gross_us_canada')


