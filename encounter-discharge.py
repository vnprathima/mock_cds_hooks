import requests

def create_stub(response_body):
    wiremock_base_url = "http://localhost:8082"
    
    mapping = {
        "request": {
            "method": "POST",
            "url": "/cds-services/mettles-encounter-discharge",
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
            "url": "/cds-services/mettles-encounter-discharge"
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
    print(f"OPTIONS stub for encounter-start created successfully")

    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.post(url, json=mapping)
    response.raise_for_status()
    print(f"POST stub for encounter-start created successfully")

def main():
    
        response_body = {
            "cards":[{
                "summary": "High risk for opioid overdose - taper now",
                "indicator": "warning",
                "links": [
                    {
                    "label": "CDC guideline for prescribing opioids for chronic pain",
                    "type": "absolute",
                    "url": "https://guidelines.gov/summaries/summary/50153/cdc-guideline-for-prescribing-opioids-for-chronic-pain---united-states-2016#420"
                    },
                    {
                    "label": "MME Conversion Tables",
                    "type": "absolute",
                    "url": "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily_dose-a.pdf"
                    }
                ],
                "detail": "Total morphine milligram equivalent (MME) is 125mg. Taper to less than 50."
                },
                {
                "summary": "High risk for opioid overdose - taper now",
                "indicator": "warning",
                "detail": "Total morphine milligram equivalent (MME) is 125mg. Taper to less than 50."
                }],
        }
        create_stub(response_body)

if __name__ == "__main__":
    main()
