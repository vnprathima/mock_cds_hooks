import requests

def create_stub():
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "GET",
            "url": "/cds-services"
        },
        "response": {
            "status": 200,
            "jsonBody": {
            "services": [
                {
                    "description": "CDS Service for Prior Authorisation",
                    "extension": {
                        "davinci-crd.configuration-options": [
                        {
                            "code": "auth-req",
                            "default": True,
                            "description": "Is prior authorization required for the current service or not, or is there additional data that needs to be collected to make that determination?",
                            "name": "Prior authorization Required",
                            "type": "boolean"
                        },
                        {
                            "code": "documentation",
                            "default": False,
                            "description": "Are there additional documentation requirements",
                            "name": "Documentation",
                            "type": "boolean"
                        }
                        ]
                    },
                    "hook": "order-sign",
                    "id": "mettles-order-sign",
                    "prefetch": {
                        "coverageBundle": "Coverage?patient={{context.patientId}}&_include=Coverage:payor",
                        "deviceRequestBundle": "DeviceRequest?_id={{context.draftOrders.DeviceRequest.id}}&_include=DeviceRequest:patient&_include=DeviceRequest:performer&_include=DeviceRequest:requester&_include=DeviceRequest:device&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner",
                        "medicationRequestBundle": "MedicationRequest?_id={{context.medications.MedicationRequest.id}}&_include=MedicationRequest:patient&_include=MedicationRequest:intended-dispenser&_include=MedicationRequest:requester:PractitionerRole&_include=MedicationRequest:medication&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner",
                        "serviceRequestBundle": "ServiceRequest?_id={{context.draftOrders.ServiceRequest.id}}&_include=ServiceRequest:patient&_include=ServiceRequest:performer&_include=ServiceRequest:requester&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner"
                    },
                    "title": "Mettles CDS Service",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                },
                {
                    "description": "CDS Service for ORder Dispatch",
                    "extension": {
                        "davinci-crd.configuration-options": [
                        {
                            "code": "auth-req",
                            "default": True,
                            "description": "Is prior authorization required for the current service or not, or is there additional data that needs to be collected to make that determination?",
                            "name": "Prior authorization Required",
                            "type": "boolean"
                        },
                        {
                            "code": "documentation",
                            "default": False,
                            "description": "Are there additional documentation requirements",
                            "name": "Documentation",
                            "type": "boolean"
                        }
                        ]
                    },
                    "hook": "order-dispatch",
                    "id": "mettles-order-dispatch",
                    "title": "mettles CDS Service",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                },
                {
                    "description": "CDS Service for Order Select",
                    "extension": {
                        "davinci-crd.configuration-options": [
                        {
                            "code": "auth-req",
                            "default": True,
                            "description": "Is prior authorization required for the current service or not, or is there additional data that needs to be collected to make that determination?",
                            "name": "Prior authorization Required",
                            "type": "boolean"
                        },
                        {
                            "code": "documentation",
                            "default": False,
                            "description": "Are there additional documentation requirements",
                            "name": "Documentation",
                            "type": "boolean"
                        }
                        ]
                    },
                    "prefetch": {
                        "coverageBundle": "Coverage?patient={{context.patientId}}&_include=Coverage:payor",
                        "deviceRequestBundle": "DeviceRequest?_id={{context.draftOrders.DeviceRequest.id}}&_include=DeviceRequest:patient&_include=DeviceRequest:performer&_include=DeviceRequest:requester&_include=DeviceRequest:device&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner",
                        "medicationRequestBundle": "MedicationRequest?_id={{context.medications.MedicationRequest.id}}&_include=MedicationRequest:patient&_include=MedicationRequest:intended-dispenser&_include=MedicationRequest:requester:PractitionerRole&_include=MedicationRequest:medication&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner",
                        "serviceRequestBundle": "ServiceRequest?_id={{context.draftOrders.ServiceRequest.id}}&_include=ServiceRequest:patient&_include=ServiceRequest:performer&_include=ServiceRequest:requester&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner"
                    },
                    "hook": "order-select",
                    "id": "mettles-order-select",
                    "title": "Mettles Order Select",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                },
                {
                    "description": "CDS Service for Encounter Start",
                    "prefetch": {
                        "coverageBundle": "Coverage?patient={{context.patientId}}&_include=Coverage:payor",
                    },
                    "hook": "encounter-start",
                    "id": "mettles-encounter-start",
                    "title": "Mettles Encounter Start",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                },
                {
                    "description": "CDS Service for Encounter Discharge",
                    "prefetch": {
                        "coverageBundle": "Coverage?patient={{context.patientId}}&_include=Coverage:payor",
                    },
                    "hook": "encounter-discharge",
                    "id": "mettles-encounter-discharge",
                    "title": "Mettles Encounter Discharge",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                },
                {
                    "description": "CDS Service for Appointment Book",
                    "prefetch": {
                        "serviceRequestBundle": "ServiceRequest?_id={{context.appointments.Appointment.basedOn}}&_include=ServiceRequest:patient&_include=ServiceRequest:performer&_include=ServiceRequest:requester&_include=PractitionerRole:organization&_include=PractitionerRole:practitioner",
                        "appointmentBundle": "Appointment?_id={{context.appointments.Appointment.id}}&_include=Appointment:based-on&_include=Appointment:patient&_include=Appointment:practitioner&_include=Appointment:practitioner:PractitionerRole&_include:iterate=PractitionerRole:organization&_include:iterate=PractitionerRole:practitioner&_include=Appointment:location",
                        "coverageBundle": "Coverage?patient={{context.patientId}}"
                    },
                    "hook": "appointment-book",
                    "id": "mettles-appointment-book",
                    "title": "Mettles Appointment Book",
                    "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation."
                }
            ]
            },
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
        }
    }

    url = f"{wiremock_base_url}/__admin/mappings"
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print("Stub created successfully")

if __name__ == "__main__":
    create_stub()
