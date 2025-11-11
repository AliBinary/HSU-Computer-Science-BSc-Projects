using System.Data;
using System.Data.SqlClient;


namespace hakimApp.Data.DbContext
{
    public class DapperContext
    {
        public readonly string _connectionString;
        public DapperContext(IConfiguration configuration)
        {

            var constring = configuration.GetConnectionString("SqlConnection");
            _connectionString = constring;
        }
        public IDbConnection CreateConnection()
        {
            return new SqlConnection(_connectionString);
        }
    }
}
