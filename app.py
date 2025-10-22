from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample "database"
products = {
    "PROD1": {"name": "Custom Hoodie", "price": 500.0},
    "PROD2": {"name": "Custom Mug", "price": 200.0}
}
orders = {
    # Example: "ORD123": {"status": "pending"}
}

#Dummy order for testing
orders["ORD123"] = {"status": "confirmed"}

SHIPPING_FEE = 50.0

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

@app.route('/api/order/summary', methods=['POST'])
def order_summary():
    data = request.get_json()
    if not data or "productId" not in data or not data["productId"]:
        return jsonify({"message": "productId required"}), 400
    if data["productId"] not in products:
        return jsonify({"message": "Product not found"}), 404
    if "quantity" not in data:
        return jsonify({"message": "quantity required"}), 400
    try:
        qty = int(data["quantity"])
    except:
        return jsonify({"message": "Quantity must be an integer"}), 400
    if qty < 1:
        return jsonify({"message": "Quantity must be at least 1"}), 400
    if "customText" in data and len(data["customText"]) > 100:
        return jsonify({"message": "customText too long"}), 400
    if "customImageUrl" in data and data["customImageUrl"]:
        if not is_valid_url(data["customImageUrl"]):
            return jsonify({"message": "customImageUrl must be a valid URL"}), 400
   
    price = products[data["productId"]]['price']
    subtotal = price * qty
    total = subtotal + SHIPPING_FEE
    return jsonify({
        "subtotal": subtotal,
        "shippingFee": SHIPPING_FEE,
        "total": total
    }), 200

@app.route('/api/order/status/<orderId>', methods=['GET'])
def order_status(orderId):
    if orderId not in orders:
        return jsonify({"message": "Order not found"}), 404
    return jsonify({
        "orderId": orderId,
        "orderStatus": orders[orderId]['status']
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
