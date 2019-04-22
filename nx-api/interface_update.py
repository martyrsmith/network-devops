import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    s = login()
    get_interface(s)
    change_interface(s)


def login():
    url = "https://localhost:8443/api/mo/aaaLogin.json"

    payload = {"aaaUser": {"attributes": {"name": "admin", "pwd": "cisco"}}}

    headers = {
        'Accept': "application/yang-data+json",
        'Content-Type': "application/json"
    }

    session = requests.Session()
    session.request("POST",
                    url,
                    data=json.dumps(payload),
                    headers=headers,
                    verify=False)
    return session


def get_interface(session):
    url = "https://localhost:8443/api/mo/sys/intf/phys-[eth1/35].json"

    headers = {
        'Accept': "application/yang-data+json",
        'Content-Type': "application/json"
    }

    response = session.request("GET", url, headers=headers, verify=False)
    print(json.dumps(response.json()['imdata'][0], sort_keys=True, indent=2))
    return response


def change_interface(session):
    url = "https://localhost:8443/api/mo/sys/intf/phys-[eth1/35].json"

    payload = {
        "l1PhysIf": {
            "attributes": {
                "nativeVlan": "vlan-2",
                "trunkVlans": "2,3",
                "descr": "Server 1"
            }
        }
    }
    headers = {
        'Accept': "application/yang-data+json",
        'Content-Type': "application/json"
    }

    response = session.request("POST",
                               url,
                               data=json.dumps(payload),
                               headers=headers,
                               verify=False)
    print('-' * 100)
    print(response)
    return response


main()
