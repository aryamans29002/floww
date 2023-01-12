# Python Core Imports
import json
from math import trunc
import random
import requests
from datetime import datetime

# Django Core Imports
from django.shortcuts import render
from django.http import HttpResponse

# Django Auth Imports

# REST API
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Database Imports
from .models import ErrorLogApi, UsageLogApi

# Variable Imports
#from .floww_variables import SERVICE_LIST, RENTAL_PLANS_AVAILABLE, PRODUCT_LIST

# Contant Imports
#from main_project.constants import TASK_DETAILS_BASE_URL









# Edit Order Details

class EditOrderInstructions(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        pass
 
    def post(self, request):
        # Get user_id from Token auth. Django DB (user_id/uid) -> Company Detail DB (uid) -> user_id

        #user_uid = request.user.username
        user_id = 'testing'#CompanyDetails.objects.get(user_uid=user_uid).user_id

        # try:

        # Sample POST data: { “vendorCode”:”VEN88762”, ”productDescription”:”Bottles”, ”companyName”:”Myntra”, ”deliveryDate”:”13/12/2021”, “orderType”:”perOrder”, ”orderList” : [ {“pickup”:”F-205”, “pickupPincode”: “400076”, “pickupNo”:”9999999999”, “drop”:”F-205”, “dropPincode”: “400076”, “dropNo”:”99999”, “weight”:”small”, “instruction”:”Delivery to watchman”}, {} ], “rentalPlan”: ”plan1”, “serviceList”:[“same_day”,”otp”]}
        # To check, if the orderId parameter is sent correctly
        try:
            order_id = str(request.data.get('orderId'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_id_not_found', 'message': 'Either orderId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)

        try:
            instructions = str(request.data.get('instruction'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'instruction_not_found', 'message': 'Either instruction is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)


        # To check, if the order (via orderId) is present in the database
        try:            
            # From the vendor_code, take out vendor charge data 
            #order_query = OrderDetails.objects.get(order_id=order_id)

            order_query = {
                'instructions':'xyz'
            }

        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            
            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)

        try:
            #order_query.instructions = str(instructions)
            #order_query.save()

            order_query['instructions'] = instructions
            status = 'success'

            # ----------------Logging
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=True, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(
            {'status': status})
            return Response(response, status=201)
        
        except Exception as e:
            status = 'failure'
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(
            {'status': status})
            return Response(response, status=400)

    def delete(self, request):
        pass

    def put(self, request):
        pass








# Get Order Details

class GetOrderDetails(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        # Get user_id from Token auth. Django DB (user_id/uid) -> Company Detail DB (uid) -> user_id

        #user_uid = request.user.username
        user_id = 'testing'#CompanyDetails.objects.get(user_uid=user_uid).user_id

        # To check, if the orderId parameter is sent correctly
        try:
            order_id = str(request.query_params.get('orderId'))
        except Exception as e:

            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetOrderDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_id_not_found', 'message': 'Either orderId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)
        
            # To check, if the task (via taskId) is present in the database
        try:
            #order_query = OrderDetails.objects.get(order_id=order_id)
            order_query = {
                'pickup_address':'xyz',
                'drop_address':'xyz',
                'pickup_pincode':'xyz',
                'drop_pincode':'xyz',
                'pickup_contact_no':'xyz',
                'drop_contact_no':'xyz',
                'weight':'xyz',
                'status':'xyz',
                'instructions':'xyz',
            }
            pickup_address = order_query.pickup_address #dictionary {}
            drop_address = order_query.drop_address  
            pickup_pincode = order_query.pickup_pincode 
            drop_pincode = order_query.drop_pincode 
            pickup_contact_no = order_query.pickup_contact_no 
            drop_contact_no = order_query.drop_contact_no 
            weight = order_query.weight
            status = order_query.status                         # It is a list containing an object
            instructions = order_query.instructions 

            # Get Task Id also
            #task_query = TaskDetails.objects.get(orders_list={'order_id':order_id})
            task_id = 'xyz'#task_query.task_id
            

            data = {'orderId': order_id, 'pickup': pickup_address, 'drop': drop_address, 'pickupPincode': int(pickup_pincode), 
            'dropPincode': int(drop_pincode), 'pickupNo': pickup_contact_no, 'dropNo': drop_contact_no, 'weight': float(weight), 
            'instruction': instructions, 'orderStatusList':status, 'taskId':task_id}


            # ----------------Logging
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=True, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(data)
            return Response(response, status=200)

        except Exception as e:
            
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetOrderDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)
        
        

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass






# Track Order

class Track_Order(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        # Get orderID from Token auth. Django DB (orderID/oid) -> Company Detail DB (oid) -> orderID

        #orderID = request.order.ordername
        orderId = 'testing'#CompanyDetails.objects.get(order_uid=order_uid).order_id

        # To check, if the orderId parameter is sent correctly
        try:
            order_id = str(request.query_params.get('orderId'))
        except Exception as e:

            # ----------------Logging
            ErrorLogApi.objects.create(api_name='Track_Order', error_val=e, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)
            UsageLogApi.objects.create(api_name='Track_Order', api_success=False, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)

            response = json.dumps({'status': 400, 'error': 'order_id_not_found ', 'message': 'Either orderId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)
        
        # To check, if the order (via orderId) is present in the database
        try:
            #order_query = OrderDetails.objects.get(order_id=order_id)
            order_query = {
                'Status':'xyz',
                'Timestamp ':'xyz',
            }
            orderStatus = order_query.Status #dictionary {}
            orderTimestamp = order_query.Timestamp 
           
            data = {'Status': orderStatus, 'Timestamp': orderTimestamp}

            # ----------------Logging
            UsageLogApi.objects.create(api_name='Track_Order', api_success=True, timestamp=str(int(datetime.now().timestamp())),order_id=orderId)

            response = json.dumps(data)
            return Response(response, status=200)

        except Exception as e:
            
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='Track_Order', error_val=e, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)
            UsageLogApi.objects.create(api_name='Track_Order', api_success=False, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)

            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)

        except Exception as e:
            
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='Track_Order', error_val=e, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)
            UsageLogApi.objects.create(api_name='Track_Order', api_success=False, timestamp=str(int(datetime.now().timestamp())), order_id=orderId)

            response = json.dumps({'status': 400, 'error': 'status_not_found', 'message': 'There are no statuses saved in database for this order'})                # [EDIT]
            return Response(response, status=400)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass


# Cancel Orders

class Cancel_Orders(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        pass
 
    def post(self, request):
        # Get orderList from Token auth. Django DB (OrderList/orderid) -> Company Detail DB (orderlist) -> orderlist

        
        orderlist = ["sample 1","sample 2","sample 3"]
        #orderList”: [ “ORD-0000236”, “ORD-00000211”, “ORD-00000211”] i.e a sample orderlist
       
        try:
            order_list= list(request.data.get('orderlist'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='Cancel_Orders', error_val=e, timestamp=str(int(datetime.now().timestamp())),   order_list=orderlist)
            UsageLogApi.objects.create(api_name='Cancel_Orders', api_success=False, timestamp=str(int(datetime.now().timestamp())),   order_list= orderlist)

            response = json.dumps({'status': 400, 'error': 'order_list_not_found ', 'message': 'Either orderList is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)

        # To check, if the order (via orderlist) is present in the database
        try:            
           

            order_query = {
                'status':'xyz',
                'notCancelled':["sample 1","sample 2","sample 3"]
            }

        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='Cancel_Orders', error_val=e, timestamp=str(int(datetime.now().timestamp())),order_list=orderlist)
            UsageLogApi.objects.create(api_name='Cancel_Orders', api_success=False, timestamp=str(int(datetime.now().timestamp())),order_list=orderlist)
            
            response = json.dumps({'status': 400, 'error': 'order_list_structure_error ', 'message': 'orderList array structure seems incorrect'})                # [EDIT]
            return Response(response, status=400)

      

    def delete(self, request):
        pass

    def put(self, request):
        pass




# Get Task Details

class GetTaskDetails(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        # Get task_id from Token auth. Django DB (task_id/tid) -> Company Detail DB (tid) -> task_id 
        #task_uid = request.task.taskname
        task_id = 'testing'#CompanyDetails.objects.get(user_uid=user_uid).user_id

        # To check, if the orderId parameter is sent correctly
        try:
            task_id = str(request.query_params.get('taskID'))
        except Exception as e:

            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetTaskDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), task_id=task_id)
            UsageLogApi.objects.create(api_name='GetTaskDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), task_id=task_id)

            response = json.dumps({'status': 400, 'error': 'task_id_not_found ', 'message': 'Either taskId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)
        
       # To check, if the order (via orderId) is present in the database
        try:
            #order_query = OrderDetails.objects.get(order_id=order_id)
            task_query = {
                'vendorCode':'xyz',
                'vendorName':'xyz',
                'vendorConatactNo':'xyz',
                'vendorWebLink':'xyz',
                'productDescription':'xyz',
                'companyName':'xyz',
                'contactNo':'xyz',
                'estimatedCost': 0.00,
                'correctedCost': 0.00,
                'currency':'xyz',
                'deliveryTimestamp':'xyz',
                'taskTimestamp':'xyz',
                'orderType':'xyz',
                'orderList':['xyx'],
                'rentalPlan':'xyz',
                'serviceList':['xyx']
            }
            vendorCode = task_query.vendorCode #dictionary {} # change this task_query["vendorCode"]
            vendorName = task_query.vendorName 
            vendorConatactNo = task_query.vendorConatactNo 
            vendorWebLink = task_query.vendorWebLink 
            productDescription = task_query.productDescription
            companyName = task_query.companyName 
            contactNo= task_query.contactNo
            estimatedCost = task_query.estimatedCost                         
            correctedCost = task_query.correctedCost
            currency = task_query.currency
            deliveryTimestamp = task_query.deliveryTimestamp
            taskTimestamp = task_query.taskTimestamp
            orderType = task_query.orderType
            orderList = task_query.orderList
            rentalPlan = task_query.rentalPlan
            serviceList = task_query.serviceList


            task_id = 'xyz'
            

            data = {'vendorCode': vendorCode, 'vendorName': vendorName, 'vendorConatactNo': vendorConatactNo, 'vendorWebLink': vendorWebLink, 
            'productDescription': productDescription, 'companyName': companyName, 'contactNo': contactNo, 'estimatedCost': float(estimatedCost),
            'correctedCost': float(correctedCost), 'currency': currency, 'deliveryTimestamp':deliveryTimestamp, 'taskTimestamp':taskTimestamp,'orderType':orderType,
            'orderList':list(orderList),'rentalPlan':rentalPlan,'serviceList':list(serviceList)}

            # ----------------Logging
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=True, timestamp=str(int(datetime.now().timestamp())), task_id=task_id)

            response = json.dumps(data)
            return Response(response, status=200)

        except Exception as e:
            
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetTaskDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), task_id=task_id)
            UsageLogApi.objects.create(api_name='GetTaskDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), task_id=task_id)

            response = json.dumps({'status': 400, 'error': 'task_not_found ', 'message': 'taskId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)
        
        

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass



# Estimate Task Cost

class EstimateTaskCost(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        pass
 
    def post(self, request):
     
        vendor_code = 'testing'

        try:
            vendorCode = str(request.data.get('vendorCode'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EstimateTaskCost', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EstimateTaskCost', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'vendor_code_not_found ', 'message': 'Either vendorCode is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)

        try:
            orderType  = str(request.data.get('orderType'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EstimateTaskCost', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EstimateTaskCost', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            
            response = json.dumps({'status': 400, 'error': 'order_type_invalid', 'message': 'This orderType is not supported by vendor, please contact the vendor for clarification'})                # [EDIT]
            return Response(response, status=400)

        try:
            orderList  = list(request.data.get('orderType'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EstimateTaskCost', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EstimateTaskCost', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            
            response = json.dumps({'status': 400, 'error': 'order_list_structure_error', 'message': 'The order object structure inside orderList is wrong'})                # [EDIT]
            return Response(response, status=400)
        
        try:
            rentalPlan  = list(request.data.get('rentalPlan'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EstimateTaskCost', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EstimateTaskCost', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            
            response = json.dumps({'status': 400, 'error': 'rental_plan_not_found ', 'message': 'Either rentalPlan is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)


        # To check, if the order (via orderId) is present in the database
        try:            
            # From the vendor_code, take out vendor charge data 
            #order_query = OrderDetails.objects.get(order_id=order_id)

            vendor_query = {
                'estimatedCost': 0.00,
                'curreny':'xyz',
                'usageWarnings': 'xyz'
            }

        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EstimateTaskCost', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EstimateTaskCost', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            
            response = json.dumps({'status': 400, 'error': 'rental_plan_not_found ', 'message': 'Either rentalPlan is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)
        try:
            #order_query.instructions = str(instructions)
            #order_query.save()

            order_query.instruction=list(instructions)
            status = 'success'

            # ----------------Logging
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=True, timestamp=str(int(datetime.now().timestamp())),  vendor_code=vendor_code)

            response = json.dumps(
            {'status': status})
            return Response(response, status=201)
        
        except Exception as e:
            status = 'failure'
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())),  vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())),  vendor_code=vendor_code)

            response = json.dumps(
            {'status': status})
            return Response(response, status=400)

    def delete(self, request):
        pass

    def put(self, request):
        pass



# Request Deliveries

class RequestDeliveries(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        pass
 
    def post(self, request):
       
        vendor_code = 'testing'

        try:
             vendorCode= str(request.data.get(' vendorCode'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'vendor_code_not_found ', 'message': 'Either vendorCode is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)

        try:
            productDescription = str(request.data.get('productDescription'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'product_invalid ', 'message': 'productDescription is not from this list'})                # [EDIT]
            return Response(response, status=400)
        
        try:
            companyName = str(request.data.get('companyName'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'vendor_not_found ', 'message': 'vendorCode is invalid'})                # [EDIT]
            return Response(response, status=400)

        try:
            deliveryTimestamp = str(request.data.get('deliveryTimestamp'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'delivery_timestamp_invalid ', 'message': 'Delivery timestamp is before the current time, please check'})                # [EDIT]
            return Response(response, status=400)
        
        try:
            orderType = str(request.data.get('orderType'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'order_type_invalid  ', 'message': 'This orderType is not supported by vendor, please contact the vendor for clarification'})                # [EDIT]
            return Response(response, status=400)
        
        try:
            orderList  = list(request.data.get('orderList'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'order_list_structure_error ', 'message': 'The order object structure inside orderList is wrong '})                # [EDIT]
            return Response(response, status=400)

        try:
            rentalPlan   = str(request.data.get('rentalPlan '))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'rental_plan_invalid', 'message': 'rentalPlan is not from the list in Docs'})                # [EDIT]
            return Response(response, status=400)

        try:
            serviceList = list(request.data.get('serviceList'))
        except Exception as e:
             # ----------------Logging
            ErrorLogApi.objects.create(api_name='RequestDeliveries', error_val=e, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='RequestDeliveries', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps({'status': 400, 'error': 'service_list_format_invalid', 'message': 'serviceList is of incorrect format, please check documentation '})                # [EDIT]
            return Response(response, status=400)


        # To check, if the order (via orderId) is present in the database
        try:            
            # From the vendor_code, take out vendor charge data 
            #order_query = OrderDetails.objects.get(order_id=order_id)

            vendor_query = {
                'status': 0.0,
                'taskID': 'xyz',
                'errorMessage':'xyz',
                'tasklink':'xyz'
            }

        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())),vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())),vendor_code=vendor_code)
            
            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)

        try:
            #order_query.instructions = str(instructions)
            #order_query.save()

            vendor_query['instructions'] = 'instructions'
            status = 'success'

            # ----------------Logging
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=True, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps(
            {'status': status})
            return Response(response, status=201)
        
        except Exception as e:
            status = 'failure'
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())),vendor_code=vendor_code)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), vendor_code=vendor_code)

            response = json.dumps(
            {'status': status})
            return Response(response, status=400)

    def delete(self, request):
        pass

    def put(self, request):
        pass
