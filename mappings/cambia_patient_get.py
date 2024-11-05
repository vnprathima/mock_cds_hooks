import requests

def create_stub():
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "GET",
            "url": "/cambia_patient"
        },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/x-ndjson",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
            "bodyFileName": "cambia_patient.ndjson"
        }
    }

    url = f"{wiremock_base_url}/__admin/mappings"
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print("Stub created successfully")

if __name__ == "__main__":
    create_stub()
