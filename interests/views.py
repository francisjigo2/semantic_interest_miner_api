from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from interests.Keyword_Extractor.extractor import getKeyword
from interests.Semantic_Similarity.similarity import get_interest_similarity_score
from interests.Semantic_Enrichment.wikipedia_utils import wikifilter,wikicategory


from .serializers import (
    InterestExtractionSerializer,
    KeywordSimilariySerializer,
    WikiCategoriesSerializer
)


class PublicInterestExtractionView(GenericAPIView):
    """
    Extracts interests from the specified text based on the selected algorithm
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = InterestExtractionSerializer

    def post(self, request, *args, **kwargs):
        inputs = self.serializer_class(data=request.data)
        inputs.is_valid(raise_exception=True)
        payload = inputs.validated_data
        interests= getKeyword(
            payload["text"], model=payload["algorithm"], num=payload["num_of_keywords"]
        )
        if payload["wiki_filter"]:
            interests = wikifilter(interests)[1]
        return Response(interests)


class PublicKeywordSimilarityView(GenericAPIView):
    """
    Returns the similarity score for 2 sets of interest terms based on the selected Algorithm
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = KeywordSimilariySerializer

    def post(self, request, *args, **kwargs):
        inputs = self.serializer_class(data=request.data)
        inputs.is_valid(raise_exception=True)
        payload = inputs.validated_data
        score = get_interest_similarity_score(
            payload["keywords_1"], payload["keywords_2"], payload["algorithm"]
        )
        return Response({"score": round((score or 0) * 100, 2)})

class PublicKeywordCategoriesView(GenericAPIView):
    """
    Returns the Wikipedia categories of interest terms
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = WikiCategoriesSerializer

    def post(self, request, *args, **kwargs):
        inputs = self.serializer_class(data=request.data)
        inputs.is_valid(raise_exception=True)
        payload = inputs.validated_data
        categories = {}
        for keyword in payload["keywords"]:
            category = wikicategory(keyword)
            categories[keyword] = category
        return Response(categories)