using System.Text;

namespace EducationalAPI.Utilities
{
    public static class QueryHelper
    {
        public static string BuildSelectQuery(string tableName, string[] columns, string? whereClause = null)
        {
            var query = new StringBuilder($"SELECT {string.Join(", ", columns)} FROM {tableName}");
            if (!string.IsNullOrWhiteSpace(whereClause))
            {
                query.Append($" WHERE {whereClause}");
            }
            return query.ToString();
        }

        public static string BuildInsertQuery(string tableName, string[] columns)
        {
            var columnNames = string.Join(", ", columns);
            var parameterNames = string.Join(", ", columns.Select(c => $"@{c}"));
            return $"INSERT INTO {tableName} ({columnNames}) VALUES ({parameterNames}); SELECT SCOPE_IDENTITY();";
        }

        public static string BuildUpdateQuery(string tableName, string[] columns, string whereClause)
        {
            var setClause = string.Join(", ", columns.Select(c => $"{c} = @{c}"));
            return $"UPDATE {tableName} SET {setClause} WHERE {whereClause}";
        }

        public static string BuildDeleteQuery(string tableName, string whereClause)
        {
            return $"DELETE FROM {tableName} WHERE {whereClause}";
        }
    }
}
