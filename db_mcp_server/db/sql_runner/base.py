"""
SQL runner capability interface.

This module contains the abstract base class for SQL execution.
"""

from abc import ABC, abstractmethod
# fmt: off  MC8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2ZUhGNlVnPT06NDIwNjc4NGU=

import pandas as pd

from db.sql_runner.models import RunSqlToolArgs, ToolContext
# pylint: disable  MS8yOmFIVnBZMlhwcWF6bW5wZmx1Ymc2ZUhGNlVnPT06NDIwNjc4NGU=

class SqlRunner(ABC):
    """Interface for SQL execution with different implementations."""

    @abstractmethod
    async def run_sql(
        self, args: RunSqlToolArgs, context: "ToolContext"
    ) -> pd.DataFrame:
        """Execute SQL query and return results as a DataFrame.

        Args:
            args: SQL query arguments
            context: Tool execution context

        Returns:
            DataFrame with query results

        Raises:
            Exception: If query execution fails
        """
        pass
