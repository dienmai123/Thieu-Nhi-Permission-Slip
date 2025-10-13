import os
import pprint
import requests

# ---- CONFIG ----
DOCUSEAL_URL = "https://api.docuseal.com/submitters"
API_TOKEN = os.getenv("DOCUSEAL_API_TOKEN") or "FmzWAds1rshavQtaN3BWjSvnHsrW9vuUVLTBMjDuZM4"  # fallback if env var not set


def fetch_submitter_names(url: str, api_token: str) -> list[str]:
    """ 
    Get cac em name that submit the form in the text field 2 ( which is their name) 
    from Docuseal. The data get remove every month.
    """
    
    headers = {"X-Auth-Token": api_token}
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        raise RuntimeError(f"Docuseal API return {response.status_code}: {response.text}")
    
    data = response.json()
    names: list[str] = []

    for submission in data.get('data',[]):
        values_map = {v['field'] :v['value'] for v in submission.get('values',[])}
        cac_em_name = values_map.get('Text Field 2')

        if cac_em_name:
            names.append(cac_em_name)

    return names

if __name__ == '__main__':
    result = fetch_submitter_names(DOCUSEAL_URL,API_TOKEN)
    print(result)



