using Microsoft.OpenApi.Models;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace hakimApp.WebFrameWork.Helpers
{
    public class RequierdHeaderParameters : IOperationFilter
    {
        public void Apply(OpenApiOperation operation, OperationFilterContext context)
        {
            if (operation.Parameters == null)
            {
                operation.Parameters = new List<OpenApiParameter>();

            }
            operation.Parameters.Add(new OpenApiParameter
            {
                Name = "PageNumber",
                In = ParameterLocation.Header,
                Required = false,
                Schema = new OpenApiSchema
                {
                    Type = "int",
                }
            });
            operation.Parameters.Add(new OpenApiParameter
            {
                Name = "SeedNumber",
                In = ParameterLocation.Header,
                Required = false,
                Schema = new OpenApiSchema
                {
                    Type = "int",

                }
            });
            operation.Parameters.Add(new OpenApiParameter
            {
                Name = "UserId",
                In = ParameterLocation.Header,
                Required = false,
                Schema = new OpenApiSchema
                {
                    Type = "int",

                }
            });
            operation.Parameters.Add(new OpenApiParameter
            {
                Name = "Lang",
                In = ParameterLocation.Header,
                Required = false,
                Schema = new OpenApiSchema
                {
                    Type = "int",

                }
            });
            operation.Parameters.Add(new OpenApiParameter
            {
                Name = "Authorization",
                In = ParameterLocation.Header,
                Required = false,
                Schema = new OpenApiSchema
                {
                    Type = "string",

                }
            });
        }
    }
}
