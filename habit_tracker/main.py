import os
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("PIXELA_USERNAME")
token = os.environ.get("PIXELA_TOKEN")
graph_id = os.environ.get("GRAPH_ID")
graph_name = os.environ.get("GRAPH_NAME")
graph_unit = os.environ.get("GRAPH_UNIT")
graph_type = os.environ.get("GRAPH_TYPE")
graph_color = os.environ.get("GRAPH_COLOR")


def format_date(date=None):
    if not date:
        date = datetime.datetime.now()
    return str(date.strftime("%Y%m%d"))


request_type_dict = {
    "post": requests.post,
    "put": requests.put,
    "get": requests.get,
    "delete": requests.delete,
}


def make_request(
    url: str, request_type: str = "post", params: dict = None, headers: dict = None
) -> str:
    request_type = request_type_dict[request_type]
    response = request_type(url=url, json=params, headers=headers)
    response.raise_for_status()
    return response.text


def create_account():
    create_account_params = {
        "username": username,
        "token": token,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    print(make_request(url="https://pixe.la/v1/users", params=create_account_params))


def create_graph():
    create_graph_params = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color,
    }
    create_graph_headers = {"X-USER-TOKEN": token}
    print(
        make_request(
            url=f"https://pixe.la/v1/users/{username}/graphs",
            params=create_graph_params,
            headers=create_graph_headers,
        )
    )


def update_graph(quantity: int = 0, date: str = None, request_type: str = "put"):
    date = format_date(date)

    upload_to_graph_headers = {"X-USER-TOKEN": token}
    upload_to_graph_params = {"date": format_date(), "quantity": str(quantity)}
    print(
        make_request(
            request_type=request_type,
            url=f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}",
            params=upload_to_graph_params,
            headers=upload_to_graph_headers,
        )
    )


# create_account()
# create_graph()
update_graph(quantity=10_013, request_type="put")
# update_graph(quantity=5, date="20220716")
