TECH_RULES = [
    {
        "name": "Nginx",
        "categories": ["Web Server"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"nginx"
            }
        ]
    }
]