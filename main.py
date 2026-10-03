from fastapi import FastAPI, HTTPException
from web3 import Web3

app = FastAPI(
    title="OnChain Risk API",
    description="A lightweight API for analyzing Ethereum wallet activity and generating rule-based risk scores.",
    version="1.0.0"
)

w3 = Web3(Web3.HTTPProvider("https://ethereum-rpc.publicnode.com"))

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "ethereum_connected": w3.is_connected()
    }

@app.get("/block")
def get_latest_block():
    return {
        "latest_block": w3.eth.block_number
    }

@app.get("/wallet/{address}")
def get_wallet(address: str):
    if not Web3.is_address(address):
        raise HTTPException(
            status_code=400,
            detail="Invalid Ethereum address"
        )
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")
    transaction_count = w3.eth.get_transaction_count(address)

    if transaction_count == 0:
        activity_risk = "high"
    elif transaction_count < 10:
        activity_risk = "medium"
    else:
        activity_risk = "low"

    risk_score = 0

    if transaction_count == 0:
        risk_score += 40
    elif transaction_count < 10:
        risk_score += 20

    if balance_eth == 0:
        risk_score += 30
    elif balance_eth < 0.01:
        risk_score += 10

    if risk_score >= 60:
        risk_level = "high"
    elif risk_score >= 30:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "address": address,
        "balance_eth": float(balance_eth),
        "transaction_count": transaction_count,
        "activity_risk": activity_risk,
        "risk_score": risk_score,
        "risk_level": risk_level
    }
