import requests
import json

def create_notification_stub():
    wiremock_base_url = "http://localhost:8082"
    response_body_template = """{
  "resourceType": "{{jsonPath request.body '$.resourceType'}}",
  "id": "{{jsonPath request.body '$.id'}}",
  "status": "active",
  "reason": "{{jsonPath request.body '$.reason'}}",
  "criteria": "{{jsonPath request.body '$.criteria'}}",
  "channel": {
    "type": "{{jsonPath request.body '$.channel.type'}}",
    "endpoint": "{{jsonPath request.body '$.channel.endpoint'}}",
    "payload": "{{jsonPath request.body '$.channel.payload'}}"
  }
}"""
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/Claim/subscribe",
          },
          
        "response": {
            "status": 200,
            "body": response_body_template,
            "transformers": ["response-template"],
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
        }
        # "response": {
        #     "status": 200,
        #     "headers": {
        #         "Content-Type": "application/json",
        #         "Access-Control-Allow-Origin": "*",
        #         "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        #         "Access-Control-Allow-Headers": "Content-Type, Authorization"
        #     },
        #     "jsonBody": response_body,
        #     "transformers": ["response-template"]
        # }
    }
    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print("Stub created successfully")

def main():
    print("inside the main------")
    create_notification_stub()
if __name__ == "__main__":
    main()