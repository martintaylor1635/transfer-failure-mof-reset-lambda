import os
import urllib3


class PdsService:
    def __init__(self):
        self.pds_adapter_url = os.environ["PDS_ADAPTER_URL"]
        self.pds_adapter_authorisation_key = os.environ["PDS_ADAPTER_AUTHORISATION_KEYS"]

    def update_mof(self, nhs_number: str) -> None:
        response = urllib3.request(
            method='PUT',
            url=self.pds_adapter_url,
            headers={
                "authorisation_keys": self.pds_adapter_authorisation_key
            }
        )

        if response.status != 200:
            pass

    def verify_mof_updated(self, nhs_number: str) -> None:
        pass
