#! /usr/bin/env python3
import argparse
from auth_main.funct_tools import *
from auth_main.utility import Cache, f_check, logging as log

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save a query as a csv. Please give valid SQL query to tenant.")
    parser.add_argument('-pw','--Password', type=str, required=False, help= 'Password of service account from config file.')
    parser.add_argument('-n','--Name', type=str, required=False, help= 'Name of the account to get the PW of. Format is Display name. EX:      user_name (resource_name)')
    args = parser.parse_args()
# Create the object for the file
f = f_check()
# Build cache. Need to move cond to the module
if args.Password:
    c = Cache(args.Password, **f.loaded['tenants'][0])
else:
    c = Cache(**f.loaded['tenants'][0])
# Security test (prob shove in module as well)
sec_test(**c.ten_info)
# Get PW
def get_pw(tenant, header, **ignored):
    log.info("Checking out PW in tenant: {tenant}".format(**f.loaded['tenants'][0]))
    # Account info
    log.info("Getting ID for account {Name}....".format(**args))
    acc_q = query_request("SELECT VaultAccount.ID, VaultAccount.UserDisplayName FROM VaultAccount WHERE \
        VaultAccount.UserDisplayName = '{Name}'".format(**args), tenant, header).parsed_json["Result"]['Results']
    acc = acc_q["ID"]
    log.info("Getting PW now....")
    pw = other_requests("/ServerManage/CheckoutPassword", ID=acc, tenant, header).parsed_json["Result"]
    log.info("PW is {Password}".format(**pw))
)
# Execute funtion
get_pw(**c.ten_info)