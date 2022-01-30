from SME.Requests import Credentials, TransactionAuthKeyRequest, HppTxnFlowParameters


from django.shortcuts import render

# Create your views here.

# get the auth key
def payment_view(request):

    credentials = Credentials("testuser", "Passw0rd", "12345678")

    request = TransactionAuthKeyRequest(credentials)
    request.base_url = "https://eshopping.nbe.com.eg/webapi/v2"

    request.hpp_parameters = HppTxnFlowParameters()
    request.hpp_parameters.tokenise_txn_check_box_default_value = True
    request.action = "payment"
    request.amount = 200
    request.currency = "AUD"
    request.crn1 = "Ref One"
    request.redirection_url = "http://merchant.com/dvtokenreceipt"
    request.tokenisation_mode = 3
    request.amex_express_checkout = False

    response = request.submit()
    print("*" * 50)
    print(request)
    print(response)
    print("*" * 50)

    return render(request, "payment/payment.html", {})
