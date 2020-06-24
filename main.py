""" Main Module """

import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from dockerhub.client import Client

logger = logging.getLogger(__name__)


class DockerHubExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(DockerHubExtension, self).__init__()
        self.dockerhub = Client()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def search_repositories(self, query):
        """ Shows the a list of DockerHub repositories """
        if len(query) < 3:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Keep typing to search on Docker Hub ...',
                    highlightable=False,
                    on_enter=DoNothingAction())
            ])

        repos = self.dockerhub.search_repos(query)

        items = []

        if not repos:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="No results found matching your criteria",
                    highlightable=False,
                    on_enter=HideWindowAction())
            ])

        for repo in repos[:8]:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="%s 🟊 %s" % (repo["name"], repo["stars"]),
                    description=repo["description"],
                    on_enter=OpenUrlAction(repo["url"]),
                    on_alt_enter=ExtensionCustomAction(
                        {"url": repo["url"]},
                        False)))  # TODO try to create a window heere.

        return RenderResultListAction(items)


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        query = event.get_argument() or ""
        return extension.search_repositories(query)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()
        RunScriptAction('hawkeye --uri="%s"' % data["url"], []).run()


if __name__ == '__main__':
    DockerHubExtension().run()
