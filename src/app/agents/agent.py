"""
智能对话Agent系统
"""
from pathlib import Path
from deepagents import create_deep_agent as create_agent
from deepagents.backends import FilesystemBackend, LocalShellBackend, CompositeBackend
from deepagents.middleware import SkillsMiddleware
# pragma: no cover  MC8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2TUdkTlVRPT06NzU3ODdiNzc=

from app.core.llms import deepseek_model
from app.tools.mcp import tools

base_dir = Path(r"C:\Users\65132\Desktop\workspace\nl2sql\src\app").resolve()

# 从文件加载系统提示词，与 memory 参考手册分离以优化上下文窗口
_SYSTEM_PROMPT_PATH = Path(__file__).parent / "SYSTEM_PROMPT.md"
SYSTEM_PROMPT = _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")

file_backend = FilesystemBackend(root_dir=base_dir, virtual_mode=True)
shell_backend = LocalShellBackend(
    root_dir=base_dir / "workspace",
    inherit_env=True,
    virtual_mode=True,
    env={"PATH": r"C:\Program Files\nodejs;C:\Users\65132\AppData\Roaming\npm;C:\Windows\System32;C:\Windows;C:\Users\65132\Desktop\workspace\harness-agent-system\.venv\Scripts;C:\Users\65132\AppData\Local\Programs\Python\Python313\Scripts"}
)
skills_middleware = SkillsMiddleware(backend=file_backend, sources=["/skills/"])
# pylint: disable  MS8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2TUdkTlVRPT06NzU3ODdiNzc=

composite_backend = CompositeBackend(
    default=shell_backend,
    routes={
        "/": file_backend,
    },
)
agent = create_agent(
    model=deepseek_model,
    tools=tools,
    memory=["/memories/AGENTS.md"],
    middleware=[
        skills_middleware,
    ],
    # skills=["/skills/"],
    backend=composite_backend,
    system_prompt=SYSTEM_PROMPT,
)
