import streamlit as st
import pandas as pd
import numpy as np

'''st.title()'''
st.title("Liju George")

'''st.write()'''
st.write("MSC_DSAI")

'''st.header()'''
st.header("Python")

'''st.latex()'''
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

'''st.text()'''
st.text('This is some text.')

'''st.caption()'''
st.caption('This is a string that explains something above.')

'''st.code()'''
code = '''def hello():
    print("Hello, Streamlit Code!")'''
st.code(code, language='python')

'''st.table()'''
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
st.table(df)

'''st.line_chart()'''
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'''st.map()'''
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

'''st.column()'''
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

   