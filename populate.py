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
  "id": "response1",
  "authored": "2024-07-29",
  "status": "in-progress",
  "item": [
    {
      "linkId": "1",
      "text": "Type of Surgery",
      "item": [
        {
          "linkId": "SurgeryPurpose",
          "text": "What is the purpose of this surgery?",
          "answer": [
            {
              "valueCoding": {
                "code": "Cosmetic",
                "display": "Cosmetic"
              },
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
                        "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "AnatomicalLocationOfSurgery",
          "text": "Is the surgery needed for:",
          "answer": [
            {
              "valueCoding": {
                "code": "Upper Eye Lid",
                "display": "Upper Eye Lid"
              },
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
                        "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
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
          "linkId": "VisionInterference",
          "text": "Is there an interference in the vision/visual field due to this condition?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "DifficultyFittingSpectacles",
          "text": "Does the patient have difficulty fitting spectacles due to this condition?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "EyelidIrritation",
          "text": "Does the patient have severe eyelid irritation due to this condition?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "Socket",
          "text": "Does the patient have Anophthalmic, Microphthalmic or Enophthalmic socket?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "DifficultyFittingProsthesis",
          "text": "Does the patient have any difficulty wearing or fitting a prosthesis due to this condition?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
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
          "linkId": "CheckDermatochalasis",
          "text": "Does the patient have Dermatochalasis?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "DifficultySpectaclesDermatochalasis",
          "text": "Does it cause significant difficulty in fitting of spectacles?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "ThyroidEyeCondition",
          "text": "Does the patient have Thyroid Eye disease/Eye infection/Eye allergy?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "CheckBlepharochalasis",
          "text": "Does the patient have blepharochalasis (eye lid edema)?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "ChronicDermatitisOrEyeIrritation",
          "text": "Does it cause chronic dermatitis/eye irritation?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "IdiopathicBlepharospasm",
          "text": "Does the patient have primary idiopathic blepharospasm?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "AnophthalmicSocket",
          "text": "Does the patient have an anophthalmic socket?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "BrowPtosis",
          "text": "Does the patient have brow ptosis?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "CheckBlepharoptosis",
          "text": "Does the patient have blepharoptosis?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
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
          "linkId": "Laterality",
          "text": "What is the laterality of the condition?",
          "answer": [
            {
              "valueCoding": {
                "code": "Unilateral",
                "display": "Unilateral"
              },
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
                        "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "AnatomicalLocationCondition",
          "text": "Is the affected eye:",
          "answer": [
            {
              "valueCoding": {
                "code": "Right",
                "display": "Right"
              },
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
                        "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
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
          "linkId": "ExcessiveSkinOverhanging",
          "text": "Is an amount of excessive skin overhanging the eyelid margin causing Pseudoptosis?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "PseudoMRD",
          "text": "Is the central pseudo MRD less than 2mm?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "RedundantTissueObscureSight",
          "text": "Does the redundant tissue obscure the line of sight?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "EdemaRedundantTissue",
          "text": "Is there any erythema/edema of the redundant tissue?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        },
        {
          "linkId": "AngleEyelidLifting",
          "text": "Is the angle between the resting field and the field performed by manually lifting the eyelid more than 12 degrees?",
          "answer": [
            {
              "valueBoolean": True,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
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
          "linkId": "ThyroidOrbitopathy",
          "text": "Does the patient have thyroid orbitopathy?",
          "answer": [
            {
              "valueBoolean": False,
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
              ]
            }
          ],
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
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
          "linkId": "EvidencePhysicalSignsUpload",
          "text": "Evidence Physical Signs Upload",
          "extension": [
            {
              "url": "http://hl7.org/fhir/StructureDefinition/questionnaireresponse-author",
              "valueReference": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ]
        }
      ]
    }
  ],
  "questionnaire": "#questionnaire-lcd1-eyelidsurgery",
  "subject": {
    "reference": "#fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
  },
  "contained": [
    {
      "resourceType": "Patient",
      "id": "fdb3d0b8-d26b-11ee-92ac-06cdd353a087",
      "extension": [
        {
          "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
          "valueCode": "M"
        },
        {
          "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
          "extension": [
            {
              "url": "ombCategory",
              "valueCoding": {
                "system": "urn:oid:2.16.840.1.113883.6.238",
                "code": "2186-5",
                "display": "Not Hispanic or Latino"
              }
            },
            {
              "url": "text",
              "valueString": "Not Hispanic or Latino"
            }
          ]
        },
        {
          "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
          "extension": [
            {
              "url": "ombCategory",
              "valueCoding": {
                "system": "urn:oid:2.16.840.1.113883.6.238",
                "code": "2186-5",
                "display": "Not Hispanic or Latino"
              }
            },
            {
              "url": "text",
              "valueString": "Not Hispanic or Latino"
            }
          ]
        }
      ],
      "identifier": [
        {
          "use": "official",
          "system": "https://github.com/synthetichealth/synthea",
          "value": "0686a374-570d-415f-b737-06ca7c3a3edb"
        },
        {
          "use": "official",
          "system": "http://hospital.smarthealthit.org",
          "value": "0686a374-570d-415f-b737-06ca7c3a3edb"
        },
        {
          "use": "official",
          "system": "http://hl7.org/fhir/sid/us-ssn",
          "value": "999-39-3074"
        }
      ],
      "active": True,
      "name": [
        {
          "use": "official",
          "family": "Carroll",
          "given": [
            "Richie"
          ]
        }
      ],
      "telecom": [
        {
          "system": "phone",
          "value": "555-367-6744",
          "use": "mobile"
        }
      ],
      "gender": "male",
      "birthDate": "2021-03-06",
      "address": [
        {
          "line": [
            "1043 Hauck Highlands"
          ],
          "city": "Hudson",
          "state": "Massachusetts",
          "country": "United States"
        }
      ],
      "maritalStatus": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
            "code": "S",
            "display": "Never Married"
          }
        ],
        "text": "Never Married"
      }
    },
    {
      "resourceType": "Coverage",
      "id": "820ff38a-15da-11ef-ba8d-06cdd353a087",
      "status": "active",
      "type": {
        "coding": [
          {
            "system": "http://snomed.info/sct",
            "code": "12345",
            "display": "Primary"
          }
        ],
        "text": "Primary"
      },
      "subscriber": {
        "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
      },
      "subscriberId": "77282625525",
      "beneficiary": {
        "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
      },
      "relationship": {
        "coding": [
          {
            "system": "https://www.hl7.org/fhir/valueset-subscriber-relationship.html",
            "code": "self",
            "display": "Self"
          }
        ],
        "text": "Self"
      },
      "payor": [
        {
          "reference": "Organization/a306625a-da4c-11ee-ae99-06cdd353a087"
        }
      ]
    },
    {
      "resourceType": "Organization",
      "id": "a306625a-da4c-11ee-ae99-06cdd353a087",
      "identifier": [
        {
          "use": "official",
          "type": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                "code": "NIIP",
                "display": "Payor ID"
              }
            ],
            "text": "Payor ID"
          },
          "system": "http://sid/us-insurer-id",
          "value": "c5cdf812-1fdd-3adf-b1-71cc8bd0789dbb"
        },
        {
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
          "value": "12762"
        },
        {
          "use": "official",
          "type": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                "code": "NIIP",
                "display": "Payor ID"
              }
            ],
            "text": "Payor ID"
          },
          "system": "http://sid/us-insurer-id",
          "value": "c5cdf812-1fdd-3adf-b1-71cc8bd0789dbb"
        },
        {
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
          "value": "12762"
        }
      ],
      "active": True,
      "type": [
        {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/organization-type",
              "code": "pay",
              "display": "Payer"
            }
          ],
          "text": "Payer"
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
      "address": [
        {
          "country": "United States"
        }
      ]
    },
    {
      "resourceType": "Encounter",
      "id": "a3be9950-15da-11ef-ba8d-06cdd353a087",
      "identifier": [
        {
          "use": "official",
          "type": {
            "text": "Nucural Encounter Identifier"
          },
          "system": "https://emr.nucural.com/encounter-identifier",
          "value": "a3be9950-15da-11ef-ba8d-06cdd353a087"
        }
      ],
      "status": "in-progress",
      "class": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code": "AMB",
        "display": "Ambulatory"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "2",
              "display": "Established"
            }
          ],
          "text": "Established"
        }
      ],
      "serviceType": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/service-type",
            "code": "7",
            "display": "Friendly Visiting"
          }
        ],
        "text": "Friendly Visiting"
      },
      "subject": {
        "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
      },
      "participant": [
        {
          "type": [
            {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                  "code": "ADM",
                  "display": "admitter"
                }
              ]
            }
          ],
          "period": {
            "start": "2024-05-19T12:23:51Z"
          },
          "individual": {
            "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
          }
        }
      ],
      "period": {
        "start": "2024-05-19T12:23:51Z",
        "end": "2024-05-19T12:23:24Z"
      },
      "diagnosis": [
        {
          "condition": {
            "reference": "Condition/985ce836-15db-11ef-ba8d-06cdd353a087"
          }
        }
      ],
      "serviceProvider": {
        "reference": "Organization/205c66c0-dc6c-11ee-ae99-06cdd353a087"
      }
    },
    {
      "resourceType": "Organization",
      "id": "205c66c0-dc6c-11ee-ae99-06cdd353a087",
      "identifier": [
        {
          "use": "official",
          "system": "http://hl7.org/fhir/sid/us-npi",
          "value": "1209345678"
        }
      ],
      "active": True,
      "type": [
        {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/organization-type",
              "code": "prov",
              "display": "Healthcare Provider"
            }
          ],
          "text": "Healthcare Provider"
        }
      ],
      "name": "Nucural Organization",
      "telecom": [
        {
          "system": "phone",
          "value": "010-234-0987"
        },
        {
          "system": "email",
          "value": "nucural.org@example.com"
        }
      ],
      "address": [
        {
          "line": [
            "Mark Street"
          ],
          "city": "Arburn",
          "state": "Alabama",
          "postalCode": "32109",
          "country": "United States"
        }
      ],
      "contact": [
        {
          "address": {
            "country": "United States"
          }
        }
      ]
    },
    {
      "resourceType": "Practitioner",
      "id": "0b6df3a8-2a6b-11ef-ba8d-06cdd353a087",
      "identifier": [
        {
          "system": "http://hl7.org/fhir/sid/us-npi",
          "value": "3453454578"
        }
      ],
      "active": True,
      "name": [
        {
          "family": "Marvick",
          "given": [
            "Helen"
          ]
        }
      ],
      "telecom": [
        {
          "system": "email",
          "value": "mounica+helen_marvick@nucural.com"
        }
      ],
      "address": [
        {
          "country": "United States"
        }
      ],
      "gender": "female"
    },
    {
      "resourceType": "ServiceRequest",
      "id": "094d86c4-4d75-11ef-ba8d-06cdd353a087",
      "extension": [
        {
          "url": "http://hl7.org/fhir/us/davinci-crd/StructureDefinition/ext-coverage-information",
          "extension": [
            {
              "url": "questionnaire",
              "valueCanonical": "https://fhir-dev.mettles.com/baseServer/fhir/Questionnaire/questionnaire-lcd1-eyelidsurgery"
            },
            {
              "url": "coverage",
              "valueReference": {
                "reference": "Coverage/820ff38a-15da-11ef-ba8d-06cdd353a087"
              }
            },
            {
              "url": "date",
              "valueDate": "2024-07-29"
            },
            {
              "url": "identifier",
              "valueString": "1970e460-9f43-4d7a-8b0b-35e22fc3e0ae"
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
          ]
        }
      ],
      "status": "active",
      "intent": "order",
      "priority": "routine",
      "code": {
        "coding": [
          {
            "system": "https://www.aapc.com/resources/medical-coding/cpt.aspx",
            "code": "15823",
            "display": "Blepharoplasty, upper eyelid; with excessive skin weighting down lid"
          }
        ],
        "text": "Blepharoplasty, upper eyelid; with excessive skin weighting down lid"
      },
      "quantityQuantity": {
        "value": 1
      },
      "subject": {
        "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
      },
      "encounter": {
        "reference": "Encounter/a3be9950-15da-11ef-ba8d-06cdd353a087"
      },
      "occurrencePeriod": {
        "start": "2024-07-31T06:37:14Z",
        "end": "2024-08-01T06:37:14Z"
      },
      "authoredOn": "2024-07-29",
      "requester": {
        "reference": "PractitionerRole/0b6df3a9-2a6b-11ef-ba8d-06cdd353a087"
      },
      "insurance": [
        {
          "reference": "Coverage/820ff38a-15da-11ef-ba8d-06cdd353a087"
        }
      ],
      "contained": [
        {
          "resourceType": "Patient",
          "id": "fdb3d0b8-d26b-11ee-92ac-06cdd353a087",
          "extension": [
            {
              "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
              "valueCode": "M"
            },
            {
              "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
              "extension": [
                {
                  "url": "ombCategory",
                  "valueCoding": {
                    "system": "urn:oid:2.16.840.1.113883.6.238",
                    "code": "2186-5",
                    "display": "Not Hispanic or Latino"
                  }
                },
                {
                  "url": "text",
                  "valueString": "Not Hispanic or Latino"
                }
              ]
            },
            {
              "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
              "extension": [
                {
                  "url": "ombCategory",
                  "valueCoding": {
                    "system": "urn:oid:2.16.840.1.113883.6.238",
                    "code": "2186-5",
                    "display": "Not Hispanic or Latino"
                  }
                },
                {
                  "url": "text",
                  "valueString": "Not Hispanic or Latino"
                }
              ]
            }
          ],
          "identifier": [
            {
              "use": "official",
              "system": "https://github.com/synthetichealth/synthea",
              "value": "0686a374-570d-415f-b737-06ca7c3a3edb"
            },
            {
              "use": "official",
              "system": "http://hospital.smarthealthit.org",
              "value": "0686a374-570d-415f-b737-06ca7c3a3edb"
            },
            {
              "use": "official",
              "system": "http://hl7.org/fhir/sid/us-ssn",
              "value": "999-39-3074"
            }
          ],
          "active": True,
          "name": [
            {
              "use": "official",
              "family": "Carroll",
              "given": [
                "Richie"
              ]
            }
          ],
          "telecom": [
            {
              "system": "phone",
              "value": "555-367-6744",
              "use": "mobile"
            }
          ],
          "gender": "male",
          "birthDate": "2021-03-06",
          "address": [
            {
              "line": [
                "1043 Hauck Highlands"
              ],
              "city": "Hudson",
              "state": "Massachusetts",
              "country": "United States"
            }
          ],
          "maritalStatus": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                "code": "S",
                "display": "Never Married"
              }
            ],
            "text": "Never Married"
          }
        },
        {
          "resourceType": "Encounter",
          "id": "a3be9950-15da-11ef-ba8d-06cdd353a087",
          "identifier": [
            {
              "use": "official",
              "type": {
                "text": "Nucural Encounter Identifier"
              },
              "system": "https://emr.nucural.com/encounter-identifier",
              "value": "a3be9950-15da-11ef-ba8d-06cdd353a087"
            }
          ],
          "status": "in-progress",
          "class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "AMB",
            "display": "Ambulatory"
          },
          "type": [
            {
              "coding": [
                {
                  "system": "http://snomed.info/sct",
                  "code": "2",
                  "display": "Established"
                }
              ],
              "text": "Established"
            }
          ],
          "serviceType": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/service-type",
                "code": "7",
                "display": "Friendly Visiting"
              }
            ],
            "text": "Friendly Visiting"
          },
          "subject": {
            "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
          },
          "participant": [
            {
              "type": [
                {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                      "code": "ADM",
                      "display": "admitter"
                    }
                  ]
                }
              ],
              "period": {
                "start": "2024-05-19T12:23:51Z"
              },
              "individual": {
                "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
              }
            }
          ],
          "period": {
            "start": "2024-05-19T12:23:51Z",
            "end": "2024-05-19T12:23:24Z"
          },
          "diagnosis": [
            {
              "condition": {
                "reference": "Condition/985ce836-15db-11ef-ba8d-06cdd353a087"
              }
            }
          ],
          "serviceProvider": {
            "reference": "Organization/205c66c0-dc6c-11ee-ae99-06cdd353a087"
          }
        },
        {
          "resourceType": "PractitionerRole",
          "id": "0b6df3a9-2a6b-11ef-ba8d-06cdd353a087",
          "active": True,
          "practitioner": {
            "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
          }
        },
        {
          "resourceType": "Coverage",
          "id": "820ff38a-15da-11ef-ba8d-06cdd353a087",
          "status": "active",
          "type": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "12345",
                "display": "Primary"
              }
            ],
            "text": "Primary"
          },
          "subscriber": {
            "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
          },
          "subscriberId": "77282625525",
          "beneficiary": {
            "reference": "Patient/fdb3d0b8-d26b-11ee-92ac-06cdd353a087"
          },
          "relationship": {
            "coding": [
              {
                "system": "https://www.hl7.org/fhir/valueset-subscriber-relationship.html",
                "code": "self",
                "display": "Self"
              }
            ],
            "text": "Self"
          },
          "payor": [
            {
              "reference": "Organization/a306625a-da4c-11ee-ae99-06cdd353a087"
            }
          ]
        }
      ]
    },
    {
      "resourceType": "Questionnaire",
      "id": "questionnaire-lcd1-eyelidsurgery",
      "meta": {
        "versionId": "46",
        "lastUpdated": "2024-04-03T11:39:12.586+00:00",
        "source": "#02LKdrA9s2Yvnzzl"
      },
      "extension": [
        {
          "url": "http://hl7.org/fhir/StructureDefinition/cqf-library",
          "valueCanonical": "https://fhir-dev.mettles.com/baseServer/fhir/Library/library-lcd1-EyelidSurgery"
        }
      ],
      "url": "https://fhir-dev.mettles.com/baseServer/fhir/Questionnaire/questionnaire-lcd1-eyelidsurgery",
      "identifier": [
        {
          "system": "http://identifiers.mettles.com/prior_authorization",
          "value": "medicare_fee_for_service-eyelid_surgery"
        }
      ],
      "version": "1.0.0",
      "name": "Prior Authorization For Blepharoplasty",
      "title": "Prior Authorization For Blepharoplasty",
      "status": "draft",
      "subjectType": [
        "Patient"
      ],
      "date": "2021-10-30",
      "publisher": "Mettle Solutions",
      "item": [
        {
          "linkId": "1",
          "text": "Type of Surgery",
          "type": "group",
          "item": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "SurgeryPurpose"
                  }
                }
              ],
              "linkId": "SurgeryPurpose",
              "text": "What is the purpose of this surgery?",
              "type": "choice",
              "required": True,
              "answerOption": [
                {
                  "valueCoding": {
                    "code": "Cosmetic",
                    "display": "Cosmetic"
                  }
                },
                {
                  "valueCoding": {
                    "code": "Reconstructive",
                    "display": "Reconstructive"
                  }
                }
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "AnatomicalLocationOfSurgery"
                  }
                }
              ],
              "linkId": "AnatomicalLocationOfSurgery",
              "text": "Is the surgery needed for:",
              "type": "choice",
              "required": True,
              "answerOption": [
                {
                  "valueCoding": {
                    "code": "Upper Eye Lid",
                    "display": "Upper Eye Lid"
                  }
                },
                {
                  "valueCoding": {
                    "code": "Lower Eye Lid",
                    "display": "Lower Eye Lid"
                  }
                }
              ]
            }
          ]
        },
        {
          "linkId": "2",
          "text": "Functional Indications",
          "type": "group",
          "item": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "VisionInterference"
                  }
                }
              ],
              "linkId": "VisionInterference",
              "text": "Is there an interference in the vision/visual field due to this condition?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "ImpairmentInDailyActivities"
                  }
                }
              ],
              "linkId": "ImpairmentInDailyActivities",
              "text": "Does it cause an impairment in daily life activities (difficulty in driving, reading)?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "VisionInterference",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "DifficultyFittingSpectacles"
                  }
                }
              ],
              "linkId": "DifficultyFittingSpectacles",
              "text": "Does the patient have difficulty fitting spectacles due to this condition?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "EyelidIrritation"
                  }
                }
              ],
              "linkId": "EyelidIrritation",
              "text": "Does the patient have severe eyelid irritation due to this condition?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "Socket"
                  }
                }
              ],
              "linkId": "Socket",
              "text": "Does the patient have Anophthalmic, Microphthalmic or Enophthalmic socket?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "DifficultyFittingProsthesis"
                  }
                }
              ],
              "linkId": "DifficultyFittingProsthesis",
              "text": "Does the patient have any difficulty wearing or fitting a prosthesis due to this condition?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "Socket",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            }
          ]
        },
        {
          "linkId": "3",
          "text": "Diagnosis Information",
          "type": "group",
          "item": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "CheckDermatochalasis"
                  }
                }
              ],
              "linkId": "CheckDermatochalasis",
              "text": "Does the patient have Dermatochalasis?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "DifficultySpectaclesDermatochalasis"
                  }
                }
              ],
              "linkId": "DifficultySpectaclesDermatochalasis",
              "text": "Does it cause significant difficulty in fitting of spectacles?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "CheckDermatochalasis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "ThyroidEyeCondition"
                  }
                }
              ],
              "linkId": "ThyroidEyeCondition",
              "text": "Does the patient have Thyroid Eye disease/Eye infection/Eye allergy?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "ThyroidChronicDermatitis"
                  }
                }
              ],
              "linkId": "ThyroidChronicDermatitis",
              "text": "Does it cause chronic dermatitis?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "ThyroidEyeCondition",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "CheckBlepharochalasis"
                  }
                }
              ],
              "linkId": "CheckBlepharochalasis",
              "text": "Does the patient have blepharochalasis (eye lid edema)?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "ChronicDermatitisOrEyeIrritation"
                  }
                }
              ],
              "linkId": "ChronicDermatitisOrEyeIrritation",
              "text": "Does it cause chronic dermatitis/eye irritation?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "CheckBlepharochalasis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "IdiopathicBlepharospasm"
                  }
                }
              ],
              "linkId": "IdiopathicBlepharospasm",
              "text": "Does the patient have primary idiopathic blepharospasm?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "AnophthalmicSocket"
                  }
                }
              ],
              "linkId": "AnophthalmicSocket",
              "text": "Does the patient have an anophthalmic socket?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "CheckPtosis"
                  }
                }
              ],
              "linkId": "CheckPtosis",
              "text": "Does the patient have ptosis?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "AnophthalmicSocket",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "PtosisDifficultyProsthesis"
                  }
                }
              ],
              "linkId": "PtosisDifficultyProsthesis",
              "text": "Does it lead to difficulty in prosthesis fitting?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "CheckPtosis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "BrowPtosis"
                  }
                }
              ],
              "linkId": "BrowPtosis",
              "text": "Does the patient have brow ptosis?",
              "type": "boolean",
              "required": True
            },
            {
              "linkId": "BrowPtosisBlepharoplasty",
              "text": "Is the blepharoplasty suggested in addition to brow ptosis repair?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "BrowPtosis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "CheckBlepharoptosis"
                  }
                }
              ],
              "linkId": "CheckBlepharoptosis",
              "text": "Does the patient have blepharoptosis?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "BlepharoptosisFunctionalDeficit"
                  }
                }
              ],
              "linkId": "BlepharoptosisFunctionalDeficit",
              "text": "Does it cause any functional deficit (visual field impairment/ brow fatigue)?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "CheckBlepharoptosis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            }
          ]
        },
        {
          "linkId": "4",
          "text": "Laterality",
          "type": "group",
          "item": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "Laterality"
                  }
                }
              ],
              "linkId": "Laterality",
              "text": "What is the laterality of the condition?",
              "type": "choice",
              "required": True,
              "answerOption": [
                {
                  "valueCoding": {
                    "code": "Unilateral",
                    "display": "Unilateral"
                  }
                },
                {
                  "valueCoding": {
                    "code": "Bilateral",
                    "display": "Bilateral"
                  }
                }
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "AnatomicalLocationCondition"
                  }
                }
              ],
              "linkId": "AnatomicalLocationCondition",
              "text": "Is the affected eye:",
              "type": "choice",
              "enableWhen": [
                {
                  "question": "Laterality",
                  "operator": "=",
                  "answerCoding": {
                    "code": "Unilateral",
                    "display": "Unilateral"
                  }
                }
              ],
              "required": True,
              "answerOption": [
                {
                  "valueCoding": {
                    "code": "Right",
                    "display": "Right"
                  }
                },
                {
                  "valueCoding": {
                    "code": "Left",
                    "display": "Left"
                  }
                }
              ]
            }
          ]
        },
        {
          "linkId": "5",
          "text": "Physical Signs",
          "type": "group",
          "item": [
            {
              "linkId": "ExcessiveSkinOverhanging",
              "text": "Is an amount of excessive skin overhanging the eyelid margin causing Pseudoptosis?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "CheckDermatochalasis",
                  "operator": "=",
                  "answerBoolean": True
                },
                {
                  "question": "CheckBlepharochalasis",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "enableBehavior": "any",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "PseudoMRD"
                  }
                }
              ],
              "linkId": "PseudoMRD",
              "text": "Is the central pseudo MRD less than 2mm?",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "ExcessiveSkinOverhanging",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            },
            {
              "linkId": "RedundantTissueObscureSight",
              "text": "Does the redundant tissue obscure the line of sight?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "EdemaRedundantTissue"
                  }
                }
              ],
              "linkId": "EdemaRedundantTissue",
              "text": "Is there any erythema/edema of the redundant tissue?",
              "type": "boolean",
              "required": True
            },
            {
              "linkId": "AngleEyelidLifting",
              "text": "Is the angle between the resting field and the field performed by manually lifting the eyelid more than 12 degrees?",
              "type": "boolean",
              "required": True
            }
          ]
        },
        {
          "linkId": "6",
          "text": "Contraindications",
          "type": "group",
          "item": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "ThyroidOrbitopathy"
                  }
                }
              ],
              "linkId": "ThyroidOrbitopathy",
              "text": "Does the patient have thyroid orbitopathy?",
              "type": "boolean",
              "required": True
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/cqf-expression",
                  "valueExpression": {
                    "language": "text/cql",
                    "expression": "CheckProptosis"
                  }
                }
              ],
              "linkId": "CheckProptosis",
              "text": "Does the patient have proptosis? ",
              "type": "boolean",
              "enableWhen": [
                {
                  "question": "ThyroidOrbitopathy",
                  "operator": "=",
                  "answerBoolean": True
                }
              ],
              "required": True
            }
          ]
        },
        {
          "linkId": "7",
          "text": "Photographic Evidence",
          "type": "group",
          "item": [
            {
              "linkId": "EvidenceDifficultyFittingProsthesis",
              "text": "Photographic documentation demonstrating abnormalities as they relate to the abnormal upper and/or lower eyelid position are required.",
              "type": "display"
            },
            {
              "linkId": "EvidencePhysicalSigns",
              "text": "Photographs of both eyelids in both frontal (straight ahead) and lateral (from the side) positions are required to demonstrate the physical signs.",
              "type": "display"
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/questionnaire-fileType",
                  "valueCode": "pdf"
                }
              ],
              "linkId": "EvidencePhysicalSignsUpload",
              "text": "Evidence Physical Signs Upload",
              "type": "attachment"
            }
          ]
        }
      ]
    }
  ],
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/context",
      "valueReference": {
        "reference": "Coverage/820ff38a-15da-11ef-ba8d-06cdd353a087"
      }
    }
  ],
  "author": {
    "reference": "Practitioner/0b6df3a8-2a6b-11ef-ba8d-06cdd353a087"
  }
}
        create_stub(response_body)

if __name__ == "__main__":
    main()
