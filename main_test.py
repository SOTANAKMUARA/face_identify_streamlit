import streamlit as st
import pandas as pd
import numpy as np


st.title('My 1st App')
st.write('データフレーム')
st.write(
  pd.DataFrame({
    '1st column' : [1,2,3,4],
    '2nd column' : [10,20,30,40]
  })
)

"""
# My 1st App
## マジックコマンド
こんな感じでできる。markdown対応。
"""

if st.checkbox('Show DataFrame'):
  chart_df = pd.DataFrame(
    np.random.randn(20,3), #random.randnは平均0,標標準偏差1の正規分布から乱数を生成。引数は列,行
    columns = ['a','b','c']
  )
  st.line_chart(chart_df)