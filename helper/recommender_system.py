
import streamlit as st
def matrix_display(top_products_index,product_details,rows,cols):
    index = 0
    columns = [st.columns(cols) for i in range(rows)]
    price,rating = st.columns(2)
    for row in range(rows):
        for col in range(cols):
            # each_product = product_details[[index]]
            with columns[row][col]:
                
                st.image('https://m.media-amazon.com/images/'+product_details.iloc[top_products_index[index]]['Image url IDS']+ '._AC_UL400_.jpg',width=100,use_column_width=100)
               
                

                st.header(f""":green[{product_details.iloc[top_products_index[index]]['discount_price']}]""")
                
            
                st.markdown(product_details.iloc[top_products_index[index]]['name'])
                
            index +=1
                
def recommender(product_index,similarity_matrix):
    """_summary_

    Args:
        product_index (_type_): int
        similarity_matrix (_type_):  array

    Returns:
        _type_: return Indexes of top 10 Similar type of products
    """
    
    return similarity_matrix[product_index]