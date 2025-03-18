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
        "cards": [],
        "systemActions": [
            {
                "description": "Update to your resource",
                "resourceId": "{{jsonPath request.body '$.context.appointments[0].id'}}",
                "type": "update"
            }
        ]
    }
    response_body["systemActions"][0]["resource"] = {
        "id": "{{jsonPath request.body '$.context.appointments[0].id'}}",
        "appointmentType": {
            "coding": [
                {
                    "code": "{{jsonPath request.body '$.context.appointments[0].appointmentType.coding[0].code'}}",
                    "display": "{{jsonPath request.body '$.context.appointments[0].appointmentType.coding[0].display'}}",
                    "system": "{{jsonPath request.body '$.context.appointments[0].appointmentType.coding[0].system'}}"
                }
            ],
            "text": "{{jsonPath request.body '$.context.appointments[0].appointmentType.text'}}"
        },
        "basedOn": [
            {
                "reference": "{{jsonPath request.body '$.context.appointments[0].basedOn[0].reference'}}"
            }
        ],
        "description": "{{jsonPath request.body '$.context.appointments[0].description'}}",
        "start": "{{jsonPath request.body '$.context.appointments[0].start'}}",
        "end": "{{jsonPath request.body '$.context.appointments[0].end'}}",
        # "participant": "{{jsonPath request.body '$.context.appointments[0].participant'}}",
        # "speciality":"{{jsonPath request.body '$.context.appointments[0].speciality'}}",
        "participant": [
            {
                "actor": {
                    "reference": "{{jsonPath request.body '$.context.appointments[0].participant[0].actor.reference'}}"
                },
                "required": "{{jsonPath request.body '$.context.appointments[0].participant[0].required'}}",
                "status": "{{jsonPath request.body '$.context.appointments[0].participant[0].status'}}"
            },
            {
                "actor": {
                    "reference": "{{jsonPath request.body '$.context.appointments[0].participant[1].actor.reference'}}"
                },
                "required": "{{jsonPath request.body '$.context.appointments[0].participant[1].required'}}",
                "status": "{{jsonPath request.body '$.context.appointments[0].participant[1].status'}}"
            }
        ],
        "status": "{{jsonPath request.body '$.context.appointments[0].status'}}",
        "resourceType": "{{jsonPath request.body '$.context.appointments[0].resourceType'}}"
    }

    response_body["systemActions"][0]["resource"]["extension"] = [
        {
            "extension": [
                {
                    "url": "coverageInfo",
                    "valueCoding": {
                        "code": "covered-prior-auth",
                        "display": "Covered with prior authorization",
                        "system": "http://hl7.org/fhir/us/davinci-crd/CodeSystem/temp"
                    }
                },
                {
                    "url": "questionnaire",
                    "valueCanonical": "https://fhir-dev.mettles.com/baseServer/fhir/Questionnaire/questionnaire-lcd1-eyelidsurgery"
                },
                {
                    "url": "coverage",
                    "valueReference": {
                        "reference": 'Coverage/'"{{jsonPath request.body '$.prefetch.coverageBundle.entry[0].resource.id'}}"
                    }
                },
                {
                    "url": "date",
                    "valueDate": "2024-05-14"
                },
                {
                    "url": "identifier",
                    "valueString": "263adc54-ecf6-41b4-8ac8-055d0068c3fd"
                },
                {
                    "url": "pa-needed",
                    "valueCode": "auth-needed"
                },
                {
                    "url": "covered",
                    "valueCode": "covered"
                },
                {
                    "url": "doc-needed",
                    "valueCode": "clinical"
                }
            ],
            "url": "http://hl7.org/fhir/us/davinci-crd/StructureDefinition/ext-coverage-information"
        }
    ]

    # response_body = {
    #     "cards": [],
    #     "systemActions": [

    #                         {
    #                             "description": "create the resource",
    #                             "type": "create",
    #                             "resource": {
    #                                 "resourceType": "ServiceRequest",
    #                                 "status": "active",
    #                                 "intent": "order",
    #                                 "code": {
    #                                     "coding": [
    #                                         {
    #                                             "system": "http://snomed.info/sct",
    #                                             "code": "2731000",
    #                                             "display": "Serologic test for Influenza A virus (procedure)"
    #                                         }
    #                                     ]
    #                                 },
    #                                 "subject": {
    #                                     "reference": "{{jsonPath request.body '$.context.patientId'}}"
    #                                 }
    #                             }
    #                         }
    #                     ]
    # }

    create_stub(response_body)


if __name__ == "__main__":
    main()
