using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using System.Collections.Generic;
using OnlineStoreAPI.Models; // جایگزین با فضای اسمی پروژه شما
using OnlineStoreAPI.Repositories; // جایگزین با فضای اسمی پروژه شما

namespace OnlineStoreAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CustomerController : ControllerBase
    {
        private readonly CustomerRepository _customerRepository;

        public CustomerController(CustomerRepository customerRepository)
        {
            _customerRepository = customerRepository;
        }

        // GET: api/Customer
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Customer>>> GetCustomers()
        {
            var customers = await _customerRepository.GetAllCustomersAsync();
            return Ok(customers);
        }

        // GET: api/Customer/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Customer>> GetCustomer(int id)
        {
            var customer = await _customerRepository.GetCustomerByIdAsync(id);
            if (customer == null)
            {
                return NotFound();
            }
            return Ok(customer);
        }

        // POST: api/Customer
        [HttpPost]
        public async Task<ActionResult> CreateCustomer(Customer customer)
        {
            await _customerRepository.CreateCustomerAsync(customer);
            return CreatedAtAction(nameof(GetCustomer), new { id = customer.CustomerId }, customer);
        }

        // PUT: api/Customer/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateCustomer(int id, Customer customer)
        {
            if (id != customer.CustomerId)
            {
                return BadRequest();
            }
            await _customerRepository.UpdateCustomerAsync(customer);
            return NoContent();
        }

        // DELETE: api/Customer/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCustomer(int id)
        {
            await _customerRepository.DeleteCustomerAsync(id);
            return NoContent();
        }
    }
}
