from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    """Create fee category."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can create categories'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Category created'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_fees(request):
    """Assign fees to students."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can assign fees'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Fees assigned'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invoice_list(request):
    """List invoices."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view invoices'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'invoices': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invoice_detail(request, invoice_id):
    """Get invoice details."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view invoice details'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'invoice': {}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def record_payment(request):
    """Record payment."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can record payments'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Payment recorded'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_history(request):
    """View payment history."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view payment history'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'payments': []}, status=status.HTTP_200_OK)
