```bash
git init; git clone https://github.com/tsragr/Test-tasks.git; cd Test-tasks; python3 -m venv venv; source venv/bin/activate
```

```bash
pip install -r requirements.txt; python test2/manage.py migrate; python test2/manage.py runserver
```
Make post HTTP request to http://127.0.0.1:8000/article/ send "article" as 1 element to return or "article_xlsx" xlsx file
to get list of values.