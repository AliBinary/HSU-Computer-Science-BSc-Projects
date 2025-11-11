using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace hakimApp.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
   // [ApiResultFilter]
    [EnableCors("AllowOrigin")]
    public class CustomApiController : ControllerBase
    {
        public int PageNumber
        {
            get
            {
                try
                {

                    return int.Parse( Request.Headers.FirstOrDefault(c => c.Key.Trim().ToLower().Equals("pagenumber")).Value.FirstOrDefault());
                }
                catch
                {
                    return 0;
                }
            }
        }
        public int SeedNumber
        {
            get
            {
                try
                {
                    return int.Parse(Request.Headers.FirstOrDefault(c => c.Key.Trim().ToLower().Equals("seednumber")).Value.FirstOrDefault());
                }
                catch
                {
                    return 0;
                }
            }
        }
        public string Authorization
        {
            get
            {
                try
                {
                    return Request.Headers.FirstOrDefault(c => c.Key.Trim().ToLower().Equals("authorization")).Value.FirstOrDefault();
                }
                catch
                {
                    return string.Empty;
                }
            }
        }
        public int UserId
        {
            get
            {
                try
                {
                    return int.Parse(Request.Headers.FirstOrDefault(c => c.Key.Trim().ToLower().Equals("userid")).Value.FirstOrDefault());
                }
                catch
                {
                    return 0;
                }
            }
        }
        public int Lang
        {
            get
            {
                try
                {
                    return int.Parse(Request.Headers.FirstOrDefault(c => c.Key.Trim().ToLower().Equals("lang")).Value.FirstOrDefault());
                }
                catch
                {
                    return 0;
                }
            }
        }
    }
}
