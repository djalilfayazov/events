from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
     def had_permission(self, request, view):
          if request.user.is_authenticated:
               return True
          
          return False
     

     def has_object_permission(self, request, view, object):
          if request.method in permissions.SAFE_METHODS:
               return True
          
          return object.userID == request.user
        
