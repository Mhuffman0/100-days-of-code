import requests


def make_request(
    request_type: str = "get",
    url: str = None,
    params: dict = None,
    data: dict = None,
    json: dict = None,
    headers: dict = None,
) -> dict:
    request_dict = {
        "get": requests.get,
        "post": requests.post,
        "delete": requests.delete,
        "put": requests.put,
    }
    request_type = request_dict[request_type]
    response = request_type(
        url=url, params=params, data=data, json=json, headers=headers
    )
    response.raise_for_status()
    # print(response.text)
    return response.json()


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, sheety_auth_token, sheety_url):
        self.sheety_auth_token = sheety_auth_token
        self.sheety_url = sheety_url
        self.flights = None

    def make_sheety_request(
        self, request_type: str = None, sheety_data: dict = None, url=None
    ):
        sheety_headers = {
            "Authorization": self.sheety_auth_token,
        }
        return make_request(
            request_type=request_type,
            json=sheety_data,
            url=url,
            headers=sheety_headers,
        )

    def get_flight_data(self):
        return self.make_sheety_request(
            request_type="get", url=self.sheety_url + "/prices"
        )

    def update_iata_codes(self, row_id: int, iata_code: str):
        url = f"{self.sheety_url}/prices/{row_id}"
        data = {
            "price": {
                "iataCode": iata_code,
            }
        }
        self.make_sheety_request(request_type="put", url=url, sheety_data=data)

    def get_customers(self):
        return self.make_sheety_request(
            request_type="get", url=self.sheety_url + "/users"
        )

    def customer_sign_up(self):
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email = None
        recheck_email = False
        while email != recheck_email:
            email = input("What is your email address?\n")
            recheck_email = input("What is your email one more time?\n")

        data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        return self.make_sheety_request(
            request_type="post", url=self.sheety_url + "/users", sheety_data=data
        )
