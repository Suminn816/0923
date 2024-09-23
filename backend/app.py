from flask import Flask, jsonify, request

app = Flask(__name__)
diaries = []
id_counter = 1

@app.route('/diary', methods =['GET', 'POST'])
def handle_diaries():
    if request.method == 'GET':
        return jsonify({'message': '일기 조회', 'diary': '다이어리 목록들'}), 200
    elif request.method == 'POST':
        body = request.json
        return jsonify({'message': '일기가 추가되었습니다.', 'diary': body}), 201
    return jsonify({'message':'hello'})


if __name__ == '__main__':
    app.run(debug=True)
