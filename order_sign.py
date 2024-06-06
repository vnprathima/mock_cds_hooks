import requests

def create_stub(code, response_body):
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/cds-services/mettles-order-sign",
            "bodyPatterns": [
                {
                    "matchesJsonPath": f"$.context.draftOrders.entry[0].resource.code.coding[?(@.code == '{code}')]"
                },
                
            ]
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
            # "fixedDelayMilliseconds": 100000
        }
    }
    options_mapping = {
        "request": {
            "method": "OPTIONS",
            "url": "/cds-services/mettles-order-sign"
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
    print(f"OPTIONS stub created successfully")

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"POST stub for code {code} created successfully")

def main():
    
    codes = [{
                "code": "15823",
                "display": "Blepharoplasty, upper eyelid; with excessive skin weighting down lid",
                "system": "https://www.aapc.com/resources/medical-coding/cpt.aspx"
            },
            {
                "code": "1315009",
                "display": "Reconstruction of eyebrow",
                "system": "http://snomed.info/sct"
            },
            {
                "code": "119000",
                "display": "Thoracoscopic partial lobectomy of lung",
                "system": "http://snomed.info/sct"
            },
            {
                "code": "166001",
                "display": "Behavioral therapy",
                "system": "http://snomed.info/sct"
            }]
    
    for code in codes:
        response_body = {
            "cards":[],
            "systemActions": [
                {
                    "description": "Update to your resource",
                    "resource": {
                        "id": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.id'}}",
                        "authoredOn": "2024-03-11",
                        "code": {
                            "coding": [
                                {
                                    "code": code["code"],
                                    "display": code["display"],
                                    "system": code["system"]
                                }
                            ],
                            "text": code["display"]
                        },
                        "encounter": {
                            "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.encounter.reference'}}"
                        },
                        "insurance": [
                            {
                                "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.insurance[0].reference'}}"
                            }
                        ],
                        "intent": "order",
                        "occurrenceDateTime": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.occurrenceDateTime'}}",
                        "priority": "routine",
                        "quantityQuantity": {
                            "value": 1
                        },
                        "requester": {
                            "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.requester.reference'}}"
                        },
                        "status": "active",
                        "subject": {
                            "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.subject.reference'}}"
                        },
                        "resourceType": "ServiceRequest"
                    },
                    "resourceId": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.id'}}",
                    "type": "create"
                }
            ]
        }
        
        if code["code"] == "15823":
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
                                "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.insurance[0].reference'}}"
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
        
        if code["code"] == "1315009":
            response_body["systemActions"][0]["resource"]["extension"] = [
                {
                    "extension": [
                        {
                            "url": "coverage",
                            "valueReference": {
                                "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.insurance[0].reference'}}"
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
                            "valueCode": "no-auth"
                        },
                        {
                            "url": "covered",
                            "valueCode": "covered"
                        }
                    ],
                    "url": "http://hl7.org/fhir/us/davinci-crd/StructureDefinition/ext-coverage-information"
                }
            ]

        if code["code"] == "119000":
            response_body["systemActions"][0]["resource"]["extension"] = [
                {
                    "extension": [
                        {
                            "url": "coverage",
                            "valueReference": {
                                "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.insurance[0].reference'}}"
                            }
                        },
                        {
                            "url": "date",
                            "valueDate": "2024-ydhgfd05-14"
                        },
                        {
                            "url": "identifier",
                            "valueString": "new 123"
                        },
                        {
                            "url": "pa-needed",
                            "valueCode": "no-auth"
                        },
                        {
                            "url": "covered",
                            "valueCode": "not-covered"
                        }
                    ],
                    "url": "http://hl7.org/fhir/us/davinci-crd/StructureDefinition/ext-coverage-information"
                }
            ]
                        
        if code["code"] == "166001":
            response_body["systemActions"][0]["resource"]["extension"] = [
                {
                    "extension": [
                        {
                            "url": "coverage",
                            "valueReference": {
                                "reference": "{{jsonPath request.body '$.context.draftOrders.entry[0].resource.insurance[0].reference'}}"
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
                            "valueCode": "no-auth"
                        },
                        {
                            "url": "covered",
                            "valueCode": "covered"
                        },
                        {
                            "url": "doc-needed",
                            "valueCode": "clinical"
                        },
                        {
                            "url": "questionnaire",
                            "valueCanonical": "https://fhir-dev.mettles.com/baseServer/fhir/Questionnaire/questionnaire-lcd1-eyelidsurgery"
                        }
                    ],
                    "url": "http://hl7.org/fhir/us/davinci-crd/StructureDefinition/ext-coverage-information"
                }
            ]

        create_stub(code["code"], response_body)

if __name__ == "__main__":
    main()
