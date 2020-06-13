from rest_framework import pagination


class ForumAPIPagination(pagination.LimitOffsetPagination):  # LimitOffsetPagination - for settings limit and offset
    page_size = 5
    # default_limit = 10 # For LimitOffsetPagination
    # max_limit = 2 # For LimitOffsetPagination
    # limit_query_param = 'lim' # For LimitOffsetPagination - instead of limit, lim must be passed in endpoint
