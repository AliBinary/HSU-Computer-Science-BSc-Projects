using hakimApp.Entities.Dto.TokenDto;
using hakimApp.WebFrameWork.Api;

namespace hakimApp.Services.Contracts
{
    public interface ITokenService
    {
        Task<Tuple<string, string>> GenerateTokenAsync(int userId);
        Task<ApiResult> ValidateRefreshTokenAsync(RefreshTokenDto refreshToken);
    }
}
