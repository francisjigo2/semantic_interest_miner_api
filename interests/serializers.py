
from rest_framework import serializers


class InterestExtractionSerializer(serializers.Serializer):
    text = serializers.CharField()
    algorithm = serializers.ChoiceField(
        choices=[
            ("Yake", "Yake"),
            ("SingleRank", "SingleRank"),
            ("TopicRank", "TopicRank"),
            ("TextRank", "TextRank"),
            ("PositionRank", "PositionRank"),
            ("Rake", "Rake"),
            ("MultipartiteRank", "MultipartiteRank"),
            ("TopicalPageRank", "TopicalPageRank"),
        ]
    )
    wiki_filter = serializers.BooleanField(default=True)
    num_of_keywords = serializers.IntegerField(default=20)


class KeywordSimilariySerializer(serializers.Serializer):
    keywords_1 = serializers.ListField()
    keywords_2 = serializers.ListField()
    algorithm = serializers.ChoiceField(
        choices=[
            ("WordEmbedding", "WordEmbedding"),
            ("WikiLinkMeasure", "WikiLinkMeasure"),
        ]
    )



class WikiCategoriesSerializer(serializers.Serializer):
    keywords = serializers.ListField()
