from rest_framework.pagination import PageNumberPagination

class TvShowPagination(PageNumberPagination): 
    page_size_query_param = 'page_size'
