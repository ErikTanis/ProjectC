using Microsoft.EntityFrameworkCore;

public class ShipmentService : IShipmentService
{

    private readonly DataContext _context;

    public ShipmentService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Shipment>> GetShipments(){
        return await _context.Shipments.ToListAsync();
    }

    public async Task<Shipment?> GetShipment(int ShipmentId){
        return await _context.Shipments.FindAsync(ShipmentId);        
    }

    public async Task<IEnumerable<Order>?> GetShipmentOrders(int ShipmentId){
        Shipment? shipment = await _context.Shipments.FindAsync(ShipmentId);
        if(shipment == null){
            return null;
        }
        return await _context.Orders.Where(o => o.ShipmentId == ShipmentId).ToListAsync();
    }

    public async Task<IEnumerable<ItemInfo>?> GetShipmentItems(int ShipmentId){
        Shipment? shipment = await _context.Shipments.FindAsync(ShipmentId);
        if(shipment == null){
            return null;
        }
        return shipment.Items;
    }

    public async Task AddShipment(Shipment shipment){
        shipment.CreatedAt = DateTime.Now;
        shipment.UpdatedAt = DateTime.Now;
        await _context.Shipments.AddAsync(shipment);
        await _context.SaveChangesAsync();
    }

    public async Task EditShipment(int ShipmentId, Shipment shipment){
        shipment.UpdatedAt = DateTime.Now;
        _context.Shipments.Update(shipment);
        await _context.SaveChangesAsync();
    }

    public async Task EditShipmentOrders(int ShipmentId, IEnumerable<Order> ShipmentOrders){
        IEnumerable<Order>? PackedOrders = await GetShipmentOrders(ShipmentId);
        if(PackedOrders == null) return;
        foreach(Order order in PackedOrders){
            if(!ShipmentOrders.Contains(order)){
                order.ShipmentId = -1;
                order.OrderStatus = OrderStatus.Scheduled;
                _context.Orders.Update(order);
            }
        }
        foreach(Order order in ShipmentOrders){
            order.ShipmentId = ShipmentId;
            order.OrderStatus = OrderStatus.Packed;
            _context.Orders.Update(order);
        }
        Shipment? shipment = await _context.Shipments.FindAsync(ShipmentId);
        if(shipment == null) return;
        shipment.UpdatedAt = DateTime.Now;
        await _context.SaveChangesAsync();
    }

    public async Task EditShipmentItems(int ShipmentId, IEnumerable<ItemInfo> ShipmentItems)
    {
        Shipment? shipment = await _context.Shipments.FindAsync(ShipmentId);
        if (shipment == null)
        {
            return;
        }

        var currentItems = shipment.Items.ToList();
        await RemoveOldItemsFromInventory(currentItems, ShipmentItems);
        await UpdateExistingItemsInInventory(currentItems, ShipmentItems);

        shipment.Items = ShipmentItems.ToList();
        _context.Shipments.Update(shipment);
        shipment.UpdatedAt = DateTime.Now;
        await _context.SaveChangesAsync();
    }

    private async Task RemoveOldItemsFromInventory(List<ItemInfo> currentItems, IEnumerable<ItemInfo> newItems)
    {
        foreach (var currentItem in currentItems)
        {
            var found = newItems.Any(item => item.ItemId == currentItem.ItemId);
            if (!found)
            {
                var inventories = await _context.Inventories
                    .Where(inv => inv.ItemId == currentItem.ItemId)
                    .ToListAsync();
                var maxInventory = inventories.OrderByDescending(inv => inv.TotalOrdered).FirstOrDefault();
                if (maxInventory != null)
                {
                    maxInventory.TotalOrdered -= currentItem.Amount;
                    maxInventory.TotalExpected = maxInventory.TotalOnHand + maxInventory.TotalOrdered;
                    _context.Inventories.Update(maxInventory);
                }
            }
        }
    }

    private async Task UpdateExistingItemsInInventory(List<ItemInfo> currentItems, IEnumerable<ItemInfo> newItems)
    {
        foreach (var currentItem in currentItems)
        {
            var newItem = newItems.FirstOrDefault(item => item.ItemId == currentItem.ItemId);
            if (newItem != null)
            {
                var inventories = await _context.Inventories
                    .Where(inv => inv.ItemId == currentItem.ItemId)
                    .ToListAsync();
                var maxInventory = inventories.OrderByDescending(inv => inv.TotalOrdered).FirstOrDefault();
                if (maxInventory != null)
                {
                    maxInventory.TotalOrdered += newItem.Amount - currentItem.Amount;
                    maxInventory.TotalExpected = maxInventory.TotalOnHand + maxInventory.TotalOrdered;
                    _context.Inventories.Update(maxInventory);
                }
            }
        }
    }

    public async Task DeleteShipment(int ShipmentId){
        Shipment? shipment = await _context.Shipments.FindAsync(ShipmentId);
        if(shipment == null){
            return;
        }
        _context.Shipments.Remove(shipment);
        await _context.SaveChangesAsync();
    }


}

public interface IShipmentService
{

    Task<IEnumerable<Shipment>> GetShipments();
    Task<Shipment?> GetShipment(int ShipmentId);
    Task<IEnumerable<Order>?> GetShipmentOrders(int ShipmentId);
    Task<IEnumerable<ItemInfo>?> GetShipmentItems(int ShipmentId);
    Task AddShipment(Shipment Shipment);
    Task EditShipment(int ShipmentId, Shipment Shipment);
    Task EditShipmentOrders(int ShipmentId, IEnumerable<Order> ShipmentOrders);
    Task EditShipmentItems(int ShipmentId, IEnumerable<ItemInfo> ShipmentItems);
    Task DeleteShipment(int ShipmentId);


}