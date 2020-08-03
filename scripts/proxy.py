from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    print(flow.request.pretty_url)
    if flow.request.pretty_url == "http://api.sunmi.com/api/financial/app/financial/1.1/?service=/checkauthcode":
        flow.response = http.HTTPResponse.make(
            200,  
            '{"code":1,"data":null,"msg":""}',  

            {"Content-Type": "text/html;charset=utf-8",
	     "Content-Encoding":"gzip",
	     "Server":"nginx",
	     "Transfer-Encoding":"chunked"
	    }  
        )
