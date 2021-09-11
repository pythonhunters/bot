import azure.functions as func

def main(request: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(f"Hello, {request.route_params.get('token')}!")
    