""" Client For Docker Hub """

import requests
import logging

API_BASE_URL = "https://hub.docker.com/v2"
REPO_PAGE_URL = "https://hub.docker.com/%user%/%repo%"

logger = logging.getLogger(__name__)


class DockerHubException(Exception):
    """ Exception when communicating with DockerHub """
    pass


class Client:
    """ DockerHub Client Class """
    def search_repos(self, filter_term):
        """ Search repositories on Docker Hub """

        response = requests.get('%s/search/repositories' % API_BASE_URL,
                                params={"query": filter_term})

        if response.status_code != 200:
            logger.error(
                "Cannot get list of repositories from DockerHub. Response: %s"
                % response.text)
            raise DockerHubException()

        data = response.json()

        items = []
        for item in data["results"]:
            url = REPO_PAGE_URL.replace("%repo%", item["repo_name"])
            if item["is_official"]:
                url = url.replace("%user%", "_")
            else:
                url = url.replace("%user%", "r")

            items.append({
                "name": item["repo_name"],
                "description": item["short_description"],
                "stars": item["star_count"],
                "pulls": item["pull_count"],
                "url": url
            })

        return items
