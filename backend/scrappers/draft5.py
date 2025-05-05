from datetime import date
import requests
from models.team import Team, Player, Draft5StatusesMapping, Match, Matches


class Draft5Scrapper:
    base_url = "https://api.draft5.gg"
    team = Team(name="Furia")

    def __init__(self, team_id: int, team_name: str):
        self.team_id = team_id
        self.team_name = team_name

    def run(self) -> Team:
        self._get_players()
        self._get_matches()

        return self.team

    def _get_players(self):
        team_url = f"{self.base_url}/teams/{self.team_id}?actual=true"
        req = requests.get(
            team_url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
            },
        )
        assert (
            req.status_code == 200
        ), f"Draft5 Request failed, received {req.status_code}"

        result = req.json()["data"]

        players = [
            Player(
                name=f"{player['playerFirstName']} {player['playerLastName']}",
                nickname=player["playerNickname"],
                country=player["playerCountry"],
                status=Draft5StatusesMapping[
                    player["playerHistory"][0]["status"]
                ].value,
                start_date=player["playerHistory"][0]["startDate"],
            )
            for player in result["playerData"]
        ]
        self.team.players = players

    def _get_matches(self):
        def _make_request(finished=False):
            req = requests.get(
                f"{self.base_url}/matches",
                params={
                    "page": 1,
                    "amount": 10,
                    "finished": 1 if finished else 0,
                    "featured": 0,
                    "team": self.team_id,
                    "showHidden": 0,
                },
            )
            assert (
                req.status_code == 200
            ), f"Draft5 Request failed, received {req.status_code}"

            result = req.json()["data"]
            return result

        def _parse_matches_response(match_list: list[dict]) -> list[Match]:
            matches = []
            for match in match_list:
                team_a = {
                    "id": match["teamA"]["teamId"],
                    "name": match["teamA"]["teamName"],
                }
                team_b = {
                    "id": match["teamB"]["teamId"],
                    "name": match["teamB"]["teamName"],
                }
                against = team_a if team_a["id"] != self.team_id else team_b
                matches.append(
                    Match(
                        against=against["name"],
                        date=date.fromtimestamp(match["matchDate"]),
                    )
                )
            return matches

        result = _make_request(finished=False)
        upcoming_matches = _parse_matches_response(result["list"])

        result = _make_request(finished=True)
        recent_matches = _parse_matches_response(result["list"])

        self.team.matches = Matches(
            upcoming=upcoming_matches,
            recent=recent_matches,
        )
