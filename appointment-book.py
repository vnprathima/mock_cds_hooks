import requests


def create_stub(response_body):
    wiremock_base_url = "http://localhost:8082"

    mapping = {
        "request": {
            "method": "POST",
            "url": "/cds-services/mettles-appointment-book",
        },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
            "jsonBody": response_body,
            "transformers": ["response-template"]
        }
    }
    options_mapping = {
        "request": {
            "method": "OPTIONS",
            "url": "/cds-services/mettles-appointment-book"
        },
        "response": {
            "status": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            }
        }
    }

    # Create OPTIONS stub
    options_url = f"{wiremock_base_url}/__admin/mappings"
    options_response = requests.post(options_url, json=options_mapping)
    options_response.raise_for_status()
    print(f"OPTIONS stub for appointment-book created successfully")

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"POST stub for appointment-book created successfully")


def main():

    response_body = {
        "cards": [
            {
                "summary": "Pre-appointment reminders",
                "detail": "The patient is due for a flu shot. Recommend scheduling an immunization at the same visit.",
                "indicator": "info",
                "source": {
                    "label": "Immunization Reminder Service",
                    "url": "https://ehr.example.com/cds-services/immunization"
                },
                "suggestions": [
                    {
                        "label": "Schedule flu shot",
                        "actions": [
                            {
                                "type": "create",
                                "resource": {
                                    "resourceType": "ServiceRequest",
                                    "status": "active",
                                    "intent": "order",
                                    "code": {
                                        "coding": [
                                            {
                                                "system": "http://snomed.info/sct",
                                                "code": "86198006",
                                                "display": "Influenza vaccination"
                                            }
                                        ]
                                    },
                                    "subject": {
                                        "reference": "{{jsonPath request.body '$.context.patientId'}}"
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "systemActions": [

                            {
                                "description": "create the resource",
                                "type": "create",
                                "resource": {
                                    "resourceType": "ServiceRequest",
                                    "status": "active",
                                    "intent": "order",
                                    "code": {
                                        "coding": [
                                            {
                                                "system": "http://snomed.info/sct",
                                                "code": "86198006",
                                                "display": "Influenza vaccination"
                                            }
                                        ]
                                    },
                                    "subject": {
                                        "reference": "{{jsonPath request.body '$.context.patientId'}}"
                                    }
                                }
                            }
                        ]
    }
    create_stub(response_body)


if __name__ == "__main__":
    main()
