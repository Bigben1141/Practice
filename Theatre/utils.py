menu=[
    {'title': "Пьесы",'url_name':'home'},
    {'title': "Актеры",'url_name':'actors'},
]

class DataMixin:
    def get_user_context(self,**kwargs):
        context=kwargs
        context['menu']=menu
        return context