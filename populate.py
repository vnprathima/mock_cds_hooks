import requests

def create_stub(response_body):
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/Questionnaire/$populate",
            "bodyPatterns": [
                {
                    "matchesJsonPath": f"$.parameter[0].name"
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
        }
    }
    options_mapping = {
        "request": {
            "method": "OPTIONS",
            "url": "/Questionnaire/$populate"
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
    print(f"OPTIONS stub for /Questionnaire/$populate created successfully")

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"POST stub for /Questionnaire/$populate created successfully")

def main():
        sample_request = {
            "resourceType": "Parameters",
            "parameter": [
                {
                    "name": "questionnaireRef",
                    "valueReference": {
                        "reference": "Questionnaire/[id]"
                    }
                },
                {
                    "name": "questionnaire",
                    "resource": {
                        "resourceType": "Questionnaire",
                        "id": "[id]",
                        "status": "active",
                        "item": [
                        {
                            "linkId": "1",
                            "text": "Patient's Name",
                            "type": "string"
                        },
                        {
                            "linkId": "2",
                            "text": "Date of Birth",
                            "type": "date"
                        },
                        {
                            "linkId": "3",
                            "text": "Gender",
                            "type": "choice",
                            "option": [
                            {
                                "valueCoding": {
                                "code": "male",
                                "display": "Male"
                                }
                            },
                            {
                                "valueCoding": {
                                "code": "female",
                                "display": "Female"
                                }
                            }
                            ]
                        }
                        ]
                    }
                },
                {
                    "name": "subject",
                    "valueString": "Patient/[patient-id]"
                }
            ]
        }
    
        response_body = {
    "resourceType": "QuestionnaireResponse",
    "id": "7fe37f2d-4a65-11ef-ba8d-06cdd353a087",
    "extension": [
        {
            "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/context",
            "valueReference": {
                "reference": "Coverage/e311004c-ec0f-11ee-8888-06cdd353a087"
            }
        }
    ],
    "questionnaire": "https://emr.nucural.com/fhir/Questionnaire/b92732a6-4a65-11ef-ba8d-06cdd353a087",
    "status": "in-progress",
    "subject": {
        "reference": "Patient/b3496955-d264-11ee-92ab-06cdd353a087",
    },
    "authored": "2024-07-25",
    "author": {
        "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
    },
    "item": [
    {
      "linkId": "1",
      "text": "Type of Surgery",
      "item": [
        {
          "answer": [
            {
              "valueCoding": {
                "code": "Cosmetic",
                "display": "Cosmetic"
              }
            }
          ],
          "linkId": "SurgeryPurpose",
          "text": "What is the purpose of this surgery?"
        },
        {
          "answer": [
            {
              "valueCoding": {
                "code": "Upper Eye Lid",
                "display": "Upper Eye Lid"
              }
            }
          ],
          "linkId": "AnatomicalLocationOfSurgery",
          "text": "Is the surgery needed for:"
        }
      ]
    },
    {
      "linkId": "2",
      "text": "Functional Indications",
      "item": [
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "VisionInterference",
          "text": "Is there an interference in the vision/visual field due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "DifficultyFittingSpectacles",
          "text": "Does the patient have difficulty fitting spectacles due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "EyelidIrritation",
          "text": "Does the patient have severe eyelid irritation due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "Socket",
          "text": "Does the patient have Anophthalmic, Microphthalmic or Enophthalmic socket?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "DifficultyFittingProsthesis",
          "text": "Does the patient have any difficulty wearing or fitting a prosthesis due to this condition?"
        }
      ]
    },
    {
      "linkId": "3",
      "text": "Diagnosis Information",
      "item": [
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "CheckDermatochalasis",
          "text": "Does the patient have Dermatochalasis?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "DifficultySpectaclesDermatochalasis",
          "text": "Does it cause significant difficulty in fitting of spectacles?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "ThyroidEyeCondition",
          "text": "Does the patient have Thyroid Eye disease/Eye infection/Eye allergy?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "CheckBlepharochalasis",
          "text": "Does the patient have blepharochalasis (eye lid edema)?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "ChronicDermatitisOrEyeIrritation",
          "text": "Does it cause chronic dermatitis/eye irritation?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "IdiopathicBlepharospasm",
          "text": "Does the patient have primary idiopathic blepharospasm?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "AnophthalmicSocket",
          "text": "Does the patient have an anophthalmic socket?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "BrowPtosis",
          "text": "Does the patient have brow ptosis?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "CheckBlepharoptosis",
          "text": "Does the patient have blepharoptosis?"
        }
      ]
    },
    {
      "linkId": "4",
      "text": "Laterality",
      "item": [
        {
          "answer": [
            {
              "valueCoding": {
                "code": "Unilateral",
                "display": "Unilateral"
              }
            }
          ],
          "linkId": "Laterality",
          "text": "What is the laterality of the condition?"
        },
        {
          "answer": [
            {
              "valueCoding": {
                "code": "Right",
                "display": "Right"
              }
            }
          ],
          "linkId": "AnatomicalLocationCondition",
          "text": "Is the affected eye:"
        }
      ]
    },
    {
      "linkId": "5",
      "text": "Physical Signs",
      "item": [
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "RedundantTissueObscureSight",
          "text": "Does the redundant tissue obscure the line of sight?"
        },
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "EdemaRedundantTissue",
          "text": "Is there any erythema/edema of the redundant tissue?"
        },
        {
          "answer": [
            {
              "valueBoolean": true
            }
          ],
          "linkId": "AngleEyelidLifting",
          "text": "Is the angle between the resting field and the field performed by manually lifting the eyelid more than 12 degrees?"
        }
      ]
    },
    {
      "linkId": "6",
      "text": "Contraindications",
      "item": [
        {
          "answer": [
            {
              "valueBoolean": false
            }
          ],
          "linkId": "ThyroidOrbitopathy",
          "text": "Does the patient have thyroid orbitopathy?"
        }
      ]
    }
  ]
}
        create_stub(response_body)

if __name__ == "__main__":
    main()
