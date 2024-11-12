using Microsoft.EntityFrameworkCore;

public class OrderService : IOrderService
{

    private readonly DataContext _context;

    public OrderService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Order>> GetOrders()
    {
        return await _context.Orders.ToListAsync();
    }

    public async Task<Order?> GetOrder(string OrderId)
    {
        return await _context.Orders.FindAsync(OrderId);
    }

    public async Task<IEnumerable<ItemInfo>?> GetOrderItems(string OrderId)
    {
        Order? order = await _context.Orders.FindAsync(OrderId);
        if(order == null){
            return null;
        }
        return order.Items;
    }

    public async Task AddOrder(Order order)
    {
        order.CreatedAt = DateTime.Now;
        order.UpdatedAt = DateTime.Now;
        await _context.Orders.AddAsync(order);
        await _context.SaveChangesAsync();
    }

    public async Task EditOrder(string OrderId, Order order)
    {
        order.UpdatedAt = DateTime.Now;
        _context.Orders.Update(order);
        await _context.SaveChangesAsync();
    }

    public async Task EditOrderItems(string OrderId, IEnumerable<Inventory> OrderItems)
    {
        var order = await _context.Orders.FindAsync(OrderId);
        if (order == null)
        {
            return;
        }

        List<ItemInfo> currentItems = order.Items.ToList();

        /* Loop through currentItems and check if they are in OrderItems
        If not, fetch the inventories for that item
        Find the inventory with the minimum TotalAllocated
        Decrease the TotalAllocated by the amount of the item in the order
        Update the TotalExpected for that inventory, to be the sum of TotalOnHand and TotalOrdered
        Finally, update the inventory in the database */
        foreach (var currentItem in currentItems)
        {
            var found = OrderItems.Any(item => item.ItemId == currentItem.ItemId);
            if (!found)
            {
                var inventories = await _context.Inventories
                    .Where(inv => inv.ItemId == currentItem.ItemId)
                    .ToListAsync();
                var minInventory = inventories.OrderBy(inv => inv.TotalAllocated).FirstOrDefault();
                if (minInventory != null)
                {
                    minInventory.TotalAllocated -= currentItem.Amount;
                    minInventory.TotalExpected = minInventory.TotalOnHand + minInventory.TotalOrdered;
                    _context.Inventories.Update(minInventory);
                    await _context.SaveChangesAsync();
                }
            }
        }
        
        /* Loop throuw currentItems and check if they are in OrderItems
        For each matching item, fetch the inventories for that item
        Find the inventory with the minimum TotalAllocated
        Adjust the TotalAllocated by adding the difference between the new items amount and the current items amount
        Update the TotalExpected for that inventory, to be the sum of TotalOnHand and TotalOrdered
        Finally, update the inventory in the database */
        foreach (var currentItem in currentItems)
        {
            var orderItem = OrderItems.First(item => item.ItemId == currentItem.ItemId);
            if (orderItem != null)
            {
                var inventories = await _context.Inventories
                    .Where(inv => inv.ItemId == currentItem.ItemId)
                    .ToListAsync();
                var minInventory = inventories.OrderBy(inv => inv.TotalAllocated).FirstOrDefault();
                if (minInventory != null)
                {
                    throw new NotImplementedException("Error in reference code: bespreken met docent");
                    minInventory.TotalAllocated += orderItem.Amount - currentItem.Amount;
                    minInventory.TotalExpected = minInventory.TotalOnHand + minInventory.TotalOrdered;
                    _context.Inventories.Update(minInventory);
                }
            }
        }

        /* Update the order with the new items
        Save the changes to the database */


    }

    public async Task DeleteOrder(string OrderId)
    {
        Order? order = await _context.Orders.FindAsync(OrderId);
        if(order == null){
            return;
        }
        _context.Orders.Remove(order);
        await _context.SaveChangesAsync();
    }



}

public interface IOrderService
{

    Task<IEnumerable<Order>> GetOrders();
    Task<Order?> GetOrder(string OrderId);
    Task<IEnumerable<ItemInfo>?> GetOrderItems(string OrderId);
    Task AddOrder(Order order);
    Task EditOrder(string OrderId, Order order);
    Task EditOrderItems(string OrderId, IEnumerable<ItemInfo> OrderItems);
    Task DeleteOrder(string OrderId);


}