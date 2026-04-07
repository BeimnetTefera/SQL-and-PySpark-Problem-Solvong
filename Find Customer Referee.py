# filter data frame
df_filtered = customer.filter((customer.referee_id != 2) | (customer.referee_id.isNull()))

# select name column
df_final = df_filtered.select("name")

display(df_final)
