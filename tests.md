API Testing Artifacts

Happy Path
Request:
curl -X POST http://127.0.0.1:5000/api/order/summary -H "Content-Type: application/json" -d "{\"productId\":\"PROD1\",\"quantity\":2,\"customText\":\"Happy Birthday!\"}"

Expected Response:
{
  "shippingFee": 50.0,
  "subtotal": 1000.0,
  "total": 1050.0
}

Error Case
Request:
curl http://127.0.0.1:5000/api/order/status/NOTREAL

Expected Response:
{
  "message": "Order not found"

}
