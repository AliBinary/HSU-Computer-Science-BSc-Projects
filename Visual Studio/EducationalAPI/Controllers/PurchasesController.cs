using System.Data;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;
using Microsoft.AspNetCore.Mvc;
using Dapper;

namespace EducationalAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PurchasesController : ControllerBase
    {
        private readonly DapperContext _context;

        public PurchasesController(DapperContext context)
        {
            _context = context;
        }

        [HttpPost("CreatePurchase")]
        public async Task<IActionResult> CreatePurchase(Purchase purchase)
        {
            using var connection = _context.CreateConnection();

            await connection.ExecuteAsync(
                "sp_CreatePurchase",
                new { purchase.UserID, purchase.CourseID, purchase.PurchaseDate, purchase.AmountPaid },
                commandType: CommandType.StoredProcedure
            );

            return Ok("Purchase created successfully");
        }
    }
}
