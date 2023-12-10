import typing


class HttpStatusCodeTypes:
    # Informational responses (100-199)
    CONTINUE = "Continue"
    SWITCHING_PROTOCOLS = "Switching Protocols"
    PROCESSING = "Processing"
    # Successful responses (200-299)
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "Non-Authoritative Information"
    NO_CONTENT = "No Content"
    RESET_CONTENT = "Reset Content"
    PARTIAL_CONTENT = "Partial Content"
    MULTI_STATUS = "Multi-Status"
    ALREADY_REPORTED = "Already Reported"
    IM_USED = "IM Used"
    # Redirection messages (300-399)
    MULTIPLE_CHOICES = "Multiple Choices"
    MOVED_PERMANENTLY = "Moved Permanently"
    FOUND = "Found"
    SEE_OTHER = "See Other"
    NOT_MODIFIED = "Not Modified"
    USE_PROXY = "Use Proxy"
    UNUSED = "(Unused)"
    TEMPORARY_REDIRECT = "Temporary Redirect"
    PERMANENT_REDIRECT = "Permanent Redirect"
    # Client error responses (400-499)
    BAD_REQUEST = "Bad Request"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "Payment Required"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "Not Found"
    METHOD_NOT_ALLOWED = "Method Not Allowed"
    NOT_ACCEPTABLE = "Not Acceptable"
    PROXY_AUTHENTICATION_REQUIRED = "Proxy Authentication Required"
    REQUEST_TIMEOUT = "Request Timeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "Length Required"
    PRECONDITION_FAILED = "Precondition Failed"
    PAYLOAD_TOO_LARGE = "Payload Too Large"
    URI_TOO_LONG = "URI Too Long"
    UNSUPPORTED_MEDIA_TYPE = "Unsupported Media Type"
    RANGE_NOT_SATISFIABLE = "Range Not Satisfiable"
    EXPECTATION_FAILED = "Expectation Failed"
    IM_A_TEAPOT = "I'm a teapot"
    MISDIRECTED_REQUEST = "Misdirected Request"
    UNPROCESSABLE_ENTITY = "Unprocessable Entity"
    LOCKED = "Locked"
    FAILED_DEPENDENCY = "Failed Dependency"
    TOO_EARLY = "Too Early"
    UPGRADE_REQUIRED = "Upgrade Required"
    PRECONDITION_REQUIRED = "Precondition Required"
    TOO_MANY_REQUESTS = "Too Many Requests"
    REQUEST_HEADER_FIELDS_TOO_LARGE = "Request Header Fields Too Large"
    UNAVAILABLE_FOR_LEGAL_REASONS = "Unavailable For Legal Reasons"
    # Server error responses (500-599)
    INTERNAL_SERVER_ERROR = "Internal Server Error"
    NOT_IMPLEMENTED = "Not Implemented"
    BAD_GATEWAY = "Bad Gateway"
    SERVICE_UNAVAILABLE = "Service Unavailable"
    GATEWAY_TIMEOUT = "Gateway Timeout"
    HTTP_VERSION_NOT_SUPPORTED = "HTTP Version Not Supported"
    VARIANT_ALSO_NEGOTIATES = "Variant Also Negotiates"
    INSUFFICIENT_STORAGE = "Insufficient Storage"
    LOOP_DETECTED = "Loop Detected"
    NOT_EXTENDED = "Not Extended"
    NETWORK_AUTHENTICATION_REQUIRED = "Network Authentication Required"
    # Unknown Type
    UNKNOWN  = "Unknown"

class HttpResponseTypes:
    INFORMATIONAL = "Informational"
    SUCCESS = "Success"
    REDIRECT = "Redirect"
    CLIENTERROR = "ClientError"
    SERVERERROR = "ServerError"
    UNKNOWN = "Unknown"

    @staticmethod
    def informational()->typing.Dict[int,str]:
        return {
    100 : "Continue" ,
    101 : "Switching Protocols",
    102 : "Processing",
    103 : "Early Hints",            
}

    @staticmethod
    def success()->typing.Dict[int,str]:
        return {
            200 : "OK" ,
            201 : "Created",
            202 : "Accepted",
            203 : "Non-Authoritative Information",            
            204 : "No Content",            
            205 : "Reset Content",            
            206 : "Partial Content",            
            207 : "Multi-Status",            
            208 : "Already Reported",            
            226 : "IM Used",            
        }

    @staticmethod
    def redirect()->typing.Dict[int,str]:
        return {
            300: "Multiple Choices",
            301: "Moved Permanently",
            302: "Found",
            303: "See Other",
            304: "Not Modified",
            305: "Use Proxy",
            306: "(Unused)",
            307: "Temporary Redirect",
            308: "Permanent Redirect",
        }

    @staticmethod
    def clientError()->typing.Dict[int,str]:
        return {
            400: "Bad Request",
            401: "Unauthorized",
            402: "Payment Required",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            406: "Not Acceptable",
            407: "Proxy Authentication Required",
            408: "Request Timeout",
            409: "Conflict",
            410: "Gone",
            411: "Length Required",
            412: "Precondition Failed",
            413: "Payload Too Large",
            414: "URI Too Long",
            415: "Unsupported Media Type",
            416: "Range Not Satisfiable",
            417: "Expectation Failed",
            418: "I'm a teapot",
            421: "Misdirected Request",
            422: "Unprocessable Entity",
            423: "Locked",
            424: "Failed Dependency",
            425: "Too Early",
            426: "Upgrade Required",
            428: "Precondition Required",
            429: "Too Many Requests",
            431: "Request Header Fields Too Large",
            451: "Unavailable For Legal Reasons",
        }
    
    @staticmethod
    def serverError()->typing.Dict[int,str]:
        return {
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout",
            505: "HTTP Version Not Supported",
            506: "Variant Also Negotiates",
            507: "Insufficient Storage",
            508: "Loop Detected",
            510: "Not Extended",
            511: "Network Authentication Required",
        }
     

