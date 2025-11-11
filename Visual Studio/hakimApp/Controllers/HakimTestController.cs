using Dapper;
using hakimApp.Data.Contracts;
using hakimApp.Entities.Dto.User;
using hakimApp.Entities.Dto.PublicDtos;
using hakimApp.WebFrameWork.Api;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using hakimApp.WebFrameWork.Helpers;
using hakimApp.Services.Contracts;
using hakimApp.Entities.Dto.TokenDto;
using Microsoft.AspNetCore.Authorization;
using System.Data;

namespace hakimApp.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class HakimTestController : CustomApiController
    {
        readonly IRepository<CustomerDto> _repository;
        readonly IRepository<LonginResultDto> _loginRepository;
        readonly ITokenService _tokenService;
        public HakimTestController(IRepository<CustomerDto> repository, IRepository<LonginResultDto> loginRepository, ITokenService tokenService)
        {
            _repository = repository;
            _loginRepository = loginRepository;
            _tokenService = tokenService;
        }

        [HttpPost("InsertUser")]
        public async Task<ActionResult<ApiResult>> InsertAsync(CustomerDto entity)
        {
            var salt = PasswordHelper.GetSecureSalt();
            var passwordHash = PasswordHelper.HashUsingPBKDF2(entity.Password, salt);
            DynamicParameters dynamicParameters = new();

            dynamicParameters.Add("@FullName", entity.FullName);
            dynamicParameters.Add("@LoginHash", passwordHash);
            dynamicParameters.Add("@ContactNumber", entity.ContactNumber);
            dynamicParameters.Add("@EmployeeCode", entity.EmployeeCode);
            dynamicParameters.Add("@SecurityCode", Convert.ToBase64String(salt));
            dynamicParameters.Add("@WorkEmail", entity.WorkEmail);
            dynamicParameters.Add("@ResidentialAddress", entity.ResidentialAddress);
            dynamicParameters.Add("@NationalID", entity.NationalID);

            return Ok(await _repository.ExecuteCommandAsync("USP_InsertCustomer", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Insert, false, UserId, false, Lang));
        }

        [HttpPut("UpdateUser")]
        [Authorize]
        public async Task<ActionResult<ApiResult>> UpdateAsync(UpdateCustomerDto entity)
        {
            var salt = PasswordHelper.GetSecureSalt();
            var passwordHash = PasswordHelper.HashUsingPBKDF2(entity.Password, salt);
            DynamicParameters dynamicParameters = new();


            dynamicParameters.Add("@Id", entity.Id);

            dynamicParameters.Add("@FullName", entity.FullName);
            dynamicParameters.Add("@LoginHash", passwordHash);
            dynamicParameters.Add("@ContactNumber", entity.ContactNumber);
            dynamicParameters.Add("@EmployeeCode", entity.EmployeeCode);
            dynamicParameters.Add("@SecurityCode", Convert.ToBase64String(salt));
            dynamicParameters.Add("@WorkEmail", entity.WorkEmail);
            dynamicParameters.Add("@ResidentialAddress", entity.ResidentialAddress);
            dynamicParameters.Add("@NationalID", entity.NationalID);

            return Ok(await _repository.ExecuteCommandAsync("USP_UpdateCustomer", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Update));
        }

        [HttpDelete("DeleteUser")]
        [Authorize]
        public async Task<ActionResult<ApiResult>> DeleteAsync(PublicIdDto<int> entity)
        {
            DynamicParameters dynamicParameters = new();
            dynamicParameters.Add("@Id", entity.Id);
            dynamicParameters.Add("@rCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
            dynamicParameters.Add("@rMsg", dbType: DbType.String, size: 4000, direction: ParameterDirection.Output);

            try
            {
                // مرحله اول: حذف توکن‌های کاربر از جدول TB_RefreshToken
                await _repository.ExecuteCommandAsync("USP_DeleteUserRefreshToken", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Delete);

                int resultCode = dynamicParameters.Get<int>("@rCode");
                string resultMessage = dynamicParameters.Get<string>("@rMsg");

                if (resultCode != 1)
                {
                    // اگر در مرحله اول حذف توکن‌ها مشکلی وجود داشت، برمی‌گردیم
                    return BadRequest(new ApiResult { Success = false, Message = resultMessage });
                }

                // مرحله دوم: حذف اطلاعات کاربر از جدول TB_Customer
                dynamicParameters = new DynamicParameters();
                dynamicParameters.Add("@Id", entity.Id);
                dynamicParameters.Add("@rCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
                dynamicParameters.Add("@rMsg", dbType: DbType.String, size: 4000, direction: ParameterDirection.Output);

                await _repository.ExecuteCommandAsync("USP_DeleteCustomer", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Delete);

                resultCode = dynamicParameters.Get<int>("@rCode");
                resultMessage = dynamicParameters.Get<string>("@rMsg");

                if (resultCode == 1)
                {
                    return Ok(new ApiResult { Success = true, Message = resultMessage });
                }

                return BadRequest(new ApiResult { Success = false, Message = resultMessage });
            }
            catch (Exception ex)
            {
                return BadRequest(new ApiResult { Success = false, Message = "خطای داخلی سرور: " + ex.Message });
            }
        }

        [HttpPost("getuserlist")]
        [Authorize]
        public async Task<ActionResult<QueryResult<SelectUserDto>>> GetAsync([FromBody] GetUserDto entity)
        {
            DynamicParameters dynamicParameters = new();
            dynamicParameters.Add("@ContactNumber", entity.ContactNumber);
            dynamicParameters.Add("@FullName", entity.FullName);
            dynamicParameters.Add("@EmployeeCode", entity.EmployeeCode);

            return Ok(await _repository.ExecuteQueryAsync("[dbo].[USP_GetUserList]", dynamicParameters, false, PageNumber, SeedNumber, false, UserId));
        }

        [HttpPost("Login")]
        public async Task<ActionResult<ApiResult>> Login(LoginDto loginDto)
        {
            DynamicParameters dynamicParameters = new DynamicParameters();
            dynamicParameters.Add("@EmployeeCode", loginDto.EmployeeCode);
            var user = await _loginRepository.ExecuteQueryAsync("[dbo].[USP_LoginUser]", dynamicParameters, true);
            if (user == null | user.Data.Count() == 0)
            {
                return Unauthorized();
            }
            var passwordHash = PasswordHelper.HashUsingPBKDF2(loginDto.Password, Convert.FromBase64String(user.Data.FirstOrDefault().SecurityCode));
            if (user.Data.FirstOrDefault().LoginHash == passwordHash)
            {
                var token = await Task.Run(() => _tokenService.GenerateTokenAsync(user.Data.FirstOrDefault().Id));

                if (token != null)
                {
                    QueryResult<TokenResponseDto> result = new();
                    var list = new List<TokenResponseDto>();
                    list.Add(new TokenResponseDto
                    {
                        UserId = user.Data.FirstOrDefault().Id,
                        AccessToken = token.Item1,
                        RefreshToken = token.Item2,
                        FullName = user.Data.FirstOrDefault().FullName,
                        PhoneNo = user.Data.FirstOrDefault().ContactNumber
                    });
                    result.Data = list;
                    result.IsSuccesed = true;
                    return Ok(result);
                }
                else
                {
                    return Unauthorized();
                }
            }
            return Unauthorized();

        }

        [HttpPost("InsertProduct")]
        public async Task<ActionResult<ApiResult>> InsertProductAsync(ProductDto product)
        {
            DynamicParameters dynamicParameters = new();

            dynamicParameters.Add("@GoodsName", product.GoodsName);
            dynamicParameters.Add("@Unit", product.Unit);
            dynamicParameters.Add("@Id", dbType: DbType.Int32, direction: ParameterDirection.Output);
            dynamicParameters.Add("@rCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
            dynamicParameters.Add("@rMsg", dbType: DbType.String, size: 4000, direction: ParameterDirection.Output);

            try
            {
                await _repository.ExecuteCommandAsync("[dbo].[USP_InsertProduct]", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Insert);

                int resultCode = dynamicParameters.Get<int>("@rCode");
                string resultMessage = dynamicParameters.Get<string>("@rMsg");

                if (resultCode == 1)
                {
                    return Ok(new ApiResult { Success = true, Message = resultMessage });
                }
                return BadRequest(new ApiResult { Success = false, Message = resultMessage });
            }
            catch (Exception ex)
            {
                return BadRequest(new ApiResult { Success = false, Message = "خطای داخلی سرور: " + ex.Message });
            }
        }


        [HttpDelete("DeleteProduct")]
        public async Task<ActionResult<ApiResult>> DeleteProductAsync(PublicIdDto<int> entity)
        {
            DynamicParameters dynamicParameters = new();
            dynamicParameters.Add("@Id", entity.Id);
            dynamicParameters.Add("@rCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
            dynamicParameters.Add("@rMsg", dbType: DbType.String, size: 4000, direction: ParameterDirection.Output);

            try
            {
                // فراخوانی Stored Procedure
                await _repository.ExecuteCommandAsync("USP_DeleteProduct", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Delete);

                // دریافت کد و پیام نتیجه
                int resultCode = dynamicParameters.Get<int>("@rCode");
                string resultMessage = dynamicParameters.Get<string>("@rMsg");

                if (resultCode == 1)
                {
                    return Ok(new ApiResult { Success = true, Message = resultMessage });
                }
                return BadRequest(new ApiResult { Success = false, Message = resultMessage });
            }
            catch (Exception ex)
            {
                return BadRequest(new ApiResult { Success = false, Message = "خطای داخلی سرور: " + ex.Message });
            }
        }

        [HttpPost("InsertOrder")]
        public async Task<ActionResult<ApiResult>> InsertOrderAsync(OrderDto entity)
        {
            DynamicParameters dynamicParameters = new();

            dynamicParameters.Add("@FK_TB_Employee_Id", entity.EmployeeId);
            dynamicParameters.Add("@FK_TB_Goods_Id", entity.GoodsId);
            dynamicParameters.Add("@Amount", entity.Amount);
            dynamicParameters.Add("@Price", entity.Price);

            return Ok(await _repository.ExecuteCommandAsync("USP_InsertOrder", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Insert, false, UserId, false, Lang));
        }


    }
}
