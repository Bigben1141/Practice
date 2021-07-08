menu=[
    {'title': "Пьесы",'url_name':'home'},
    {'title': "Актеры",'url_name':'actors'},
    {'title': "Добавить пьесу",'url_name':'addplay'},
    {'title': "Добавить актера",'url_name':'addpage'},
]

class DataMixin:
    def get_user_context(self,**kwargs):
        context=kwargs
        context['menu']=menu
        return context