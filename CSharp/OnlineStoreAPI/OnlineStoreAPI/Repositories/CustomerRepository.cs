using Dapper;
using System.Collections.Generic;
using System.Data;
using System.Threading.Tasks;
using OnlineStoreAPI.Models;
using Microsoft.Data.SqlClient;

namespace OnlineStoreAPI.Repositories
{
    public class CustomerRepository
    {
        private readonly SqlConnection _connection;

        public CustomerRepository(SqlConnection connection)
        {
            _connection = connection;
        }

        public async Task<IEnumerable<Customer>> GetAllCustomersAsync()
        {
            var query = "SELECT * FROM Customers";
            return await _connection.QueryAsync<Customer>(query);
        }

        public async Task<Customer> GetCustomerByIdAsync(int id)
        {
            var query = "SELECT * FROM Customers WHERE CustomerId = @Id";
            return await _connection.QuerySingleOrDefaultAsync<Customer>(query, new { Id = id });
        }

        public async Task CreateCustomerAsync(Customer customer)
        {
            var query = "INSERT INTO Customers (Name, Email) VALUES (@Name, @Email)";
            await _connection.ExecuteAsync(query, customer);
        }

        public async Task UpdateCustomerAsync(Customer customer)
        {
            var query = "UPDATE Customers SET Name = @Name, Email = @Email WHERE CustomerId = @CustomerId";
            await _connection.ExecuteAsync(query, customer);
        }

        public async Task DeleteCustomerAsync(int id)
        {
            var query = "DELETE FROM Customers WHERE CustomerId = @Id";
            await _connection.ExecuteAsync(query, new { Id = id });
        }
    }
}
