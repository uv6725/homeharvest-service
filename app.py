from flask import Flask, request, jsonify, send_from_directory
from homeharvest import scrape_property
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/property', methods=['GET'])
def get_property():
    address = request.args.get('address')
    zip_code = request.args.get('zip')
    listing_type = request.args.get('listing_type', 'for_sale')
    
    if not address:
        return jsonify({'error': 'Address parameter is required'}), 400
    
    try:
        location = address
        if zip_code:
            location = f"{address}, {zip_code}"
        
        properties = scrape_property(location=location, listing_type=listing_type)
        
        if properties.empty:
            return jsonify({'message': 'No properties found', 'location': location}), 404
        
        property_list = properties.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'count': len(property_list),
            'properties': property_list
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500

@app.route('/property', methods=['POST'])
def get_property_post():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    address = data.get('address')
    zip_code = data.get('zip')
    listing_type = data.get('listing_type', 'for_sale')
    
    if not address:
        return jsonify({'error': 'Address field is required'}), 400
    
    try:
        location = address
        if zip_code:
            location = f"{address}, {zip_code}"
        
        properties = scrape_property(location=location, listing_type=listing_type)
        
        if properties.empty:
            return jsonify({'message': 'No properties found', 'location': location}), 404
        
        property_list = properties.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'count': len(property_list),
            'properties': property_list
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
