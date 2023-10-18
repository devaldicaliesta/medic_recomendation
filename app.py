import streamlit as st
import pandas as pd

# Load data and cosine similarity matrix
data = pd.read_excel("data/data.xlsx")
cosine_sim = pd.read_excel("data/cosine_sim.xlsx")

def recommendation_obat(obat):
    indexprod = int(data[data['Drug Name'] == obat].index.values[0])
    similar_review = list(enumerate(cosine_sim.iloc[indexprod]))
    sorted_similar_review = sorted(similar_review, key=lambda x: x[1], reverse=True)
    aa = []
    for i in range(1, 6):
        aa.append(sorted_similar_review[i][0])
    return data.iloc[aa, :7]

def main():
    st.title("Obat Recommendation App")

    product_name = st.text_input("Enter a drug name:")
    if st.button("Recommend"):
        if product_name:
            recommended_df = recommendation_obat(product_name)
            st.write("Recommended drugs:")
            st.table(recommended_df)
        else:
            st.warning("Please enter a drug name.")

if __name__ == '__main__':
    main()
