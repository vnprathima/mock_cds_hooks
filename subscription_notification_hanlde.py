import requests
import json

def send_notification_bundle():
    wiremock_base_url = "http://localhost:8082"
    mapping = {
            "request": {
                "method": "GET",
                "url": "/subscription/notification"
            },
            "response": {
                "status": 200,
                "body": "Stub triggered successfully.",
                "headers": {
                    "Content-Type": "text/plain",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization"
                },
            }
        }

        # Create the stub in WireMock
    url = "{}/__admin/mappings".format(wiremock_base_url)
    stub_response = requests.post(url, json=mapping)
    stub_response.raise_for_status()
    print("Stub created successfully")

def main(request_body):
    # Prepare the notification bundle
    request_data = json.loads(request_body)

    # Extract base_url and fhir_url from the request body
    base_url = request_data.get('base_url')
    fhir_url = request_data.get('fhir_url')

    # Send the notification to the subscription endpoint
    endpoint = base_url+"/subscription/notification"
    headers = {'Content-Type': 'application/fhir+json'}
    notification_bundle = {
        "resourceType": "Bundle",
        "type": "notification",
        "entry": [
            {
                "resource": {
                    "resourceType": "SubscriptionStatus",
                    "status": "active",
                    "id": "123",
                    "criteria": "http://hl7.org/SubscriptionTopic/admission",
                    "type": "event-notification",
                    "eventsSinceSubscriptionStart": "2",
                    "notificationEvent": [
                    {
                        "eventNumber": "2",
                        "focus": {
                        "reference": "ClaimResponse/21652"
                        },
                    }]
                }
            },
            {
                "resource": {
                    "resourceType": "ClaimResponse",
                    "id": "21652",
                    "meta": {
                        "versionId": "1",
                        "lastUpdated": "2024-03-12T05:33:31.853-04:00",
                        "source": "#zLNnaoH9UWIX4895"
                    },
                    "contained": [
                        {
                            "id": "6df59a38-d26b-11ee-92ac-06cdd353a087",
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                                    "valueCode": "F"
                                },
                                {
                                    "extension": [
                                        {
                                            "url": "ombCategory",
                                            "valueCoding": {
                                                "code": "2186-5",
                                                "display": "Not Hispanic or Latino",
                                                "system": "urn:oid:2.16.840.1.113883.6.238"
                                            }
                                        },
                                        {
                                            "url": "text",
                                            "valueString": "Not Hispanic or Latino"
                                        }
                                    ],
                                    "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
                                },
                                {
                                    "extension": [
                                        {
                                            "url": "ombCategory",
                                            "valueCoding": {
                                                "code": "2186-5",
                                                "display": "Not Hispanic or Latino",
                                                "system": "urn:oid:2.16.840.1.113883.6.238"
                                            }
                                        },
                                        {
                                            "url": "text",
                                            "valueString": "Not Hispanic or Latino"
                                        }
                                    ],
                                    "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
                                }
                            ],
                            "active": True,
                            "address": [
                                {
                                    "city": "Groton",
                                    "country": "United States",
                                    "line": [
                                        "709 Wuckert Mill Unit 84"
                                    ],
                                    "period": {
                                        "start": "2024-07-17T20:47:39+05:30"
                                    },
                                    "postalCode": "01450",
                                    "state": "Massachusetts"
                                }
                            ],
                            "birthDate": "2004-09-18",
                            "gender": "female",
                            "identifier": [
                                {
                                    "system": "https://github.com/synthetichealth/synthea",
                                    "use": "official",
                                    "value": "45067004-8dd7-369d-b02e-40ecd9483942"
                                },
                                {
                                    "system": "http://hospital.smarthealthit.org",
                                    "use": "official",
                                    "value": "45067004-8dd7-369d-b02e-40ecd9483942"
                                },
                                {
                                    "system": "http://hl7.org/fhir/sid/us-ssn",
                                    "use": "official",
                                    "value": "999-31-6447"
                                },
                                {
                                    "system": "urn:oid:2.16.840.1.113883.4.3.25",
                                    "use": "official",
                                    "value": "S99986141"
                                }
                            ],
                            "maritalStatus": {
                                "coding": [
                                    {
                                        "code": "S",
                                        "display": "Never Married",
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                                    }
                                ],
                                "text": "Never Married"
                            },
                            "name": [
                                {
                                    "family": "Hirthe",
                                    "given": [
                                        "Mathilde"
                                    ],
                                    "use": "official"
                                }
                            ],
                            "telecom": [
                                {
                                    "system": "phone",
                                    "use": "mobile",
                                    "value": "555-269-5443"
                                }
                            ],
                            "resourceType": "Patient"
                        },
                        {
                            "id": "a306625a-da4c-11ee-ae99-06cdd353a087",
                            "active": True,
                            "address": [
                                {
                                    "city": "North Springs,",
                                    "country": "United States",
                                    "line": [
                                        "4066 Chenoweth Drive"
                                    ],
                                    "postalCode": "85214",
                                    "state": "New Jersey"
                                }
                            ],
                            "contact": [
                                {
                                    "address": {
                                        "city": "North Springs",
                                        "country": "United States",
                                        "line": [
                                            "4066 Chenoweth Drive"
                                        ],
                                        "postalCode": "85214",
                                        "state": "New Jersey"
                                    },
                                    "name": {
                                        "family": "Jacob",
                                        "given": [
                                            "Mark L"
                                        ],
                                        "use": "official"
                                    },
                                    "telecom": [
                                        {
                                            "system": "phone",
                                            "value": "+963 741 852"
                                        },
                                        {
                                            "system": "email",
                                            "value": "mark@mail.com"
                                        }
                                    ]
                                }
                            ],
                            "identifier": [
                                {
                                    "system": "http://sid/us-insurer-id",
                                    "type": {
                                        "coding": [
                                            {
                                                "code": "NIIP",
                                                "display": "Payor ID",
                                                "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                            }
                                        ],
                                        "text": "Payor ID"
                                    },
                                    "use": "official",
                                    "value": "c5cdf812-1fdd-3adf-b1-71cc8bd0789dbb"
                                },
                                {
                                    "system": "http://sid/us-insurer-code",
                                    "type": {
                                        "coding": [
                                            {
                                                "code": "NIIP",
                                                "display": "Payor Code",
                                                "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                            }
                                        ],
                                        "text": "Payor Code"
                                    },
                                    "use": "official",
                                    "value": "12762"
                                },
                                {
                                    "system": "urn:ietf:rfc:3986",
                                    "type": {
                                        "text": "urn:ietf:rfc:3986"
                                    },
                                    "use": "official",
                                    "value": "2.16.840.1.113883.13.34.110.1.110.11"
                                }
                            ],
                            "name": "Ideal Payer",
                            "telecom": [
                                {
                                    "system": "phone",
                                    "value": "+963 456 852"
                                },
                                {
                                    "system": "email",
                                    "value": "Ideal@mail.com"
                                }
                            ],
                            "type": [
                                {
                                    "coding": [
                                        {
                                            "code": "FA",
                                            "display": "Payer",
                                            "system": "https://codesystem.x12.org/005010/98"
                                        }
                                    ],
                                    "text": "Payer"
                                }
                            ],
                            "resourceType": "Organization"
                        }
                    ],
                    "identifier": [
                        {
                            "system": "http://mettles.com/drfp/identifiers",
                            "value": "b145a86f-9531-45e0-b70f-74300004e1c9"
                        },
                        {
                            "type": {
                                "text": "X12 UUID to esMD"
                            },
                            "value": "5c666e48-3293-4930-a0fd-2f61b4b42676"
                        },
                        {
                            "type": {
                                "text": "X12 esMD Transaction ID"
                            },
                            "value": "MRI0000686451EC"
                        },
                        {
                            "type": {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                        "code": "PLAC",
                                        "display": "Placer Identifier"
                                    }
                                ],
                                "text": "XDR UUID to esMD"
                            },
                            "value": "10e74b5c-e53c-4e6d-a31a-3f063820cc4c"
                        },
                        {
                            "type": {
                                "coding": [
                                    {
                                        "system": "http://test.idp.idm.cms.gov",
                                        "code": "IDM Preferred Username",
                                        "display": "Requester Identifier"
                                    }
                                ],
                                "text": "IDM Unique Identifier"
                            },
                            "system": "http://test.idp.idm.cms.gov",
                            "value": "Nucural"
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
                        "reference": "#6df59a38-d26b-11ee-92ac-06cdd353a087"
                    },
                    "created": "2024-03-12T05:33:27-04:00",
                    "insurer": {
                        "reference": "#a306625a-da4c-11ee-ae99-06cdd353a087"
                    },
                    "outcome": "queued",
                    "request": {
                        "identifier": {
                            "system": "https://tracking-id",
                            "value": "9720374706"
                        }
                    },
                    "disposition": "PA request and Supporting Documentation Submitted",
                    "item": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-itemAuthorizedDetail",
                                    "extension": [
                                        {
                                            "url": "productOrServiceCode",
                                            "valueString": "15823"
                                        }
                                    ]
                                },
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-itemAuthorizedProvider",
                                    "extension": [
                                        {
                                            "url": "provider"
                                        },
                                        {
                                            "url": "providerType",
                                            "valueString": "FA"
                                        }
                                    ]
                                },
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-itemAuthorizedProvider",
                                    "extension": [
                                        {
                                            "url": "provider"
                                        },
                                        {
                                            "url": "providerType",
                                            "valueString": "71"
                                        }
                                    ]
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
                                                                "code": "A2",
                                                                "display": "Certified Partially"
                                                            }
                                                        ]
                                                    }
                                                },
                                                {
                                                    "url": "reasonCode",
                                                    "valueString": "Successful Submission"
                                                }
                                            ]
                                        }
                                    ],
                                    "category": {
                                        "coding": [
                                            {
                                                "system": "http://terminology.hl7.org/CodeSystem/adjudication",
                                                "code": "submitted"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
    # Make the POST request
    response = requests.post(endpoint, data=json.dumps(notification_bundle), headers=headers)

    # Check response and proceed if successful
    if response.status_code == 200:
        print(f"Notification sent, response status: {response.status_code}")
        
    else:
        print(f"Failed to send notification, response status: {response.status_code}")
    send_notification_bundle()

if __name__ == "__main__":
    example_request_body = json.dumps({
        "base_url": "http://localhost:8069",
        "fhir_url": "http://localhost:8080"
    })
    main(example_request_body)
