# -ITMGT-45.03-GC-Mini-Project

# Custom Product Ordering API

A simple Flask-based REST API for placing custom product orders and tracking their statuses. This project demonstrates basic endpoint design, input validation, and error handling using Flask.

## Features

- View a summary of an order, including product details, quantity, subtotal, shipping, and total.
- Check the status of an existing order.
- Input validation for product IDs, quantity, custom text, and custom image URLs.

## Tech Stack

- Python 3
- Flask (Web Framework)

## Installation

1. Clone this repository or copy the source files.
2. Make sure Python 3 is installed.
3. Install dependencies using pip:

   ```bash
   pip install Flask
   ```

4. Run the application:

   ```bash
   python app.py
   ```

## API Usage

### 1. Order Summary

**Endpoint:**  
`POST /api/order/summary`

**Request JSON Example:**  
```json
{
  "productId": "PROD1",
  "quantity": 2,
  "customText": "Happy Birthday!",
  "customImageUrl": "https://example.com/image.png"
}
```

**Response Example:**  
```json
{
  "subtotal": 1000.0,
  "shippingFee": 50.0,
  "total": 1050.0
}
```

**Error Responses:**
- 400: Missing or invalid fields
- 404: Product not found

### 2. Order Status

**Endpoint:**  
`GET /api/order/status/<orderId>`

**Example:**  
`GET /api/order/status/ORD123`

**Response Example:**  
```json
{
  "orderId": "ORD123",
  "orderStatus": "confirmed"
}
```

**Error Responses:**
- 404: Order not found

## Testing

Sample `curl` commands for testing endpoints:

```bash
# Order summary (success)
curl -X POST http://127.0.0.1:5000/api/order/summary -H "Content-Type: application/json" -d "{\"productId\":\"PROD1\",\"quantity\":2,\"customText\":\"Happy Birthday!\"}"

# Order summary (invalid quantity)
curl -X POST http://127.0.0.1:5000/api/order/summary -H "Content-Type: application/json" -d "{\"productId\":\"PROD1\",\"quantity\":0}"

# Order status (success with demo order)
curl http://127.0.0.1:5000/api/order/status/ORD123

# Order status (error, non-existing order)
curl http://127.0.0.1:5000/api/order/status/NOTREAL
```

## Limitations
#Data resets with every server restart (no database)
#Only two sample products available
#No authentication, so all endpoints are public
#Input checks are basic (e.g., URLs, text length)
#Intended for demonstration, not production use​
