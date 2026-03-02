from rest_framework.permissions import BasePermission, IsAuthenticated

class HasRolePermission(IsAuthenticated):
    required_role = None

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        
        return request.user.role == self.required_role

class IsAdmin(HasRolePermission):
    required_role = 'Administrator'

class IsManager(HasRolePermission):
    required_role = 'Manager'

class IsTeacher(HasRolePermission):
    required_role = 'Teacher'

class IsStudent(HasRolePermission):
    required_role = 'Student'