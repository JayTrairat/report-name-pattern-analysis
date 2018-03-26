from mysql import connector as connector
import yaml

def main():
    try:
        config = []
        with open('dbconfig.yml', 'r') as e:
            config = yaml.load(e)

        connection = connector.connect(**config['mysql'])
        cursor = connection.cursor(dictionary=True)

        for index in range(0, 8):

            with open('sql_assets/naming_elements_original_type_' + str(index+1) + '.sql', 'r') as sqlcommand:
                result = cursor.execute(sqlcommand.read())

            with open('sql_assets/naming_elements_tagged_type_' + str(index+1) + '.sql', 'r') as sqlcommand:
                result = cursor.execute(sqlcommand.read())

        cursor.close()
        connection.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
