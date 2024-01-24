from flask import Flask, jsonify
from conect import success__database , close_database


app = Flask(__name__)


@app.route('/all', methods=['GET'])
def all_api():
    database_connect  = success__database()
    
    if database_connect :
        try:
            cursor = database_connect.cursor()
            
            cursor.execute("SELECT * FROM items")
            response     = cursor.fetchall()
            api_response =  [{'id': response_data[0], 'name': response_data[1]} for response_data in response]
            
            close_database(database_connect  , cursor)
            
            return jsonify(api_response)
        
        except Exception as error:
             return jsonify({'error': str(error)}), 500
        finally:
            close_database(database_connect , cursor)
        
    return jsonify({'error': 'Erro data base'}), 500

if __name__ == '__main__':
    app.run(debug=True)
            
        

        