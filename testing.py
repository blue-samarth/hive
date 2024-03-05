from beem.discussions import Query, Discussions_by_feed
from transformers import pipeline
import re

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
q = Query(limit=1, tag="muterra")
print(q)
print(Discussions_by_feed(q))
comment = ''
for h in Discussions_by_feed(q):
    comment_content = h.body
    cleaned_content = re.sub(r'<[^>]+>', '', comment_content)
    cleaned_content = cleaned_content.replace('\n', '')
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    cleaned_content = re.sub(url_pattern, '', cleaned_content)
    square_brackets_pattern = r'\[.*?\]'
    curly_brackets_pattern = r'\{.*?\}'
    cleaned_content = re.sub(square_brackets_pattern, '', cleaned_content)
    cleaned_content = re.sub(curly_brackets_pattern, '', cleaned_content)
    comment += cleaned_content

tokens = comment.split()
token = [tokens[i:i+500] for i in range(0, len(tokens), 500)]
overall = []
for chunk in token:
    chunk_text = ' '.join(chunk)
    summary = summarizer(chunk_text , min_length=30, do_sample=False)
    print(summary)
    overall.append(summary[0]['summary_text'])
ret = ' '.join(overall)
print(ret)