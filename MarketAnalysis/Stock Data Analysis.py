# Databricks notebook source
from pyspark.sql.functions import max

# COMMAND ----------

df = spark.read.format('delta')\
    .load('dbfs:/user/hive/warehouse/tesla_data_2020_csv')

display(df)

# COMMAND ----------

df.select(max("Adj_Close"), max("Volume"))\
    .withColumnRenamed('max(Adj_Close)', "Max_Close")\
        .withColumnRenamed('max(Volume)', "Max_Volume")\
            .show(truncate=False)

# COMMAND ----------

print('ciao')
