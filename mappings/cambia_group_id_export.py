import requests

def create_stub():
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "GET",
            "url": "/7bb58dbd-c45c-409a-8ca0-c14c97c19c2d/$davinci-data-export"
        },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/x-ndjson",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
                "Content-Location": "http://localhost:8082/Group/export-status"
            }
        }
    }

    url = f"{wiremock_base_url}/__admin/mappings"
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print("Stub created successfully")

if __name__ == "__main__":
    create_stub()
