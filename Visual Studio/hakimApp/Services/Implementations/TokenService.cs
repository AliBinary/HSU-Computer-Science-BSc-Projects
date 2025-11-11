using Dapper;
using hakimApp.Data.Contracts;
using hakimApp.Data.Repositories;
using hakimApp.Entities.Dto.TokenDto;
using hakimApp.Entities.Models;
using hakimApp.Services.Contracts;
using hakimApp.WebFrameWork.Api;
using hakimApp.WebFrameWork.Helpers;

namespace hakimApp.Services.Implementations
{
    public class TokenService : ITokenService
    {
        readonly IRepository<RefreshToken> _repository;
        public TokenService(IRepository<RefreshToken> repository)
        {
            _repository = repository;
        }
        public async Task<Tuple<string, string>> GenerateTokenAsync(int userId)
        {


        var accessToken = await TokenHelper.GenerateAccessToken(userId);
            var refreshToken = await TokenHelper.GenerateRefreshToken();
            DynamicParameters parameters = new();
            parameters.Add("@Id", userId);
            var result = await _repository.ExecuteQueryAsync("dbo.usp_getUserRefreshToken", parameters, true);
            var salt = PasswordHelper.GetSecureSalt();
            var refreshTokenHashed = PasswordHelper.HashUsingPBKDF2(refreshToken, salt);
            if (result.Data != null && result.Data.Count() > 0)
            {
                await _repository.ExecuteCommandAsync("dbo.usp_deleteUserRefreshToken", parameters, operationType: WebFrameWork.Enums.Enums.OperationType.Delete);
            }
            parameters = new DynamicParameters();
            parameters.Add("@FK_User_Id", userId);
            parameters.Add("@TokenHash", refreshTokenHashed);
            parameters.Add("@TokenSalt", Convert.ToBase64String(salt));
            parameters.Add("@ExpireDate", DateTime.Now.AddDays(1));

            var addRefreshTokenResult = await _repository.ExecuteCommandAsync("dbo.usp_insertUserRefreshToken", parameters, operationType: WebFrameWork.Enums.Enums.OperationType.Insert);
            if (addRefreshTokenResult.IsSuccesed)
            {
                return new Tuple<string, string>(accessToken, refreshToken);
            }
            return null;
        }

        public async Task<ApiResult> ValidateRefreshTokenAsync(RefreshTokenDto refreshTokenDto)
        {
            DynamicParameters parameters = new();
            parameters.Add("@Id", refreshTokenDto.UserId);
            var result = await _repository.ExecuteQueryAsync("dbo.usp_getUserRefreshToken", parameters, true);
            if (result.Data == null | result.Data.Count() == 0)
            {
                result.IsSuccesed = false;
                result.Message = "کاربر معتبر نیست و یا خارج شده اید";
            }
            var refreshTokenToValidateHash = PasswordHelper.HashUsingPBKDF2(refreshTokenDto.RefreshToken, Convert.FromBase64String(result.Data.FirstOrDefault().TokenSalt));
            if (result.Data.FirstOrDefault().TokenHash != refreshTokenToValidateHash)
            {
                result.IsSuccesed = false;
                result.Message = "شناسه بروزرسانی توکن معتبر نیست";
            }
            if (result.Data.FirstOrDefault().ExpireDate < DateTime.Now)
            {
                result.IsSuccesed = false;
                result.Message = "شناسه بروزرسانی توکن منقضی شده است";
            }
            result.IsSuccesed = true;
            return result;
        }


    }
}
