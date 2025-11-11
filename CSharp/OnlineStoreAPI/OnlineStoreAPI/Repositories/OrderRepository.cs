using Dapper;
using System.Collections.Generic;
using System.Data;
using System.Threading.Tasks;
using OnlineStoreAPI.Models;
using Microsoft.Data.SqlClient;

namespace OnlineStoreAPI.Repositories
{
    public class OrderRepository
    {
        private readonly SqlConnection _connection;

        public OrderRepository(SqlConnection connection)
        {
            _connection = connection;
        }

        public async Task<IEnumerable<Order>> GetAllOrdersAsync()
        {
            var query = "SELECT * FROM Orders";
            return await _connection.QueryAsync<Order>(query);
        }

        public async Task<Order> GetOrderByIdAsync(int id)
        {
            var query = "SELECT * FROM Orders WHERE OrderId = @Id";
            return await _connection.QuerySingleOrDefaultAsync<Order>(query, new { Id = id });
        }

        public async Task CreateOrderAsync(Order order)
        {
            var query = "INSERT INTO Orders (CustomerId, OrderDate) VALUES (@CustomerId, @OrderDate)";
            await _connection.ExecuteAsync(query, order);
        }

        public async Task UpdateOrderAsync(Order order)
        {
            var query = "UPDATE Orders SET CustomerId = @CustomerId, OrderDate = @OrderDate WHERE OrderId = @OrderId";
            await _connection.ExecuteAsync(query, order);
        }

        public async Task DeleteOrderAsync(int id)
        {
            var query = "DELETE FROM Orders WHERE OrderId = @Id";
            await _connection.ExecuteAsync(query, new { Id = id });
        }
    }
}
