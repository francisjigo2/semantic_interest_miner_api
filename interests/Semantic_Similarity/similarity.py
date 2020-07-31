from .WikiLink_Measure.Wiki import wikisim
from .Word_Embedding.IMsim import calculate_similarity


def get_interest_similarity_score(
    keyword_list_1, keyword_list_2, algorithm="WordEmbedding"
):
    if algorithm == "WordEmbedding":
        return calculate_similarity(keyword_list_1, keyword_list_2, embedding="Glove")
    else:
        return wikisim(keyword_list_1, keyword_list_2)