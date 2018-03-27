import mysql.connector as connector
from string import Template
import yaml

def main():
    with open('dbconfig.yml', 'r') as config:
        dbconfig = yaml.load(config)

    try:
        connection = connector.connect(**dbconfig['mysql'])
        cursor = connection.cursor(dictionary=True, buffered=True)

        cursor.execute("select id, naming_element from naming_elements_tagged_type_1")
        cursor_for_update = connection.cursor(dictionary=True, buffered=True)
        for elem in (cursor):
            query = "update naming_elements_tagged_type_1 set naming_position = 'PRE' where id = '{id}'".format(**dict(id = elem['id']))
            print(query)
            cursor_for_update.execute(query)
        cursor_for_update.close()
        connection.commit()
        cursor.close()
    except Exception as e:
        print(e)
    else:
        connection.close()

if __name__ == "__main__":
    main()
