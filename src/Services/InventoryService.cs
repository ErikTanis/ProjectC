using Microsoft.EntityFrameworkCore;

public class InventoryService : IInventoryService
{

    private readonly DataContext _context;

    public InventoryService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Inventory>?> GetInventories(){
        return await _context.Inventories.ToListAsync();
    }


    public async Task<Inventory?> GetInventory(int InventoryId){
        return await _context.Inventories.FindAsync(InventoryId);
    }


    public async Task<Inventory?> AddInventory(Inventory inventory){
        inventory.CreatedAt = DateTime.Now;
        inventory.UpdatedAt = DateTime.Now;
        await _context.Inventories.AddAsync(inventory);
        await _context.SaveChangesAsync();
        return await GetInventory(inventory.Id);
    }


    public async Task UpdateInventory(int InventoryId, Inventory inventory){
        inventory.Id = InventoryId;
        inventory.UpdatedAt = DateTime.Now;
        _context.Inventories.Update(inventory);
        await _context.SaveChangesAsync();
    }


    public async Task DeleteInventory(int InventoryId){
        Inventory? inventory = await _context.Inventories.FindAsync(InventoryId);
        if(inventory == null) return;
        _context.Inventories.Remove(inventory);
        await _context.SaveChangesAsync();
    }



}

public interface IInventoryService
{

    Task<IEnumerable<Inventory>?> GetInventories();
    Task<Inventory?> GetInventory(int InventoryId);
    Task<Inventory?> AddInventory(Inventory inventory);
    Task UpdateInventory(int InventoryId, Inventory inventory);
    Task DeleteInventory(int InventoryId);

}