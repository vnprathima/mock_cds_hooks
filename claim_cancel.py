import requests

def create_stub(response_body):
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/Claim/$cancel",
          },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
            "jsonBody": response_body,
            "transformers": ["response-template"]
        }
    }
    options_mapping = {
        "request": {
            "method": "OPTIONS",
            "url": "/Claim/$cancel"
        },
        "response": {
            "status": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            }
        }
    }

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"DELETE stub for Claim/$cancel created successfully")

def main():
        response_body = {
            "resourceType": "OperationOutcome",
            "issue": [
                {
                    "severity": "information",
                    "code": "informational",
                    "details": {
                        "text": "Claim successfully cancelled"
                    }
                }
            ]
        }
        create_stub(response_body)

if __name__ == "__main__":
    main()
