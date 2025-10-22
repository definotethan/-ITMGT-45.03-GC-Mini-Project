Ethan Aquino, Arianna Chan, Paul Kim, Harmonie Lin

**GC Mini-Project: “Ship One Useful API”**

| Context |
| :---: |

Feature / flow this supports: 

- Product customization and order management in the CustomKeeps e‑commerce application, enabling customers to configure and purchase personalized items.

User outcome (what becomes possible): 

- Customers can quickly compute an order total including product price, quantity, and shipping fee, and check the current order status.

Why this is a win today: 

- Demonstrates a complete order quoting and tracking flow (calculate + status check) using an in‑memory data model without requiring authentication or persistence, suitable for rapid iteration and testing.

| API Choice |
| :---: |

Calculate:

- POST /api/order/summary: returns order subtotal, shipping fee, and total based on selected product and quantity.

Update Status:

- GET /api/order/status/:orderId: returns current order status for an existing order ID.

| Endpoint Mini-Spec |
| :---: |

**POST /api/order/summary**

Purpose: 

- Returns an itemized order total with validations for product existence, quantity, and optional customization.

Request Body (JSON):

{  
  "productId": "PROD1",  
  "quantity": 2,  
  "customText": "Happy Birthday\!",  
  "customImageUrl": "https://example.com/design.png"  
}  
Sample Success Response (200 OK):  
{  
  "subtotal": 1000.0,  
  "shippingFee": 50.0,  
  "total": 1050.0  
}  
Validation & Error Responses:

| Scenario | Response |
| :---- | :---- |
| MissingproductId | 400 → {"message":"productId required"} |
| Unknown productId | 404 → {"message":"Product not found"} |
| Missingquantity | 400 → {"message":"quantity required"} |
| Non‑integer quantity | 400 → {"message":"Quantity must be an integer"} |
| Quantity \< 1 | 400 → {"message":"Quantity must be at least 1"} |
| customText\> 100 chars | 400 → {"message":"customText too long"} |
| Invalid URL incustomImageUrl | 400 → {"message":"customImageUrl must be a valid URL"} |
| Unexpected error | 500 → {"message":"Something went wrong"} |

Validation Rules:

- productId: required; must be one of PROD1, PROD2.  
- quantity: required integer ≥ 1.  
- customText: optional; ≤ 100 characters.  
- customImageUrl: optional; valid HTTP/HTTPS URL if provided.

Computation Logic:

- Subtotal = product.price × quantity  
- Shipping Fee = 50.0  
- Total = subtotal + shippingFee


**GET /api/order/status/:orderId**

Purpose:

- Fetches current order status from the in‑memory orders dictionary.

Sample Path:

- /api/order/status/ORD123

Sample Success Response (200 OK):

{  
  "orderId": "ORD123",  
  "orderStatus": "confirmed"  
}  
Validation & Error Responses:

| Scenario | Response |
| :---- | :---- |
| UnknownorderId | 404 → {"message":"Order not found"} |
| Unexpected error | 500 → {"message":"Something went wrong"} |

Validation Rules:

- orderId: required; must exist in orders dict.

| Test-Plan |
| :---: |

| Endpoint | Scenario | Request (curl) | Expected Status | Expected Response |
| :---- | :---- | :---- | :---- | :---- |
| POST /api/order/summary | ✅ Happy path – valid product and quantity | curl \-X POST http://127.0.0.1:5000/api/order/summary \-H "Content-Type: application/json" \-d '{"productId":"PROD1","quantity":2,"customText":"Happy Birthday\!"}' | 200 OK | { "subtotal": 1000.0, "shippingFee": 50.0, "total": 1050.0 } |
| POST /api/order/summary | ❌ Error – quantity = 0 | curl \-X POST http://127.0.0.1:5000/api/order/summary \-H "Content-Type: application/json" \-d '{"productId":"PROD1","quantity":0}' | 400 Bad Request | { "message": "Quantity must be at least 1" } |
| GET /api/order/status/:orderId | ✅ Happy path – existing order | curl http://127.0.0.1:5000/api/order/status/ORD123 | 200 OK | { "orderId": "ORD123", "orderStatus": "confirmed" } |
| GET /api/order/status/:orderId | ❌ Error – non‑existent order | curl http://127.0.0.1:5000/api/order/status/NOTREAL | 404 Not Found | { "message": "Order not found" } |

