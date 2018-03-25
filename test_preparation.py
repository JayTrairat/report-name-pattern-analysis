import mysql.connector as connector
from string import Template

def main():
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'naming_analysis'
    }
    try:
        connection = connector.connect(**config)

        content = []
        with open('assets/type_1/output_only_1_export.csv', 'r') as file:
            # read contents each line into array
            contents = file.readlines()
            # remove empty line
            contents = [content.strip() for content in contents]
            # split content in each line by | seperator
            contents = [content.split('|') for content in contents]

        cursor = connection.cursor(dictionary=True)
        cursor.execute('truncate naming_elements')
        connection.commit()

        for content in contents:
            for item in content:
                query = ("insert into naming_elements(datatype_id, naming_element, naming_position) values('{datatype_id}', '{naming_element}', '{naming_position}')")
                vars = dict(
                    datatype_id = '0',
                    naming_element = item,
                    naming_position = 'UNKNOWN'
                )
                cursor.execute(query.format(**vars))
                connection.commit()

        cursor.close()

    except connector.Error as error:
        print(error)
    else:
        connection.close()

if __name__ == "__main__":
    main()
