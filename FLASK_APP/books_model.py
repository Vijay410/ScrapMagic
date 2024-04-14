import mysql.connector
import json
from datetime import datetime
from flask import make_response, jsonify,request
class BooksModel:
    """
    A class to handle user-related operations in a database.
    """

    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='***',
                database='books'
            )
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print('Database connected Successfully')
        except Exception as e:
            print('Unable to connect to database', e)

    def get_books_data(self,current_user):

            self.cur.execute(f"SELECT * FROM books order by id ")
            result = self.cur.fetchall()
            if result:
                return make_response({'response':result})
            else:
                return make_response({'response':"No Data Found"})

    def create_books(self,books_Data):
            "Create API"

            # Extract book data from the request
            if not isinstance(books_Data, list):
                return make_response({'response': 'Invalid data format'}, 400)  # 400 for Bad Request status
            try:
                for book_data in books_Data:
                    required_keys = {'title', 'price', 'category', 'availability', 'product_type'}
                    if not all(key in book_data for key in required_keys):
                        return make_response({'response': f'Missing or incorrect keys: {", ".join(required_keys)}'}, 400)
                    title = book_data.get('title')
                    price = book_data.get('price')
                    category = book_data.get('category')
                    availability = book_data.get('availability')
                    product_type = book_data.get('product_type')
                    print(title,price,category,availability,product_type)
                    # Add more attributes as needed
                    self.cur.execute("INSERT INTO books (title, price, category, availability, product_type) VALUES (%s, %s, %s, %s, %s)",
                                        (title, price, category, availability, product_type))
                self.con.commit()  # Commit the transaction
                return make_response({'response': 'Books created successfully'}, 201)  # 201 for Created status
            
            except Exception as e:
                self.con.rollback()  # Rollback the transaction if an error occurs
                return make_response({'response': f'Error: {str(e)}'}, 500)  # 500 for Internal Server Error status

    def update_data(self, books_data,id):
        """ Update table based on id """
        print(id)
        for books in books_data:
            self.cur.execute(f"UPDATE books set title = '{books.get('title')}' where id = {id} ")
        return "Data Updated Sucessfully"

    def delete_data(self, id):
        if id:
            self.cur.execute(f"DELETE FROM books WHERE id={id}")
            return make_response({"message": "DELETED_SUCCESSFULLY"}, 202)
        return make_response({"message": "CONTACT_DEVELOPER"}, 500)
