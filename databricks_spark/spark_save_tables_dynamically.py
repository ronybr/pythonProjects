# Databricks notebook source
# ############################################
# Inov Azure Data Lake Access Configurations #
# ############################################

#AZURE GEN 1
configs = {"dfs.adls.oauth2.access.token.provider.type": "ClientCredential",
           "dfs.adls.oauth2.client.id": "xxxx",
           "dfs.adls.oauth2.credential": dbutils.secrets.get(scope = "xxx", key = "xxx"),
           "dfs.adls.oauth2.refresh.url": "https://xxxx/"}

spark.conf.set("dfs.adls.oauth2.access.token.provider.type", "ClientCredential")
spark.conf.set("dfs.adls.oauth2.client.id", "xxxxxx")
spark.conf.set("dfs.adls.oauth2.credential", "xxxx")
spark.conf.set("dfs.adls.oauth2.refresh.url", "https://xxxx/")


# COMMAND ----------

# MAGIC %md 
# MAGIC ## THIS NOTEBOOK HAS TWO PROCESS:                                                                                          
# MAGIC DON'T RUN ALL BELOW BEFORE READ EVERYTHING

# COMMAND ----------

# MAGIC %md 
# MAGIC ## 1 - CREATE TABLES ON DATABRICKS BASED ON CSV FILES STORED ON AZURE DATA LAKE THAT LOADED BY SQOOP PROCESS

# COMMAND ----------

# MAGIC %md 
# MAGIC THE PROCCESS IS GENERIC, SO TO ADAPT FOR YOUR PROCESS JUST CHANGE THE VARIABLES "db", "source_tmp" AND "originPath".         
# MAGIC $db = Correspond the database name and also used as path for mount                                                        
# MAGIC $source_tmp = Path on Azure Data Lake where the files containing column names e datatype will be read, were written by sqoop.
# MAGIC $originPath = Path on Azure Data Lake where the files containing the data foreach table will be read, were written by sqoop.                                                                                                                   

# COMMAND ----------

# MAGIC %md
# MAGIC #How does it works ?
# MAGIC 
# MAGIC 
# MAGIC The script will create the database if not exists using the variable $db, then use it. After that will list all files stored on "$originPath" to get the names foreach table, so will check which files are not name by "part-m" and delete them, the process just use files named by "part-m". 
# MAGIC 
# MAGIC So, the files stored on "$source_tmp" will be read to get the columns names for all tables and them save then as table on Databricks using Spark.

# COMMAND ----------

#db Vars
db = "OAS"
mount_point = "/mnt/" + db + "/"

# COMMAND ----------

###########################################################
#### MOUNT ALREADY DONE !! JUST EXECUTE FOR NEW MOUNTS ####
###########################################################

# unmount 
#dbutils.fs.unmount(mount_point = mount_point)

# mount
#dbutils.fs.mount(
#  source = "adl://ddpazfs.azuredatalakestore.net/refined/refining_operations/processes/oas/",
#  mount_point = mount_point,
#  extra_configs = configs)

# COMMAND ----------

#ESTE MOUNT SERVE PARA OS FICHEIROS COM AS COLUMN_NAMES E DATATYPES DE CADA TABELA OAS, QUE SERÃO GRAVADOS NA AREA TMP VIA SQOOP
#db Vars
db_tmp = db
mount_point_tmp = "/mnt/" + db_tmp + "/" + "tmp/"
#DEV
#source_tmp = "adl://ddpazfslab.azuredatalakestore.net/refined/refining_operations/processes/tmp/SQOOP_RESULT/"
#originPath = "adl://ddpazfslab.azuredatalakestore.net/refined/refining_operations/processes/oas/"

#PRD
#source_tmp = "adl://ddpazfs.azuredatalakestore.net/config/refining_operations/oas/metadata/"
#originPath = "adl://ddpazfs.azuredatalakestore.net/refined/refining_operations/processes/oas/"

# COMMAND ----------

###########################################################
#### MOUNT ALREADY DONE !! JUST EXECUTE FOR NEW MOUNTS ####
###########################################################

# unmount 
#dbutils.fs.unmount(mount_point = mount_point_tmp)

# mount
#dbutils.fs.mount(
#  source = source_tmp,
#  mount_point = mount_point_tmp,
#  extra_configs = configs)

# COMMAND ----------

#CREATE TABLES ON DATABRICKS BASED ON FILES LOADED ON AZURE DATA LAKE BY SQOOP
from pyspark.sql.types import *
from pyspark.sql.functions import *

#create database
spark.sql("create database if not exists " + db)

#drop database and all tables
#spark.sql("drop database if  exists XXX cascade")

# use database
spark.sql("use " + db)

