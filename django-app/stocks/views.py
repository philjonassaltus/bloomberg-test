# stocks/views.py
from django.shortcuts import render
import yfinance as yf

magnificent_seven = {
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


def company_list(request):
    return render(request, "stocks/company_list.html", {"companies": magnificent_seven})


def stock_data_view(request):
    stock_data = []

    for key, value in magnificent_seven.items():
        data = yf.download(key, start="2025-04-01", end="2025-04-10")
        # Convert to something we can use in the template
        records = (
            data[["Close", "Open"]].round(2).reset_index().to_dict(orient="records")
        )

        stock_data.append(
            {
                "name": value["name"],
                "ticker": key,
                "description": value["description"],
                "records": records,
            }
        )

    return render(request, "stocks/stock_data.html", {"stock_data": stock_data})
