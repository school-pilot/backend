import uuid

from fees.models import Invoice, Payment

import requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_invoice(request):
    """Create an invoice."""
    if request.user.role != 'school_admin':
        return Response({'error': 'Only school admins can create invoices'}, status=status.HTTP_403_FORBIDDEN)
    
    student_id = request.data.get('student_id')
    term_id = request.data.get('term_id')
    total_amount = request.data.get('total_amount')
    status = request.data.get('status')
    issued_date = request.data.get('issued_date')
    
    invoice = Invoice.objects.create(
        student_id=student_id,
        term_id=term_id,
        total_amount=total_amount,
        status=status,
        issued_date=issued_date
    )
    
    invoice.save()
    
    return Response({'message': 'Invoice created'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def initiate_payment(request, invoice_id):
    """Initiate a payment."""
    if request.user.role != "school_admin":
        return Response({'error': 'Only school admins can initiate payments'}, status=status.HTTP_403_FORBIDDEN)

    
    title = request.data.get('title')
    description = request.data.get('description')
    invoice = Invoice.objects.filter(id=invoice_id).first()
    
    if not invoice:
        return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if not title:
        return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not description:
        return Response({'error': 'Description is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Here you would integrate with your payment gateway to process the 
    try:
        tx_ref = str(uuid.uuid4())  # Generate a unique transaction reference
        url = "https://api.flutterwave.com/v3/payments"
        
        headers = {
            "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "tx_ref": tx_ref,
            "amount": invoice.total_amount,
            "currency": "NGN",
            "redirect_url": "https://your-redirect-url.com/payment-callback",
            "payment_options": "card,banktransfer",
            "customer": {
                "email": request.user.email,
                "phonenumber": "080****",
                "name": request.user.get_full_name()
            },
            "customizations": {
                "title": f"Payment for {title}",
                "description": f"{description}",
                "logo": "https://your-school-logo-url.com/logo.png"
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        payment = Payment.objects.create(
            invoice=invoice,
            amount=invoice.total_amount,
            payment_method='flutterwave',
            reference=tx_ref,
            confirmed_by=request.user.staffprofile
        )
        return Response(response.json(), status=200)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # subscription payment
    