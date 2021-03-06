from pyframework.commands.listen import Listen

from src.commands.actions.download_entity import DownloadEntity as DownloadEntityAction
from src.commands.actions.download_place import DownloadPlace as DownloadPlaceAction
from src.commands.actions.recommendation import Recommend as RecommendAction
from src.commands.fire.fire_city_restaurants_download import FireCityRestaurantsDownload
from src.commands.fire.fire_restaurants_info_download import FireRestaurantsInfoDownload
from src.commands.tasks.download_entity import DownloadEntity as DownloadEntityTask
from src.commands.tasks.download_place import DownloadPlace as DownloadPlaceTask
from src.commands.tasks.recommendation import Recommend as RecommendTask
from src.commands.tools.generate_sentimental_analyzer import GenerateSentimentalAnalyzer
from src.commands.tools.train import Train as RecommendCommand
from src.commands.tools.generate_wordsclud import GenerateWordsCloud

metadata = {
    "commands": {
        # Fire.
        'fire:cityDownload': FireCityRestaurantsDownload,
        'fire:restaurantsInfoDownload': FireRestaurantsInfoDownload,

        # Actions.
        'download:place:ready:action': DownloadPlaceAction,
        'download:entity:ready:action': DownloadEntityAction,
        'recommendation:ready:action': RecommendAction,

        # Tasks.
        'download:place:ready:task': DownloadPlaceTask,
        'download:entity:ready:task': DownloadEntityTask,
        'recommendation:ready:task': RecommendTask,

        # Tools.
        'tools:generateSentimentalAnalyzer': GenerateSentimentalAnalyzer,
        'tools:train': RecommendCommand,
        'tools:generateWordsCloud': GenerateWordsCloud,

        # Py-framework commands.
        'Listen': Listen,
    },
    'cliTimeout': 60,
}
