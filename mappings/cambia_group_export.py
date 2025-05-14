import requests

def create_stub():
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "GET",
            "url": "/Group/export-status"
        },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/x-ndjson",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
            "jsonBody": {
                "transactionTime": "2024-11-04T12:15:48.201768991",
                "request": "https://fhir-uat.cambiahealth.com/paa/v1/bulkstatus/8874f3e6-952b-4313-bfee-efa11e22d86d",
                "requiresAccessToken": True,
                "output": [
                    {
                        "type": "Patient",
                        "count": 2,
                        "url": "https://test.nucural.com/wiremock/cambia_patient"
                    },
                    {
                        "type": "Coverage",
                        "count": 2,
                        "url": "https://test.nucural.com/wiremock/cambia_coverage"
                    },
                    {
                        "type": "ExplanationOfBenefit",
                        "count": 4,
                        "url": "https://test.nucural.com/wiremock/cambia_explanationOfBenefit"
                    },
                    {
                        "type": "Condition",
                        "count": 4,
                        "url": "https://test.nucural.com/wiremock/cambia_condition"
                    },
                    {
                        "type": "Observation",
                        "count": 4,
                        "url": "https://test.nucural.com/wiremock/cambia_observation"
                    }
                ],
                "error": []
            }
        }
    }

    url = f"{wiremock_base_url}/__admin/mappings"
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print("Stub created successfully")

if __name__ == "__main__":
    create_stub()
