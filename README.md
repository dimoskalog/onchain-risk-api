# OnChain Risk API

A lightweight REST API for analyzing Ethereum wallet activity and generating rule-based risk scores.

Built with Python, FastAPI, and Web3.py.

## Features

- Connects to the Ethereum blockchain through a public RPC endpoint
- Retrieves the latest Ethereum block number
- Validates Ethereum wallet addresses
- Retrieves wallet ETH balances
- Retrieves wallet transaction counts
- Generates a simple rule-based activity risk assessment
- Returns a numerical risk score and risk level
- Includes automated API tests
- Interactive API documentation through Swagger UI

## Tech Stack

- Python
- FastAPI
- Web3.py
- pytest
- Uvicorn

## API Endpoints

### Health Check

```http
GET /health
```

Checks whether the API is running and connected to Ethereum.

Example response:

```json
{
  "status": "healthy",
  "ethereum_connected": true
}
```

### Latest Block

```http
GET /block
```

Returns the latest Ethereum block number.

Example response:

```json
{
  "latest_block": 12345678
}
```

### Wallet Risk Analysis

```http
GET /wallet/{address}
```

Analyzes an Ethereum wallet using its balance and transaction activity.

Example response:

```json
{
  "address": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
  "balance_eth": 5.67,
  "transaction_count": 5967,
  "activity_risk": "low",
  "risk_score": 0,
  "risk_level": "low"
}
```

## Risk Scoring

The current risk model uses wallet transaction activity:

- 0 transactions: +40 risk points
- 1–9 transactions: +20 risk points
- 10+ transactions: +0 risk points

Risk levels:

- 0–29: Low
- 30–59: Medium
- 60+: High

The scoring model is intentionally simple and designed to be extended with additional on-chain indicators.

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload --port 8001
```

The API will be available locally at:

`http://127.0.0.1:8001`

Interactive Swagger documentation:

`http://127.0.0.1:8001/docs`

## Running Tests

```bash
python -m pytest
```

## Future Improvements

Potential extensions include:

- Wallet age analysis
- Token transfer activity
- Smart-contract interaction analysis
- Suspicious transaction-pattern detection
- Configurable risk rules
- Additional automated tests
- Containerized deployment

## Disclaimer

The risk score is a rule-based demonstration for educational and portfolio purposes. It should not be interpreted as financial, compliance, or fraud-detection advice.