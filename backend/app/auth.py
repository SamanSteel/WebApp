from ldap3 import Server, Connection, ALL
from fastapi import HTTPException

LDAP_SERVER = "192.168.20.11"
DOMAIN = "RAFA-GROUP.com"


def authenticate(user: str, password: str):
    server = Server(LDAP_SERVER, get_info=ALL)
    user_dn = f"{user}@{DOMAIN}"  # Make sure this format is correct

    conn = Connection(server, user=user_dn, password=password, auto_bind=True)
    if not conn.bound:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print(conn.user)
    return True


if __name__ == "__main__":
    try:
        if authenticate("A.Varasteh", "Ali@20002000"):
            print("SUCCESS")
    except HTTPException as e:
        print(f"Authentication failed: {e.detail}")
