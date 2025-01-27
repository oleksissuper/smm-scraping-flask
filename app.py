from flask import Flask, jsonify, request
from flask_cors import CORS
from config.settings import settings
from db.get_records import Records


app = Flask(__name__)
CORS(app)


@app.route('/api/networks', methods=['GET'])
def get_networks():
    datas = {
        "networks": settings.services.networks,
        "filters": settings.services.filters
    }
    return jsonify(datas)

@app.route('/api/records', methods=['POST'])
def get_records():
    try:
        request_data = request.json
        records = Records().get(request_data)
        return jsonify({"status":True, "records": records})
    except Exception as ex:
        print(ex)
    return jsonify({"status": False, "error": "something wrong with API"})



if __name__ == '__main__':
    app.run(debug=True)