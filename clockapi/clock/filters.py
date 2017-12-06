from rest_framework import filters

class OwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that request user view his own objects
    """
    def filter_queryset(self, request, queryset, view):
        """
        :param request: HTTP Request
        :param queryset: View QuerySet
        :param view: View Instance
        :return: QuerySet filter by the user request as the owner
        """
        return queryset.filter(user=request.user)