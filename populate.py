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
              "valueBoolean": False
            }
          ],
          "linkId": "VisionInterference",
          "text": "Is there an interference in the vision/visual field due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
            }
          ],
          "linkId": "DifficultyFittingSpectacles",
          "text": "Does the patient have difficulty fitting spectacles due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "EyelidIrritation",
          "text": "Does the patient have severe eyelid irritation due to this condition?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
            }
          ],
          "linkId": "Socket",
          "text": "Does the patient have Anophthalmic, Microphthalmic or Enophthalmic socket?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
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
              "valueBoolean": True
            }
          ],
          "linkId": "CheckDermatochalasis",
          "text": "Does the patient have Dermatochalasis?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
            }
          ],
          "linkId": "DifficultySpectaclesDermatochalasis",
          "text": "Does it cause significant difficulty in fitting of spectacles?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "ThyroidEyeCondition",
          "text": "Does the patient have Thyroid Eye disease/Eye infection/Eye allergy?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
            }
          ],
          "linkId": "CheckBlepharochalasis",
          "text": "Does the patient have blepharochalasis (eye lid edema)?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
            }
          ],
          "linkId": "ChronicDermatitisOrEyeIrritation",
          "text": "Does it cause chronic dermatitis/eye irritation?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "IdiopathicBlepharospasm",
          "text": "Does the patient have primary idiopathic blepharospasm?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "AnophthalmicSocket",
          "text": "Does the patient have an anophthalmic socket?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "BrowPtosis",
          "text": "Does the patient have brow ptosis?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
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
              "valueBoolean": True
            }
          ],
          "linkId": "RedundantTissueObscureSight",
          "text": "Does the redundant tissue obscure the line of sight?"
        },
        {
          "answer": [
            {
              "valueBoolean": False
            }
          ],
          "linkId": "EdemaRedundantTissue",
          "text": "Is there any erythema/edema of the redundant tissue?"
        },
        {
          "answer": [
            {
              "valueBoolean": True
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
              "valueBoolean": False
            }
          ],
          "linkId": "ThyroidOrbitopathy",
          "text": "Does the patient have thyroid orbitopathy?"
        }
      ]
    }
  ]
            },
        {
            "linkId": "2",
            "text": "Functional Indications",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "VisionInterference",
                    "text": "Is there an interference in the vision/visual field due to this condition?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "DifficultyFittingSpectacles",
                    "text": "Does the patient have difficulty fitting spectacles due to this condition?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "EyelidIrritation",
                    "text": "Does the patient have severe eyelid irritation due to this condition?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "Socket",
                    "text": "Does the patient have Anophthalmic, Microphthalmic or Enophthalmic socket?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                }
            ]
        },
        {
            "linkId": "3",
            "text": "Diagnosis Information",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "CheckDermatochalasis",
                    "text": "Does the patient have Dermatochalasis?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "ThyroidEyeCondition",
                    "text": "Does the patient have Thyroid Eye disease/Eye infection/Eye allergy?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "CheckBlepharochalasis",
                    "text": "Does the patient have blepharochalasis (eye lid edema)?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "IdiopathicBlepharospasm",
                    "text": "Does the patient have primary idiopathic blepharospasm?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "AnophthalmicSocket",
                    "text": "Does the patient have an anophthalmic socket?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "BrowPtosis",
                    "text": "Does the patient have brow ptosis?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "CheckBlepharoptosis",
                    "text": "Does the patient have blepharoptosis?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                }
            ]
        },
        {
            "linkId": "4",
            "text": "Laterality",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "Laterality",
                    "text": "What is the laterality of the condition?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "manual"
                                        },
                                        {
                                            "url": "author",
                                            "valueReference": {
                                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "valueCoding": {
                                "code": "Unilateral",
                                "display": "Unilateral"
                            }
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "AnatomicalLocationCondition",
                    "text": "Is the affected eye:",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "manual"
                                        },
                                        {
                                            "url": "author",
                                            "valueReference": {
                                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "valueCoding": {
                                "code": "Right",
                                "display": "Right"
                            }
                        }
                    ]
                }
            ]
        },
        {
            "linkId": "5",
            "text": "Physical Signs",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "RedundantTissueObscureSight",
                    "text": "Does the redundant tissue obscure the line of sight?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "EdemaRedundantTissue",
                    "text": "Is there any erythema/edema of the redundant tissue?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "AngleEyelidLifting",
                    "text": "Is the angle between the resting field and the field performed by manually lifting the eyelid more than 12 degrees?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": True
                        }
                    ]
                }
            ]
        },
        {
            "linkId": "6",
            "text": "Contraindications",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "ThyroidOrbitopathy",
                    "text": "Does the patient have thyroid orbitopathy?",
                    "answer": [
                        {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/information-origin",
                                    "extension": [
                                        {
                                            "url": "source",
                                            "valueCode": "auto"
                                        }
                                    ]
                                }
                            ],
                            "valueBoolean": False
                        }
                    ]
                }
            ]
        },
        {
            "linkId": "7",
            "text": "Photographic Evidence",
            "item": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
                            "valueReference": {
                                "reference": "Practitioner/d3edddb0-dfd5-11ee-8888-06cdd353a087"
                            }
                        }
                    ],
                    "linkId": "EvidencePhysicalSignsUpload",
                    "text": "Evidence Physical Signs Upload"
                }
            ]
        }
    ]
}
        create_stub(response_body)

if __name__ == "__main__":
    main()
