using hakimApp.Entities.Dto.User;

namespace hakimApp.WebFrameWork.Api
{
    public class QueryResult<T> : ApiResult
    {
        public IEnumerable<T> Data { get; set; }
        public int TotalCount { get; set; }

        internal object Select(Func<object, SelectProductDto> value)
        {
            throw new NotImplementedException();
        }
    }
}