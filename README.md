# semantic_interest_miner_api

This is the api for the main algorithms that was used by semantic interest miner web application.

## Before start the server:

Install the required dependencies using `pip install -r requirements.txt`

This project also requires external resources that can be obtained using:
```
python -m nltk.downloader stopwords
python -m nltk.downloader universal_tagset
python -m spacy download en # download the english model
```

Please download word embedding model(GloVe) and convert it into word2vec format, refer this link.

Please put the converted file under the `interests/Semantic_Similarity/Word_Embedding/data` .


To make migrations using:

```
python manage.py makemigrations
python manage.py migrate
```


## To start the server:
Run `python manage.py runserver`
<br>
Check the api docs at `127.0.0.0:8000/docs` after the server start.
