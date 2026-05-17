"""
版权所有 (c) 2023-2026 北京慧测信息技术有限公司(但问智能) 保留所有权利。

本代码版权归北京慧测信息技术有限公司(但问智能)所有，仅用于学习交流目的，未经公司商业授权，
不得用于任何商业用途，包括但不限于商业环境部署、售卖或以任何形式进行商业获利。违者必究。

授权商业应用请联系微信：huice666
"""

import logging
from langchain_core.language_models import ModelProfile

from app.core.settings import settings
# noqa  MC8zOmFIVnBZMlhwcWF6bW5wZmx1Ymc2UWpKWWRnPT06YjlmMmI1ZjE=

# 配置日志
logger = logging.getLogger(__name__)
# pylint: disable  MS8zOmFIVnBZMlhwcWF6bW5wZmx1Ymc2UWpKWWRnPT06YjlmMmI1ZjE=

# 创建文本处理模型
def create_deepseek_model():
    """创建文本处理模型"""
    from langchain_deepseek import ChatDeepSeek
    try:
        model = ChatDeepSeek(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_BASE_URL,
            model=settings.LLM_MODEL,
            temperature=0.3,
            extra_body={"thinking": {"type": "disabled"}},
        )
        model.profile = ModelProfile(max_input_tokens=120000)
        return model
    except ImportError:
        logger.warning("langchain_deepseek not available")
        return None
    except Exception as e:
        logger.error(f"Failed to create text model: {e}")
        return None

def create_text_model():
    """创建文本处理模型"""
    from langchain_openai import ChatOpenAI
    try:
        model = ChatOpenAI(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_BASE_URL,
            model=settings.LLM_MODEL,
            temperature=0.3,
            extra_body={"thinking": {"type": "disabled"}},

        )
        model.profile = ModelProfile(max_input_tokens=120000)
        return model
    except ImportError:
        logger.warning("langchain_deepseek not available")
        return None
    except Exception as e:
        logger.error(f"Failed to create text model: {e}")
        return None

deepseek_model = create_deepseek_model()
# fmt: off  Mi8zOmFIVnBZMlhwcWF6bW5wZmx1Ymc2UWpKWWRnPT06YjlmMmI1ZjE=
