from rest_framework.pagination import PageNumberPagination


class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 's'
    max_page_size = 20