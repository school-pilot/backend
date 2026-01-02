from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscription_plans(request):
    """Get available subscription plans."""
    plans = [
        {'id': 1, 'name': 'Basic', 'price': 100, 'features': ['Students', 'Teachers']},
        {'id': 2, 'name': 'Pro', 'price': 250, 'features': ['Students', 'Teachers', 'Results', 'Attendance']},
        {'id': 3, 'name': 'Enterprise', 'price': 500, 'features': ['All']}
    ]
    return Response({'plans': plans}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_subscription(request):
    """Get school's current subscription."""
    if request.user.role != 'school_admin':
        return Response({'error': 'Only school admins can view subscriptions'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'subscription': {}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upgrade_subscription(request):
    """Upgrade to a new subscription plan."""
    if request.user.role != 'school_admin':
        return Response({'error': 'Only school admins can upgrade subscriptions'}, status=status.HTTP_403_FORBIDDEN)
    plan_id = request.data.get('plan_id')
    return Response({'message': f'Upgraded to plan {plan_id}'}, status=status.HTTP_200_OK)
