using Dapper;
using hakimApp.Data.Contracts;
using hakimApp.Data.DbContext;
using hakimApp.WebFrameWork.Api;
using hakimApp.WebFrameWork.Enums;

namespace hakimApp.Data.Repositories
{
    public class Repository<T> : IRepository<T>
    {
        public readonly DapperContext _context;
        public Repository(DapperContext context)
        {
            _context = context;
        }
        public async Task<ApiResult> ExecuteCommandAsync(string query, DynamicParameters parameters, Enums.OperationType operationType, bool injectUserId = false, int userId = 0, bool injectLang = false, int lang = 0)
        {
            if (parameters == null) parameters = new DynamicParameters();
            if (operationType == Enums.OperationType.Insert)
            {
                parameters.Add("@Id", 0, dbType: System.Data.DbType.Int32, direction: System.Data.ParameterDirection.Output);
            }
            if (injectUserId)
            {
                parameters.Add("@FK_User_Id", userId);
            }
            if (injectLang)
            {
                parameters.Add("@Lang", lang);//lang=0 for persian and lang=1 for English
            }
            parameters.Add("@rCode", 0, dbType: System.Data.DbType.Int32, direction: System.Data.ParameterDirection.Output);
            parameters.Add("@rMsg", string.Empty, dbType: System.Data.DbType.String, direction: System.Data.ParameterDirection.Output);
            using (var repo = _context.CreateConnection())
            {
                await repo.ExecuteAsync(query, parameters, commandType: System.Data.CommandType.StoredProcedure);
                var rCode = parameters.Get<int>("@rCode") == 0 ? false : true;
                return new ApiResult
                {
                    IsSuccesed = rCode,
                    Message = parameters.Get<string>("@rMsg"),
                    IdentityKey = operationType == Enums.OperationType.Insert && rCode ? parameters.Get<int>("@Id") : 0
                };
            }
        }

        public async Task<QueryResult<T>> ExecuteQueryAsync(string query, DynamicParameters parameters, bool skipPageInation = false, int pageNo = 0, int seedNo = 10, bool injectUserId = false, int userId = 0, bool injectLang = false, int lang = 0)
        {
            if (parameters == null) parameters = new DynamicParameters();
            if (!skipPageInation)
            {

                parameters.Add("@TotalCount", 0, dbType: System.Data.DbType.Int32, direction: System.Data.ParameterDirection.Output);
                parameters.Add("@PageNo", pageNo, dbType: System.Data.DbType.Int32);
                parameters.Add("@SeedNo", seedNo, dbType: System.Data.DbType.Int32);
            }
            if (injectUserId)
            {
                parameters.Add("@FK_User_Id", userId);
            }
            if (injectLang)
            {
                parameters.Add("@Lang", lang);//lang=0 for persian and lang=1 for English
            }
            using (var repo = _context.CreateConnection())
            {
                var result = await repo.QueryAsync<T>(query, parameters, commandType: System.Data.CommandType.StoredProcedure);
                return new QueryResult<T>
                {
                    Data = result,
                    TotalCount = !skipPageInation ? parameters.Get<int>("@TotalCount") : result.Count()
                };
            }
        }

        public DapperContext GetContext()
        {
            return _context;
        }
    }
}
