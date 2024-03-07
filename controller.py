import flask 
from flask import request, jsonify , render_template
from transformers import pipeline
import re
from beem import Hive
from beem.discussions import Query, Discussions_by_feed
from beem.account import Account

h = Hive()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    import tetsttt
    transactions = tetsttt.transactions
    return render_template('index.html', transactions=transactions , block_num=tetsttt.current_block_num)

@app.route('/search' , methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        def get_user_transactions(username):
            # count = 5
            # trans = []
            account = Account(username, blockchain_instance=h)
            transactions = account.history(use_block_num=False, only_ops=['transfer'])
            print(f"Transactions for {username}:")
            for transaction in transactions:
                return transaction
        trans = get_user_transactions(search)
        # trans = get_user_transactions(search)
        print(trans)
        print(1)
        return render_template('search.html', transaction=trans)

@app.route('/summarize' , methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        tag1 = request.form['tag']
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        q = Query(limit=1, tag=tag1)
        print(q)
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
        return render_template('summarize.html', summary=ret)
    import testing 
    return render_template('summarize.html', summary=testing.ret)



if __name__ == '__main__':
    app.run()
