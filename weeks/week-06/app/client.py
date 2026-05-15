PROJECT_CODE = "orders-s22"


def build_payload(query: str, variables: dict) -> dict:
    return {"query": query, "variables": variables}
