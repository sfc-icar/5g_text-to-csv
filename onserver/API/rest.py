from flask import Blueprint, request, abort, jsonify,Flask
import pymysql.cursors
import json

app = Flask(__name__)

@api.route('/xyz', methods=['GET'])
def list_user():
    conn = pymysql.connect(
        host='localhost',
        user='feles5g',
        db='5gfeles',
        charset='utf8mb4',
        password='local5g',
        cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cursor:
        sql = "SELECT lat,lon,alt,SNR FROM gndr_main"
        cursor.execute(sql)
        result = cursor.fetchall()
    enc = json.dumps(result)
    return enc


#@api.route('/xyz/<int:user_id>', methods=['GET'])
#def get_user(user_id=None):
#    user = User.query.filter_by(id=user_id).first()
#    return jsonify(user.to_dict())


@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
