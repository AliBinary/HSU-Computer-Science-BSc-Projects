using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using System.Collections.Generic;
using OnlineStoreAPI.Models; // فضای اسمی را با فضای اسمی پروژه‌ی خود جایگزین کنید
using OnlineStoreAPI.Repositories; // فضای اسمی را با فضای اسمی پروژه‌ی خود جایگزین کنید

namespace OnlineStoreAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class OrderController : ControllerBase
    {
        private readonly OrderRepository _orderRepository;

        public OrderController(OrderRepository orderRepository)
        {
            _orderRepository = orderRepository;
        }

        // GET: api/Order
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Order>>> GetOrders()
        {
            var orders = await _orderRepository.GetAllOrdersAsync();
            return Ok(orders);
        }

        // GET: api/Order/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Order>> GetOrder(int id)
        {
            var order = await _orderRepository.GetOrderByIdAsync(id);
            if (order == null)
            {
                return NotFound();
            }
            return Ok(order);
        }

        // POST: api/Order
        [HttpPost]
        public async Task<ActionResult> CreateOrder(Order order)
        {
            await _orderRepository.CreateOrderAsync(order);
            return CreatedAtAction(nameof(GetOrder), new { id = order.OrderId }, order);
        }

        // PUT: api/Order/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateOrder(int id, Order order)
        {
            if (id != order.OrderId)
            {
                return BadRequest();
            }
            await _orderRepository.UpdateOrderAsync(order);
            return NoContent();
        }

        // DELETE: api/Order/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteOrder(int id)
        {
            await _orderRepository.DeleteOrderAsync(id);
            return NoContent();
        }
    }
}
