# Filter that satisfy both conditions
df_filtered = products.filter((products.low_fats == "Y") & (products.recycleable == "Y"))

# select the column to be displayed from filtered data frame
df_final = df_filtered.select("products_id")

# display the data frame
display(df_final)
