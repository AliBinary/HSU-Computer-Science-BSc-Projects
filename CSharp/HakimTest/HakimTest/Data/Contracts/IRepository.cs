using Dapper;
using hakimApp.WebFrameWork.Api;
using Microsoft.AspNetCore.Http;
using Microsoft.OpenApi.Models;

namespace hakimApp.Data.Contracts
{
    public interface IRepository<T>
    {
        Task<ApiResult> ExecuteCommandAsync(string query, DynamicParameters parameters, WebFrameWork.Enums.Enums.OperationType operationType, bool injectUserId = false, int userId = 0, bool injectLang = false, int lang = 0);
    }
}