for allFiles in dbutils.fs.ls(originPath):
    
    TableName = allFiles[1][:-1]
    
    # READ THE FILE THAT CONTAINS COLUMN NAMES FOREACH TABLE
    #filesStruct = 'adl://ddpazfslab.azuredatalakestore.net/refined/refining_operations/processes/tmp/SQOOP_RESULT/' + TableName
    filesStruct = source_tmp + TableName
    
    # READ THE FILE THAT CONTAINS THE DATA WITH NO HEADER
    filePath = originPath + TableName

    for fileName in dbutils.fs.ls(filePath):
        fileName = fileName[1]
        # print(fileName[:6])

        # DELETE FILES WITH EXTENSION NOT EQUAL "part-m"
        if (fileName[0] == "_") and (fileName[:6] != "part-m"):
            dbutils.fs.rm(filePath + '/' + fileName)
            print("DELETANDO: " + filePath + '/' + fileName)
        elif (fileName[:6] == "part-m"):
            startSchema = 'schema = StructType(['
            endSchema = '])'

            #newVar = ''
            for file in dbutils.fs.ls(source_tmp + TableName):
              file = file[0]
              
              if file[-8:] == "_SUCCESS":
                print("PRA DELETAR: " + file)
                dbutils.fs.rm(file)
              else:
                df = spark.read.format('csv').options(header = 'false', delimiter = ',', nullValue='null').load(file)

                fieldsNames = df.select(collect_list(col('_c0'))).first()[0]
                #dataTypes = df.select(collect_list(col('_c1'))).first()[0]
                
                # CREATE DATAFRAME WITH RIGHT DATATYPES BASED ON DATA, BUT HAS NO HEADER
                df = spark.read.format('csv') \
                          .options(header = 'false', delimiter = ',', nullValue='null') \
                          .option("quote", '"') \
                          .option("mode", "PERMISSIVE") \
                          .option("inferSchema","true") \
                          .load(filePath)
              
                dflistColumns = df.columns

                mapping = dict(zip(dflistColumns, fieldsNames))
                df.select([col(c).alias(mapping.get(c, c)) for c in df.columns]) \
                  .write.format('csv')\
                  .mode('overwrite')\
                  .option('compression', 'gzip')\
                  .option('header', 'false')\
                  .option('delimiter', ',')\
                  .option('nullValue', 'null')\
                  .option('path', filePath)\
                  .saveAsTable(TableName)


# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## 2 - CREATE TABLES ON DATABRICKS BASED ON CSV FILES STORED ON AZURE DATA LAKE THAT WERE PARSED FROM .mdb TO .csv

# COMMAND ----------

# MAGIC %md 
# MAGIC THE PROCCESS IS GENERIC, SO TO ADAPT FOR YOUR PROCESS JUST CHANGE THE VARIABLES "db_mdb" AND "source_mdb".
# MAGIC $db_mdb = Correspond the database name and also used as path for mount                                                     
# MAGIC $source_mdb = Path on Azure Data Lake where the files will be read

# COMMAND ----------

# MAGIC %md
# MAGIC #How does it works ?
# MAGIC 
# MAGIC 
# MAGIC The script will create the database if not exists using the variable $db_mdb, then use it and also will be used on mount if necessary. After that will list all files stored on "$source_mdb" to get the names foreach table, so will check which files are not name by "part-" and delete them, the process just use files named by "part-". 
# MAGIC 
# MAGIC So all files will be written as tables on Databricks using Spark.

# COMMAND ----------

#db Vars
db_mdb = "MDB"
mount_point_mdb = "/mnt/" + db_mdb
source_mdb = "adl://ddpazfslab.azuredatalakestore.net/refined/refining_operations/processes/grtmps/"

# COMMAND ----------

###########################################################
#### MOUNT ALREADY DONE !! JUST EXECUTE FOR NEW MOUNTS ####
###########################################################

# unmount 
#dbutils.fs.unmount(mount_point = mount_point_tmp)

# mount
#dbutils.fs.mount(
#  source = source_mdb,
#  mount_point = mount_point_mdb,
#  extra_configs = configs)

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

#create database
spark.sql("create database if not exists " + db_mdb + "_teste")

#drop database and all tables
#spark.sql("drop database if  exists XXX cascade")

# use database
spark.sql("use " + db_mdb + "_teste")

for allFiles in dbutils.fs.ls(source_mdb):
    
    TableName = allFiles[1][:-1]
    tablePath = allFiles[0]

    for file in dbutils.fs.ls(tablePath):
      file = file[0]
      fileToDel = file.split("/")[8]
      
      if fileToDel[0] == "_":
        print("PRA DELETAR:" + file)
        dbutils.fs.rm(file)

      df = spark.read.format('csv') \
                .options(header = 'true', delimiter = ',', nullValue='null') \
                .option("quote", '"') \
                .option("mode", "PERMISSIVE") \
                .option("inferSchema","true") \
                .load(file)

      df.coalesce(1) \
        .write.format('csv')\
        .mode('overwrite')\
        .option('compression', 'gzip')\
        .option('header', 'true')\
        .option('delimiter', ',')\
        .option('nullValue', 'null')\
        .option('path', tablePath)\
        .saveAsTable(TableName)

