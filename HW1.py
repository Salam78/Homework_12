import psycopg2
import txt as txt


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data


def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


def insert_data_to_database(data):
    connection = psycopg2.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table (data TEXT)")
    cursor.execute("INSERT INTO my_table VALUES (?)", (data,))
    connection.commit()
    connection.close()


def retrieve_data_from_database():
    connection = psycopg2.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT data FROM my_table")
    result = cursor.fetchone()
    connection.close()
    if result:
        return result[0]
    else:
        return None


file_path = 'Mobiles.txt'
data_to_insert = read_data_from_file(file_path)
insert_data_to_database(data_to_insert)

retrieved_data = retrieve_data_from_database()
if retrieved_data:
    output_file_path = 'output.txt'
    write_data_to_file(output_file_path, retrieved_data)
    print("Данные успешно извлечены из базы данных и записаны в файл:", output_file_path)
else:
    print("База данных пуста.")
