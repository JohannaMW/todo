# from django.contrib.auth import get_user_model
# from rest_framework import permissions
#
# UserProfile = get_user_model()  # Reference active User model
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Write permissions are only allowed to the owner of the snippet.
#         if isinstance(obj, UserProfile):
#             return obj == request.user
#         else:
#             return obj.owner == request.user