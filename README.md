# NL2SQL — 自然语言到 SQL 的演示与服务

一个用于将自然语言查询转换为 SQL 并在多种数据库引擎上执行的示例服务。该仓库包含模型代理、数据库引擎适配层和一个可启动的轻量服务器，用于本地调试与集成测试。

**主要功能**
- 将自然语言问题解析为 SQL 查询（NL → SQL）。
- 支持多种数据库引擎（Postgres、MySQL、SQLite、BigQuery、ClickHouse 等）。
- 可本地启动的 API 服务（参见 `start_server.py`）。

**仓库结构（简要）**
- `start_server.py`：项目启动器，用于运行本地服务。
- `db_mcp_server/`：数据库适配与执行器实现，按数据库类型组织引擎封装。
- `src/app/`：代理（agents）、技能（skills）和工具（tools）实现，用于 NL2SQL 的任务分解与推理流程。
- `pyproject.toml`：项目元数据与依赖声明。

快速上手
1. 建议使用 Python 3.10+ 创建虚拟环境并激活：

	```powershell
	python -m venv .venv
	.venv\Scripts\activate
	```

2. 安装依赖（使用 `pyproject.toml` 或已有的 requirements）：

	```powershell
	pip install -e .
	# 或者如果你有 requirements.txt：
	# pip install -r requirements.txt
	```

3. 启动本地服务：

	```powershell
	python start_server.py
	```

4. 打开浏览器或使用 curl 访问服务提供的 API（具体端点见代码中的 `server.py` 实现）。

开发与调试建议
- 在 `src/app/agents` 和 `src/app/skills` 目录中查看示例技能与系统提示模板，便于自定义 NL→SQL 的推理链。
- 数据库连接配置位于 `db_mcp_server/db/config.py`，测试时可使用 SQLite 或项目已包含的测试数据目录。

贡献
- 欢迎提交 issue 或 PR。请在 PR 中添加可复现的测试用例或示例。对文档和错误修复尤为欢迎。

许可证
- 本仓库采用开源友好许可（仓库根目录如有 LICENSE，请参考）。

联系方式
- 如果需要更详细的使用说明、样例请求或想要我为你定制 README 的某些部分，请告诉我你希望包含的文档细节（例如：示例查询、API 端点、运行截图）。

