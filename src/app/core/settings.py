"""
版权所有 (c) 2023-2026 北京慧测信息技术有限公司(但问智能) 保留所有权利。

本代码版权归北京慧测信息技术有限公司(但问智能)所有，仅用于学习交流目的，未经公司商业授权，
不得用于任何商业用途，包括但不限于商业环境部署、售卖或以任何形式进行商业获利。违者必究。

授权商业应用请联系微信：huice666
"""

import os
import logging
from typing import Any, Dict, List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()
logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    # LLM配置
    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "deepseek-v4-flash")

    # 日志配置
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "agentic_rag.log")
    ENABLE_DETAILED_LOGGING: bool = os.getenv("ENABLE_DETAILED_LOGGING", "true").lower() == "true"
# fmt: off  MC80OmFIVnBZMlhwcWF6bW5wZmx1Ymc2YkdOMFRnPT06ZmJjYWMxZGI=

    class Config:
        case_sensitive = True
        env_file = ".env"

    def validate_configuration(self) -> List[str]:
        """
        验证配置的有效性

        Returns:
            配置问题列表，空列表表示配置正常
        """
        issues = []

        # 检查必需的API密钥
        if not self.LLM_API_KEY:
            issues.append("LLM_API_KEY is required for DeepSeek models")
# type: ignore  MS80OmFIVnBZMlhwcWF6bW5wZmx1Ymc2YkdOMFRnPT06ZmJjYWMxZGI=

        return issues

    def get_safe_config(self) -> Dict[str, Any]:
        """
        获取安全的配置信息（隐藏敏感信息）

        Returns:
            安全的配置字典
        """
        config = self.model_dump()

        # 隐藏敏感信息
        sensitive_keys = [
            "LLM_API_KEY", "SECRET_KEY"
        ]
# pragma: no cover  Mi80OmFIVnBZMlhwcWF6bW5wZmx1Ymc2YkdOMFRnPT06ZmJjYWMxZGI=

        for key in sensitive_keys:
            if key in config and config[key]:
                config[key] = "***" + config[key][-4:] if len(config[key]) > 4 else "***"

        return config


def create_settings() -> Settings:
    """创建并验证设置"""
    settings = Settings()

    # 验证配置
    issues = settings.validate_configuration()
    if issues:
        logger.warning("Configuration issues found:")
        for issue in issues:
            logger.warning(f"  - {issue}")

    return settings

# 该代码会自动执行，并且只会执行一次（单例设计模式）
settings = create_settings()
# pragma: no cover  My80OmFIVnBZMlhwcWF6bW5wZmx1Ymc2YkdOMFRnPT06ZmJjYWMxZGI=

