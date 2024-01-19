from rest_framework import permissions

class IsMemberOfGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='SpecificGroupName').exists()
