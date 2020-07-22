import configparser
import sqlalchemy
import os
import pandas as pd

# Get properties for database connectivity and mode from ConfigFile
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'ConfigFile.properties')
config = configparser.RawConfigParser()
config.read(initfile)
database_username = config.get('DatabaseSection', 'database_username')
database_password = config.get('DatabaseSection', 'database_password')
database_ip = config.get('DatabaseSection', 'database_ip')
database_name = config.get('DatabaseSection', 'database_name')
data_importer_mode = config.get('DatabaseSection', 'database_mode')

# create connection
database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                      database_ip, database_name))


def read_data_from_db_table(table_name):
    metadata = sqlalchemy.MetaData()
    census = sqlalchemy.Table(table_name, metadata, autoload=True, autoload_with=database_connection)
    # query data
    query = sqlalchemy.select([census])
    result_proxy = database_connection.execute(query)
    result_set = result_proxy.fetchall()
    result_dataframe = pd.DataFrame(result_set)
    # Set dataframe columns to be the same as database columns
    result_dataframe.columns = result_set[0].keys()
    return result_dataframe

