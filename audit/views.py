from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def audit_logs(request):
    """Get system audit logs (super_admin only)."""
    if request.user.role != 'super_admin':
        return Response({'error': 'Only super admins can view audit logs'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'logs': []}, status=status.HTTP_200_OK)
