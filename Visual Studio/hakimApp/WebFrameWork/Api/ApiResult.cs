using System.Net;
using System.Text.Json;

namespace hakimApp.WebFrameWork.Api
{
    public class ApiResult
    {
        public ApiResult()
        {

        }
        public ApiResult(bool isSuccess, HttpStatusCode httpStatusCode, string message)
        {
            IsSuccesed = isSuccess;
            StatusCode = (int)httpStatusCode;
            Message = message;
        }
        public bool IsSuccesed { get; set; } = true;
        public int StatusCode { get; set; } = (int)HttpStatusCode.OK;
        public string Message { get; set; } = "";
        public int IdentityKey { get; set; }
        public bool Success { get; internal set; }

        public override string ToString()
        {
            return JsonSerializer.Serialize(this);

        }
    }
}