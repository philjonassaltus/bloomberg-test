import yfinance as yf

companies = {
    "AAPL": {
        "ticker": "AAPL",
        "name": "Apple",
        "description": "A global technology company known for its consumer electronics, software, and services.",
    },
    "MSFT": {
        "ticker": "MSFT",
        "name": "Microsoft",
        "description": "A multinational technology company that develops and licenses software, hardware, and services.",
    },
    "AMZN": {
        "ticker": "AMZN",
        "name": "Amazon",
        "description": "A multinational technology company that focuses on e-commerce, digital streaming, and cloud computing.",
    },
    "GOOGL": {
        "ticker": "GOOGL",
        "name": "Alphabet",
        "description": "The parent company of Google, known for its search engine, advertising platform, and other services.",
    },
    "META": {
        "ticker": "META",
        "name": "Meta Platforms",
        "description": "The parent company of Facebook, Instagram, and WhatsApp, a social media giant.",
    },
    "NVDA": {
        "ticker": "NVDA",
        "name": "Nvidia",
        "description": "A multinational technology company that designs and manufactures graphics processing units (GPUs).",
    },
    "TSLA": {
        "ticker": "TSLA",
        "name": "Tesla",
        "description": "A multinational electric vehicle and clean energy company.",
    },
}

if __name__ == "__main__":
    for key, value in companies.items():
        print(value["name"])
        data = yf.download(key, start="2025-04-01", end="2025-04-10")
        print(data[["Close", "Open"]])
