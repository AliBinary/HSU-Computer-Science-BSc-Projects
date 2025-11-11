using Dapper;
using hakimApp.Data.Contracts;
using hakimApp.WebFrameWork.Api;
using HakimTest.Entites.Dto.User;
using Microsoft.AspNetCore.Mvc;

readonly IRepository<CustomerDto> _repository;
public HakimTestController(IRepository<CustomerDto> repository)
{
    _repository = repository;
}
[HttpPost("InsertUser")]
public async Task<ActionResult<ApiResult>> InsertAsync(CustomerDto entity)
{
    DynamicParameters dynamicParameters = new();
    dynamicParameters.Add("@FullName", entity.FullName);
    dynamicParameters.Add("@PasswardHash", entity.PasswardHash);
    dynamicParameters.Add("@PhoneNO", entity.PhoneNO);
    dynamicParameters.Add("@UserName", entity.UserName);
    dynamicParameters.Add("@PasswordSalt", entity.PasswordSalt);
    dynamicParameters.Add("@Email", entity.Email);
    return Ok(await _repository.ExecuteCommandAsync("UsP_InsertCustomer", dynamicParameters, WebFrameWork.Enums.Enums.OperationType.Insert, false, UserId, false, Lang));
}