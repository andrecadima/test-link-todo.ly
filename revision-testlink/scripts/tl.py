"""Cliente mínimo XML-RPC de TestLink. La clave se lee de TESTLINK_DEVKEY y nunca se imprime."""
import os
import sys
import xmlrpc.client

URL = "http://68.211.149.112/lib/api/xmlrpc/v1/xmlrpc.php"
PROJECT_NAME = "Todo.ly"


def devkey():
    k = os.environ.get("TESTLINK_DEVKEY")
    if not k:
        sys.exit("Falta la variable de entorno TESTLINK_DEVKEY")
    return k


def proxy():
    return xmlrpc.client.ServerProxy(URL, allow_none=True)


def call(method, **args):
    args["devKey"] = devkey()
    p = proxy()
    fn = p
    for part in method.split("."):
        fn = getattr(fn, part)
    return fn(args)
