import requests

def delete_all_stubs():
    wiremock_base_url = "http://localhost:8082"
    url = "{}/__admin/mappings".format(wiremock_base_url)
    response = requests.delete(url)
    response.raise_for_status()
    print("All stubs deleted successfully")

if __name__ == "__main__":
    delete_all_stubs()