from langchain_mcp_adapters.client import MultiServerMCPClient
from app.utils.path_resolver import wrap_tool
# noqa  MC8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2Um5ZeFJRPT06ZGJkYjRmMTY=

# pylint: disable  MS8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2Um5ZeFJRPT06ZGJkYjRmMTY=

def get_mcp_tools():
    import asyncio
    client = MultiServerMCPClient(
            {
                "mcp-db": {
                    "transport": "http",  # HTTP-based remote server
                    # Ensure you start your weather server on port 8000
                    "url": "http://localhost:8000/mcp",
                },
                # "mcp-db": {
                #     "transport": "stdio",
                #     "command": "python",
                #     "args": ["./app/db/server.py"],
                # },
                "mcp-server-chart": {
                    "transport": "stdio",
                    "command": "npx",
                    "args": ["-y", "@antv/mcp-server-chart"]
                },
                "llmwiki": {
                    "transport": "stdio",
                    "command": "npx",
                    "args": ["llm-wiki-compiler", "serve", "--root", "C:/Users/65132/Desktop/nl2sql/nl2sql4"],
                    "env": {
                        "LLMWIKI_PROVIDER": "openai",
                        "LLMWIKI_MODEL": "deepseek-chat",
                        "OPENAI_API_KEY": "sk-da6245f6665d4a62ae2dfc2ef12cd16e",
                        "OPENAI_BASE_URL": "https://api.deepseek.com"
                    }
                }
            },

        )
    _tools = asyncio.run(client.get_tools())
    return [wrap_tool(t) for t in _tools]
tools = get_mcp_tools()