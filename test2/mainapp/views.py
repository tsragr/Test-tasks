import asyncio

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.models import Article
from mainapp.utils import main


class ArticleView(APIView):

    def post(self, request):
        data = asyncio.run(main())
        if request.POST.get('article'):
            article = int(request.POST.get('article'))
            single_data = list(filter(lambda el: el['id'] == article, data))[0]
            return Response(Article(article=single_data['id'], brand=single_data['brand'], title=single_data['name']))
        article_xlsx = list(map(int, request.FILES.get('article_xlsx').read().decode('utf-8').split()))
        data_result = list(filter(lambda el: el['id'] in article_xlsx, data))
        data_res = [Article(article=el['id'], brand=el['brand'], title=el['name']) for el in data_result]
        return Response(data_res)
