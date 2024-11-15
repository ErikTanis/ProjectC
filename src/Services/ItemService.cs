using Microsoft.EntityFrameworkCore;

public class ItemService : IItemService
{

    private readonly DataContext _context;

    public ItemService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Item>?> GetItems(){
        return await _context.Items.ToListAsync();
    }


    public async Task<Item?> GetItem(string ItemId){
        return await _context.Items.FindAsync(ItemId);
    }


    public async Task<IEnumerable<Inventory>?> GetInventories(string ItemId){
        return await _context.Inventories.Where(inv => inv.ItemId == ItemId).ToListAsync();
    }


    public async Task<InventoryTotal?> GetTotals(string ItemId){
        IEnumerable<Inventory>? inventories = await GetInventories(ItemId);
        if(inventories == null) return null;
        InventoryTotal total = inventories.Aggregate(new InventoryTotal(), (acc, inv) => {
            acc.TotalExpected += inv.TotalExpected;
            acc.TotalOrdered += inv.TotalOrdered;
            acc.TotalAllocated += inv.TotalAllocated;
            acc.TotalAvailable += inv.TotalAvailable;
            return acc;
        });
        return total;
    }


    public async Task<Item?> AddItem(Item item){
        item.CreatedAt = DateTime.Now;
        item.UpdatedAt = DateTime.Now;
        await _context.Items.AddAsync(item);
        await _context.SaveChangesAsync();
        return await GetItem(item.Uid);
    }


    public async Task UpdateItem(string ItemId, Item item){
        item.Uid = ItemId;
        item.UpdatedAt = DateTime.Now;
        _context.Items.Update(item);
        await _context.SaveChangesAsync();
    }


    public async Task DeleteItem(string ItemId){
        Item? item = await _context.Items.FindAsync(ItemId);
        if(item == null) return;
        _context.Items.Remove(item);
        await _context.SaveChangesAsync();
    }




}

public interface IItemService
{

    Task<IEnumerable<Item>?> GetItems();
    Task<Item?> GetItem(string ItemId);
    Task<IEnumerable<Inventory>?> GetInventories(string ItemId);
    Task<InventoryTotal?> GetTotals(string ItemId);
    Task<Item?> AddItem(Item item);
    Task UpdateItem(string ItemId, Item item);
    Task DeleteItem(string ItemId);

}