from flask import Blueprint, jsonify, current_app, request
import mysql.connector

def get_db_cursor():
    connection = mysql.connector.connect(**current_app.config['DB_CONFIG'])
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

def fetch_query_results(query, pot_id, fetchone=False):
    connection, cursor = get_db_cursor()
    if pot_id is not None:
        cursor.execute(query, (pot_id,))
    else:
        cursor.execute(query)
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/ping")
def ping():
    return jsonify({"message": "API läuft"})

@views_blueprint.route("/average-measurements", methods=["GET"])
def average_measurements():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = "SELECT * FROM viw_AllValues_Today WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route("/sunlight-30days", methods=["GET"])
def get_sunlight_30days():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = "SELECT * FROM viw_SunlightPerDay_last30Days WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route('/latest-value', methods=['GET'])
def get_latest_value():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = '''
        SELECT created, temperature, air_humidity, ground_humidity
        FROM viw_LatestValuePerPot
        WHERE pot_id = %s
    '''
    return fetch_query_results(query, pot_id, fetchone=True)

@views_blueprint.route("/all-pot-ids", methods=["GET"])
def get_all_pot_ids():
    query = "SELECT DISTINCT pot_id FROM viw_LatestValuePerPot"
    return fetch_query_results(query, pot_id=None)
