import requests

def create_stub(response_body):
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/Claim/$inquire",
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
            "url": "/Claim/$submit"
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
    print(f"OPTIONS stub for Claim/$submit created successfully")

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"POST stub for Claim/$submit created successfully")

def main():
    
        response_body = {
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "ClaimResponse",
                        "id": "1230",
                        "meta": {
                            "versionId": "1",
                            "lastUpdated": "2024-06-11T10:00:31.123+00:00"
                        },
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewAction",
                                "valueCode": "A2"
                            },
                            {
                                "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewActionReason",
                                "valueCode": "0U"
                            }
                        ],
                        "identifier": [
                            {
                                "system": "http://identifiers.mettles.com",
                                "value": "2LWL6CRK53Z00G7J"
                            },
                            {
                                "system": "http://mettles.com/identifiers/REVIEW_IDENTIFICATION_NUMBER",
                                "value": "QPBAC7391291509"
                            },
                            {
                                "system": "http://prior_auth",
                                "value": "677556c6-27d9-11ef-a034-65e441e9259f"
                            }
                        ],
                        "status": "active",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/claim-type",
                                    "code": "institutional",
                                    "display": "Institutional"
                                }
                            ],
                            "text": "Institutional"
                        },
                        "use": "preauthorization",
                        "patient": {
                            "reference": "Patient/977"
                        },
                        "created": "2024-06-11T10:00:27+00:00",
                        "insurer": {
                            "identifier": {
                                "use": "official",
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "NIIP",
                                            "display": "Payor Code"
                                        }
                                    ],
                                    "text": "Payor Code"
                                },
                                "system": "http://sid/us-insurer-code",
                                "value": "23456"
                            }
                        },
                        "request": {
                            "reference": "Claim/1229",
                            "identifier": {
                                "system": "http://prior_auth",
                                "value": "677556c6-27d9-11ef-a034-65e441e9259f"
                            }
                        },
                        "outcome": "queued",
                        "item": [
                            {
                                "extension": [
                                    {
                                        "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-itemTraceNumber",
                                        "valueIdentifier": {
                                            "system": "http://payer.tracenumber.system",
                                            "value": "9876543210"
                                        }
                                    }
                                ],
                                "itemSequence": 1,
                                "adjudication": [
                                    {
                                        "extension": [
                                            {
                                                "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewAction",
                                                "extension": [
                                                    {
                                                        "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewActionCode",
                                                        "valueCodeableConcept": {
                                                            "coding": [
                                                                {
                                                                    "system": "http://codesystem.x12.org/005010/306",
                                                                    "code": "A2"
                                                                }
                                                            ]
                                                        }
                                                    },
                                                    {
                                                        "url": "reasonCode",
                                                        "valueCodeableConcept": {
                                                            "coding": [
                                                                {
                                                                    "system": "https://codesystem.x12.org/external/886",
                                                                    "code": "0U"
                                                                }
                                                            ]
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        "category": {
                                            "coding": [
                                                {
                                                    "system": "http://terminology.hl7.org/CodeSystem/adjudication",
                                                    "code": "priorAuth",
                                                    "display": "Prior Authorisation"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ],
                        "processNote": [
                            {
                                "number": 1,
                                "text": "Request accepted; Pending for further review"
                            }
                        ]
                    }
                },
                {
                    "resource": {
                        "resourceType": "Patient",
                        "id": "977",
                        "meta": {
                            "versionId": "1",
                            "lastUpdated": "2024-05-07T14:29:08.474+00:00",
                            "source": "#kyJ2HnR6vuVM6Op4"
                        },
                        "text": {
                            "status": "generated",
                            "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><div class=\"hapiHeaderText\">Prathima Vorrey <b>NAGA </b></div><table class=\"hapiPropertyTable\"><tbody><tr><td>Identifier</td><td>prathima123</td></tr><tr><td>Address</td><td><span>1840 S CENTRAL ST </span><br/><span>Visalia </span><span>United States </span></td></tr><tr><td>Date of birth</td><td><span>01 November 1950</span></td></tr></tbody></table></div>"
                        },
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                                "valueCode": "M"
                            }
                        ],
                        "identifier": [
                            {
                                "use": "official",
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "UMB",
                                            "display": "Member Number"
                                        }
                                    ],
                                    "text": "Member Number"
                                },
                                "system": "http://example.org/cdex/payer/member-ids",
                                "value": "prathima123"
                            },
                            {
                                "use": "official",
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "pat",
                                            "display": "Patient Account Number"
                                        }
                                    ],
                                    "text": "Patient Account Number"
                                },
                                "system": "http://example.org/cdex/provider/patient-ids",
                                "value": "9876543210"
                            }
                        ],
                        "active": True,
                        "name": [
                            {
                                "use": "official",
                                "family": "Naga",
                                "given": [
                                    "Prathima",
                                    "Vorrey"
                                ]
                            }
                        ],
                        "telecom": [
                            {
                                "system": "phone",
                                "value": "0850 077 3285",
                                "use": "mobile"
                            }
                        ],
                        "gender": "male",
                        "birthDate": "1950-11-01",
                        "address": [
                            {
                                "line": [
                                    "1840 S CENTRAL ST"
                                ],
                                "city": "Visalia",
                                "postalCode": "533216",
                                "country": "United States",
                                "period": {
                                    "start": "2024-05-07T19:59:03+05:30"
                                }
                            }
                        ],
                        "maritalStatus": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                                    "code": "M",
                                    "display": "Married"
                                }
                            ],
                            "text": "Married"
                        },
                        "communication": [
                            {
                                "language": {
                                    "coding": [
                                        {
                                            "system": "urn:ietf:bcp:47",
                                            "code": "en_US",
                                            "display": "English (US)"
                                        }
                                    ],
                                    "text": "English (US)"
                                }
                            }
                        ]
                    }
                }
            ]
        }
        create_stub(response_body)

if __name__ == "__main__":
    main()
