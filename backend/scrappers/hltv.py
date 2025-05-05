import requests


class HltvScrapper:
    base_url = "https://www.hltv.org"

    def __init__(self, team_id: int, team_name: str):
        self.team_id = team_id
        self.team_name = team_name

    def get_team_page(self):
        team_url = f"{self.base_url}/team/{self.team_id}/{self.team_name}"
        # team_url = self.base_url

        req = requests.get(
            team_url,
            headers={
                # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            },
        )
        assert (
            req.status_code == 200
        ), f"Hltv Request failed, received {req.status_code}"
        breakpoint()
