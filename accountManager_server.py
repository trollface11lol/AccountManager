import logging
from concurrent import futures
import time

import grpc
import accountsmanager_v1_pb2_grpc
import accountsmanager_v1_pb2


import datetime


def lines():
    with open('bd.txt') as f:
        n = 0
        for line in f:
            n += 1
        return n


class AccountsManagerServicer(accountsmanager_v1_pb2_grpc.AccountsManagerServicer):
    def GetAccounts(self, request, context):
        counts = lines()
        reply = accountsmanager_v1_pb2.GetAccountsResponse()
        reply.count.text = counts
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    accountsmanager_v1_pb2_grpc.add_AccountsManagerServicer_to_server(AccountsManagerServicer(), server)
    server.add_insecure_port("localhost:50011")
    server.start()
    print(str(datetime.datetime.now()) + "server started on 50011")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
