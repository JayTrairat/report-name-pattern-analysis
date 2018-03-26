import mysql.connector as connector
from string import Template

def main():
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'naming_analysis'
    }
    try:
        connection = connector.connect(**config)
        for index in range(0, 8):

            content = []
            with open(('assets/type_{type}/output_only_{type}_export.csv').format(**dict(type = str(index+1))), 'r', encoding='utf8') as file:
                contents = file.readlines()
                contents = [content.strip() for content in contents]
                contents = [content.split('|') for content in contents]

            cursor = connection.cursor(dictionary=True)
            cursor.execute(("truncate naming_elements_original_type_{type}").format(**dict(type = str(index+1))))
            connection.commit()

            for content in contents:
                for item in content:
                    query_1 = ("insert into naming_elements_original_type_{type}(datatype_id, naming_element, naming_position) values('{datatype_id}', '{naming_element}', '{naming_position}')")
                    query_2 = ("insert into naming_elements_tagged_type_{type}(datatype_id, naming_element, naming_position) values('{datatype_id}', '{naming_element}', '{naming_position}')")
                    vars = dict(
                        type = str(index+1),
                        datatype_id = '0',
                        naming_element = item,
                        naming_position = 'UNKNOWN'
                    )
                    cursor.execute(query_1.format(**vars))
                    cursor.execute(query_2.format(**vars))
                    connection.commit()

            cursor.close()

    except connector.Error as error:
        print(error)
    else:
        connection.close()

if __name__ == "__main__":
    main()
